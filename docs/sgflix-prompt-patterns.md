---
name: sgflix-prompt-patterns
description: Reusable prompt engineering templates and patterns from 90+ SGFLIX productions
type: reference
---

# SGFLIX Prompt Engineering Patterns (Proven at Scale)

**Discovery Date**: 2026-05-18
**Source**: Analysis of 90+ production runs, 46 character bibles
**Pattern Maturity**: Production-hardened, battle-tested

## Core Pattern Philosophy

**The "Identity Lock" System**: All prompts use hierarchical locking to ensure consistency:
1. **CHARACTER_IDENTITY_LOCK**: Immutable core attributes (morphology, cranial, surface, chromatic)
2. **DO_NOT_CHANGE**: Explicit declaration of unchangeable elements
3. **BOUNDED_VARIATION**: Clearly defined allowable variations (pose, lighting intensity)
4. **IDENTITY_CONSTRAINTS**: Enforcement rules for each generation

**Why This Works**: DALL-E 3 tends to drift across generations. Locking prevents:
- Hair color/style changes
- Costume detail loss
- Body proportion shifts
- Prop inconsistencies

## Pattern 1: Single Frame Generation

### Template Structure
```markdown
Generate an image with the following prompt, dont change it(DO NOT CHANGE THIS PROMPT, IT'S ALREADY AN IMPROVED PROMPT) -

aspect ratio: [9:16 vertical | 16:9 horizontal | 3:4 portrait | 1:1 square]

subject: [archetype] inspired by [style reference], not an exact real celebrity likeness; [detailed appearance], calm [expression].
pose and expression: [specific mood, body language].
wardrobe: [clothing, accessories, style notes].
scene: [environment, background, context], [key visual elements].
comedic contradiction: [ironic element, visual joke].
camera: [camera angle and composition].
lighting and style: [mood and color palette].

negative instructions: no exact [celebrity] likeness, no readable [brand] branding, [specific restrictions].
```

### Key Pattern Elements

**1. "Not an exact real celebrity likeness"**
- **Why**: Prevents DALL-E safety filters from blocking generation
- **How**: Use archetype language ("legendary pop-diva", "young blond pop-star performer")
- **Result**: Legal safety + creative freedom

**2. Comedic Contradiction Field**
- **Why**: SGFLIX core humor mechanic
- **How**: Irony between character status and situation
- **Example**: "the diva is checking a shimmering vocal-coat labeled only by a blank claim ticket while a tiny coat-check attendant solemnly stamps a giant card that says nothing readable"

**3. Negative Instructions with "No Exact" Phrasing**
- **Why**: DALL-E ignores generic "no logos" but respects "no exact [brand] branding"
- **How**: Specific prohibition of trademarked elements
- **Pattern**: "no exact [celebrity] likeness, no readable [brand] branding, no real [property]"

### Aspect Ratio Selection Guide

| Ratio | Use Case | DALL-E Size |
|-------|----------|-------------|
| 9:16 vertical | Mobile/short-form video frames | 1024x1792 |
| 16:9 horizontal | Storyboard/composition planning | 1792x1024 |
| 3:4 portrait | Character reference sheets | 1024x1365 |
| 1:1 square | Social media posts | 1024x1024 |

## Pattern 2: Shared Choices Storyboard

### Template Structure
```markdown
Use case: infographic-diagram
Asset type: SGFLIX Shared Choices director's-bible storyboard board, [landscape production board | professional planning image]
Primary request: Create a polished director's-bible storyboard board for [PROJECT_TITLE]. This is a single image that functions as a visual production board, not a video.
Layout: [aspect ratio] board, clean grid, [premium studio pitch-board | infographic] design. Use mostly visual panels and icons; minimal small label text is acceptable but avoid long readable paragraphs.
Content: [character description]; hero props include [list]. Floor plan shows [spatial relationships]. Storyboard panels show: [panel-by-panel description].
Style: [cinematic satirical editorial | photoreal reference images], [lighting description], [color palette description], no real logos, no exact celebrity likeness, no watermark.
Avoid: [specific brand logos], [specific platform logos], readable brand names, dense tiny text, exact public figure identity, video frames, low-resolution collage.
```

### Board Structure Patterns

**1. Multi-Section Grid Layout**
```
┌─────────────────────────────────────────┐
│  HEADER: SHARED CHOICES                 │
│  Subtitle: [EPISODE_TITLE]              │
├─────────────────────────────────────────┤
│ 1. CHARACTER + HERO PROPS REFERENCE     │
│    [character silhouette, props list]    │
├─────────────────────────────────────────┤
│ 2. ENVIRONMENT / SET DESIGN + FLOOR PLAN │
│    [location description, blocking diag] │
├─────────────────────────────────────────┤
│ 3. STORYBOARD - [N] CUTS                │
│    Cut 1: [description] [camera]         │
│    Cut 2: [description] [camera]         │
│    ...                                   │
├─────────────────────────────────────────┤
│ 4. LIGHTING / MOOD / STYLE NOTES        │
│    [lighting setup, color palette]       │
└─────────────────────────────────────────┘
```

**2. Storyboard Panel Notation**
```markdown
Cut [N]: [panel description]
Camera: [camera position, lens choice, movement notes]
Action: [what happens in this panel]
Lighting: [lighting setup, mood, time of day]
Audio: [suggested sound effects or dialogue]
Props: [key items visible in frame]
Colors: [dominant colors, palette notes]
```

### Color Palette Specification Pattern
```markdown
Color palette swatches [color1 / color2 / color3 / color4]

Common SGFLIX Palettes:
- Tabloid Cinema: warm museum gold / glossy black / paparazzi-white highlights
- Broadcast Control: cold fluorescent blue / monitor glow / warning red / evidence-bag beige
- Festival Stage: warm amber desert-stage / LED cyan-purple contrast / crowd phone lights
- Legal Comedy: navy / gray / white / broadcast blue / warning red
```

## Pattern 3: Character Bible Generation

### Identity Lock Schema
```markdown
CHARACTER_IDENTITY_LOCK:
  name: [Character Name]
  character_class: [humanoid | hybrid | creature | mecha]
  age_cohort: [age specification with safety constraint]
  species: [species details]
  role: [character role]
  morphology_lock: [body type, build, posture, gait, silhouette]
  cranial_lock: [facial features, hair, expressions, baseline]
  surface_lock: [clothing, accessories, style, partitions]
  appendage_lock: [limb consistency, anatomical rules, extremity topology]
  accessory_prop_lock: [signature items, weapons, tools, attachment rules]
  chromatic_lock: [primary / secondary / accent / metallic / emissive / neutral]
  material_lock: [fabric types, surfaces, weathering, finish]
  style_lock: [production style, rendering technique, lighting protocol]
  signature_visual_hooks: [5-7 key recognizable elements]

DO_NOT_CHANGE: [list of immutable attributes]
BOUNDED_VARIATION: [allowable changes: pose, expression intensity, lighting]
PRESENTATION_CONSTRAINT: [professional framing, safety rules, age-appropriate guidelines]
```

### Page-by-Page Structure (8-Page Bible)

**Page 1: PRIMARY_HERO_REFERENCE**
- Task: Instantiate canonical identity
- Composition: Full-body + cranial portrait inset
- Goal: Maximum legibility of all identity elements

**Page 2: MORPHOLOGY_VARIATIONS**
- Task: Show pose/expression range
- Composition: 3-4 action poses
- Goal: Demonstrate character movement

**Page 3: SURFACE_TREATMENT**
- Task: Clothing/accessory details
- Composition: Close-ups, flat lays
- Goal: Material and texture clarity

**Page 4: CHROMATIC_MATERIAL**
- Task: Color palette and materials
- Composition: Swatches, material samples
- Goal: Color accuracy reference

**Page 5: PROP_ACCESSORY**
- Task: Signature props and weapons
- Composition: Props in use, isolated views
- Goal: Prop integration rules

**Page 6: EXPRESSION_RANGE**
- Task: Emotional spectrum
- Composition: 6-8 expression headshots
- Goal: Character performance baseline

**Page 7: ACTION_DYNAMIC**
- Task: Combat/action poses
- Composition: Dynamic action shots
- Goal: Motion and impact clarity

**Page 8: STYLE_REFERENCE**
- Task: Final style guide
- Composition: Best-of compilation
- Goal: Production reference sheet

### Morphological Class Dispatch

**Character Classes** with class-specific terminology:
- **humanoid**: "class-appropriate appendages", "human cranial topology"
- **hybrid**: "demon/spirit fusion", "aura attachment without topology change"
- **creature**: "non-human anatomy", "alternative limb configurations"
- **mecha**: "mechanical construction", "articulated joints", "armor panels"

Each class triggers different:
- Appendage rules (limb count, topology)
- Cranial terminology (human vs demon vs mechanical)
- Surface treatment (cloth vs organic vs metal)
- Material assumptions (fabric vs skin vs plating)

## Pattern 4: Error Handling and Repair

### Placeholder Pattern
```markdown
When generation fails (billing_hard_limit_reached):

1. Create blank PNG with error notes:
   - Image dimensions: [target size]
   - Text overlay: "PLACEHOLDER - Billing limit reached"
   - Error details: [timestamp, error code]

2. Save prompt beside failed image:
   - Filename: [image_name]_prompt.md
   - Content: Full generation prompt
   - Metadata: Generation attempt timestamp

3. Flag for repair queue:
   - Add to repair list with priority
   - Note specific issue from QC
   - Schedule regeneration when credits reset
```

### Repair Prompt Pattern
```markdown
Generate an image with the following prompt, dont change it(DO NOT CHANGE THIS PROMPT, IT'S ALREADY AN IMPROVED PROMPT) -

[Original detailed prompt]

REPAIR INSTRUCTIONS: Fix [specific issue from QC] while preserving all other elements. Maintain character consistency, scene composition, and style.

Common repairs:
- Fix distorted hands or extra fingers
- Remove unintended text or watermarks
- Correct color drift from identity lock
- Restore missing props or accessories
- Adjust lighting that's too dark/harsh
```

### QC Checklist Pattern
```markdown
QC Review for [asset_name]:

Identity Consistency:
□ Morphology matches lock (body type, build)
□ Cranial features match lock (hair, face)
□ Surface treatment matches lock (clothing, accessories)
□ Chromatic signature matches lock (colors)
□ Props/accessories match lock

Technical Quality:
□ No distorted extremities
□ No extra fingers/limbs
□ No unintended text
□ No watermarks
□ No celebrity likeness (unless archetype)

Production Readiness:
□ Resolution matches spec
□ Aspect ratio correct
□ File size in range (2-3MB)
□ Prompt saved beside image
□ Metadata documented

Issues found: [list or "NONE"]
Repair needed: [YES/NO]
Repair priority: [1-3 or N/A]
```

## Pattern 5: Temporal Sequencing

### Before/After Prompt Pattern
```markdown
v01_prompt.md:
"before the [event reveal]"
"pre-[event] state"
"moment before [change]"

v02_prompt.md:
"after the [event reveal]"
"post-[event] state"
"moment after [change]"

Example:
v01: "before the helicopter reveal" → normal festival grandeur
v02: "after the helicopter reveal" → crowd chaos, intervention underway
```

### Narrative Continuity Locking
```markdown
To maintain visual narrative across related frames:

1. Establish base elements in v01:
   - Fixed environment (location, lighting)
   - Fixed character positions
   - Fixed prop placement

2. Vary only specified elements in v02+:
   - Character actions/expressions
   - Specific prop interactions
   - Camera angle/composition

3. Lock narrative anchor points:
   - Unchanging background elements
   - Consistent character models
   - Fixed spatial relationships
```

## Advanced Pattern Techniques

### 1. The "Archetype" Evasion
**Problem**: DALL-E blocks exact celebrity likenesses
**Solution**: Use archetype language that evokes without copying

```markdown
Instead of: "Mariah Carey in a coat check"
Use: "a fictional legendary pop-diva archetype inspired by champagne glamour and vocal-superstar poise"

Instead of: "Justin Bieber at Coachella"
Use: "caricatured young blond pop-star performer in oversized hoodie at festival laptop table"
```

### 2. The "Generic Brand" Evasion
**Problem**: DALLE blocks trademarked logos
**Solution**: Descriptive generics that evoke the category

```markdown
Instead of: "YouTube logo"
Use: "generic stacked video-thumbnail LED wall"

Instead of: "Coachella logo"
Use: "festival stage with palm silhouettes and stage truss"

Instead of: "ABC logo"
Use: "generic alphabet-network broadcast control room"
```

### 3. The "Unreadable Text" Technique
**Problem**: DALL-E generates gibberish text
**Solution**: Design for text-free visual communication

```markdown
Design Principles:
- Use visual icons instead of text labels
- Color coding for categories (not text)
- Spatial relationships for information hierarchy
- Symbolic marks instead of words

When text is necessary:
- "minimal small label text is acceptable but avoid long readable paragraphs"
- "short labels should be readable where possible"
- "no tiny text" (prevents DALL-E from attempting text rendering)
```

### 4. The "Safety First" Constraints
**Problem**: DALL-E safety filters can be over-sensitive
**Solution**: Explicit safety framing in prompts

```markdown
For minor characters:
PRESENTATION_CONSTRAINT: Apply professional production framing calibrated to declared morphological class. Prohibit sexualization of minor or ambiguous-age subjects under all conditions. Keep all age-appropriate characters fully clothed and non-suggestive.

For sensitive topics:
- "no cruel or mocking content"
- "no mocking body features"
- "no cruel rejection poster"
- "celebrity energy without direct copying"
```

## Anti-Patterns to Avoid

### 1. Loose Identity Locking
**Bad**: "character has red hair and green clothes"
**Good**: `cranial_lock: long straight crimson-red hair` + `surface_lock: magenta/pink school uniform`

**Why**: "Has" allows drift, "lock" prevents it

### 2. Generic Style References
**Bad**: "anime style"
**Good**: "1990s supernatural shonen anime production model sheet, crisp cel-shaded rendering, clean construction lines"

**Why**: Specificity prevents style drift across generations

### 3. Negative Instructions Without Specificity
**Bad**: "no logos"
**Good**: "no exact [brand] branding, no real [platform] logo"

**Why**: DALL-E ignores generic prohibitions but respects specific ones

### 4. Changing Identity Between Pages
**Bad**: Page 1 says "green jacket", Page 3 says "blue jacket"
**Good**: Lock `surface_lock: green gakuran school jacket` once, reference lock on all pages

**Why**: Inconsistency forces manual repair or re-generation

### 5. Ignoring Age Cohort Constraints
**Bad**: "sexy teen character in revealing outfit"
**Good**: "age-appropriate teen protagonist, fully clothed, non-suggestive"

**Why**: Safety filters + ethical production standards

## Template Library

### Quick-Start Templates

**Character Introduction (9:16)**
```markdown
Generate an image with the following prompt, dont change it(DO NOT CHANGE THIS PROMPT, IT'S ALREADY AN IMPROVED PROMPT) -

aspect ratio: 9:16 vertical

subject: a fictional [archetype] inspired by [style reference], not an exact real celebrity likeness; [detailed appearance], calm [expression].
pose and expression: [specific mood, body language].
wardrobe: [clothing, accessories, style notes].
scene: [environment description], [key visual elements].
comedic contradiction: [ironic twist or visual joke].
camera: [camera angle and composition].
lighting and style: [mood and color palette].

negative instructions: no exact [celebrity] likeness, no readable [brand] branding, [specific restrictions].
```

**Shared Choices Storyboard (16:9)**
```markdown
Use case: infographic-diagram
Asset type: SGFLIX Shared Choices director's-bible storyboard board, landscape production board
Primary request: Create a polished director's-bible storyboard board for a fictional SGFLIX short called "[TITLE]". This is a single image that functions as a visual production board, not a video.
Layout: landscape 16:9 board, clean grid, premium studio pitch-board design. Use mostly visual panels and icons; minimal small label text is acceptable but avoid long readable paragraphs.
Content: [character description]; hero props include [list]. Floor plan shows [spatial relationships]. Storyboard panels show: [panel-by-panel description].
Style: [cinematic style], [lighting description], [color palette description], no real logos, no exact celebrity likeness, no watermark.
Avoid: [specific brand logos], [specific platform logos], readable brand names, dense tiny text, exact public figure identity, video frames, low-resolution collage.
```

**Character Bible Page 1 (3:4)**
```markdown
Generate exactly PAGE 1: PRIMARY_HERO_REFERENCE of an 8-page character design bible for morphological class [class]. Emit one discrete image only.

CHARACTER_IDENTITY_LOCK:
  name: [Character Name]
  character_class: [humanoid | hybrid | creature | mecha]
  age_cohort: [age specification]
  species: [species details]
  role: [character role]
  morphology_lock: [body type, build, posture, gait, silhouette]
  cranial_lock: [facial features, hair, expressions, baseline]
  surface_lock: [clothing, accessories, style, partitions]
  appendage_lock: [limb consistency, anatomical rules]
  accessory_prop_lock: [signature items, weapons, tools]
  chromatic_lock: [primary / secondary / accent / metallic / emissive / neutral]
  material_lock: [fabric types, surfaces, weathering]
  style_lock: [production style, rendering technique]
  signature_visual_hooks: [5-7 key elements]

DO_NOT_CHANGE: [list of immutable attributes]
BOUNDED_VARIATION: pose, expression intensity, lighting strength
PRESENTATION_CONSTRAINT: [professional framing, safety rules]

PAGE_TASK: Instantiate canonical identity reference via combined full-body and cranial portrait views.
ASPECT_RATIO: 3:4
COMPOSITION_SPEC: Single-subject framing: one clean full-body view plus one larger cranial portrait inset on the same page, maximum legibility of morphology, cranial features, clothing/surface treatment, props, and chromatic signature. Neutral production background.
IDENTITY_CONSTRAINTS: Preserve the locked morphology, cranial topology, surface treatment, appendage configuration, accessory topology, chromatic signature, and material classes exactly.
TECHNICAL_CONSTRAINTS: scale-invariant production reference; full visibility where full body is requested; clean silhouette; material legibility; large readable labels only if needed; no tiny text; no textured or busy backgrounds; one character identity only.
CLASS_DISPATCH: Apply declared morphological class terminology and maintain class-appropriate production framing.
STYLE_VECTOR: [specific anime/production style], crisp cel-shaded rendering, clean construction lines, controlled linework density, high material readability, neutral studio/background protocol, professional character design bible page.
AVOID_CONSTRAINTS: ["identity feature vector drift", "morphological or cranial topology alteration", "surface treatment or accessory topology modification", "extraneous subjects or random elements", "extremity cropping", "appendage or manipulator distortion", "scale inconsistency across views", "sexualized framing of minor or ambiguous-age characters", "busy textured background", "tiny unreadable text elements"]
```

## How to Apply These Patterns

### For New Content Production
1. Choose the appropriate template (Single Frame / Storyboard / Character Bible)
2. Fill in bracketed placeholders with project-specific details
3. Apply identity locks for character consistency
4. Use aspect ratio optimization for target format
5. Include negative instructions for safety/legal compliance

### For Prompt Iteration
1. Start with v01 prompt using template
2. Review generated image for identity drift
3. Create v02 repair prompt if needed
4. Maintain all identity locks in repair
5. Only vary the specific element needing correction

### For Batch Processing
1. Create JSONL queue with template structure
2. Use consistent identity locks across all items
3. Vary only bounded variation elements
4. Implement placeholder strategy for failures
5. Use repair queue for QC corrections

## Conclusion

These patterns are **production-hardened from 90+ actual runs**. They represent the difference between:
- **Experimental prompts**: Work once, hard to reproduce
- **Pattern-based prompts**: Reliable, scalable, maintainable

The key insight is that **prompt engineering is not creative writing**—it's **specification writing**. The more precise and structured the specification, the more reliable the output.

**Use these patterns as your foundation, then customize for your specific use case.**
