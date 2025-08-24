# Files, Exceptions, and Errors in Python

This repository contains two simple Python programs that demonstrate basic file handling operations in Python.



## Task 1: Read a File and Handle Errors
**File:** `task1_read_file.py`

### Problem Statement:
- Opens and reads a text file named `sample.txt`.
- Prints its content line by line.
- Handles errors gracefully if the file does not exist.

### Expected Output:
If the file exists:
```

Reading file content:
Line 1: This is a sample text file.
Line 2: It contains multiple lines.
Line 3: You can add more lines here.
Line 4: Python will read them one by one.

```

If the file does not exist:
```

Error: The file 'sample.txt' was not found.

```

---

## Task 2: Write and Append Data to a File
**File:** `task2_write_append.py`

### Problem Statement:
- Takes user input and writes it to a file named `output.txt`.
- Appends additional data to the same file.
- Reads and displays the final content of the file.

### Expected Output:
```

Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.
Enter additional text to append: Learning file handling in Python.
Data successfully appended.
Final content of output.txt:
Hello, Python!
Learning file handling in Python.

