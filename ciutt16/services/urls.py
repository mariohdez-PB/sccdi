from django.urls import path
from .views import ServiceListView, ServiceDetailView, ServiceCreate, ServiceUpdate, ServiceDelete, PostListView, PostDetailView, PostCreate, PostUpdate, PostDelete

services_patterns = ([
    path('', ServiceListView.as_view(), name='services'),
    path('<int:pk>/<slug:slug>/', ServiceDetailView.as_view(), name='service'),
    path('create/', ServiceCreate.as_view(), name='create'),
    path('update/<int:pk>/', ServiceUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ServiceDelete.as_view(), name='delete'),
], 'services')

post_patterns = ([
    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>/<slug:slug>/', PostDetailView.as_view(), name='post'),
    path('create/', PostCreate.as_view(), name='create'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='delete'),
], 'posts')

