# Chaining Commands - Loops

## Bash For Loops

- Iterate over lists, ranges, or command output
- Basic syntax:
  ```bash
  for item in list; do
      command $item
  done
  ```
- Examples:
  ```bash
  # Loop over numbers
  for i in {1..5}; do echo $i; done

  # Loop over files
  for file in *.txt; do cat $file; done

  # Loop over command output
  for user in $(who | cut -d' ' -f1); do
      echo "Hello $user"
  done
  ```

--- 