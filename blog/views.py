from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormMixin
from django.core.mail import send_mail, BadHeaderError
from .models import Post, ContactForm, Comment, CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Render html pages for navbar links
def index(request):
    return render(request, 'index.html')

def start(request):
    return render(request, 'start.html')

def destinations(request):
    return render(request, 'destinations.html')

# Render the about page, it's email form, and get form data to save it
def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            email = form.cleaned_data['email_address']
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, email, ['johnfuhrmeister12@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    form = ContactForm()
    return render(request, 'about.html', {'form': form})

# Render html pages for organizing posts by country
def mexico(request):
    return render(request, 'mexico.html')

def colombia(request):
    return render(request, 'colombia.html')

def argentina(request):
    return render(request, 'argentina.html')

# Render html pages for admin posts page and for each blog post
class Posts(ListView):
    model = Post
    template_name = 'posts.html'
    ordering = ['-id']

class ArticleDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'blogpostdetail.html'
    form_class = CommentForm

    # When submitting a comment return to the same page
    def get_success_url(self):
        return self.request.path

    # Load in custom comment form
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    # Get form information and handle comment replies
    def post(self, request, slug):
        self.object = self.get_object()
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(reply__isnull=True)
        form = self.get_form()
        if form.is_valid():
            parent_obj = None
            try:
                reply_id = int(request.POST.get('comment_id'))
            except:
                reply_id = None
            if reply_id:
                parent_obj = Comment.objects.get(id=reply_id)
                if parent_obj:
                    reply_comment = form.save(commit=False)
                    reply_comment.reply = parent_obj
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(request.path_info)

# Render html pages for adding, editing, and deleting posts
class AddPost(CreateView):
    model = Post
    template_name = 'addpost.html'
    fields = ['title', 'body']

class EditPost(UpdateView):
    model = Post
    template_name = 'editpost.html'
    fields = '__all__'

class DeletePost(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('posts')

