import os
import shutil


def copy_files():

    # Display a list of directories
    # print(os.listdir())

    # Change path to folder containing files
    os.chdir("testproject")

    # Obtain the list of files in the directory
    try:

        for file in os.listdir():
            file_name, file_ext = os.path.splitext(file)

            # print(file_name)
            file_prefix, file_surfix = os.path.splitext(file_name)

            # Remove the dot from the surfix
            file_surfix = file_surfix.strip()[1:]

            # Unpacking the date into dd, mm & yy
            file_day = file_surfix.strip()[:2]
            file_month = file_surfix.strip()[2:4]
            file_year = file_surfix.strip()[4:6]
            # print(file_month)

        # Change file format if you need to re-arrange the current format
        # new_file_format = '{}-{}'.format(file_surfix, file_prefix)
        # print(new_file_format)

            # # Make folders by month and copy files by the month it was created into month-folder subdirectory

            if (file_year == str(18)) and (file_month == str("12")):
                os.makedirs("2018/12", exist_ok=True)
                shutil.move(file, '2018/12/')
            if (file_year == str(18)) and (file_month == str("11")):
                os.makedirs("2018/11", exist_ok=True)
                shutil.move(file, '2018/11')
            if (file_year == str(18)) and (file_month == str("10")):
                os.makedirs("2018/10", exist_ok=True)
                shutil.move(file, '2018/10')
            if (file_year == str(18)) and (file_month == str("09")):
                os.makedirs("2018/09", exist_ok=True)
                shutil.move(file, '2018/09')
            if (file_year == str(18)) and (file_month == str("08")):
                os.makedirs("2018/08", exist_ok=True)
                shutil.move(file, '2018/08')
            if (file_year == str(18)) and (file_month == str("07")):
                os.makedirs("2018/07", exist_ok=True)
                shutil.move(file, '2018/07')
            if (file_year == str(18)) and (file_month == str("06")):
                os.makedirs("2018/06", exist_ok=True)
                shutil.move(file, '2018/06')
            if (file_year == str(18)) and (file_month == str("05")):
                os.makedirs("2018/05", exist_ok=True)
                shutil.move(file, '2018/05')
            if (file_year == str(18)) and (file_month == str("04")):
                os.makedirs("2018/04", exist_ok=True)
                shutil.move(file, '2018/04')
            if (file_year == str(18)) and (file_month == str("03")):
                os.makedirs("2018/03", exist_ok=True)
                shutil.move(file, '2018/03')
            if (file_year == str(18)) and (file_month == str("02")):
                os.makedirs("2018/02", exist_ok=True)
                shutil.move(file, '2018/02')
            if (file_year == str(18)) and (file_month == str("01")):
                os.makedirs("2018/01", exist_ok=True)
                shutil.move(file, '2018/01')

        # print(os.getcwd())
        # print(os.getcwd())

    except FileExistsError as e:
        print(e)
