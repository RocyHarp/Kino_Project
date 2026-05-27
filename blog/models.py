from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва фільму")
    content = models.TextField(verbose_name="Огляд фільму")
    author_name = models.CharField(max_length=100, verbose_name="Автор огляду")
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100, verbose_name="Глядач")
    content = models.TextField(verbose_name="Текст коментаря")
    created_at = models.DateTimeField(auto_now_add=True)