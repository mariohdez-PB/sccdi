from django.urls import path
from .views import ServiceListView, ServiceDetailView, ServiceCreate, ServiceUpdate, ServiceDelete, PostListView, PostDetailView, PostCreate, PostUpdate, PostTeacherUpdate, PostDelete, InscriptionListView, InscriptionDetailView, InscriptionCreate, InscriptionUpdate, InscriptionDelete, GradeUpdate

services_patterns = ([
    path('', ServiceListView.as_view(), name='services'),
    path('<int:pk>/<slug:slug>/', ServiceDetailView.as_view(), name='service'),
    path('create/', ServiceCreate.as_view(), name='create'),
    path('update/<int:pk>/', ServiceUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ServiceDelete.as_view(), name='delete'),
], 'services')

posts_patterns = ([
    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>/<slug:slug>/', PostDetailView.as_view(), name='post'),
    path('create/', PostCreate.as_view(), name='create'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='update'),
    path('attendance/<int:pk>/', PostTeacherUpdate.as_view(), name='attendance'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='delete'),
], 'posts')

inscriptions_patterns = ([
    path('', InscriptionListView.as_view(), name='inscriptions'),
    path('<int:pk>/', InscriptionDetailView.as_view(), name='inscription'),
    path('create/', InscriptionCreate.as_view(), name='create'),
    path('update/<int:pk>/', InscriptionUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', InscriptionDelete.as_view(), name='delete'),
], 'inscriptions')

grades_patterns = ([
    path('update/<int:pk>/', GradeUpdate.as_view(), name='update'),
], 'grades')
