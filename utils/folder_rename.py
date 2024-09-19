import os
import shutil
from datetime import datetime, timedelta

from Sleeping_Posts.sleeping_posts_db import add_or_update_item
# dobavit' fynkciu, dl9 sohraneni9 v db


def folder_rename(new_name, path):
    my_date = datetime.now().strftime("%y-%m-%d")
    my_full_date = datetime.strptime(my_date, "%y-%m-%d")
    folders_list = os.listdir(path)
    time_counter = 0
    day = 0

    for folder in folders_list:

        if time_counter == 0:
            time_counter = "04-00"
        elif time_counter == "04-00":
            time_counter = "08-00"
        elif time_counter == "08-00":
            time_counter = "16-00"
        elif time_counter == "16-00":
            time_counter = "20-00"
        else:
            time_counter = "04-00"
        folder_name = f"{new_name}_{my_date}_{time_counter}"
        folder_new_name = f"{path}/{folder_name}"
        os.mkdir(folder_new_name)
        pic_rename(f"{path}/{folder}", folder_new_name, folder_name)

        if time_counter == "20-00":
            day += 1
            my_date = my_full_date + timedelta(days=day)
            my_date = my_date.strftime("%y-%m-%d")
            print(my_full_date, my_date)

        os.rmdir(f"{path}/{folder}")


def pic_rename(path, new_path, folder_name):
    pic_list = os.listdir(path)
    counter = 0
    for pic in pic_list:
        # add_or_update_item(f"{pic}", f"{path}/{pic}", '0', f"{folder_name}_{counter}.png", f"{new_path}/{folder_name}_{counter}.png")
        shutil.copy2(f"{path}/{pic}", f"{new_path}/{folder_name}_{counter}.png")
        os.remove(f"{path}/{pic}")
        counter += 1

if __name__ == '__main__':
    folder_rename("CatRuler", "D:/Py repos/CatRuler/Sleeping_Posts/SP_folder")