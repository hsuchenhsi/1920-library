from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm


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
