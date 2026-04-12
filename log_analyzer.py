import argparse
import sys
import re

parser = argparse.ArgumentParser(description="Enter File name for analysis:")
parser.add_argument("logfile")

pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'

args = parser.parse_args()
try:
    with open(args.logfile) as f:
        for line in f:
            match= re.match(pattern,line)
            if match:
                timestamp = match.group(1)
                level = match.group(2)
                message = match.group(3)
                print(f"[{level}] {timestamp} -> {message}")
            else:
                print(f'Skipped malformed line') 
            
except FileNotFoundError:
    print(f"Error: file '{args.logfile}' not found")
    sys.exit(1)