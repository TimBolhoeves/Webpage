from django import forms

# First param is the value (displayed on the home page in light grey), second param is what the End-User sees
TYPE_CHOICES= [
    ('Electronics', 'Electronics'),
    ('Logos', 'Logos'),
    ]

class ItemForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    price = forms.CharField(max_length=100)
    type = forms.CharField(label='Type of product', widget=forms.Select(choices=TYPE_CHOICES))
    stock = forms.CharField()
    image = forms.ImageField()