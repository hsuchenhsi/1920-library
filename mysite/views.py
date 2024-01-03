from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm



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
    return render(request, 'accounts/index.html')


#首頁
def index(request):
    return render(request, 'accounts/index.html')
#註冊
def sign_up(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def custom_register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            # 在這裡處理註冊邏輯
            # 例如，創建新用戶，處理表單數據等
            return redirect('home')  # 將 'home' 替換為你的首頁路徑
    else:
        form = CustomRegistrationForm()

    return render(request, 'registration.html', {'form': form})

# 註冊
def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')  #重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)
