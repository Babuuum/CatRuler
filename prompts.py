import random
prompts = ['кот самурай, в стиле попарт']
def prompt_generation():
    names = ['рыбак', 'самурай', 'инженер', 'лучник', 'байкер']
    background = []
    style = ['под сакурой', 'в визуальном стиле попарт', 'в визуальном стиле, Нихонга', 'в визуальном стиле ренесанс', 'в визуальном стиле vhs horror', 'в визуальном стиле проиведений лавкрафта', 'в визуальном стиле киберпанк', 'в стиле аниме']
    return f'нарисованный кот {random.choice(names)}, {random.choice(style)}'


#hoky, lavkraft, vhs_horros, renesans, cyberpunk
#mb l9gyshek
#cvet fona cvet osnovnogo arta
#4to bi 3alaikanie koti shli v istorii