# Live Network Traffic Analysis via Wireshark — Learning Log

## Overview
- **Date:** September 11, 2026
- **Tool Used:** Wireshark Packet Analyzer
- **Environment:** Host Laptop (Live Network Interface Capture)
- **Objective:** Capture live network traffic, filter specific core protocols, and analyze packet structures across the OSI layers.

---

## Captured Protocol Analysis

### 1. Domain Name System (DNS) Resolution
*   Filter Used: `dns`
*   Observation: Documented the request and response pattern used to change human-readable website names into logical IP addresses.

![Wireshark DNS packet capture log](dns_capture.png)

### 2. Transmission Control Protocol (TCP) Three-Way Handshake
*   Filter Used: `tcp.flags.syn == 1`
*   Observation: Isolated the initialization phase of local TCP connections.

![Wireshark TCP SYN and SYN-ACK handshake capture](tcp_handshake.png)

### 3. Hypertext Transfer Protocol (HTTP/HTTPS) Traffic Evaluation
*   Filter Used: `http`
*   Observation: The capture filter showed minimal plain-text HTTP entries because modern web traffic uses encrypted HTTPS.

![Wireshark HTTP and HTTPS port 443 evaluation](http_evaluation.png)

---

## Technical Synthesis: Operational Observations

*   **Analysis Realization:** Working with live packet analysis connects network theory to operational reality. Seeing the exact bytes move from a Layer 7 DNS query down to a Layer 4 TCP connection provides clear proof of how the encapsulation models studied on Day 10 operate in real time.

---
*Next Objective: Deepening traffic analysis capabilities using specific operational capture filters.*
