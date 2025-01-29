# Understanding the `context` Parameter

- Context files tell the AI how to respond to best meet your needs.
- Fabric expects the files to be in the `~/.config/fabric/contexts` directory.
- Use `-C` or `--context` to specify the context file.
- use `-x` to list the context files.

## Move the files and try them out:

```
cp context-*.md /home/ken/.config/fabric/contexts/  

echo "explain the CIA Traid" | fabric -C context-expert.md -p raw_query

echo "explain the CIA Traid" | fabric -C context-layperson.md -p raw_query
```

--- 