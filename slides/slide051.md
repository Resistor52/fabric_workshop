# Hands on Exercise: Summarize a Pattern

```bash
# Summarize the extract_wisdom pattern
fabric p extract_wisdom --dry-run | fabric -p summarize_prompt > output.md
cat output.md 

# Use `tee` to write to a file and stdout
fabric -p extract_wisdom --dry-run | fabric -p summarize_prompt | tee output.md
```

TIP: Try different models! (This works best with OpenAI GPT4o)

---
