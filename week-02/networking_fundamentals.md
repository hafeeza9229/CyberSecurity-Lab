# Network Architecture and OSI Model Fundamentals — Learning Log

## Overview

* **Date:** September 10, 2026
* **Source:** Professor Messer Network Fundamentals Series
* **Environment:** Host Laptop (Conceptual Research)
* **Objective:** Understand how data moves through a network using the OSI and TCP/IP models, with a focus on the layers that are important for cybersecurity and network monitoring.

---

## Technical Core Concepts Defined

The **OSI (Open Systems Interconnection) model** is a standard 7-layer framework used to explain how data is prepared, transmitted, and delivered across a network.

For network traffic monitoring, the following three layers are especially important:

### 1. Layer 7: The Application Layer

**Definition:**
The Application Layer is the layer closest to the user. It provides network communication services to applications and software.

**Operational Context:**
This layer includes high-level protocols used by applications, such as:

* **HTTP/HTTPS** — used for web communication
* **DNS** — used to translate domain names into IP addresses
* **SMTP** — used for email communication

From a security perspective, this layer can be monitored to detect suspicious web activity, malicious scripts, and unusual application behavior.

---

### 2. Layer 4: The Transport Layer

**Definition:**
The Transport Layer manages communication between two devices and controls how data is transferred between them.

**Operational Context:**
The two main protocols at this layer are:

* **TCP (Transmission Control Protocol)** — provides reliable and error-checked data delivery.
* **UDP (User Datagram Protocol)** — provides faster communication without establishing a connection.

This layer also uses **port numbers** to identify specific network services. For example:

* **Port 443** — HTTPS
* **Port 22** — SSH

From a security perspective, this layer is important for firewall rules, port filtering, and identifying which services are communicating over the network.

---

### 3. Layer 3: The Network Layer

**Definition:**
The Network Layer is responsible for moving data between different networks and determining how packets reach their destination.

**Operational Context:**
This layer uses **IP addresses**, including IPv4 and IPv6, to identify devices and networks.

**Routers** mainly operate at Layer 3. They examine destination IP addresses and determine the appropriate path for forwarding packets.

From a security perspective, Layer 3 information can be used to:

* Identify suspicious source IP addresses
* Block known malicious IP addresses
* Detect communication with command-and-control servers
* Create and manage network Access Control Lists (ACLs)

---

## Practical Synthesis: Encapsulation in a Real-World Connection

### 1. Application Phase — Layer 7

A user opens a corporate intranet website. The browser creates an HTTPS request containing the application data.

### 2. Transport Phase — Layer 4

The system uses **TCP** to transport the request. The communication is associated with **destination port 443**, which is commonly used for HTTPS traffic.

### 3. Network Phase — Layer 3

The data is then packaged into an IP packet. The packet contains the **source IP address** of the user's device and the **destination IP address** of the web server.

The network devices use these IP addresses to determine where the packet should be sent.

---

**Next Objective:** Transition from theoretical network concepts to live traffic monitoring by deploying **Wireshark** on Day 11.
