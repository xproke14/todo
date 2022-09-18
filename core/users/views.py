from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings
import os
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth import views as auth_views

from .forms import CustomUserCreateForm
from .models import CustomUser
from categories.models import Category
from tasks.models import Task


class CreateUserView(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = CustomUserCreateForm
    template_name = 'users/register.html'
    success_message = 'User %(email)s created successfully!'

    def get_success_url(self):
        return reverse('login')


class ProfileDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = CustomUser
    fields =['image']
    template_name = 'users/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_count'] = Category.objects.filter(user=self.request.user).count()
        cats = Category.objects.filter(user=self.request.user)
        context['task_count'] = Task.objects.filter(category__in=cats).count()
        return context

    def test_func(self):
        if self.get_object() ==self.request.user:
            return True
        return False

class ProfileImageView(ProfileDetailView):
    template_name = 'users/profile_image.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        static_list = os.listdir(os.path.join(settings.BASE_DIR, 'users/static/users'))
        static = dict()
        for fila in static_list:
            # {filename: filepath}
            static[fila] = 'users/' + fila
        context['static'] = static
        return context

class ProfileImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    template_name = 'users/profile_image_confirm.html'
    fields = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = 'users/' + self.kwargs.get('pic_name')
        return context

    def test_func(self):
        if self.get_object() == self.request.user:
            return True
        return False

    def form_valid(self, form):
        # no need to specify path - automatically picks up media/ 
        form.instance.image = self.kwargs.get('pic_name')
        # the same files as in static/ must be in media/. static/ used for rendering, media/ used for user profile update
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk':self.object.id})


class PasswordChangeCustomView(SuccessMessageMixin, auth_views.PasswordChangeView):

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.id})

    template_name= 'users/password_change.html'
    success_message = 'Password changed successfully!'