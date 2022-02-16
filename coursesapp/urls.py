from django.contrib import admin
from django.urls import path
from .views import CourseListView, CategoryListView, ContactListView, BranchListView

urlpatterns = [
    path('categories', CategoryListView.as_view()),
    path('branches', BranchListView.as_view()),
    path('contacts', ContactListView.as_view()),
    path('courses', CourseListView.as_view())
]
