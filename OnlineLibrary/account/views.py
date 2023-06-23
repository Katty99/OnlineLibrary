from django.shortcuts import render, redirect

from OnlineLibrary.account.forms import ProfileForm, DeleteProfileForm
from OnlineLibrary.account.models import Profile
from OnlineLibrary.book.models import Book


# Create your views here.
def profile(request):
    account = Profile.objects.first()
    context = {'account': account}
    return render(request, template_name='account/profile.html', context=context)


def profile_edit(request):
    account = Profile.objects.first()
    if request.method == "GET":
        form = ProfileForm(initial=account.__dict__)
        context = {'form': form, 'account': account}
        return render(request, template_name='account/edit-profile.html', context=context)

    else:
        form = ProfileForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            context = {'form': form}
            return render(request, template_name='account/edit-profile.html', context=context)


def profile_delete(request):
    account = Profile.objects.first()
    books = Book.objects.all()
    if request.method == 'GET':
        form = DeleteProfileForm(initial=account.__dict__)
        context = {'form': form, 'account': account}
        return render(request, template_name='account/delete-profile.html', context=context)

    elif request.method == 'POST':
        account.delete()
        books.delete()
        return redirect('home')
    return render(request, template_name='account/delete-profile.html')
