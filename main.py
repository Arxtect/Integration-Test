import unzip
import os
import sys
import comparePDF, compileLocal
from wasmer import engine, Store, Module, Instance

# Get the list of the zip files needed
def list_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def list_directories(directory):
    dir_list = []
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            dir_list.append(os.path.join(root, dir))
    return dir_list

# make sure we are in the right directory
os.system("cd /Users/zhengbowen/nondefault/Intern/Arxtext")
engine = "xelatex"
## define the directory and the unzip directory
directory = "./test-files"
unzip_dir = "./tem-unzipped-files"

# unzip the files
file_list = list_files(directory)
for file in file_list:
    if file.endswith(".zip"):
        unzip.unzip_files(file, unzip_dir)
    else:
        print(f"Skipping {file}")
os.system(f"rm -rf ./tem-unzipped-files/__MACOSX")

dirs = list_directories(unzip_dir)
# compile the files locally
for dir in dirs:
    compileLocal.compile_latex(engine, dir)

# compare the files
file_path1 = "./file1.pdf"
file_path2 = "./file2.pdf"

mode = "non-stop"
if len(sys.argv) > 1:
    mode = sys.argv[1]

# if mode == "non-stop":
    # go through the whole directory and compare all files
# else mode == "stop":
    # stop when the first difference is found

res = comparePDF.compare_pdf(file_path1, file_path2)
if res is True:
    print("The two PDFs are identical.")
else:
    print("The two PDFs are different.")

# remove the unzipped files
# os.system(f"rm -rf ./tem-unzipped-files")