from django import forms
from .models import Service, Post, Inscription

class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['title', 'subtitle', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subtitulo'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }
        labels = {
            'title':'', 'subtitle':'', 'content': ''
        }

class PostForm(forms.ModelForm):

    class Meta:
        CHOICES = (
            ('pendiente', 'Pendiente'),
            ('iniciado', 'Iniciado'),
            ('finalizado', 'Finalizado'),
        )
        model = Post
        fields = ['title', 'schedule', 'place', 'classroom', 'content', 
            'attendance', 'status', 'course', 'teacher']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'schedule': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Horarios'}),
            'place': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Edificio'}),
            'classroom': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Aula'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'},choices=[('Pendiente', 'Pendiente'),('Iniciado', 'Iniciado'),('Finalizado', 'Finalizado')]),
            'course': forms.Select(attrs={'class':'form-control','placeholder':'Curso'}),
            'teacher': forms.Select(attrs={'class':'form-control','placeholder':'Profesor'}),
        }
        labels = {
            'title':'', 'schedule': '', 'place':'', 'classroom': '', 'content':'', 'attendance': 'Asistencias', 'status':'', 'course': '', 'teacher': ''
        }

class InscriptionForm(forms.ModelForm):

    class Meta:
        model = Inscription
        fields = ['student', 'course']
        widgets = {
        }
        labels = {
            'student':'', 'course':''
        }

class GradeForm(forms.ModelForm):

    class Meta:
        model = Inscription
        fields = ['fstGrade', 'sndGrade', 'trdGrade', 'fthGrade']
        widgets = {
            'fstGrade': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Parcial 1'}),
            'sndGrade': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Parcial 2'}),
            'trdGrade': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Parcial 3'}),
            'fthGrade': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Parcial 4'}),
        }
        labels = {
            'fstGrade':'', 'sndGrade':'', 'trdGrade': '', 'fthGrade': ''
        }