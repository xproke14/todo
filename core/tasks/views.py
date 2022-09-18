from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView, UpdateView

from tasks.models import Task


class DeleteTaskView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'

    def get_success_url(self):
        return reverse('category', kwargs={'pk':self.object.category.id})

    def test_func(self):
        category = self.get_object().category
        if category.user == self.request.user:
            return True
        return False


class EditTaskView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    template_name = 'tasks/task_edit.html'
    fields = ['name', 'done']

    def get_success_url(self):
        return reverse('category', kwargs={'pk':self.object.category.id})

    def test_func(self):
        category = self.get_object().category
        if category.user == self.request.user:
            return True
        return False