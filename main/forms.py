from django import forms

class AddForm(forms.Form):
    name = forms.CharField()
    about = forms.CharField(required=False,widget=forms.Textarea)
    is_completed = forms.BooleanField(required=False,)