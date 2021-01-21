testproject folder:
1. It represents the source data and I do have some samples in it.
2. Some of the sample files will have multiple entry just to test my script can iterate multiple times which it does. E.g. month of September has thee entries
3. This script has no limit on the number of files it can add to the folder as long as the files are for the year 2018. 

copy_script.py module
4. To add the files to the target directory, run the "copy_script.py" command
5. My script is idempotent, okay to run the command multiple times

remove_script.py module
6. To remove all the files from each sub-folder in the 2018 folder, run the "remove_script.py" command
7. You will be required to enable/disable some of the scripts in the "Delete file in folder #"
8. Only enable/disable based on the sub-folders that have been created


