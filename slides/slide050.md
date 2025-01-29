# Hands on Exercise: Summarize All Patterns

```bash
# Loop through all patterns
for pattern in $(fabric -l); do echo "- "$pattern; done

for pattern in $(fabric -l); do 
    echo -e "\n## "$pattern | tee -a summaries.md;
    fabric -p $pattern --dry-run | fabric -p summarize_prompt | tee -a summaries.md;
done
```

Protip: Ask AI to explain commplicated CLI commands

Note the use of append mode `tee -a` to add to the file.

--- 