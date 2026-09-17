# TCP/IP Deep Dive: Logical Ports and Common Protocols — Learning Log

## Overview

* **Date:** September 21, 2026
* **Source:** Professor Messer Network Fundamentals Series
* **Tool Used:** Wireshark Packet Analyzer
* **Objective:** Understand the role of transport-layer port numbers and identify common networking protocols used during security analysis.

---

## Technical Core Concepts

### 1. Difference Between IP Addresses and Port Numbers

**IP Address:** An IP address is a logical address used to identify a device or network interface and route data to the correct host.

**Port Number:** A port number identifies the specific application or network service that should receive the data on that host.

A simple way to understand this is: **the IP address identifies the correct building, while the port number identifies the correct room inside that building.**

---

### 2. Common Networking Protocols

| Port Number | Protocol | Purpose & Security Importance                                                                                                                                                     |
| :---------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **21**      | FTP      | Used for file transfers. FTP normally sends information without encryption, so its traffic can be exposed. Unexpected FTP traffic should be investigated on a production network. |
| **22**      | SSH      | Provides encrypted remote access to systems. It is commonly used for securely managing servers over an untrusted network.                                                         |
| **53**      | DNS      | Converts domain names into IP addresses. DNS commonly uses UDP for normal queries and TCP for larger transfers, such as zone transfers.                                           |
| **80**      | HTTP     | Used for standard web traffic without encryption. Its contents can potentially be viewed by network monitoring tools.                                                             |
| **443**     | HTTPS    | Used for encrypted web communication through TLS, helping protect data from interception.                                                                                         |

---

## Wireshark Filtering and Verification

I tested port-based filters in Wireshark to observe network traffic and understand how different protocols use transport-layer ports.

### Query Test 1: HTTPS

**Filter used:**
`tcp.port == 443`

**Observation:**
The filter was accepted by Wireshark, and the packet list showed traffic using TCP port 443. This allowed me to identify HTTPS connections by their port number rather than using a general protocol filter.

---

### Query Test 2: DNS over TCP

**Filter used:**
`tcp.port == 53`

**Observation:**
The packet list was empty. This showed that the DNS traffic generated during the test was not using TCP port 53. Normal DNS queries commonly use **UDP port 53**, which is why this TCP filter did not display the expected traffic.

---

## Next Objective

The next step is to move from basic network analysis to **SOC triage simulations**, beginning with my first security alert investigation on Wednesday.
