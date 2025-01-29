# Prompts Deep Dive: Crafting Effective Prompts

## Key Elements

- Be clear and specific in your instructions
- Break complex tasks into smaller steps
- Include relevant context and constraints
- Use consistent formatting and structure
- Specify the desired output format

## Example
```bash
# Less effective
echo "analyze this: $(cat document.txt)" | fabric -p ai

# More effective
echo "analyze this technical document and highlight security implications: $(cat document.txt) " | fabric -p ai
```