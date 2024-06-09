import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly",1)
        self.assertEqual(magazine.name, "Tech Weekly")

    # def test_author_str_representation(self):
    #     author = Author(1, "John Doe")
    #     self.assertEqual(str(author), "Author(ID: 1, Name: John Doe)")

    def test_article_str_representation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(str(article), "Article(ID: 1, Title: Test Title, Author ID: 1, Magazine ID: 1)")

    # def test_magazine_str_representation(self):
    #     magazine = Magazine(1, "Tech Weekly", 1)
    #     self.assertEqual(str(magazine), "Magazine(ID: 1, Name: Tech Weekly)")

    # def test_article_create_method(self):
    #     article = Article.create(1, 1, "Test Title", "Test Content")
    #     self.assertEqual(article.title, "Test Title")
    #     self.assertEqual(article.content, "Test Content")

if __name__ == "__main__":
    unittest.main()
