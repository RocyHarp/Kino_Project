from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Action', 'Бойовик'),
        ('Comedy', 'Комедія'),
        ('Drama', 'Драма'),
        ('Sci-Fi', 'Фантастика'),
    ]

    title = models.CharField(max_length=200, verbose_name="Назва")
    content = models.TextField(verbose_name="Огляд")
    author_name = models.CharField(max_length=100, verbose_name="Автор")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Action', verbose_name="Категорія")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def str(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100, verbose_name="Автор коментаря")
    content = models.TextField(verbose_name="Коментар")
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Коментар від {self.author_name}"