from Sleeping_Posts.db_core import session
from Sleeping_Posts.models import Posts

from tkinter import Tk, Label, Entry, Button
from PIL import Image, ImageTk

def tags_updater():
    for post in session.query(Posts).all():
        if post.tags == "no_tag":
            print(post.pictures[0].name)

            root = Tk()
            root.title("Открытие изображения")

            image_path = f"{post.folder_path}/{post.pictures[0].name}"  # Укажите путь к вашему изображению
            image = Image.open(image_path)

            photo = ImageTk.PhotoImage(image)

            label = Label(root, image=photo)
            label.pack()

            # Запускаем главный цикл Tkinter
            root.mainloop()

            tags = str(input("введите без ошибок теги из списка: образы: рыбак, самурай, инженер, байкер, хакер, айдол, кавбой, гонщик; \n"
                                 "стили: сакура, popart, Нихонга, ренесанс, vhs_horror, лавкрафт, cyberpunk, anime \n"
                                 "В формамте: образ, стиль например: рыбак, Нихонга\n"
                                 "Ввод: "))

            post.tags = tags
            session.add(post)
    session.commit()

if __name__ == '__main__':
    tags_updater()