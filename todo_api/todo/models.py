from django.db import models


class TodoList(models.Model):
    text = models.CharField("Text", max_length=200, default=None)
    isCompleted = models.BooleanField(default=False)
    category = models.ForeignKey('TodoCategory', on_delete=models.CASCADE, null=True)


class TodoCategory(models.Model):
    title = models.CharField("Title", max_length=100, default=None, db_index=True)

    def __str__(self):
        return self.title

