# views.py
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Publisher, Book
from django.shortcuts import get_object_or_404


# url(r'^publishers/$', PublisherList.as_view()),

class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'


class PublisherDetail(DetailView):

    context_object_name = 'publisher'

    # to samo co model = Publisher
    queryset = Publisher.objects.all()  

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context


class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'


class AcmeBookList(ListView):

    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='ACME Publishing')
    template_name = 'books/acme_list.html'


# url(r'^books/([\w-]+)/$', PublisherBookList.as_view()),
class PublisherBookList(ListView):

    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherBookList, self).get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context