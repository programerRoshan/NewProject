from django.shortcuts import render,get_object_or_404
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post
from .forms import PostForm
def posts_create(request):
	form = PostForm()
	form = PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully created the Post")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"form":form,
	}
	return render(request, "post_create.html",context)

def posts_list(request):
	if request.user.is_authenticated:
		queryset_list = Post.objects.all().order_by("-timestamp")
		query = request.GET.get('q')
		if query:
			queryset_list = queryset_list.filter(Q(title__icontains=query)
				| Q(content__icontains=query)).distinct()
		paginator = Paginator(queryset_list, 5) # Show 25 contacts per get_pag
		page = request.GET.get('page')
		queryset = paginator.get_page(page)
		context = {
		"set":queryset
		}
		return render(request, "list.html",context)
	else:
		return HttpResponse("<h1> PLEASE LOGIN </h1>")

def posts_detail(request,id=None):
	instance = get_object_or_404(Post,id=id)
	context = {
	"instance":instance
	}
	return render(request,"details.html",context)

def posts_update(request,id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form":form,
	}
	return render(request, "post_form.html",context	)

def base(request):
		return render(request, "base.html",{}	)

def posts_delete(request,id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	return HttpResponseRedirect(instance.get_home())
