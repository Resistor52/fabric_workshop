# Create a temporary file for concatenation
touch combined.md

# Find the highest slide number
last_slide=$(ls slide*.md | sort -V | tail -n 1 | sed 's/slide\([0-9]*\).md/\1/')
echo "Found $last_slide slides"

# Loop through slides in numerical order
for i in $(seq -f "%03g" 1 $last_slide); do
    if [ -f "slide${i}.md" ]; then
        # Add horizontal rule before each slide (except the first)
        if [ "$i" != "001" ]; then
            echo -e "\n---\n" >> combined.md
        fi
        cat "slide${i}.md" >> combined.md
        echo "Added slide${i}.md"
    fi
done

# Convert to PowerPoint with template
pandoc -f markdown \
       -t pptx \
       -V slide-level=1 \
       --highlight-style=espresso \
       --reference-doc=template.pptx \
       combined.md \
       -o workshop.pptx

# Clean up
rm combined.md
echo "PowerPoint file created: workshop.pptx"