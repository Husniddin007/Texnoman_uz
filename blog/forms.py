from django import forms
from blog.models import Blog, Tag, Category, Comment


class TagForm(forms.Form):
    name = forms.CharField(help_text='tag name kiriting',
                           label='Tag_name',
                           widget=forms.TextInput(attrs={"class": "form-controls"})
                           )


class BlogForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({"class": "form-controls"})
        self.fields['category'].widget.attrs.update({"class": "form-controls"})

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Blog
        fields = ["title", "description", "image", "category", "tags", "user"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
