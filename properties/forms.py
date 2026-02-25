from django import forms
from .models import Property
from .models import PropertyLocation
from .models import Listing

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price']

class PropertyLocationForm(forms.ModelForm):
    class Meta:
        model = PropertyLocation
        fields = ['address', 'city', 'country', 'latitude', 'longitude']

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['price', 'status']
