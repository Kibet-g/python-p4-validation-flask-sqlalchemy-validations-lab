#!/usr/bin/env python3

from random import choice as rc

from faker import Faker

from app import app
from models import db, Author, Post

fake = Faker()

with app.app_context():

    Author.query.delete()
    Post.query.delete()

    authors = []
    for n in range(25):
        author = Author(
            name=fake.unique.name(),
            phone_number=str(fake.random_number(digits=10, fix_len=True))
        )
        authors.append(author)

    db.session.add_all(authors)
    posts = []
    for n in range(25):
        post = Post(
            title=rc(["Won't Believe This Secret", "Top 10 Secrets", "Guess What Happened"]),
            content=fake.paragraph(nb_sentences=50),
            category=rc(['Fiction', 'Non-Fiction']),
            summary=fake.text(max_nb_chars=250)
        )
        posts.append(post)

    db.session.add_all(posts)

    db.session.commit()
