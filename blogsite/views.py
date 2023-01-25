from django.shortcuts import render
from .models import BlogPost
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
# Create your views here.

#function to display a list of all blogs
def blog_list(request):
    blog_posts = BlogPost.objects.all()
    context = {'blog_posts': blog_posts}
    return render(request, 'blogsite/blog_list.html', context )

#function to retrieve a blog details
def blog_detail(request, pk):
    blog_post = BlogPost.objects.get(pk=pk)
    context = {'blog_post': blog_post}
    return render(request, 'blogsite/blog_detail.html', context)

#function to update 
class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'author']
    template_name = 'blogsite/blog_form.html'
    success_url = reverse_lazy('blog_list')
#delete function

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blogsite/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')