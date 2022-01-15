from django.shortcuts import render
from likeblog.forms import BlogPostForm
from likeblog.models import Blog, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


# View all the blogs
def view_allBlogs(request):
    blogs=Blog.objects.all().order_by('-date_posted')
    categoryList=Category.objects.all()
    paginator=Paginator(blogs,5)
    page=request.GET.get('page')
    try:
        blogs=paginator.page(page)
    except PageNotAnInteger:
        blogs=paginator.page(1)
    except EmptyPage:
        blogs=paginator.page(paginator.num_pages)
    context={'page_title':'All Blogs','blogs':blogs,'categoryList':categoryList,'page':page}
    return render(request,'blogs.html',context)


def view_aBlog(request,blog_id):
    blog=Blog.objects.get(id=blog_id)
    categoryList=Category.objects.all()
    context={'page_title':blog.title,'blog':blog,'categoryList':categoryList}
    return render(request,'blog.html',context)

def addBlog(request):
    form=BlogPostForm()
    if request.method=='POST':
        form=BlogPostForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('view_allBlog')
    return render(request,'addblog.html',{'form':form})


