from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import blogForm

# Create your views here.

def bloghome(request):
    blog = Blog.objects.all()
    #블로그 모든 글들을 대상으로
    blogList = Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blogList, 3)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return해 준다.
    posts = paginator.get_page(page) #해당페이지 번호에 해당하는 페이지가 posts에 저장
    return render(request,'bloghome.html',{'blog' : blog, 'posts' : posts})

def blogdetail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blogdetail.html' ,{'blog' : blog_detail})

def blognew(request):
    if request.method == 'POST': #폼 다채우고 저장버튼 눌렀을 때
        form = blogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.blog_date = timezone.now()
            post.save()
            return redirect('blogdetail', post.id)
        return redirect('bloghome')
    else:  #글을 쓰기위해 들어갔을 때
        form = blogForm()
        return render(request,'blognew.html', {'form':form})


def blogedit(request, blog_id):
    post = get_object_or_404(Blog, pk = blog_id)
    if request.method == 'GET':  #수정하려고 들어갔을 때
        form = blogForm(instance = post)
        return render(request, 'blogedit.html', {'form' : form})
    else:   #수정 끝나고 수정 버튼을 눌렀을 때
        form = blogForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.blog_date = timezone.now()
            post.save()
            return redirect('/blogapp/blogdetail/' + str(blog_id))
        return redirect('bloghome')

def blogdelete(request, blog_id):
    deleteBlog =  Blog.objects.get(id = blog_id)
    deleteBlog.delete()
    return redirect('bloghome')