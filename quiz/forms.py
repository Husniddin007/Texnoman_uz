from django import forms


class QuizForm(forms.Form):
    name = forms.CharField(help_text='quiz name kiriting',
                           label='Quiz_name',
                           widget=forms.TextInput(attrs={"class": "form-controls"})
                           )
