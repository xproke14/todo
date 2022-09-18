from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateCategoryView.as_view(), name='category_create'),
    path('<pk>/', category_view, name='category'),
    path('<pk>/delete/', DeleteCategoryView.as_view(), name='category_delete'),
    path('<pk>/edit/', EditCategoryView.as_view(), name='category_edit'),
    
]
