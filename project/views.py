from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse

projectlist = [
    {'id':'1','title':"hamro project","description":"lauda lasan ho"},
    {'id':'2','title':"tero project","description":"lauda lasan ho"},
    {'id':'3','title':"hattiko project","description":"lauda lasan ho"},
]

def projects(request):
    title = "Projects list page"
    number = 15
    context = { "title":title, "number":number, "projects":projectlist}
    return render(request, 'project/projects.html', context)

def project (request, pid):
    projectItem = None
    for project in projectlist:
        if(project['id'] == pid):
            projectItem = project
    
    return render(request, 'project/single-project.html', {'projectItem': projectItem})
