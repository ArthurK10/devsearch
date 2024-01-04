from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'SolarStream',
        'description': "SolarStream is an initiative focused on harnessing solar energy for sustainable water purification."
    },
    {
        'id': '2',
        'title': 'GreenScape',
        'description': "GreenScape is an urban greening project that aims to transform cityscapes by integrating vertical gardens."
    },
    {
        'id': '3',
        'title': 'EduTech Bridge',
        'description': "EduTech Bridge is an educational technology project aimed at bridging the digital divide in education."
    },
]

# Create your views here.
def projects(request):
    msg = 'brown recluse'
    num = 9
    context = {'massage': msg, 'number': num, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})