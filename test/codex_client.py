#!/usr/bin/env python3
"""
Codex App-Server Image Generation Client
Communicates with local Codex app-server via JSON-RPC for headless image generation
"""

import json
import sys
import subprocess
import time
from pathlib import Path

class CodexAppServerClient:
    """Client for Codex app-server JSON-RPC communication"""

    def __init__(self):
        self.proc = None
        self.request_id = 0
        self.thread_id = None

    def start_server(self):
        """Start Codex app-server in background"""
        print("Starting Codex app-server...")
        self.proc = subprocess.Popen(
            ["codex", "app-server"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1  # Line buffered
        )

        # Give it time to start
        time.sleep(2)
        print(f"✅ Codex app-server started (PID: {self.proc.pid})")

    def send_request(self, method, params=None, notification=False):
        """Send JSON-RPC request to app-server"""
        self.request_id += 1

        message = {
            "method": method,
            "params": params or {}
        }

        if not notification:
            message["id"] = self.request_id

        json_line = json.dumps(message) + "\n"
        self.proc.stdin.write(json_line)
        self.proc.stdin.flush()

        if notification:
            return None

        # Read response
        while True:
            try:
                line = self.proc.stdout.readline()
                if not line:
                    raise Exception("No response from server")

                response = json.loads(line.strip())

                # Skip notifications, look for response to our request
                if "id" in response and response["id"] == self.request_id:
                    if "error" in response:
                        raise Exception(f"RPC Error: {response['error']}")
                    return response.get("result")

            except json.JSONDecodeError:
                continue  # Skip non-JSON lines

    def initialize(self):
        """Initialize connection with app-server"""
        print("Initializing connection...")

        # Step 1: Initialize request
        init_result = self.send_request("initialize", {
            "clientInfo": {
                "name": "sgflix-jumperx-test",
                "title": "SGFLIX Jumperx Integration Test",
                "version": "1.0.0"
            },
            "capabilities": {
                "experimentalApi": True
            }
        })

        print(f"✅ Initialized: {init_result}")

        # Step 2: Initialized notification
        self.send_request("initialized", notification=True)
        print("✅ Handshake complete")

    def start_thread(self, model="gpt-5.4"):
        """Start a new thread"""
        print(f"Starting thread with model: {model}...")

        result = self.send_request("thread/start", {
            "model": model
        })

        self.thread_id = result.get("thread", {}).get("id")
        print(f"✅ Thread started: {self.thread_id}")
        return self.thread_id

    def generate_image(self, prompt_text):
        """Send image generation prompt"""
        print("Sending image generation prompt...")

        result = self.send_request("turn/start", {
            "threadId": self.thread_id,
            "input": [
                {
                    "type": "text",
                    "text": prompt_text
                }
            ]
        })

        print("✅ Turn started")
        return result

    def read_responses(self, timeout=120):
        """Read all responses from server"""
        print("Reading responses (timeout: {}s)...".format(timeout))

        start_time = time.time()
        responses = []

        while time.time() - start_time < timeout:
            try:
                line = self.proc.stdout.readline()
                if not line:
                    break

                line = line.strip()
                if not line:
                    continue

                try:
                    response = json.loads(line)
                    responses.append(response)

                    # Log important responses
                    if "method" in response:
                        print(f"[Notification] {response['method']}")
                    elif "result" in response:
                        print(f"[Response] {response.get('id', 'unknown')}: OK")
                    elif "error" in response:
                        print(f"[Error] {response.get('id', 'unknown')}: {response['error']}")

                except json.JSONDecodeError:
                    print(f"[Raw] {line[:100]}...")

            except Exception as e:
                print(f"Error reading: {e}")
                break

        return responses

    def close(self):
        """Close connection to app-server"""
        if self.proc:
            self.proc.stdin.close()
            self.proc.terminate()
            print("✅ Connection closed")


def main():
    """Test Codex app-server image generation"""
    client = CodexAppServerClient()

    try:
        # Read the prompt
        prompt_file = Path("/tmp/sgflix-jumperx-test/planning/frame_prompt.md")
        if not prompt_file.exists():
            print(f"❌ Prompt file not found: {prompt_file}")
            sys.exit(1)

        prompt_text = prompt_file.read_text()
        print(f"Loaded prompt ({len(prompt_text)} chars)")

        # Start server
        client.start_server()

        # Initialize
        client.initialize()

        # Start thread
        client.start_thread(model="gpt-5.4")

        # Send image generation prompt
        client.generate_image(prompt_text)

        # Read responses (this will block until done)
        print("\n" + "="*60)
        print("Waiting for image generation...")
        print("="*60 + "\n")

        responses = client.read_responses(timeout=120)

        # Save responses
        output_file = Path("/tmp/sgflix-jumperx-test/generation/responses.json")
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(json.dumps(responses, indent=2))

        print(f"\n✅ Responses saved to: {output_file}")
        print(f"Total responses: {len(responses)}")

    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        client.close()


if __name__ == "__main__":
    main()
