import os
from os import path

print("        ------------------------------------------------------")
print("""
      ________                ______                             
      ___  __ \_____ ________ ___  /______ _____________ ________
      __  /_/ /_  _ \___  __ \__  / _  __ `/_  ___/_  _ \__  ___/
      _  _, _/ /  __/__  /_/ /_  /  / /_/ / / /__  /  __/_  /    
      /_/ |_|  \___/ _  .___/ /_/   \__,_/  \___/  \___/ /_/     
                     /_/                                         
        """)
print("                        Replacer v1 04/29/2019")
print("                          Author: Duy Dao \n")
print("        ------------------------------------------------------\n")
print("         Type in the filename and extension of the file")
print("         containing words or characters that you wish to replace.")
print("         Hit Enter. (example: 'text.txt')\n")
print("         - Enter the 'Old Word' or old characters to be replaced.")
print("         - Enter the 'New Word' or characters that replaces.\n")
print("         Becareful of whitespace and inaccurate spelling.")
print("         This script WILL OVERWRITE your data.")
print("\n")
print("        Make sure this script is placed in the target directory")
print("        ------------------------------------------------------\n")

print("             CURRENT PATH: " + os.getcwd() + "\n")
filename = input("             Please enter filename with extension: ")
print("\n")


with open(filename, 'r') as f:
    newFile=f.read()
    print("         Please becareful as this script will overwrite your file\n")
    input1 = input('             Old Word: ')
    input2 = input('             New Word: ')
    print("\n             You words are now changed.")
    print("             Exiting...")

    while input1 in newFile:
        newFile=newFile.replace(input1, input2)
     
with open(filename, 'w') as f:
    f.write(newFile)
