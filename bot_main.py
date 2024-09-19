import requests
import os
from dotenv import load_dotenv


def send_message(image):
    # with open(image, 'rb') as file:
    #     encoded_image = base64.urlsafe_b64encode(file.read()).decode('utf-8')

    load_dotenv()

    access_token = os.getenv('vk_access_token')
    token = os.getenv('vk_token')
    group_id = os.getenv('vk_group_id')
    version_vk = os.getenv('version_vk')
    album_id = os.getenv('vk_album_id')
    print(access_token, token, group_id, version_vk, album_id)

    url = 'https://api.vk.com/method/photos.getUploadServer'
    response_from_getUploadServer = requests.post(
        url=url,
        params={
            'access_token': access_token,
            'group_id': group_id,
            'v': version_vk,
            'album_id': album_id,
        }
    )

    url = response_from_getUploadServer.json()['response']['upload_url']
    json_response_from_UploadServer = requests.post(
        url=url,
        files={
            'file1': (
                image[0],
                open(image[0], 'rb'),
                'multipart/form-data',
            ),
            'file2': (
                image[1],
                open(image[1], 'rb'),
                'multipart/form-data',
            ),
            'file3': (
                image[2],
                open(image[2], 'rb'),
                'multipart/form-data',
            ),
            'file4': (
                image[3],
                open(image[3], 'rb'),
                'multipart/form-data',
            ),
        }
    ).json()
    print(json_response_from_UploadServer)

    url = "https://api.vk.com/method/photos.save"
    response = requests.post(
        url=url,
        params={
            'access_token': access_token,
            'v': version_vk,
            'album_id': album_id,
            'group_id': group_id,
            'server':json_response_from_UploadServer['server'],
            'photos_list':json_response_from_UploadServer['photos_list'],
            'hash': json_response_from_UploadServer['hash'],
        }
    )
    print(response.json())

    url = "https://api.vk.com/method/wall.post"
    response = requests.post(
        url=url,
        params={
            'access_token': token,
            'from_group': 1,
            'owner_id': f'-{group_id}',
            'attachments': [f'photo-{group_id}_{response.json()["response"][0]["id"]},'
                            f'photo-{group_id}_{response.json()["response"][1]["id"]},'
                            f'photo-{group_id}_{response.json()["response"][2]["id"]},'
                            f'photo-{group_id}_{response.json()["response"][3]["id"]}'],
            'v': version_vk,
        }
    )

    print(response.json())

#https://zenno.pro/kak-poluchit-access-token-prilozheniya-vk-com/ dl9 poly4eni9 tokena