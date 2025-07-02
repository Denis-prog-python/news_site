from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    author_name = models.CharField(max_length=100, verbose_name="Автор")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'