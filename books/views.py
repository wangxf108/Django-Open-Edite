from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.views.generic.edit import UpdateView
from .models import Author 
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin



class HomeView(TemplateView):
    template_name = 'books/home.html'

class AuthorListView(ListView):
    model = Author
    template_name = 'books/author_list.html'

# createview 从表单拿到数据，并且将数据加入到模型中
class AuthorCreateView(CreateView):
    model = Author
    template_name = 'books/author_create.html'
    # 此处添加field，相当于创建了一个form，另外form也可以单独拿出去，创建一个form.py
    fields = ['name',]

    def form_valid(self, form):

        # 成功添加author，然后返回成功添加信息，调用的是父类的form_valid()
        messages.add_message(
            self.request, 
            messages.SUCCESS,
            'The author has been added'
        )
        return super().form_valid(form)


class AuthorDetailView(DetailView):
    model = Author
    template_name = "books/author_detail.html"



# SingleObjectMixin----select one item from database
# FormView----receive the form from page
class AuthorBooksUpadateView(SingleObjectMixin, FormView):

    model = Author
    template_name = 'books/author_book_edit.html'
