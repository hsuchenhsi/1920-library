from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect
from django.db.models import Q
from django.db.models import Q


# Create your views here.
def homepage(request):
    posts=Post.objects.all()
    now=datetime.now()
    return render(request,'index.html',locals())


def showpost(request, slug):
	try:
		post = Post.objects.get(slug = slug)
		if post != None:
			return render(request, 'post.html', locals())
	except:
		return redirect('/')

def post_view(request,post_id):
	post=Post.objects.get(id=post_id)
	form=PostForm(instance=post)
	return render(request,'post.html',{'post':post,'form':form})

def index(request):
    return render(request, 'index.html')

'''
def booking(request):
    if request.method == 'GET':
        # form = UserRegisterForm()
        return render(request, 'register.html', locals())
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_password = form.cleaned_data['user_password']
            user_password_confirm = form.cleaned_data['user_password_confirm']
            if user_password == user_password_confirm:
                user = user.objects.create_user(user_name, user_email, user_password)
                message = f'註冊成功！'
            else:
                message = f'兩次密碼不一致！'    
        return render(request, 'register.html', locals())
    else:
        message = "ERROR"
        return render(request, 'register.html', locals())
'''

def search_books(request):
    query = request.GET.get('q', '')  
    books = Post.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(body__icontains=query))
    return render(request, 'search_books.html', {'books': books, 'query': query})

def login_view(request):
	return render(request,'login.html')


