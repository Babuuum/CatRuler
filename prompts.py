import random


prompts = ['кот самурай, в стиле попарт']


def prompt_generation():
    names = ['рыбак', 'самурай', 'инженер', 'байкер', 'хакер', 'айдол', 'кавбой', 'гонщик']
    background = []
    style = {'под сакурой': 'сакура', 'в визуальном стиле попарт': 'popart', 'в визуальном стиле, Нихонга': 'Нихонга', 'в визуальном стиле ренесанс': 'ренесанс', 'в визуальном стиле vhs horror': 'vhs_horror', 'в визуальном стиле проиведений лавкрафта': 'лавкрафт', 'в визуальном стиле киберпанк': 'cyberpunk', 'в стиле аниме': 'anime'}
    pose_action = []
    # порода
    species = []

    name_tag = random.choice(names)
    key_list = list(style.keys())
    style_tag = random.choice(key_list)

    prompt = [f'нарисованный кот {name_tag}, {style_tag}', [name_tag, style[style_tag]]]

    print(prompt)
    return prompt


#hoky, lavkraft, vhs_horros, renesans, cyberpunk
#mb l9gyshek
#cvet fona cvet osnovnogo arta
#4to bi 3alaikanie koti shli v istorii
#добавить выборку популярных тегов на каждый запрос например вместо сакура, [сакура, sakura, япония], добавлять общие теги