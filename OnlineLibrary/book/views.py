from django.shortcuts import render, redirect

from OnlineLibrary.account.models import Profile
from OnlineLibrary.book.forms import BookForm
from OnlineLibrary.book.models import Book


# Create your views here.
def add_book(request):
    form = BookForm(request.POST or None)
    account = Profile.objects.first()
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {'form': form, 'account': account}
    return render(request, template_name='book/add-book.html', context=context)


def edit_book(request, id):
    book = Book.objects.get(id=id)
    account = Profile.objects.first()
    if request.method == 'GET':
        context = {'form': BookForm(initial=book.__dict__), 'account': account}
        return render(request, template_name='book/edit-book.html', context=context)

    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {'form': form, 'account': account}
            return render(request, template_name='book/edit-book.html', context=context)


def details_book(request, id):
    book = Book.objects.get(id=id)
    account = Profile.objects.first()
    context = {'book': book, 'account': account}
    return render(request, template_name='book/book-details.html', context=context)


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('home')