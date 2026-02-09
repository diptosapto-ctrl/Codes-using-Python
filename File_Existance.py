from pathlib import Path
file_name=Path("C:/Users/User/file1.txt")
if file_name.exists():
    print("File exists can not create")
else:
    print("File doesn't exists, Creating!!")

    fh=open("file_name","xt")
    fh.write("Congrats!! You just created a nbew file")
    fh.close()

