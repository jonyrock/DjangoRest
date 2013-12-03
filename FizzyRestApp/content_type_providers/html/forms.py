from django import forms
from FizzyRestApp.models import Manufacturer

class ManufacturerForm(forms.Form):
    title = forms.CharField(max_length=100)
    yearFounded = forms.IntegerField()
    imageUrl = forms.URLField(max_length=100)

    def get_obj(self):
        m = Manufacturer()
        m.title = self.data['title']
        m.yearFounded = self.data['yearFounded']
        m.imageUrl = self.data['imageUrl']
        return m

class DrinkForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    calories = forms.IntegerField()
    imageUrl = forms.URLField(max_length=100)

    def get_obj(self):
        m = Manufacturer()
        m.title = self.data['title']
        m.description = self.data['description']
        m.calories = self.data['calories']
        m.imageUrl = self.data['imageUrl']
        return m