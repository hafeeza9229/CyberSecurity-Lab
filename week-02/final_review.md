# Week 2 Final Review and Technical Synthesis — Learning Log

## Overview
- **Date:** September 17, 2026
- **Objective:** Review and consolidate technical competencies spanning Windows internal structures, authentication auditing, conceptual network layering, and live packet capture analysis.

---

## Retrospective Analysis & Knowledge Verification

A full audit of this week's technical logs confirms foundational progression in host-based and network-based defensive operations.

### 1. Windows Operating System Architecture
*   **Concepts Mastered:** Established a definitive baseline separating active user-mode processes from persistent background system services managed by the Service Control Manager. Deconstructed the operational role of `svchost.exe` as a shared process container designed to host multiple dynamic-link library (.dll) services for optimal resource conservation.

### 2. Endpoint Security Auditing
*   **Concepts Mastered:** Developed functional navigation and filtering capabilities inside the Windows Security Log subsystem (`eventvwr.msc`). Focused on tracking authentication telemetry through specific, standardized indicators:
    *   `Event ID 4624`: Successful system logon verification, detailing account identities and specific logon types (e.g., interactive local authentication versus network-driven connections).
    *   `Event ID 4625`: Failed authentication tracking, mapping targeted user account profiles to help catch potential brute-force attempts.

### 3. Network Infrastructure & Packet Analysis
*   **Concepts Mastered:** Linked abstract network models directly to active data traffic. Transitioned from the theoretical layers of the Open Systems Interconnection (OSI) framework to live network analysis by deploying Wireshark on the host interface. Isolated several core network actions:
    *   `DNS Resolution`: Captured the request/response string sequences that resolve domain targets to logical IP paths.
    *   `TCP Handshake Verification`: Isolated early session initialization by filtering for baseline synchronization indicators (`[SYN]` and `[SYN, ACK]`).
    *   `Display Filter Querying`: Mastered advanced querying logic, testing endpoint separation commands (`ip.addr`), structural exclusions (`!(arp or icmp or dns)`), and clear-text payload indexing (`tcp contains`).

---

## Target Areas for Technical Revisit

The following technical areas have been logged for secondary review during upcoming deep-dive lab exercises:
*   **Encrypted Traffic Dissection:** Exploring how security analysts evaluate anomalous traffic trends within encrypted TLS payloads on Port 443, since raw application data is masked by modern HTTPS encryption.
*   **Advanced Logic Combinations:** Practicing the compounding use of logical operators (AND/OR/NOT) within Wireshark to isolate multi-vector communication anomalies more efficiently.

---
*Week 2 Portfolio finalized. Next Objective: Transitioning to Semester Mode to balance advanced networking protocols with university academic sessions.*
