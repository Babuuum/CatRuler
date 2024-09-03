import requests
import base64
# acess_token = 'vk1.a.JIYnQvrq1T6lNnl9yP6vBV1tbm3mbH7edMpPb1imtSBHNsJEkHZS1-DUW_cikzOf7x2_e0z9NTYj7TOyqgIn6njQ-AvONKqRL2CZHW0NMUXnCjnxGlZGTcziSdT3YJfazNrWfpuXB8FND-1wXL6SIjEDTYovoJZ0gw75IxJkkewP5xud9neFeJ5K0DFBwCShsghftdVN0G0Svn8T5J2GAQ'
# url = 'https://api.vk.com/method/photos.getUploadServer'
# response_from_getUploadServer = requests.post(
#     url=url,
#     params={
#         'access_token': acess_token,
#         'group_id': 209710041,
#         'v': "5.199",
#         'album_id': 282399639,
#     }
# ).json()
# print(response_from_getUploadServer)
# test = requests.get('https://id.vk.com/authorize?response_type=code&client_id=52203073scope=groups%20wall%20photos&redirect_uri=https%3A%2F%2FCatRuler.com&state=XXXRandomZZZ&code_challenge=K8KAyQ82WSEncryptedVerifierGYUDj8K&code_challenge_method=s256')
# print(test.text)


def send_message(image):
    # with open(image, 'rb') as file:
    #     encoded_image = base64.urlsafe_b64encode(file.read()).decode('utf-8')

    access_token = 'vk1.a.JIYnQvrq1T6lNnl9yP6vBV1tbm3mbH7edMpPb1imtSBHNsJEkHZS1-DUW_cikzOf7x2_e0z9NTYj7TOyqgIn6njQ-AvONKqRL2CZHW0NMUXnCjnxGlZGTcziSdT3YJfazNrWfpuXB8FND-1wXL6SIjEDTYovoJZ0gw75IxJkkewP5xud9neFeJ5K0DFBwCShsghftdVN0G0Svn8T5J2GAQ'

    token = '7b68af4d9ed314ac12be15e3f589aff54f604c38012c00f6200ca95af4e877172e9a50e5316cee07729f6'
    group_id = 209710041
    group_id_1 = 52203073
    version_vk = "5.199"
    album_id = 282399639

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