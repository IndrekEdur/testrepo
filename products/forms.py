from django import forms

from .models import Product, Comment, Hours
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'Project', 'hours', 'author', 'performer', 'is_completed', 'description']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
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

class HoursForm(forms.ModelForm):
    class Meta:
        model = Hours
        fields = ['quantity', 'inserted_at', 'date']

        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'inserted_at': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'}),
        }

        labels = {
            'quantity': 'Enter quantity of working hours',
            'inserted_at': 'This is the time of inserting information ',
            'date': 'Enter the date and time when the work was carried out ',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }