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
    def test_author_str_representation(self):
        author = Author(1, "John Doe")
        self.assertEqual(str(author), "Author(ID: 1, Name: John Doe)")
    def test_article_str_representation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(str(article), "Article(ID: 1, Title: Test Title, Author ID: 1, Magazine ID: 1)")
    def test_magazine_str_representation(self):
        magazine = Magazine(1, "Tech Weekly", 1)
        self.assertEqual(str(magazine), "Magazine(ID: 1, Name: Tech Weekly)")
    def test_article_create_method(self):
        article = Article.create(1, 1, "Test Title", "Test Content")
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")
    def test_magazine_articles(self):
        magazine = Magazine.create("Tech Weekly", "Tech")
        Article.create(1, magazine.id, "Test Title", "Test Content")
        self.assertEqual(len(magazine.articles()), 1)
    def test_magazine_setters(self):
        magazine = Magazine(1, "Tech Weekly", "Tech")
        magazine.name = "New Name"
        magazine.category = "New Category"
        self.assertEqual(magazine.name, "New Name")
        self.assertEqual(magazine.category, "New Category")
    def test_magazine_getters(self):
        magazine = Magazine(1, "Tech Weekly", "Tech")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Tech")
    def test_magazine_articles_with_no_articles(self):
        magazine = Magazine.create("Tech Weekly", "Tech")
        self.assertEqual(magazine.articles(), [])
    def test_magazine_contributors_with_no_contributors(self):
        magazine = Magazine.create("Tech Weekly", "Tech")
        self.assertEqual(magazine.contributors(), [])
    def test_magazine_getters_with_different_inputs(self):
        magazine = Magazine(1, "Tech Weekly", "Tech")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Tech")
        magazine.name = "New Name"
        magazine.category = "New Category"
        self.assertEqual(magazine.name, "New Name")
        self.assertEqual(magazine.category, "New Category")
    def test_magazine_getters_with_different_inputs(self):
        magazine = Magazine(1, "Tech Weekly", "Tech")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Tech")
        magazine.name = "New Name"
        magazine.category = "New Category"
        self.assertEqual(magazine.name, "New Name")
        self.assertEqual(magazine.category, "New Category")
if __name__ == "__main__":
    unittest.main()
