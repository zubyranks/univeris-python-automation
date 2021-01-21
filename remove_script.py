import os
from create import copy_files

# Delete the files in folder 12


# Remove the files from the target directory
# print(os.getcwd())


def remove_files():

    # Delete the files in folder 12
    os.chdir("testproject/2018/12")
    for file in os.listdir():
        os.remove(file)
        # print(os.getcwd())

        # Delete the files in folder 11
        os.chdir("../11")
        for file in os.listdir():
            os.remove(file)

        # Delete the files in folder 10
        os.chdir("../10")
        for file in os.listdir():
            os.remove(file)

        # Delete the files in folder 09
        os.chdir("../09")
        for file in os.listdir():
            os.remove(file)

        # # Delete the files in folder 08
        # os.chdir("../08")
        # for file in os.listdir():
        #     os.remove(file)

        # # Delete the files in folder 07
        # os.chdir("../07")
        # for file in os.listdir():
        #     os.remove(file)

        # # Delete the files in folder 06
        # os.chdir("../06")
        # for file in os.listdir():
        #     os.remove(file)

        # # Delete the files in folder 05
        # os.chdir("../05")
        # for file in os.listdir():
        #     os.remove(file)

        # Delete the files in folder 04
        os.chdir("../04")
        for file in os.listdir():
            os.remove(file)

        # Delete the files in folder 03
        os.chdir("../03")
        for file in os.listdir():
            os.remove(file)

        # Delete the files in folder 02
        os.chdir("../02")
        for file in os.listdir():
            os.remove(file)

        # # Delete the files in folder 1
        # os.chdir("../01")
        # for file in os.listdir():
        #     os.remove(file)


print("********************************************************")
print("********************************************************")
print("All the files have been removed from each sub-folder")
print("********************************************************")
print("********************************************************")


remove_files()
