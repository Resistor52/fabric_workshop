# Essential Linux Commands

## Basic Text Operations

- **cat**: Display file contents
  ```bash
  cat file.txt
  ```

- **head/tail**: View start/end of files
  ```bash
  head -n 5 file.txt    # First 5 lines
  tail -f log.txt       # Follow log updates
  ```

- **grep**: Search text patterns
  ```bash
  grep "error" log.txt  # Find "error" in file
  ```

- **echo**: Print text
  ```bash
  echo "Hello World"    # Display text
  ```

- **tee**: Read/write streams
  ```bash
  echo "test" | tee output.txt  # Display and save
  ```

These commands form the foundation of text processing in Linux and are essential for working with Fabric's input/output streams. 