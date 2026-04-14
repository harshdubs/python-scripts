import argparse
import sys
import re
from collections import Counter
from datetime import datetime


parser = argparse.ArgumentParser(description="Analyze a log file and produce a summary report")
parser.add_argument("logfile")
args = parser.parse_args()

counts = Counter()
error_hours = Counter()
error_entries = []

pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'

try:
    with open(args.logfile) as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                timestamp = match.group(1)
                level = match.group(2)
                message = match.group(3)
                counts[level] += 1
                if level == "ERROR":
                    error_entries.append((timestamp, message))
                    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                    error_hours[dt.hour] += 1
            else:
                print(f"Skipped malformed line: {line.strip()}")

    with open("report.txt", "w") as r:
        r.write("LOG ANALYSIS REPORT\n")
        r.write("===================\n\n")

        total = sum(counts.values())
        r.write(f"Total lines parsed: {total}\n\n")

        r.write("=== Level Counts ===\n")
        r.write(f"INFO:     {counts['INFO']}\n")
        r.write(f"WARNING:  {counts['WARNING']}\n")
        r.write(f"ERROR:    {counts['ERROR']}\n")
        r.write(f"CRITICAL: {counts['CRITICAL']}\n\n")

        if error_entries:
            peak_hour, peak_count = error_hours.most_common(1)[0]
            r.write("=== Peak Error Hour ===\n")
            r.write(f"Hour {peak_hour:02d}:00 had {peak_count} errors\n\n")

            r.write(f"=== All ERROR Entries ({len(error_entries)} total) ===\n")
            for timestamp, message in error_entries:
                r.write(f"{timestamp} - {message}\n")
        else:
            r.write("No errors found\n")

    print("Report written to report.txt")

except FileNotFoundError:
    print(f"Error: file '{args.logfile}' not found")
    sys.exit(1)