#!/usr/bin/env python3

import os
import sys
import shutil
from pathlib import Path

# Create a temporary directory
temp_dir = Path("temp_slides")
temp_dir.mkdir(exist_ok=True)

# Get all slide files and sort them
slide_files = sorted([f for f in Path().glob("slide*.md")])

if not slide_files:
    print("No slide files found!")
    sys.exit(1)

# Renumber all slides sequentially
for index, file in enumerate(slide_files, start=1):
    new_name = f"slide{index:03d}.md"
    print(f"Processing {file} -> {new_name}")
    shutil.copy(file, temp_dir / new_name)

print("\nNew sequence in temp_slides:")
for file in sorted(temp_dir.glob("*.md")):
    print(file.name)

input("\nPress Enter to replace old slides with new numbering or Ctrl+C to cancel")

# Remove original files
for file in slide_files:
    file.unlink()

# Move new files back to main directory
for file in temp_dir.glob("*.md"):
    shutil.move(str(file), ".")
temp_dir.rmdir()

print("\nRenumbering complete. Final sequence:")
for file in sorted(Path().glob("slide*.md")):
    print(file.name) 