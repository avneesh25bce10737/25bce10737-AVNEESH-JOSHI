# Python Algorithmic Toolkit

This project is a console-based application that provides a suite of tools for common algorithmic tasks. It is built entirely from scratch using standard Python libraries, focusing on concepts from introductory computer science and problem-solving.

The application is structured into three distinct modules for a clean separation of concerns:
1.  A main user-facing toolkit (`main_toolkit.py`)
2.  A number theory logic module (`number_theory.py`)
3.  A data analysis logic module (`data_analysis.py`)

---

# Features

This toolkit provides an interactive menu with the following capabilities:

# Number Theory Tools
**GCD:** Find the Greatest Common Divisor (GCD) of two numbers.
**Prime Factors:** Generate a list of prime factors for any integer.
**Base Conversion:** Convert a decimal number to any base (handles negative numbers).
**Fast Power:** Calculate large powers efficiently (a^b) using the python built in libraries.

# Data & Array Tools
**Find Maximum:** Find the largest value in a list of numbers.
**Remove Duplicates:** Remove all duplicate entries from a list (uses a Set for efficiency).
**Find K-th Smallest:** Find the K-th smallest unique element in a list.
**Fibonacci:** Generate the first N numbers of the Fibonacci sequence.

# User-Friendly Interface
* A simple, interactive command-line menu that loops until the user quits.
* Built using a Top-Down Design modular approach (logic separated into 3 files).

---

# Project Structure

The project is organized into three separate Python modules:
* `main_toolkit.py`: The entry point of the application. It handles all user interaction, prints the menu, gets user input, and calls functions from the other modules.
* `number_theory.py`: A library module containing all logic related to pure mathematics (GCD, prime factors, base conversion, fast power).
* `data_analysis.py`: A library module containing all logic related to list processing (find max, remove duplicates, Kth smallest, Fibonacci).

---

# How to Run

1.  Ensure you have **Python 3.x** installed on your system.
2.  Place all three files (`main_toolkit.py`, `number_theory.py`, `data_analysis.py`) in the same directory.
3.  Open a terminal or command prompt.
4.  Navigate to the directory containing the files.
5.  Run the main application file using the following command:

    ```bash
    python main_toolkit.py
    ```

6.  Follow the on-screen menu prompts to use the toolkit.

# Syllabus Concepts Demonstrated

This project was built to specifically demonstrate mastery of the following concepts from the course syllabus:

**Modules and Functions:** The project is split into 3 distinct modules, with each task encapsulated in a well-defined function.
**Python Control Flow:** The main menu uses a `while True` loop and an extensive `if-elif-else` block for conditional logic. `break` is used for exiting the program.
**Data Structures:**
    **Lists:** Used for all array-based problems and for data input.
    **Sets:** Used for an efficient implementation of `remove_duplicates`.
    **Tuples:** Used for `tuple assignment` in the fibonacci_sequence function.
**Fundamental Algorithms:** Implements `Base Conversion`, `Fibonacci Sequence`.
**Factoring Methods:** Implements `GCD`, `Computing Prime Factors`, and `Raising a Number to Large Power`.
**Array Techniques:** Implements `Finding the Maximum`, `Removal of Duplicates`, and `Finding the Kth smallest element`.

---

**Author:**Avneesh joshi 25bce10737
**Course:**problem solving and introduction to programming CSE1021 
