from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Service, Post, Inscription
from .forms import ServiceForm, PostForm, PostTeacherForm, InscriptionForm, GradeForm

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
# Views about Services
class ServiceListView(ListView):
    model = Service

class ServiceDetailView(DetailView):
    model = Service

@method_decorator(staff_member_required, name='dispatch')
class ServiceCreate(CreateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('services:services')

@method_decorator(staff_member_required, name='dispatch')
class ServiceUpdate(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('services:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('services:services')

# Views about posts
class PostListView(ListView):
    model = Post
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post

@method_decorator(staff_member_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts:posts')

class PostTeacherUpdate(PermissionRequiredMixin, UpdateView):
    model = Post
    form_class = PostTeacherForm
    template_name_suffix = '_update_form'
    permission_required = 'services.change_post'

    def get_success_url(self):
        return reverse_lazy('posts:attendance', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('posts:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts:posts')

# Views about inscriptions
@method_decorator(staff_member_required, name='dispatch')
class InscriptionListView(ListView):
    model = Inscription
    paginate_by = 25

class InscriptionDetailView(PermissionRequiredMixin, DetailView):
    model = Inscription
    permission_required = 'services.change_inscription'

@method_decorator(staff_member_required, name='dispatch')
class InscriptionCreate(CreateView):
    model = Inscription
    form_class = InscriptionForm
    success_url = reverse_lazy('inscriptions:inscriptions')

@method_decorator(staff_member_required, name='dispatch')
class InscriptionUpdate(UpdateView):
    model = Inscription
    form_class = InscriptionForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('inscriptions:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class InscriptionDelete(DeleteView):
    model = Inscription
    success_url = reverse_lazy('inscriptions:inscriptions')

# Views about grades
class GradeUpdate(PermissionRequiredMixin,UpdateView):
    model = Inscription
    form_class = GradeForm
    template_name_suffix = '_update_form'
    permission_required = 'services.change_inscription'

    def get_success_url(self):
        return reverse_lazy('grades:update', args=[self.object.id]) + '?ok'
