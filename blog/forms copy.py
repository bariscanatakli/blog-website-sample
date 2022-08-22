from .models import Comment
from django import forms
from django_summernote.widgets import SummernoteWidget
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


# Apply summernote to specific fields.
class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

# Sign Up Form
class SignUpForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2', 
            ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'col-md-12'}),
            'email': forms.EmailInput(attrs={'class': 'col-md-12'}),
            'password1': forms.EmailInput(attrs={'class': 'col-md-12'}),
            'password2': forms.EmailInput(attrs={'class': 'col-md-12'}),
        }
        help_texts = {
            'User': 'Group to which this message belongs to',
        }

# Profile Form
class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
            'last_name', 
            'email',
            ]