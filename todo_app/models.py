from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True) #blank - необязательно к заполнению
    created = models.DateTimeField(auto_now_add=True) # auto_now_add - значение создается автоматически
    datecompleted = models.DateTimeField(null=True, blank=True) # делаем отметку о выполнении (аналогично blank, но в дататх, т.к. есть четкие рамки используем null, blank добавили чтобы не было обязательно при создании через админку
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): # для отображения назания
        return self.title

