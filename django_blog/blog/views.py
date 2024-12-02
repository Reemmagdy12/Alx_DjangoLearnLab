from django.shortcuts import render, redirect
from .forms import SignUPForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth import login
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView, ListView
from .models import Post
from django.urls import reverse_lazy

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
    
class ListPosts(ListView):
    model = Post
    template_name = 'ListPosts.html'
    context_object_name = 'posts'

class PostDetails(DetailView):
    model = Post
    template_name = 'PostDetails.html'
    context_object_name = 'posts'

class DeletePost(DeleteView,LoginRequiredMixin,UserPassesTestMixin):
    model = Post
    template_name = 'DeletePost.html'
    context_object_name = 'post'
    success_url = reverse_lazy('ListPosts')
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
@login_required
class CreatePost(CreateView):
    model = Post
    template_name = 'CreatePost.html'

class UpdatePost(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content']
    template_name = 'UpdatePost.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author



