# Advanced Wireshark Display Filtering — Learning Log

## Overview
- **Date:** September 12, 2026
- **Source:** Chris Greer — Top 10 Wireshark Filters Video Lesson
- **Tool Used:** Wireshark Packet Analyzer
- **Objective:** Master common network display filters to isolate endpoints, prune background noise, and identify specific packet protocols.

---

## Technical Notes: Top 10 Wireshark Filters Defined

### 1. `ip.addr == 10.0.0.1`
*   **What it does:** Filters the entire capture to show only the traffic traveling to or from a specific IP address.
*   **Why it is useful:** It strips away unrelated network data so you can focus entirely on the network activities of one specific computer or server.

### 2. `tcp or dns`
*   **What it does:** Displays all packets that use either the TCP protocol or the DNS protocol at the same time.
*   **Why it is useful:** It is excellent for tracking web traffic alongside its matching domain name lookups without seeing other noisy protocols.

### 3. `tcp.port == 443`
*   **What it does:** Filters traffic to show packets using port 443 as either their starting point (source) or final destination.
*   **Why it is useful:** Port 443 is the standard port for secure, encrypted web traffic (HTTPS), making this filter necessary for auditing secure web connections.

### 4. `tcp.analysis.flags`
*   **What it does:** Tells Wireshark to isolate and display only the packets that contain system warnings or errors.
*   **Why it is useful:** It instantly flags network performance problems, such as dropped packets, duplicate acknowledgements, or retransmissions.

### 5. `!(arp or icmp or dns)`
*   **What it does:** Uses the exclamation mark `!` to mean "NOT", completely hiding all ARP, ICMP (ping), and DNS background traffic from your screen.
*   **Why it is useful:** Known as "pruning the log," it cleans up standard background network noise so you can spot the actual data sessions you want to analyze.

### 6. `follow tcp stream` (Resulting Filter: `tcp.stream == X`)
*   **What it does:** Converts a single packet selection into a continuous chronological log of that exact conversation between two machines.
*   **Why it is useful:** Instead of manually searching for scattered packets, right-clicking and selecting this feature allows you to read a communication thread from start to finish.

### 7. `tcp contains "facebook"`
*   **What it does:** Scans inside the raw data payload of all TCP packets to look for the literal word "facebook".
*   **Why it is useful:** It helps security analysts detect clear-text keywords, unencrypted usernames, or specific application traffic hidden in the data stream.

### 8. `http.response.code == 200`
*   **What it does:** Displays only the HTTP server responses that returned a status code of 200, which means "OK" or successful.
*   **Why it is useful:** It helps you separate successful web page connections from communication errors like 404 (Not Found) or 500 (Server Error).

### 9. `http.request`
*   **What it does:** Isolates only the specific packets where a client machine is actively asking a web server for data (like a GET request).
*   **Why it is useful:** It creates a clean list showing exactly which website links or paths a computer attempted to open.

### 10. `tcp.flags.syn == 1`
*   **What it does:** Filters the capture to show only the synchronization `[SYN]` packets used to initiate a connection.
*   **Why it is useful:** It shows you when a connection is starting. In security monitoring, seeing thousands of these hitting a server quickly from one location flags a potential Denial-of-Service (DoS) attack.

---

## Hands-On Verification Log
*   **Testing Execution:** Opened a local traffic capture interface in Wireshark and tested the logical station filter syntax `ip.addr` using a visible endpoint address.
*   **Observation:** The background of the entry bar turned green, confirming the filter syntax was correct. The interface successfully removed all unrelated local background noise, confirming that I can easily isolate traffic trends on demand.

---
*Next Objective: Reviewing accumulated network logs during the Day 13 buffer phase to prepare for the final Week 2 portfolio push.*
