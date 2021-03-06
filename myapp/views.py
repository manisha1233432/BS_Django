from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, admin_only
from django.contrib.auth.models import Group
# Create your views here.


@unauthenticated_user
def registerpage(request):
    form =  CreateUserForm()
    if request.method == 'POST':
        form =  CreateUserForm(request.POST)
        if form.is_valid():
            userf = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            userf.groups.add(group)
            messages.success(request, "Account was created for" +username)
            return redirect('myapp:login')
    context={ 'form':form}
    return render(request, "myapp/register.html",context)   

@unauthenticated_user
def loginpage(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password= request.POST.get('password')

        usern = authenticate(request, username=username, password= password)
        if usern is not None:
            login(request,usern)
            return redirect('/')
        else:
            messages.info(request,"Username or Password is incorrect")

    context={}
    return render(request, "myapp/login.html",context)


def logoutuser(request):
    logout(request)
    return redirect("myapp:login")


@login_required(login_url='myapp:login')
def index(request):
    book_list = Book.objects.all()
    context={
        'book_list':book_list
    }
    return render(request,"myapp/index.html",context)

@login_required(login_url='myapp:login')
def detail(request,book_id):
    book = Book.objects.get(id=book_id)
    return render(request,'myapp/detail.html',{'book':book})

@login_required(login_url='myapp:login')
@admin_only
def add_book(request):
    if request.method =="POST":
        name = request.POST.get('book',)
        author = request.POST.get('author',)
        book_image = request.FILES['book_image']
        book_upload = request.FILES['book_upload']
        book = Book(book=name, author=author, book_image=book_image, book_upload=book_upload )
        book.save()

    return render(request, 'myapp/add_book.html')

@login_required(login_url='myapp:login')
@admin_only
def update(request, id):
    book = Book.objects.get(id = id)
    form = BookForm(request.POST or None,request.FILES, instance = book)
    if form.is_valid():
       form.save()
       return redirect('/')
    return render(request, 'myapp/edit.html',{'form' : form, 'book' : book})

@login_required(login_url='myapp:login')
@admin_only
def delete(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')


