import os
import time
from datetime import datetime, timedelta
import base64


from Generators.multi_img import multi_img
from prompts import prompt_generation

from Sleeping_Posts.db_core import session
from Sleeping_Posts.models import Posts, Pictures

from Generators.generate_text_gc import generate_text
from Generators.generate_text_gemini import generate_text_g


def sleeping_posts_save(img_counter=10):
    post = session.query(Posts).all()
    base_path = post[0].folder_path[:-24]
    print(base_path)
    four_am = "04-00"
    eight_am = "08-00"
    four_pm = "16-00"
    eight_pm = "20-00"
    counter = 0
    day = 0
    # connsole logi

    last_file = post[-1].date

    print(last_file)

    my_date = last_file[-14:-6]
    time_counter = last_file[-5:]

    if time_counter == '20-00':
        day = my_date[-2:]
        day = int(day) + 1
        my_date = my_date[0:6] + str(day)
        my_full_date = datetime.strptime(my_date, "%y-%m-%d")
        day = 0

    print(my_date, time_counter)

    for i in range(img_counter):
        # s etim 4to to pridymat', mojno daje v odny dirrektoriu sohranit'
        if time_counter == 0:
            time_counter = four_am
        elif time_counter == four_am:
            time_counter = eight_am
        elif time_counter == eight_am:
            time_counter = four_pm
        elif time_counter == four_pm:
            time_counter = eight_pm
        else:
            time_counter = four_am

        img_list = img_generator()
        save_path = dir_creation(base_path, my_date, time_counter)
        text = generate_text_g(img_list[1][0])

        if text == "Нужно включить vpn":
            text = generate_text_g(img_list[1][0])

        print(time_counter)
        print(my_date, save_path, img_list, text)

        new_post = Posts(date=f"{my_date}_{time_counter}", folder_path=save_path, tags=f"{img_list[1][0]}, {img_list[1][1]}", post_text=text)
        session.add(new_post)
        # ybrat' cikl pyst' po na3vaniu vi3ivaet fynkciu

        for img in img_list[0]:
            img_name = f"CatRuler_{my_date}-{time_counter}_{counter}"
            counter += 1
            img_name = save_base64_image(img, save_path, img_name)
            my_post = session.query(Posts).filter_by(folder_path=save_path).first()
            post_id = my_post.id
            new_pic = Pictures(name=img_name, post_id=post_id)
            session.add(new_pic)
        session.commit()

        counter = 0

        if time_counter == "20-00":
            day += 1
            my_full_date = datetime.strptime(my_date, "%y-%m-%d")
            my_date = my_full_date + timedelta(days=day)
            my_date = my_date.strftime("%y-%m-%d")
            print(my_full_date, my_date)

        time.sleep(300)

    print("so3dano 40 filov")


def img_generator(img_counter=15):
    prompt = prompt_generation()
    print(prompt[1])
    result = multi_img(img_counter, prompt[0])
    print(len(result))
    return [result, prompt[1]]


def dir_creation(base_path, date, date_counter):
    directory_name = f"CatRuler_{date}_{date_counter}"
    full_path = f'{base_path}/{directory_name}'
    os.mkdir(full_path)
    print(full_path)
    return full_path


def save_base64_image(base64_string: str, save_path: str, file_name: str):
    image_data = base64.b64decode(base64_string[0])
    img_name = f'{file_name}.png'
    full_path = f'{save_path}/{img_name}'

    with open(full_path, 'wb') as file:
        file.write(image_data)

    print(f"Изображение под названием: {img_name} сохранено по пути: {full_path}")
    return img_name


if __name__ == "__main__":
    sleeping_posts_save(10)
