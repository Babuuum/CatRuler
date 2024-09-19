import os
import shutil


from Sleeping_Posts.db_core import session



from Sleeping_Posts.db_core import engine
from Sleeping_Posts.models import Sleeping_Posts
from Sleeping_Posts.sleeping_posts_db import add_or_update_item


# sdelat' vivod vseh i3obrajenii v okno
# prostoi cikl s inpytami i outpytami i sohraneniem v db





def sleeping_posts_marker():
    items = session.query(Sleeping_Posts).all()
    tags = '0'
    counter = 0
    for item in items:
        counter += 1
        if item.published != True:
            print(f"{item.name} измените пост")

            if item.distortion == None:
                distortion = input('есть ли искажения? +/-: ')
                if distortion == '+':
                    item.distortion = True
                elif distortion == '-':
                    item.distortion = False
                else:
                    print('hyin9')

            if item.cat == None:
                cat = input('на картинке кот? +/-: ')
                if cat == '+':
                    item.cat = True
                elif cat == '-':
                    item.cat = False
                else:
                    print('hyin9')

            if item.fancy == None:
                fancy = int(input('оцените картинку по 10-тибальной: '))
                if fancy >= 0 and fancy <= 10:
                    item.fancy = fancy
                else:
                    print('hyin9')

            if tags != '0':
                item.tags = tags
            elif item.tags == '0' or item.tags == None:
                tags = str(input("введите без ошибок теги из списка: образы: рыбак, самурай, инженер, байкер, хакер, айдол, кавбой, гонщик; \n"
                                 "стили: сакура, popart, Нихонга, ренесанс, vhs_horror, лавкрафт, cyberpunk, anime \n"
                                 "В формамте: образ, стиль например: рыбак, Нихонга\n"
                                 "Ввод: "))

        if counter == 10:
            break


            #viberete kotov 4 kotov v odnom stile i nastroenie, raspolojite ih v ramkah topa po krasote
        session.commit()



if __name__ == '__main__':
    sleeping_posts_marker()

# peredelat' vs pod novyu db
# a tak je 4to bi vse bralos' i3 db

# final'nii re3yl'tat, doljen soderjat' kota v opredelennom settinge, be3 iskajenii, vse pik4i doljni bit' c opredelennom stile, tekst doljen bit', ne 18+, ne soderjat' ekstremistkie viska3ivani9 ili syicidal'nie