from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from posts.models import Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост',
        )

    def test_models_have_correct_lenght_str_post(self):
        """Проверка длины __str__ post."""
        error_name = f'Вывод не имеет {settings.LEN_OF_POSTS} символов'
        self.assertEqual(self.post.__str__(),
                         self.post.text[:settings.LEN_OF_POSTS],
                         error_name)


class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )

    def test_models_have_correct_lenght_str_group(self):
        """Проверка __str__ для group."""
        error_name = 'Вывод __str__ для group не совпадает с ожидаемым'
        self.assertEqual(self.group.__str__(),
                         self.group.title,
                         error_name)
