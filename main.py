import os
import sys
import argparse
import comparePDF, compileLocal, unzip, clear, compileWeb
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
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            dir_list.append(full_path)
    return dir_list

# parameters
parser = argparse.ArgumentParser(description="Process some files.")
parser.add_argument('--mode', type=str, default='non-stop', help='Mode of operation')
parser.add_argument('--engine', type=str, default='xelatex', help='LaTeX engine to use')
args = parser.parse_args()
# make sure we are in the right directory
os.system("cd /Users/zhengbowen/nondefault/Intern/Arxtext")
clear.clear()

## define the directory and the unzip directory
mode = args.mode
engine = args.engine
directory = "./test-files"
unzip_dir = "./tem-unzipped-files"

# unzip the files
if not os.path.exists(unzip_dir):
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
    compileWeb.compile_latex(engine, dir)

# compare the files
result_list = list_directories("./Results")
for result in result_list:
    file_list = list_files(result)
    file_path1 = ""
    file_path2 = ""
    for file in file_list:
        if file.endswith("_local.pdf"):
            file_path1 = file
        elif file.endswith("_web.pdf"):
            file_path2 = file
        else:
            print(f"Skipping {file}")
    if file_path1 == "" or file_path2 == "":
        comparePDF.check_pdf(file_path1, result, "local")
        comparePDF.check_pdf(file_path2, result, "web")
        continue # error message 
    res = comparePDF.compare_pdf(file_path1, file_path2)
    if res is False:
        if mode == "stop":
            break
