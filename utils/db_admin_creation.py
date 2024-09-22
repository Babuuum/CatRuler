import os

from Sleeping_Posts.db_core import session
from Sleeping_Posts.models import Posts, Pictures

from typing import List, Dict


def spm_posts_db_autocompletion(path):
    folders_list = os.listdir(path)
    for folder in folders_list:
        post_path = f"{path}/{folder}"
        date = folder[9:]

        print(folder)

        post = Posts(date=date, folder_path=post_path)

        session.add(post)

        spm_pictures_db_autocompletion(post_path)
        print(f"{post_path}, добавленна в базу данных")
    session.commit()


def spm_pictures_db_autocompletion(post_path):
    pic_list = os.listdir(post_path)
    for name in pic_list:
        post = session.query(Posts).filter_by(folder_path=post_path).first()
        post_id = post.id

        picture = Pictures(name=name, post_id=post_id)
        session.add(picture)

        print(f"{name}, добавленна в базу данных")
    session.commit()


def show_data_base():
    # Вывод данных из таблицы Posts
    print("Posts:")
    for post in session.query(Posts).all():
        print(
            f"ID: {post.id}, Date: {post.date}, Pictures: {post.pictures}, Folder Path: {post.folder_path}, Tags: {post.tags}, Post Text: {post.post_text}, Published: {post.published}, Published Date: {post.published_date}")
        for pic in post.pictures:
            print(pic.name)
    # Вывод данных из таблицы Pictures
    print("\nPictures:")
    for picture in session.query(Pictures).all():
        print(
            f"ID: {picture.id}, Name: {picture.name}, Post ID: {picture.post_id}, To Publish: {picture.to_publish}, Distortion: {picture.distortion}, Cat: {picture.cat}, Fancy: {picture.fancy}")


if __name__ == '__main__':
    # spm_posts_db_autocompletion("D:/Py repos/CatRuler/Sleeping_Posts/SP_folder")
    show_data_base()
