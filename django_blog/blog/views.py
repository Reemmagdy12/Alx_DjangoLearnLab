from django.shortcuts import render, redirect , get_object_or_404
from .forms import SignUPForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth import login
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView, ListView
from .models import Post , Comment
from django.db.models import Q
from taggit.models import Tag


# Create your views here.
@login_required
def home(request):
    return render(request, 'blog/home.html')

def register(request):
    if request.method == 'POST' :
        form = SignUPForm(request.POST)
        if form.is_valid :
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            redirect('home')
    else :
        context = {
            form : SignUPForm
        }
        return render (request, 'registration/register.html',context)
    
@login_required
def profile(request):
    if request.method == 'POST' :
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        redirect('profile')
    else:
        return render (request,'profile.html',{'user':request.user})
    
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    

class PostDeleteView(DeleteView,LoginRequiredMixin,UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
@login_required
class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']
    template_name = 'blog/post_form.html'

class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comments'

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'blog/comment_detail.html'

class CommentDeleteView(DeleteView,LoginRequiredMixin,UserPassesTestMixin):
    model = Comment
    template_name = 'blog/comment_delete.html'
    success_url = '/'
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

class CommentUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
def search_posts(request):
    query = request.GET.get('q','')
    results = Post.objects.none()
    if query :
        results = Post.objects.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(tags__name__icontains=query)
        ).distinct()
    return render(request,'blog/search_results.html',{'query':query, 'results':results})

def posts_by_tag(request,tag_slug):
    tag = get_object_or_404(Tag,slug = tag_slug)
    posts = Post.objects.filter(tags__in=[tag])
    return render(request,'blog/posts_by_tag.html',{'tag':tag, 'posts':posts})



