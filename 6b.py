# Write a python program to create a ZIP file of a particular folder which contains several files inside it
import os
import sys
import pathlib
import zipfile

dirname = input("Enter directory name that you want to zip: ")
if not os.path.isdir(dirname):
  print("Directory doesnot exists ")
  sys.exit(0)

curDir = pathlib.Path(dirname)
with zipfile.ZipFile("myzip.zip", mode='w') as archive:
  for file_path in curDir.rglob("*"):
    archive.write(file_path, os.path.relpath(file_path, curDir))

if os.path.isfile("myzip.zip"):
  print("Zip file created successfully")
else:
  print("zip file failed")