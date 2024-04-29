from django import forms

from .models import Product, Comment, Hours, Project
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

from .models import Document
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file', )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'Project', 'hours', 'author', 'performer', 'is_completed', 'description']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control', 'multiple': True}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'Project': forms.Select(attrs={'class': 'form-control'}),
            'hours': forms.TextInput(attrs={'class': 'form-control'}),
            'performer': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'completed': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Enter Job Name',
            'image': 'Select an Image ',
            'Project': 'Select Project ',
            'hours': 'Enter estimated hours ',
            'description': 'Enter a Description ',
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'is_active', 'project_number', 'dropbox_link', 'budget_dropbox_link']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.NullBooleanSelect (attrs={'class': 'form-control'}),
            'project_number': forms.TextInput(attrs={'class': 'form-control'}),
            'dropbox_link': forms.TextInput(attrs={'class': 'form-control'}),
            'budget_dropbox_link': forms.TextInput(attrs={'class': 'form-control'}),
        }

class HoursForm(forms.ModelForm):
    class Meta:
        model = Hours
        fields = ['quantity', 'date' ]

        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'}),
        }

        labels = {
            'quantity': 'Enter quantity of working hours',
            'product': 'Here you can change the job if needed',
            'date': 'Enter the date and time when the work was carried out ',
        }

class GeneralHoursForm(forms.ModelForm):
    class Meta:
        model = Hours
        fields = ('owner','project','product','quantity', 'date' )

        widgets = {
            'owner': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'}),
        }

        labels = {
            'owner': 'Select the owner of the hours',
            'project': 'Select the project the hours belong to',
            'product': 'Select the job the hours belong to',
            'quantity': 'Enter quantity of working hours',
            'date': 'Enter the date and time when the work was carried out ',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }