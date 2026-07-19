# Most computer programs need to store or retrieve information. 
 # A program may need to save user details, read configuration settings, 
 # process a large dataset, generate a report, or record application errors. 
# # Variables store data only while a program is running. Once the program stops,
 #  the values stored in memory are usually lost. 
#  Files provide a way to store data permanently so that it can be accessed later.
 # # Python provides built-in tools for creating, opening, reading, writing, 
 # updating, and deleting files. 
 # It also includes specialized modules for working
 #  with structured file formats such as CSV and JSON.
# A file is a collection of data stored on a storage device such as a hard drive, 
 # # solid-state drive, USB drive, or cloud storage system.
 # # Files usually have two main components: 
# # 1. File name :The name used to identify the file.
 # #    report.txt 
# #    students.csv
 # #    settings.json
 # #    photo.jpg 
#  2. **File extension** : The part after the final dot in the file name.  
# It often indicates the type of content stored in the file.
 # #    * `.txt` — plain text
 # #    * `.csv` — comma-separated values
 # #    * `.json` — JSON data
 # #    * `.py` — Python source code
 # #    * `.jpg` — image 
# #    * `.pdf` — PDF document 
# # A file extension helps users and programs understand 
#  the expected format, but it does not guarantee that the file
 #  actually contains that type of data.
# 4. Types of Files
 # # Python commonly works with two broad categories of files. 
# #  4.1 Text Files
 # # Text files store information as readable characters. 
# # Examples include:
 # # * Text documents
 # # * Python source files 
# # * CSV files 
# # * JSON files
 # # * HTML files 
# # * Log files 
# # A text file might contain:
 # # ```text
 # # Python is easy to learn.
 # # File handling allows permanent data storage.
 # When Python opens a file in text mode, it converts stored bytes into characters using an encoding such as UTF-8.
#   4.2 Binary Files:
 # # Binary files store information as raw bytes rather than directly readable text. 
# # Examples include:
 # # * Images 
# # * Audio files 
# # * Videos
 # # * PDF documents
 # # * Compressed archives 
# # * Executable files 
# # Binary data should normally be opened using binary modes such as `"rb"` or `"wb"`.
#   5. Opening a File :
# # Python uses the built-in `open()` function to open a file.
 # # ### Syntax # file_object = open(file_name, mode, encoding) 
# # The arguments are:
 # # * `file_name`: The name or path of the file. 
# # * `mode`: The operation to perform, such as reading or writing.
 # # * `encoding`: The character encoding used for text files.

# file = open("dict.py", "r", encoding="utf-8")
# content =file.read() 
# print(content)
# print(file.closed) 
# file.close() 
# print(file.closed) 

# # This statement opens `notes.txt` in read mode.
# #  6. File Modes # The file mode tells Python how the file will be used.
# # \ # | Mode  | Meaning                           
# # | ----- | ------------------------------------------------------ | 
# # | `"r"` | Opens a file for reading                         
# # |`"w"` | Opens a file for writing and replaces existing content
# # | `"a"` | Opens a file for appending                           
# # | `"x"` | Creates a new file and fails if it already exists      | |
# # | `"t"` | Opens a file in text mode                              
# # | `"b"` | Opens a file in binary mode                           
# # | `"+"` | Opens a file for both reading and writing              
# # ### Common combinations 
# # | Mode   | Description                                     
# # | ------ | ------------------------------------------------ |
# # | `"rt"` | Read a text file                             
# # | `"rb"` | Read a binary file                             
# # | `"wt"` | Write to a text file                            
# # | `"wb"` | Write to a binary file                           
# # | `"r+"` | Read and write without deleting existing content | 
# # | `"w+"` | Read and write while replacing existing content  | 
# # | `"a+"` | Read and append                                  | 
# # Text mode is the default mode. Therefore:
# # open("notes.txt", "r") == open("notes.txt", "r") 
# #Closing a File: 
# # After working with a file, it should be closed.

# file = open("Hello.py", "r", encoding="utf-8")
# content = file.read() 
# file.close() 

# # Closing a file:
# # * Releases system resources. 
# # * Ensures buffered data is written properly. 
# # * Prevents unnecessary file locks. 
# # * Reduces the chance of data corruption. 
# # A file can be checked using the `closed` attribute:
 
# file = open("Hello.py", "r", encoding="utf-8") 
# print(file.closed) # False 
# file.close() # file closing  
# print(file.closed) # true  

# # However, manually calling `close()` is not the preferred approach because an error 
# # may occur before Python reaches the closing statement.
# # 8. The `with` Statement 
# # The recommended way to work with files is the `with` statement. 
# # When the `with` block ends, Python closes the file automatically, 
# #  even if an exception occurs.

# with open("condition.py", "r", encoding="utf-8") as file: 
#   content = file.read()
#   print(content) 
#   print(file.closed) 
# print(file.closed)

# # This is called using a **context manager**.

# # Advantages of `with` include: 

# # * Automatic file closing
# # * Cleaner code 
# # * Safer resource management 
# # * Better exception handling
# # In most Python programs, file operations should use `with open(...)`.

# # Part I: Reading Text Files 

# #9. Reading an Entire File with `read()` 
# # The `read()` method reads the contents of a file. 
# # Suppose `message.txt` contains:
# #  text 
# # Welcome to Python. 
# # This chapter explains file handling.

# with open("condition.py", "r", encoding="utf-8") as file:
#   content = file.read() 
#   print(content)
#  # This chapter explains file handling.
#  # ``` # The returned content is a string. 
# # ```python
#   print(type(content)) 

# #Reading a limited number of characters 
# # A number can be passed to `read()`:

# with open("dict.py", "r", encoding="utf-8") as file: 
#  first_ten = file.read(10) 
#  print(first_ten) 

# #This reads at most ten characters. 
# # Reading an entire file is convenient, but it may use too much memory when the file is very large.
#  # 10. Reading One Line with `readline()` 
# # The `readline()` method reads one line at a time.

# with open("Hello.py", "r", encoding="utf-8") as file: 
#  first_line = file.readline() 
#  second_line = file.readline() 
#  print(first_line) 
#  print(second_line) 

# # A line usually ends with the newline character `\n`. 
# # To remove surrounding whitespace and the newline character, use `strip()`:

with open("tuple.py", "r", encoding="utf-8") as file: 
    first_line = file.readline().strip() 
print(first_line)

# # 11. Reading All Lines with `readlines()` 
# # The `readlines()` method reads all lines and returns them as a list.
 
# with open("tuple.py", "r", encoding="utf-8") as file: 
#  lines = file.readlines() 
#  print(lines)

# # Each item in the list represents one line.
#  # ```python for line in lines:   
#   
# print(line.strip())

#  # Although useful for small files, `readlines()` stores the entire file in memory. 
# #  12. Reading a File Line by Line 
#  # The most memory-efficient method for processing a text file is to iterate over the file object. 

with open("tuple.py", "r", encoding="utf-8") as file:
    for line in file:        
     print(line.strip())
# #Python reads each line when it is needed rather than loading the entire file at once. 
# # This approach is recommended for large files.
# #Example: Counting lines 

line_count = 0 
with open("tuple.py", "r", encoding="utf-8") as file:    
 for line in file:        
  line_count += 1         
print("Number of lines:", line_count) 

# # A shorter version is:  

#  with open("message.txt", "r", encoding="utf-8") as file: 
#    line_count = sum(1 for line in file)  
#  print("Number of lines:", line_count)

# #   13. Counting Words and Characters

#  with open("message.txt", "r", encoding="utf-8") as file: 
# content = file.read() 
# character_count = len(content) 
# word_count = len(content.split()) 
# line_count = len(content.splitlines()) 
# print("Characters:", character_count) 
# print("Words:", word_count) 
# print("Lines:", line_count) 

# #  The (`split)` method separates the text using whitespace.
# # The `splitlines()` method separates the text into lines without retaining newline characters.
# # Writing Text Files 
# #Writing with `"w"` Mode
# # The `"w"` mode opens a file for writing. 
# # If the file does not exist, Python creates it.
# # If the file already exists, Python deletes its current content before writing new data. 
# with open("session1/message.txt", "w", encoding="utf-8") as file: 
# file.write("We are learning python file system .And it is useful to handle different type of files  ") 

#  # Python file handling is useful. 

# # Important warning 

# # Opening an existing file in `"w"` mode removes its previous content immediately. 


# #  15. Writing Multiple Lines
#  # The `write()` method does not automatically add a newline. 

# with open("session1/message.txt", "w", encoding="utf-8") as file:
#     file.write("First line.\n")
#     file.write("Second line") 
#    file.write("Third line.") 

# # The `\n` escape sequence creates a new line.

#  # 16. Using `writelines()` 
# # # The `writelines()` method writes a sequence of strings.

# lines = [ 
#     "Apple\n",
#     "Banana", 
#     "Mango\n" 
#  ]
# with open("fruit.txt", "w", encoding="utf-8") as file: 
#     file.writelines(lines) 

# # `writelines()` does not automatically insert newline characters. 
# # They must be included in the strings. 
# # A more flexible alternative is:

#  fruits = ["Apple", "Banana", "Mango"] 
# with open("fruits.txt", "w", encoding="utf-8") as file: 
#     for fruit in fruits:
#   file.write(f"{fruit}\n") 

# #17. Appending with `"a"` Mode 
# # Append mode adds new content to the end of an existing file.  
# with open("activity.log", "a", encoding="utf-8") as file: 
#   file.write("User logged in.\n") 

# # Running the code multiple times adds multiple lines 
# #  instead of replacing the previous content. 
# # Append mode is useful for: 
# # * Log files 
# # * Transaction histories 
# # * Attendance records 
# # * Activity records 
# # * Audit trails 

# #  18. Creating a New File with `"x"` Mode 

# # The `"x"` mode creates a new file. 
# with open("output.txt", "x", encoding="utf-8") as file: 
#     file.write("This is a new file.") 

# # If `new_file.txt` already exists, Python raises a `FileExistsError`.

# #  try: 

# with open("new_file.txt", "x", encoding="utf-8") as file: 
#     file.write("This is a new file.") # except FileExistsError: 
#     print("The file already exists.")

# #   Use `"x"` when existing data must not be overwritten accidentally. 
# # File Positions :
# #. The File Pointer 
# # When a file is opened, Python maintains a current position called the 
# #  **file pointer** or **cursor**.
#   # The pointer indicates where the next read or write operation will occur
 
# with open("/Users/pinkisharma/Desktop/python/session1/fun.py", "r", encoding="utf-8") as file: 
#     print(file.read(6))
#     print(file.read(30))

# #  The second `read(5)` starts from the position where the first operation ended. 


# #Finding the Current Position with `tell()` 
# # The `tell()` method returns the current file position. 
# #
# with open("session1/fun.py", "r", encoding="utf-8") as file: 
#     print(file.tell()) 
#     file.read(5)
#     print(file.tell())

#  # In text mode, the returned value should be treated as an opaque position value rather 
#  # than always assuming it is a simple character number. 

# # Changing the Position with `seek()`
#  # The `seek()` method changes the current file position. 

# with open("session1/fun.py", "r", encoding="utf-8") as file:
#    first_read = file.read(7) 
#     print(first_read) 
#    file.seek(1) 
#    second_read = file.read(10) 
#    print(second_read) 

# # `file.seek(0)` moves the pointer back to the beginning. 
# # This is useful when a file needs to be read again without reopening it. 