from Generate_img.generate_img import img_creation
from prompts import prompt_generation
from save_img import save_image


def multi_img(number, prompt):
    counter = 0
    result = []
    while number > counter:
        result.append(img_creation(prompt))
        counter += 1
    print(len(result))
    return result
