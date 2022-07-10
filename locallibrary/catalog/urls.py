from django.urls import re_path as url 
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name = 'books'),
    url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail')
]