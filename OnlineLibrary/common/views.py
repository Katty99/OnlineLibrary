from django.shortcuts import render, redirect

from OnlineLibrary import account
from OnlineLibrary.account.forms import ProfileForm
from OnlineLibrary.account.models import Profile
from OnlineLibrary.book.models import Book


# Create your views here.
def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def home_with_user(request):
    profile = get_profile()
    books = Book.objects.all()

    context = {
        'profile': profile,
        'books': books
    }

    return render(request, 'common/home-with-profile.html', context)


def home_without_user(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'common/home-no-profile.html', context)


def home(request):
    profile = Profile.objects.first()
    if profile:
        return home_with_user(request)

    return home_without_user(request)
