from django.shortcuts import render, redirect
from .forms import SignUPForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth import login
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView, ListView
from .models import Post

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



