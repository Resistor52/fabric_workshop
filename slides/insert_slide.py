#!/usr/bin/env python3

import os
import sys
import shutil
from pathlib import Path

# Check if starting number was provided
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <starting_slide_number>")
    print(f"Example: {sys.argv[0]} 5 (will increment all slides from slide005.md onwards)")
    sys.exit(1)

start_num = int(sys.argv[1])

# Create a temporary directory
temp_dir = Path("temp_slides")
temp_dir.mkdir(exist_ok=True)

# Get all slide files and sort them
slide_files = sorted([f for f in Path().glob("slide*.md")])

# First, copy slides before the start number as-is
for file in slide_files:
    current_num = int(file.stem[5:])  # Extract number from 'slideXXX'
    if current_num < start_num:
        print(f"Keeping {file} unchanged")
        shutil.copy(file, temp_dir)

# Then copy all slides from start number with incremented numbering
for file in slide_files:
    current_num = int(file.stem[5:])  # Extract number from 'slideXXX'
    if current_num >= start_num:
        new_num = current_num + 1
        new_name = f"slide{new_num:03d}.md"
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