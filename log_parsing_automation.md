# Security Log Parsing and Automation Fundamentals — Learning Log

## Overview
- **Date:** September 7, 2026
- **Language:** Python 3
- **Environment:** Local Ubuntu Virtual Machine terminal
- **Objective:** Develop an automated script to parse system authentication logs and aggregate security events.

---

## The Security Problem
Manual review of security architecture logs (firewalls, servers, intrusion detection systems) is impossible at scale due to the thousands of event lines generated daily. Security operations require automated tools to parse raw strings, detect specific indicators of compromise (IoCs), and flag malicious activity such as brute-force attacks.

---

## Implementation Methodology

### 1. Mock Log Creation
Generated a structured testing log named `sample.log` simulating system authentication traffic:
- Log configuration tracks timestamps, event descriptions, status states (succeeded/failed), and targeted usernames.

### 2. Logic Flow of the Automation Script (`log_parser.py`)
The python script implements programmatic text parsing through the following operational logic:
1. Initializes a baseline integer counter at zero to track targets.
2. Interacts with the file system using a secure context manager (`with open`) to open the target file in read-only mode.
3. Iteracts through the dataset sequentially, evaluating text one line at a time.
4. Leverages conditional logic to inspect strings for the specific security keyword indicator ("failed").
5. Increments the state counter by 1 upon every positive string match.
6. Outputs the aggregated metric calculation to the terminal interface upon completing file evaluation.

---

## Automation Script Execution Results

Running the command `python3 log_parser.py` processed the log file cleanly:
- **Output:** `Number of failed login attempts: 2`

This basic programmatic filter accurately identified the targeted anomalies within the raw mock data structure, validating the code logic.

---
*Next Objective: Transitioning to advanced scripting, argument parsing, and standard log extraction tools.*
