from django import forms

st_choices = (
    ("1", "Shark Teeth"),
    ("2", "Sea Shells")
)

class CreateNewPost(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    text = forms.CharField(label="Description", max_length=1000)
    s_or_t = forms.MultipleChoiceField(choices=st_choices)
    picture = forms.ImageField(required=False)