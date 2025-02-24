import unzip
import os
import sys
import comparePDF
from wasmer import engine, Store, Module, Instance

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
# Step 1: Load the WebAssembly module
# store = Store(engine.Universal())
# module = Module(store, open("./SwiftLaTeX-arxtect/xetex.wasm", "rb").read())

# Step 2: Create an instance of the module
# instance = Instance(module)

# Step 3: Define a function to compile LaTeX
# def compile_latex(tex_file):
#     # Load the LaTeX source code
#     with open(tex_file, 'r') as f:
#         tex_code = f.read()
    
#     # Here you would need to interface with the WebAssembly module
#     # This part depends on how the WASM module is designed
#     # For example, if the module has a function `compile`:
    
#     # Call the WASM function to compile LaTeX
#     result = instance.exports.compile(tex_code)
    
#     return result

# # Step 4: Call the function with your .tex file
# output = compile_latex("example.tex")
# print(output)

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