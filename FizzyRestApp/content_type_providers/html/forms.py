from django import forms
from FizzyRestApp.models import Task

class TaskForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=0)
    fileUrl = forms.URLField(max_length=100)

    def get_obj(self):
        t = Task()
        t.title = self.data['title']
        t.fileUrl = self.data['imageUrl']
        return t