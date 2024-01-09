from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
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


def search_books(request):
    query = request.GET.get('q', '')  
    books = Post.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(body__icontains=query))
    return render(request, 'search_books.html', {'books': books, 'query': query})