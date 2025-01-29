# Chaining Commands to Exploit CLI Power

## The Power of Unix Philosophy
- Each program does one thing well
- Programs work together
- Programs handle text streams as universal interface

## Understanding Subshells
- A subshell is a child process of the current shell
- Created using `$()` or backticks `` ` ``
- Example: `echo "Today is $(date)"`
- Nested commands execute from innermost to outermost
- Useful for command substitution and complex pipelines

--- 