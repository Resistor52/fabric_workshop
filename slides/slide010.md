# File Redirection Basics

- **Standard Input (stdin)**: `<` or `0<`
  ```bash
  fabric -p ai < input.txt
  ```

- **Standard Output (stdout)**: `>` or `1>`
  ```bash
  fabric -p summarize > output.txt     # Overwrite
  fabric -p summarize >> output.txt    # Append
  ```

- **Standard Error (stderr)**: `2>`
  ```bash
  fabric -p not_a_pattern 2> errors.log
  ```

## Common Patterns

- **Combine stdout and stderr**:
  ```bash
  fabric -p ai > all.log 2>&1
  ```

- **Discard output**:
  ```bash
  fabric -p test > /dev/null
  ```

Remember: Single `>` overwrites, double `>>` appends 