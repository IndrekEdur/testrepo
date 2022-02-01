from django import forms

from .models import Product, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'Project', 'hours', 'description']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'Project': forms.Select(attrs={'class': 'form-control'}),
            'hours': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Enter Job Name',
            'image': 'Select an Image ',
            'Project': 'Select Project ',
            'hours': 'Enter estimated hours ',
            'description': 'Enter a Description ',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }