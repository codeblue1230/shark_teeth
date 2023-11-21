from django import forms

class CreateNewPost(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    text = forms.CharField(max_length=1000)
    picture = forms.ImageField(required=False)