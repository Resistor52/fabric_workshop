# Workshop Slides Directory

This directory contains the workshop presentation materials in markdown format, along with utilities for generating presentations.

## Directory Contents

### Slide Files
- Individual slides are stored as separate markdown files (`slideXXX.md`)
- Numbered sequentially (001-055) to maintain presentation order
- Each slide ends with a horizontal rule (`---`)

### Special Files
- `Mastering_Fabric_Workshop.md`: Workshop syllabus
- `survey.md`: Workshop feedback survey
- `template.pptx`: PowerPoint template for styling

### Utility Scripts
- `generate-powerpoint.sh`: Combines slides into PowerPoint
- `insert_slide.py`: Manages slide numbering when adding slides
- `fix_numbering.py`: Repairs and resequences slide numbers

## Using the Scripts

### PowerPoint Generation
The `generate-powerpoint.sh` script:
1. Combines all numbered slides in order
2. Adds proper slide breaks
3. Converts to PowerPoint using pandoc
4. Applies styling from template.pptx

Usage:
```bash
./generate-powerpoint.sh
```

### Slide Insertion
The `insert_slide.py` script helps maintain proper numbering when adding new slides between existing ones.

Usage:
```bash
python insert_slide.py
```

### Fix Slide Numbering
The `fix_numbering.py` script helps repair slide numbering when slides are deleted creating gaps in numbers:
1. Creates a temporary directory
2. Copies all slides with sequential numbering
3. Replaces original files after confirmation
4. Maintains slide content while fixing numbers

Usage:
```bash
python fix_numbering.py
```

## Adding New Slides

1. Name files following the pattern: `slideXXX.md`
2. Include horizontal rule (`---`) at end of each slide
3. Use `insert_slide.py` if adding between existing slides
4. Run `fix_numbering.py` if slide numbers get out of sequence
5. Run `generate-powerpoint.sh` to update presentation

## Markdown Guidelines

- Use H1 (`#`) for slide titles
- Use H2 (`##`) for main sections
- Include code blocks with language specification
- End each slide with horizontal rule
- Keep content concise and readable

## Notes

- Test PowerPoint generation after adding slides
- Maintain consistent formatting across slides
- Review generated PowerPoint for proper formatting
- Keep slide numbers sequential
- Run fix_numbering.py if sequence gets broken 