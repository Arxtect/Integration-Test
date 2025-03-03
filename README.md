# Integration-Test
This is for the integration test

For now, it can run, but it does not run properly. Due to the wasm compile issues, the current compileWeb.py is just a placeholder.



## Set up

* needs latex in your local as the compare group

* needs some packages you may pip when you see the error
* Replace test-files directory with your test directory.

## Instruction

### Step 1

git clone to local

```cmd
git clone git@github.com:Arxtect/Integration-Test.git
```

### Step 2

Run the main.py 

```cmd
python main.py
```

### Step 3

Check the result in the comparePDF.log file.

## Notice

* All the files in the ``test-files`` directory should be zip file, and each zip file contains a latex project.
* In each latex project, it should contain a ``main.tex`` file, otherwise, it will not compile properly.

* There are some parameters you can choose but for now you don't need to know, since it do not work properly now.
* I have uploaded a ``comparePDF.log`` as an example output of the ``test-files``. The result is basically in this form but, for now, is meaningless since I use the placeholder for the Webassembly compile.

