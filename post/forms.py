from django import forms

from post.models import Post, Comment


class AddPostForm(forms.ModelForm):
    content = forms.CharField(label='',
                              widget=forms.Textarea(attrs={
                                  'rows': '5',
                                  'placeholder': 'Napisz coś'
                              }))
    photo = forms.ImageField(label='', required=False)

    class Meta:
        model = Post
        fields = ('content', 'photo')

class AddCommentForm(forms.ModelForm):
    content = forms.CharField(label='',
                              widget=forms.Textarea(attrs={
                                  'rows': '4',
                                  'placeholder': 'Comment'
                              }))

    class Meta:
        model = Comment
        fields = ('content', )