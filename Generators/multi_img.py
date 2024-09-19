import time

from Generators.generate_img import img_creation
from prompts import prompt_generation
from save_img import save_image


def multi_img(number, prompt):
    counter = 0
    result = []
    while number > counter:
        try:
            result.append(img_creation(prompt))
            counter += 1
        except:
            time.sleep(300)
    return result
