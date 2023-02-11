import os

file_path = "/Users/shivambhushan/Downloads/RESUME Shivam Bhushan.pdf"

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print('file has successfully been removed')

else:
    print('this file does not exist')