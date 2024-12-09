from django import forms

class teacherForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=200)
    password = forms.CharField(min_length=8)

class loginForm(forms.Form):
    email = forms.CharField(max_length=200)
    password = forms.CharField(min_length=6)

class studentForm(forms.Form):
    name = forms.CharField(max_length=200)
    age = forms.IntegerField()
    dream = forms.CharField(max_length=200)
    clasS = forms.CharField(max_length=200)
