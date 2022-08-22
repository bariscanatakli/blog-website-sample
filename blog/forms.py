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
    username = forms.CharField(max_length=30,)
    email = forms.EmailField(max_length=254,)
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2',    
            
            ]
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'col-md-12'})
        self.fields['email'].widget.attrs.update({'class': 'col-md-12'})
        self.fields['password1'].widget.attrs.update({'class': 'col-md-12'})
        self.fields['password2'].widget.attrs.update({'class': 'col-md-12'})

# Profile Form
class ProfileForm(UserCreationForm):
    username = forms.CharField(max_length=30,)
    email = forms.EmailField(max_length=254,)
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            ]
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'bg-light form-control'})
        self.fields['email'].widget.attrs.update({'class': 'bg-light form-control'})
        
   
        