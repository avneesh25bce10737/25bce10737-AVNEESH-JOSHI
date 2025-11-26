# Project Statement

**Project Title:** Python Algorithmic Toolkit
**Student Name:** Avneesh Joshi
**Registration Number:** 25BCE10737
**Course:** Introduction to Problem Solving and Programming

---

## 1. Problem Definition
In introductory computer science, students often encounter distinct problems requiring specific mathematical or data-manipulation algorithms. Typically, these are solved in isolated scripts. The problem addressed by this project is the lack of a unified, interactive system that consolidates these fundamental tools.

The **Python Algorithmic Toolkit** solves this by providing a single, menu-driven interface that allows users to perform Number Theory calculations (such as GCD and Prime Factorization) and Data Analysis operations (such as finding maximums and sorting) without restarting the program.

## 2. Project Objectives
The primary objectives of this project are:
* **To demonstrate Modular Programming:** separating logic into distinct files (`number_theory.py`, `data_analysis.py`, `main_toolkit.py`) to improve code readability and reusability.
* **To implement Fundamental Algorithms:** proving understanding of iterative loops, conditional logic, and mathematical formulas.
* **To utilize Python Data Structures:** applying Lists for data storage and Sets for duplicate removal.
* **To create a User-Friendly Interface:** designing a CLI (Command Line Interface) that is easy to navigate.

## 3. Methodology and Approach
The application is built using a **Top-Down Design** approach, utilizing only Python's standard libraries. The system is divided into three functional modules:

### A. The Controller (main_toolkit.py)
This acts as the entry point. It utilizes a `while True` loop to keep the application running and handles all user Input/Output (I/O). It validates menu choices and calls the appropriate functions from the logic modules.

### B. Number Theory Module (number_theory.py)
Handles pure mathematical operations. Key algorithms include:
* **Greatest Common Divisor (GCD):** Implemented using a reverse iteration loop to find the largest common divisor.
* **Prime Factorization:** Uses trial division to decompose an integer into its prime components.
* **Base Conversion:** Uses modular arithmetic (`%`) and integer division (`//`) to convert decimals to binary, octal, etc.

### C. Data Analysis Module (data_analysis.py)
Handles list processing. Key techniques include:
* **Duplicate Removal:** Converts the list to a Python `Set` to instantly filter unique values.
* **Fibonacci Generation:** Uses tuple unpacking `(a, b = b, a+b)` for an efficient iterative sequence generation.
* **K-th Smallest Number:** Sorts the list and retrieves the element at index `k-1`.

## 4. Scope and Limitations
**Scope:**
The project covers 8 distinct algorithmic tasks suitable for integer and list-based operations. It is designed for console usage.

**Limitations:**
* The interface is text-based (CLI), not graphical (GUI).
* The `fast_power` function relies on Python's native operators rather than a custom "Divide and Conquer" algorithm.
* Input validation assumes users enter integers when requested; non-integer inputs may cause runtime errors.

## 5. Learning Outcomes
Through the development of this toolkit, the following concepts were mastered:
* **Module Import Mechanics:** How to link local Python files.
* **Control Flow:** Deepened understanding of `while` loops, `for` loops, and `if-elif-else` chains.
* **Algorithm Efficiency:** Learned the difference between linear scans (finding max) and more complex operations (sorting).
* **Data Types:** Practical experience converting between Strings, Integers, and Lists.

## 6. Declaration
I, **Avneesh Joshi**, hereby declare that this project is my original work, developed to demonstrate the concepts learned in the course **Introduction to Problem Solving and Programming**. All algorithms were implemented based on course materials and standard programming practices.

---
