# Linux User Groups and Identity Management — Learning Log

## Overview
- **Date:** September 1, 2026
- **Source:** LabEx (Linux User Group and File Permissions)
- **Environment:** Local Ubuntu Virtual Machine
- **Objective:** Understand Linux identity structures, user creation, supplementary group management, and account restriction mechanisms.

---

## Technical Tasks Completed

### 1. Identity Inspection and Account Creation
*   Investigated current user identities and system context using terminal verification commands.
*   Practiced creating isolated testing accounts to simulate administrative control over user access.

### 2. Supplementary Group Management
*   Analyzed how primary and secondary (supplementary) groups function to grant nested permissions.
*   Practiced modifying user group associations to scale or restrict access across shared directories.

### 3. Controlling File Ownership
*   Evaluated how files inherit permissions from their creator.
*   Explored the boundaries of modifying file and directory ownership to ensure structural security.

### 4. Account Locking Mechanics
*   Studied the administrative process of inspecting and changing account lock statuses.
*   Learned how a system administrator can temporarily invalidate a user's password or lock an account entirely to prevent unauthorized access.

---

## Professional Reflections and Insights

### Progress and Constraints:
*   **Concepts Mastered:** The mechanics of adding users to supplementary groups to scale permissions cleanly without altering individual file access control lists.
*   **Current Roadblock:** Distinguishing the operational differences between locking an account via password expiration versus changing structural shell permissions requires a deeper look into system files like `/etc/shadow`.

---
*Next Objective: Resuming the lab to cover default permissions (Umask) and special permissions (Sticky Bit, Setgid) before moving to OverTheWire Bandit.*
