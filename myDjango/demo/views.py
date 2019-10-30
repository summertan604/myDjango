from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return HttpResponse("Hello, world!")


def detail(request):
    book_list = Book.objects.order_by('-pub_date')[:5]
    context = {'book_list': book_list}
    return render(request, 'demo/detail.html', context)


def add_book(request):
    if request.method == 'POST':
        temp_name = request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']

        from django.utils import timezone
        temp_book = Book(name=temp_name, author=temp_author, pub_house=temp_pub_house, pub_date=timezone.now())
        temp_book.save()
        return HttpResponseRedirect(reverse('demo:detail'))
    return render(request, 'demo/add.html')


def delete_book(request, book_id):
    temp_book_id = book_id
    Book.objects.filter(id=temp_book_id).delete()
    return HttpResponseRedirect(reverse('demo:detail'))


def edit_book(request, book_id):
    temp_book_id = book_id
    book = Book.objects.filter(id=temp_book_id).first()
    context = {'book': book}
    if request.method == 'POST':
        temp_name = request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']
        from django.utils import timezone
        Book.objects.filter(id=temp_book_id).update(name=temp_name, author=temp_author,
                                                    pub_house=temp_pub_house, pub_date=timezone.now())
        return HttpResponseRedirect(reverse('demo:detail'))
    return render(request, 'demo/edit.html', context)
