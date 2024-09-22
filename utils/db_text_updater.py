import time

from Sleeping_Posts.db_core import session
from Sleeping_Posts.models import Posts, Texts
from Generators.generate_text_gc import generate_text
from Generators.generate_text_gemini import generate_text_g
from Generators.multi_text import multi_text



def text_updater_old():
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

def text_updater():
    posts = session.query(Posts).all()

    for post in posts:
        tag = post.tags.split(', ')[0]
        text_list = multi_text(2, tag)
        post_id = post.id
        for new_text in text_list:
            text = Texts(post_id=post_id, text=new_text)
            session.add(text)
    session.commit()


def miss_values():
    texts = session.query(Texts).all()

    for text in texts:
        if text.text == 'ужно включить' or text.text == 'Нужно включить vpn':
            tag = session.query(Posts).filter_by(id=text.post_id).first()
            text.text = generate_text_g(tag)
            if text.text == 'Нужно включить vpn':
                text.text = generate_text_g(tag)
        session.add(text)
    session.commit()

if __name__ == '__main__':
    #text_updater()
    miss_values()
    #text_updater_old()