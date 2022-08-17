from django import forms

class ItemForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    price = forms.CharField(max_length=100)
    type = forms.CharField()
    stock = forms.CharField()
    image = forms.ImageField()