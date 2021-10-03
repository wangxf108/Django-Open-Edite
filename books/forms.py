from django.forms.models import inlineformset_factory
from .models import Author, Book


# inlineformset_factory 这个函数属于一个magic ，可以将通过外键的形式，将book中，特定的author的book取出，也可以执行三个table
AuthorBooksFormset = inlineformset_factory(Author, Book, fields=('title',))