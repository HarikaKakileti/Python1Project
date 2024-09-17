#Escape Sequence
print("Hello World")
print("Hello\nWorld")  # \n - newline
print("Hello\tWorld")  # \t - tabline
print("Hello\bWorld")  # \b - backspace


dir = 'C:\Harika\n.txt'

#To overcome this issue we need to use double quotes but output will be printed in two lines
dir = "C:\Harika\n.txt"
print(dir)
#where this r concept will be used  - Automation API,Web Automation,file_path = r concept
# double and single quote will give output for raw text
dir = r"C:\Harika\n.txt"  # r can be used to print raw text
dir1 = r'C:\Harika\n.txt'  # r can be used to print raw text
print(dir)
print(dir1)

