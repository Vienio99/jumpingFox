from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, SearchResultsView, AboutView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),


    path('search/', SearchResultsView.as_view(), name='search_results'),

    
    path('post/new', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
]
