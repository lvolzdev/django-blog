from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.

def list(request):
    blogs = Blog.objects.all()
    return render(request, 'list.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id) #(클래스 이름, identitiy)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')

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
    return redirect('list')



