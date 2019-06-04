from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse

from book import models

# Create your views here.

def add_book(request):
    if request.method == 'GET':
        return render(request, "add_book.html")
    else:
        title = request.POST.get('title')
        price = request.POST.get('price')
        publisher = request.POST.get('publisher')
        pub_date = request.POST.get('pub_date')
        models.BookMS.objects.create(title=title, price=price,
            publisher=publisher, pub_date=pub_date)
        return redirect("/list_book/")

def list_book(request):
    books = models.BookMS.objects.all()
    print(books)
    return render(request, "list_book1.html", {'books':books})

def edit_book(request, book_id):
    if request.method == "GET":
        book = models.BookMS.objects.filter(pk=book_id).first()
        return render(request, "edit_book.html", {"book":book})
    else:
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']
        print(data)
        models.BookMS.objects.filter(pk=book_id).update(**data)
        return redirect(reverse("list_book"))

def del_book(request, b_id):
    models.BookMS.objects.filter(pk=b_id).delete()
    return redirect(reverse("list_book"))

def index(request):
    return redirect(reverse("list_book"))