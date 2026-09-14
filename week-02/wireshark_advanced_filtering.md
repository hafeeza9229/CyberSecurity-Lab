# Advanced Wireshark Display Filtering — Learning Log

## Overview
- **Date:** September 12, 2026
- **Source:** Chris Greer — Top 10 Wireshark Filters Video Lesson
- **Tool Used:** Wireshark Packet Analyzer
- **Objective:** Expand network traffic analysis capabilities by mastering advanced display filters to isolate endpoints and identify potential malicious activity.

---

## Technical Advanced Filters Learned

### 1. Unified Station Filtering
*   **Filter Syntax:** `ip.addr == [IP_Address]`
*   **Operational Purpose:** This filter strips away all surrounding network noise and displays packets where the specified IP address is either the source or the destination. It maps complete, isolated conversations between two specific endpoints.
*   **Advanced Syntax Variations:** Using `ip.src == [IP_Address]` isolates packets coming *from* a specific host, while `ip.dst == [IP_Address]` targets packets sent *to* that host.

### 2. Payload Inspection for Network Auditing
*   **Filter Syntax:** `tcp contains "[string]"` (or `udp contains "[string]"`)
*   **Operational Purpose:** This filter searches for the string in the content of any IP packet, regardless of the transport protocol. It is useful for security tracking, such as identifying if devices are communicating with unauthorized domains or checking for plain-text usernames traveling over unencrypted channels.

### 3. Application Response Performance Auditing
*   **Filter Syntax:** `http.response.code == 200`
*   **Operational Purpose:** Used during web application analysis to filter traffic based on specific web server responses. While code 200 flags successful connections, it can be swapped to `404` or `500` codes to quickly trace server errors or find broken connection links during a security investigation.

---

## Hands-On Verification Log

*   **Testing Execution:** Opened a local traffic capture in Wireshark and tested the logical station filter syntax `ip.addr`.
*   **Observation:** Extracted a live external destination IP address from the packet list and applied it to the filter bar. The interface turned green, confirming correct syntax, and successfully removed all unrelated local background traffic. This isolated the communication stream down to that single target endpoint.

---
*Next Objective: Reviewing accumulated network logs during the Day 13 buffer phase to prepare for the final Week 2 portfolio push.*
