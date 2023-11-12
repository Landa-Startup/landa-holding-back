from django.urls import path
from .views import BlogList,BlogDeatialsView,TagsView,CategoriesView

app_name="blog"

urlpatterns = [
    path('list',BlogList.as_view(),name='blog-list'),
    path('category-list',TagsView.as_view(),name='tags-list'),
    path('tag-list',CategoriesView.as_view(),name='categories-list'),
    path('details/<slug:slug>/', BlogDeatialsView.as_view(), name='blog-details'),]
