# Fabric Workshop Exercises

This document contains hands-on exercises using Fabric commands shown throughout the workshop. Each section focuses on different aspects of using Fabric effectively.

## Basic Fabric Commands

```bash
# View help and available options
fabric --help

# List available patterns
fabric -l

# List available models
fabric -L

# Simple hello world pattern
fabric --pattern hello_world
fabric -p hello_world  # Short form
fabric -s -p hello_world  # With streaming output

# View a pattern without running it
fabric -p summarize --dry-run
```

## Working with Files and Patterns

```bash
# Basic file processing
cat input.md | fabric -p summarize

# Analyze different types of content
cat emailheader.txt | fabric -p analyze_email_headers | tee headers.md
cat aws-flowlog.txt | fabric -p analyze_logs | tee flowlog.md
cat security.log | fabric -p analyze_logs

# Document analysis
cat threat_report.md | fabric -p analyze_claims
cat advisory.md | fabric -p create_cyber_summary
cat threat_report.md | fabric -p analyze_threat_report_trends
cat architecture.md | fabric -p create_stride_threat_model
```

## Using Context Files

```bash
# Try different contexts
cp context-*.md ~/.config/fabric/contexts/  # Move the files
echo "explain the CIA Triad" | fabric -C context-expert.md -p raw_query
echo "explain the CIA Triad" | fabric -C context-layperson.md -p raw_query
```

## Pattern Analysis 

```bash
# Examine pattern contents
fabric -p extract_wisdom --dry-run | fabric -p summarize_prompt > output.md

# Using tee to see and save output
fabric -p extract_wisdom --dry-run | fabric -p summarize_prompt | tee output.md

# List and summarize all patterns
for pattern in $(fabric -l); do 
    echo -e "\n## "$pattern | tee -a summaries.md
    fabric -p $pattern --dry-run | fabric -p summarize_prompt | tee -a summaries.md
done
```


## Create a new pattern

```bash
# Set up pattern directory
export PATTERN_DIR="$HOME/.config/fabric/patterns"
mkdir -p $PATTERN_DIR/analyze_aws_cloudtrail

# Create the pattern
echo "Analyzing AWS CloudTrail logs that identifies privilege escalation attempts" | fabric -p create_pattern | tee $PATTERN_DIR/analyze_aws_cloudtrail/system.md

# Inspect the pattern
cat $PATTERN_DIR/analyze_aws_cloudtrail/system.md

# Test the pattern
cat cloudtrail.log | fabric -p analyze_aws_cloudtrail
```

## Security Analysis Examples

```bash
# Network traffic analysis
tcpdump -r dns-remoteshell.pcap -A | fabric -p analyze_logs -m gemini-2.0-flash-exp | tee remoteshell.md

# Log analysis with different patterns
cat incident.json | fabric -p create_sigma_rules
cat security.log | fabric -p analyze_incident
cat security.log | fabric -p extract_poc
```

## Tips for Running Exercises

1. Start with basic commands to get familiar with Fabric
2. Use `--dry-run` to preview pattern behavior
3. Save outputs using `tee` for review
4. Experiment with different patterns on the same input
5. Try modifying prompts to see how outputs change
6. Try different models

Note: Some exercises may require specific input files (like logs or configuration files). Sample files are provided in the practice_files directory. 