import base64


def save_image(images):
    img_list = []
    counter = 0
    for image in images:
        image_data = base64.b64decode(image[0])
        with open(f"folder/generated_image{counter}.png", "wb") as file:
            file.write(image_data)
        img_list.append(f"folder/generated_image{counter}.png")
        counter += 1
    print(img_list)
    return img_list



