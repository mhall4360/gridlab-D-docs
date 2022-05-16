# Script name       : Python test- line test 
# Link              : https://github.com/geekcomputers/Python/blob/master/testlines.py
# Created           : 5-16-22
# Description       : learning how to use python with online test
# Purpose           : Open up a file and writes whatever is set "

def write_to_file(filename, txt):
  with open(filename, "w") as file_object:
    s = file_object.write(txt)
    
if __name__ == "__main__":
  write_to_file("test.txt", "I am beven")
