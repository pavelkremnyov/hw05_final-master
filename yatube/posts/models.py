from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200, verbose_name='Название сообщества')
    slug = models.SlugField(
        unique=True,
        verbose_name='Тэг сообщества',
        help_text='Укажите одним словом тематику сообщений в сообществе')
    description = models.TextField(
        verbose_name='Описание сообщества')

    class Meta:
        verbose_name = 'Сообщество',
        verbose_name_plural = 'Сообщества'

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст сообщения')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        'Group',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='group',
        verbose_name='Сообщество'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True
    )

    class Meta:
        verbose_name = 'Сообщение',
        verbose_name_plural = 'Сообщения'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:settings.LEN_OF_POSTS]


class Comment(models.Model):
    post = models.ForeignKey(
        Post, blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('Текст комментария',
                            help_text='Введите текст комментария')
    created = models.DateTimeField(
        'Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='follower')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')
