from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
def profile(request):
    return render(request, 'music/profile.html')

class HomeView(ListView):
    model = Music
    template_name = 'music/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['top_rated'] = Music.objects.all().order_by('-rating')
        context['most_popular'] = Music.objects.all().order_by(
            '-popularity_count')
        context['recent_releases'] = Music.objects.all().order_by(
            '-year_of_release')
        return context

class MusicList(ListView):
    model = Music
    paginate_by = 5

class MusicDetail(DetailView):
    model = Music

    def get_object(self):
        object = super(MusicDetail, self).get_object()
        object.popularity_count += 1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(MusicDetail, self).get_context_data(**kwargs)
        context['links'] = MusicLink.objects.filter(music=self.get_object())
        context['related_music'] = Music.objects.filter(
            category=self.get_object().category)
        return context

class MusicCateory(ListView):
    model = Music
    paginate_by = 5

    def get_queryset(self):
        self.category = self.kwargs['category']
        return Music.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(MusicCateory, self).get_context_data(**kwargs)
        context['music_category'] = self.category
        return context


class MusicLanguage(ListView):
    model = Music
    paginate_by = 5

    def get_queryset(self):
        self.language = self.kwargs['lang']
        return Music.objects.filter(language=self.language)

    def get_context_data(self, **kwargs):
        context = super(MusicLanguage, self).get_context_data(**kwargs)
        context['music_language'] = self.language
        return context

class MusicSearch(ListView):
    model = Music
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list

class MusicYear(YearArchiveView):
    queryset = Music.objects.all()
    date_field = 'year_of_release'
    make_object_list = True
    allow_future = True
    pagignate_by = 5

def contact(request):
    return render(request, 'contact.html')

def terms(request):
    return render(request, 'terms.html')


def about_us(request):
    return render(request, 'about_us.html')

def AddMusic(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('add_music_submission')
    else:
        form = MusicForm()
    return render(request, 'add.html', {'form' : form})

def AddMusic_admin(request):
    if request.method == 'POST':
        form = MusicForm2(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('add_music_submission')
    else:
        form = MusicForm2()
    return render(request, 'add_admin.html', {'form' : form})

def add_music_submission(request):
    return render(request, 'add_music_submission.html')

def login(request):
    return render(request, 'music/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'music/register.html', {'form': form})
