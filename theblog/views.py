from django.shortcuts import render,get_object_or_404,redirect
from .forms import *
from . models import *
# Create your views here.
def HomeView(request):
    post=Post.objects.all()
    return render(request,'home.html',{'all_post':post})


def DetailView(request,pk):
    post=get_object_or_404(Post,id=pk)

    return render(request,'detail_blog.html',{
        'post':post
    })

def PostCreateView(request):
    postForm=PostRegistrationForm(request.POST or None)
    if request.method=="POST":
        post=postForm.save(commit=False)
        post.author=request.user
        post.save()
        return redirect('detail_blog', pk=post.id)
    context={
        'postForm':postForm,
    }
    return render(request,'create_post.html',context)

def PostEditView(request,pk):
    post=get_object_or_404(Post,id=pk)
    postForm=PostRegistrationForm(request.POST or None,instance=post)
    if request.method=='POST' :
        if postForm.is_valid():
            postForm.save()
            return redirect('detail_blog',pk=pk)
    context={
        'postForm':postForm,
        'post':post
    }    
    return render(request,'edit_post.html',context)

def DeletePostView(request,pk):
    post=get_object_or_404(Post,id=pk)
    if request.method=='POST':
        post.delete()
        return redirect('Home')
    return render(request,'delete_post.html',{'post':post})