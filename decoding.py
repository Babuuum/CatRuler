import base64


def save_image(images):
    for image in images:
        image_data = base64.b64decode(image)
        counter = 0
        with open(f"folder/generated_image{counter}.png", "wb") as file:
            file.write(image_data)
        return f"folder/generated_image{counter}.png"



