import time

from Sleeping_Posts.db_core import session
from Sleeping_Posts.models import Posts
from Generators.generate_text_gc import generate_text
from Generators.generate_text_gemini import generate_text_g



def text_updater():
    for post in session.query(Posts).all():
        # if post.post_text == "no_text":
        if post.post_text == "Нужно включить vpn":

            prompt = post.tags.split(', ')[0]
            new_text = generate_text_g(prompt)

            post.post_text = new_text
            print(new_text)
            session.add(post)
            time.sleep(5)

    session.commit()


if __name__ == '__main__':
    text_updater()