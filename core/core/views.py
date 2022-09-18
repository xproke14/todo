from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from categories.models import Category

@login_required
def main(request):
    cat = Category.objects.filter(user=request.user).first()
    return redirect(reverse('category', kwargs={'pk':cat.id}))