from Sleeping_Posts.db_core import Base, engine
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Posts(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[str] = mapped_column(unique=True, nullable=False)
    folder_path: Mapped[str] = mapped_column(unique=True, nullable=False)
    pictures: Mapped[list['Pictures']] = relationship("Pictures", back_populates="post")
    tags: Mapped[str] = mapped_column(unique=False, nullable=False, default='no_tag')
    texts: Mapped[list['Texts']] = relationship("Texts", back_populates="post")
    #peremestit' v texts
    post_text: Mapped[str] = mapped_column(unique=False, nullable=False, default='no_text')
    published: Mapped[bool] = mapped_column(unique=False, nullable=False, default=False)
    published_date: Mapped[str] = mapped_column(unique=True, nullable=True)
    vk_stats:  Mapped['VK_stats'] = relationship("VK_stats", uselist=False, back_populates="post")


class Pictures(Base):
    __tablename__ = "pictures"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))
    post: Mapped['Posts'] = relationship("Posts", back_populates="pictures")
    to_publish: Mapped[bool] = mapped_column(unique=False, nullable=True)
    distortion: Mapped[bool] = mapped_column(unique=False, nullable=True)
    cat: Mapped[bool] = mapped_column(unique=False, nullable=True)
    fancy: Mapped[int] = mapped_column(unique=False, nullable=True)


class VK_stats(Base):
    __tablename__ = "vk_stats"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))
    post: Mapped['Posts'] = relationship("Posts", back_populates="vk_stats")
    vk_post_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    likes: Mapped[int] = mapped_column(unique=False, nullable=True)
    # mojno sdelat' foregin key, i hranit' commenti, tak je i u3erov
    comments: Mapped[int] = mapped_column(unique=False, nullable=True)
    views: Mapped[int] = mapped_column(unique=False, nullable=True)
    tags: Mapped[str] = mapped_column(unique=False, nullable=False)


class Texts(Base):
    __tablename__ = "texts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))
    post: Mapped['Posts'] = relationship("Posts", back_populates="texts")
    text: Mapped[str] = mapped_column(unique=False, nullable=False)


# inst -
# tg -
# mb v'ebat' v otdel'nii proekt vsu reklamy(krome toi kotora9 tegi 4ekaet)
# dl9 tg bota, id, tg_id, nickname, post_id(one to many), likes, banned

# ad - prosmotri laiki i podpiski, tg i vk
# nyjna tablica dl9 sbora obshih laikov, kommentov, podpisok i prosmotrov
# dobavit' v modeli kyda poidet, inst, vk, tg, inst+vk
Base.metadata.create_all(engine)
