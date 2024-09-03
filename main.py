import time
from datetime import datetime

from prompts import prompt_generation
from bot_main import send_message
from Generate_img.multi_img import multi_img
from save_img import save_image

if __name__ == '__main__':
    while True:
        current_time = datetime.now().strftime("%H:%M")
        print(current_time)
        if current_time == "04:00" or current_time == "08:00" or current_time == "16:00" or current_time == "20:00":
            prompt = prompt_generation()
            print(prompt)
            result = multi_img(4, prompt)
            path = save_image(result)
            send_message(path)
            time.sleep(3600)
        else:
            time.sleep(1800)



#naiti ra3meri i3obrajenii aktyal'nie dl9 vseh prikolov
#so3dat' osnovnie prompti
#os.env vnedrit'
#кота в разных популярных амплуа, японской культуры

#mojno v teorii sgenerirovat' 100 kotov po tegam naprimer, kot samyrai v stile barokko, gde teg bydet barokko, kot, samyrai
#gl9nytt' kak pisat' prompti

#vnedrit' konsolidaciu

#nyjna podyshka i3 i3obrajenii nyjna bd
#neirost' generusha9 na osnove tekyshih
#v teorii mojno perepyblikovivat' yspeshnie kartinki i3 neskol'kih grypp

#docker

#ybrat' url safe, ebanyt' 4ere3 oblako

#podobrat' aktyal'nie ra3meri

#v teorii mojet pomo4' grafana(opensource 9ndeks disk)
#podognat' ra3meri ra3reshenie i td
#v teorii mojno poiskat' neironky, kotora9 vedet kontrol' kaa4estva

#nado vivodit' tegi, vo vrem9 generacii i pyblikovat' ih
#tak je roflonadpis' v dyhe arta, v stile epohi i3 interesov kota, naprimer po kodeksy bysido, ne ykravshii so stola kolbasy, ne mojet na3ivat's9 samyraem
#tak je sobirat' laiki i views, i i3 etih laikov formirovat' grafiki po tegam, naprimer vse posti s etim tegom kakoi profit i td
#mojno dobavit' porody v prompt
#kak dobrat's9 do 5000 tis94 podpis4ikov, i skol'ko eto bydet stoit'
#davat' ves tegy, na osnove laikov


#strategii reklami
#sbor metrik
#bot kotorii testiryet effektivnost' reklami

#dopolnit' CatRuler proverkami i bd, a tak je tegami
#tak je ocenivat' yspeshnost' promptov
