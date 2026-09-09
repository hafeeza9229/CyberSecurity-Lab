# Windows Event Viewer Auditing — Learning Log

## Overview
- **Date:** September 9, 2026
- **Tool Used:** Windows Event Viewer (`eventvwr.msc`)
- **Environment:** Host Windows Operating System (Security Logs)
- **Objective:** Analyze Windows Security Log structures, isolate critical authentication Event IDs, and establish foundational filtering capabilities.

---

## Technical Core Concepts Defined

### 1. The Windows Security Log Subsystem
*   **Definition:** A centralized operating system journal that records security-relevant events as defined by the system's audit policies. It tracks user authentications, privilege changes, and file access attempts.
*   **Operational Context:** Unlike plain-text Linux syslog structures, Windows logs events using unique numeric identifiers called Event IDs. This standardized layout allows automated security tools to parse, filter, and alert on system anomalies without searching for variable text strings.

### 2. Critical Authentication Event IDs
*   **Event ID 4624 (Successful Logon):** Generated every time a user account successfully authenticates to the system. The log entry tracks details such as the specific account name, the source network address, and the Logon Type (e.g., Logon Type 2 for local keyboard access or Logon Type 3 for network-based connections).
*   **Event ID 4625 (Failed Logon):** Generated every time an authentication attempt fails. This log records the targeted account name, the source machine, and failure status codes, making it the primary indicator for tracking brute-force attempts.

---

## Technical Synthesis: Connecting to Script-Based Automation

*   **The Analytical Parallel:** On Day 5, I engineered a Python script (`log_parser.py`) to parse raw text lines searching for the literal string keyword "failed" to track security events in an un-structured log file. 
*   **The Enterprise Application:** Analyzing Windows Event Viewer highlights the exact same core concept, scaled up to an enterprise standard. Instead of parsing a file for the word "failed", a Windows log parser filters specifically for Event ID 4625. The underlying objective remains identical: filtering a high-volume data stream down to a single, measurable indicator of compromise.

---
*Next Objective: Transitioning from host-based monitoring to network-level architectures with the OSI Model and TCP/IP basics on Day 10.*
