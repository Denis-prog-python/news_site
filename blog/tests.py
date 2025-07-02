from django.test import TestCase
from .models import Post
from django.utils import timezone

class PostModelTest(TestCase):
    def test_post_creation(self):
        post = Post.objects.create(
            title="Тестовая новость",
            content="Это тестовое содержание новости",
            author_name="Тестовый автор"
        )
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), post.title)