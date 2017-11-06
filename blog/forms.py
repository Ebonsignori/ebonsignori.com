from django import forms

from .models import Post, Category, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'author', 'category', 'text')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'slug')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)