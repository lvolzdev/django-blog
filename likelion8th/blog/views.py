from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .form import BlogForm
# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id) #(클래스 이름, identitiy)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
#1. 데이터가 입력된 후 제출 버튼을 누르고 데이터 저장 = post
#2. 정보가 입력되지 않은 빈칸으로 되어있는 페이지 보여주기 = get
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES) #입력값
        if form.is_valid():
            content = form.save(commit = False) #임시저장. 보류
            content.pub_data = timezone.now()
            content.save() #이제 값들 다 채워졌으니 저장해줌
            return redirect('home') #메인페이지 돌아가기

    else:
        form = BlogForm() #form변수에 빈 BlogForm객체를 담아주자
        return render(request, 'new.html', {'form':form})



def create(request):
    new_blog = Blog() #새로운 객체를 만들어
    new_blog.title = request.POST['title']
    new_blog.pub_data = timezone.datetime.now()
    new_blog.body = request.POST['body'] #name이 body인 html 태그 안의 정보를 가져와서 new_blog의 body 컬럼에 저장해
    new_blog.save()
    return redirect('/blog/'+str(new_blog.id))

def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, blog_id): # new 함수와 똑같. 차이점은 아이디 필요
    update_blog = get_object_or_404(Blog, pk = blog_id)
    update_blog.title = request.POST['title']
    update_blog.pub_data = timezone.datetime.now()
    update_blog.body = request.POST['body'] 
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk = blog_id)
    delete_blog.delete()
    return redirect('home')



