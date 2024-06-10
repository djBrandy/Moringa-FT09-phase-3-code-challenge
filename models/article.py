# class Article:
#     def __init__(self, id, title, content, author_id, magazine_id):
#         self.id = id
#         self.title = title
#         self.content = content
#         self.author_id = author_id
#         self.magazine_id = magazine_id

#     def __repr__(self):
#         return f'<Article {self.title}>'
from database.setup import get_db_connection
class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._id = id
        self._author_id = author_id
        self._magazine_id = magazine_id
        self._title = title
        self._content = content
    @property
    def id(self):
        return self._id
    @property
    def author_id(self):
        return self._author_id
    @property
    def magazine_id(self):
        return self._magazine_id
    @property
    def title(self):
        return self._title
    @property
    def content(self):
        return self._content
    @classmethod
    def create(cls, author_id, magazine_id, title, content):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (author_id, magazine_id, title, content) VALUES (?, ?, ?, ?)', (author_id, magazine_id, title, content))
        conn.commit()
        article_id = cursor.lastrowid
        conn.close()
        return cls(article_id, title, content, author_id, magazine_id)
    def __str__(self):
        return f"Article(ID: {self._id}, Title: {self._title}, Author ID: {self._author_id}, Magazine ID: {self._magazine_id})"
