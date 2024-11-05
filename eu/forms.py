from django import forms

class teacherForm(forms.Form):
    name = forms.CharField(max_length=200)

class studentForm(forms.Form):
    name = forms.CharField(max_length=200)
    age = forms.IntegerField()
    dream = forms.CharField(max_length=200)
    teacher = forms.CharField(max_length=200)
