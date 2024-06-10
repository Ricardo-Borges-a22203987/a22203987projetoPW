from django import forms
from .models import Post,Comment,Rating

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'




class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = '__all__'





class RatingForm(forms.ModelForm):
  class Meta:
    model = Rating
    fields = '__all__'

