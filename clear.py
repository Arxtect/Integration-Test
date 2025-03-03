import os
# remove the unzipped files

def clear():
    os.system(f"rm -rf ./tem-unzipped-files")
    os.system(f"rm -rf ./Results")
    os.system(f"rm -rf comparePDF.log")

