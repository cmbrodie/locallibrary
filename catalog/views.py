from django.shortcuts import render


from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site"""

    # Generate counts of some of the main objects
    booklist = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    bookword = Book.objects.filter(title__contains="lord").count()
    genreword = Genre.objects.filter(name__contains="fantasy").count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()

    # The 'all()' is implied by default
    num_authors = Author.objects.count()

    context = {
        "genreword": genreword,
        "bookword": bookword,
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "booklist": booklist,
    }

    return render(request, "index.html", context=context)


class BookListView(generic.ListView):
    model = Book
    # context_object_name = "book_list"
    # queryset = Book.objects.filter(title__contains="Si")
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context dict
        return context

    # change the ordering:
    queryset = Book.objects.order_by("title")
    paginate_by = 2
    # pages accessed by passing GET params: to access page 2 /catalog/books/?page=2


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    # context_object_name = "author_list"


class AuthorDetailView(generic.DetailView):
    model = Author
