from django.utils import timezone
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)


# Create new model for Author
#     Author should have properties for first_name and last_name
#     Create a new model for Post
#     Post should have properties for title, content, date_posted, and author -- date_posted should automatically populate with current date on create -- author should be a foreign key that points back to the Author of the post(s)