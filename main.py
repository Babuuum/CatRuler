import json
import time
from datetime import datetime

import requests
from decoding import save_image
from bot_main import send_message
from prompts import prompt_generation


class Text2ImageAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=1  , width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        print(data)
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)

def img_creation(prompt):
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '4C32278F0269204483679DB7E4E1C17D',
                        '218513EA52E81B78F4BD3DCAC78F4967')
    model_id = api.get_model()
    uuid = api.generate(prompt, model_id)
    images = api.check_generation(uuid)
    print(images)
    return images


if __name__ == '__main__':
    while True:
    #     current_time = datetime.now().strftime("%H:%M")
    #
    #     if current_time == "03:45" or current_time == "18:00":
        prompt = prompt_generation()
        print(prompt)
        result = img_creation(prompt)
        path = save_image(result)
        send_message(path)
        time.sleep(3600)



#надо что бы он принимал промпт
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
