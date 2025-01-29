# Handling Edge Cases & Errors

## Best Practices

- Anticipate potential failure modes
- Include error handling instructions
- Validate input data quality
- Plan for unexpected outputs
- Use defensive prompting techniques

## Example
```bash
# With error handling
echo "Review this log file for security incidents. If the file is empty or corrupted, report the issue. If no incidents found, explicitly state that. Log: : $(cat security.log)" | fabric -p ai
```

--- 