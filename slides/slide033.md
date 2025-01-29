# Balancing Precision & Flexibility

## Finding the Sweet Spot

- Be precise enough to get desired results
- Leave room for LLM's capabilities
- Avoid over-constraining the response
- Allow for creative solutions
- Use guardrails when needed

## Example
```bash
# Too rigid
echo "Write exactly 5 bullet points about security" | fabric -p ai

# Better balance
echo "Write a concise security analysis focusing on key risks. Use bullet points." | fabric -p ai
```

--- 