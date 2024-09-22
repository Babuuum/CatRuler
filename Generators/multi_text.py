from Generators.generate_text_gc import generate_text
from Generators.generate_text_gemini import generate_text_g


def multi_text(nubmer, prompt):
    all_text = []
    for laap in range(nubmer):
        all_text.append(generate_text_g(prompt)[1:-4])
    for laap in range(nubmer):
        all_text.append(generate_text(prompt)[1:-1])
    return all_text

if __name__ == "__main__":
    a = multi_text(3, 'самурай')
    print(a, len(a))
