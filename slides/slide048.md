# Creating Custom Patterns

## Example: AWS CloudTrail Analysis Pattern

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
--- 