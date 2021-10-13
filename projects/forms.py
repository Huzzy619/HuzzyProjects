from django.forms import Form, fields, models
from .models import Works


# This class creates the form 

class WorksForm (models.ModelForm):
    class Meta:
        model = Works
        fields = ('Project_title', 'About_project')




