from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Todo(TimeStampMixin):
    title = models.CharField(max_length=100)
    description = models.TextField()
    favourite = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)

    def __str__(self):
        return self.title