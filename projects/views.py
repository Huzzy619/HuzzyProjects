from projects.models import Works
from django.shortcuts import render
from .forms import WorksForm 
from django.contrib import messages
from django.views.generic import ListView




# Create your views here.

# This method processes the form and save the data onto the database after validation 
def registerProject (request):
    if request.method == 'POST':
        form = WorksForm (request.POST)
        if form.is_valid:
            form.save()
            title = form.cleaned_data.get('Project_title')
            messages.success(request, f'The work titled "{title}" has been saved to the database')
    else:
        form = WorksForm ()
    
    return render ( request, 'projects/base.html', {'form':form}  )
        
# This is a class based view that helps project information from the database onto html file before it is displayed
class ProjectListView (ListView):
    model = Works  # name of relation

    template_name = 'projects/home.html'  

    context_object_name = 'works' # the object name with which the attributes of the relation will be extracted


