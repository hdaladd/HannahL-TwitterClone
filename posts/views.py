from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())


    posts = Post.objects.all().order_by('-created_at')[:20]


    return render(request, 'posts.html', 
                  {'posts': posts})



def delete(request, post_id):
    #Find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def like(request, post_id):
    count = Post.objects.get(id= post_id)
    count.count += 1
    count.save()
    
    return HttpResponseRedirect('/')


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    form = PostForm   
    
    return render(request, 'edit.html', {'post': post,'form':form})