import unzip
import os

# Get the list of the zip files needed
def list_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

# make sure we are in the right directory
os.system("cd /Users/zhengbowen/nondefault/Intern/Arxtext")

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

# compile the files

# compare the files

# remove the unzipped files
# os.system(f"rm -rf ./tem-unzipped-files")