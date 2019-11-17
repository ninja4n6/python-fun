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

try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile


"""
Module that extract text from MS XML Word document (.docx).
(Inspired by python-docx <https://github.com/mikemaccana/python-docx>)
"""

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'


def get_docx_text(path):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)

    paragraphs = []
    for paragraph in tree.getiterator(PARA):
        texts = [node.text
                 for node in paragraph.getiterator(TEXT)
                 if node.text]
        if texts:
            paragraphs.append(''.join(texts))

    return '\n\n'.join(paragraphs)


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