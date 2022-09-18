from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from categories.models import Category
from tasks.models import Task
from tasks.forms import TaskForm


# Hybrid: DetailCategoryView + CreateTaskView (model = Task)
@login_required
def category_view(request, pk):
    
    # get + post context:
    cur_cat = Category.objects.get(id = pk)
    count = Category.objects.filter(user=request.user).count()

    # test_func:
    if cur_cat.user != request.user:
        return HttpResponse(status=403)

    if request.method != 'POST':
        task_form = TaskForm()
        all_cats = Category.objects.filter(user=request.user)
        tasks = Task.objects.filter(category = cur_cat).order_by('done', '-created')
        context = {'task_form':task_form, 'cur_cat':cur_cat, 'all_cats':all_cats, 'tasks':tasks, 'count':count}
        return render(request, 'categories/category.html', context)
    else:
        task_form = TaskForm(request.POST)
        task_form.instance.category = cur_cat
        if task_form.is_valid():
            task_form.save()
        return redirect(reverse('category', kwargs={'pk':cur_cat.id}))


class DeleteCategoryView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'categories/category_delete.html'

    def get_success_url(self):
        return reverse('main')

    def test_func(self):
        # users can delete only their own cat AND there is > 1 cat so that user does not end up with 0 cats.
        if self.get_object().user == self.request.user and Category.objects.filter(user=self.request.user).count() > 1:
            return True
        return False


class EditCategoryView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    template_name = 'categories/category_edit.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('category', kwargs={'pk':self.object.id})

    def test_func(self):
        if self.get_object().user == self.request.user:
            return True
        return False


class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'categories/category_create.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('category', kwargs={'pk':self.object.id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)