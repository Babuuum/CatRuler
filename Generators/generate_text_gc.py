import requests
import uuid
import json
import os
from dotenv import load_dotenv
# въебать бан циатам 18+


def generate_text(prompt, access_token='0'):
    load_dotenv()

    if access_token == '0':
        access_token = os.getenv('gc_access_token')

    prompt_text = f'сгенерируй короткую цитату {prompt}'
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": prompt_text
            }
        ],
        "stream": False,
        "repetition_penalty": 1
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'

    }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False).json()
    print(response)
    if 'choices' in response:
        return response['choices'][0]['message']['content']
    elif 'status' in response:
        if response['status'] == 401:
            new_access_token = new_token()
            return generate_text(prompt, new_access_token)


def new_token():

    load_dotenv()

    auth = os.getenv('gc_auth')

    rq_uid = str(uuid.uuid4())
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    payload = 'scope=GIGACHAT_API_PERS'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': rq_uid,
        'Authorization': f'Basic {auth}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False).json()
    print(response)
    access_token = response["access_token"]
    # new_token_save(access_token)
    print(access_token)
    return access_token


def new_token_save(new_token):
    file_path = "D:/Py repos/CatRuler/.env"
    key = 'gc_access_token'

    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                file.write(f"{key}= '{new_token}'\n")


if __name__ == "__main__":
    generate_text('самурай')
    # new_token()

# deep ai kryta9 shtyka