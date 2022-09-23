import os
from django.shortcuts import render
import subprocess
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse
from .models import files

def index(request):
    a = files.objects.all()

    return render(request,'index.html',{'a':a})
    # return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def upload(request):
    # link = os.path.join(os.getcwd(),"static/p_pdf/unit3.pptx")
    # print(os.path.join('static/p_pdf/unit3.pptx'))
    # print(os.path.join(os.getcwd(),'static/p_pdf/unit3.pptx'))
    # print(type(request.FILES['file']))
    request_file = request.FILES['file']

    print( request_file.name)

    file = files(file_name=request_file,file=request_file,extension=request_file.name.split('.')[-1])
    file.save()
    print(file.file,type(file.file),file.file_name,'26')
    # file.file_name = file



    print(type(file.filename),file.filename,'name')
   

    # file.save()
    try:
        # if files.objects.filter()

        p = subprocess.Popen(f"ppt2pdf file ./media/{file.file}",
                     stdout=subprocess.PIPE, shell=True)
        print(p.communicate())
        # print(link)
        # return HttpResponse("Done...")'/
        print(type(file.file_name) , "file",file.file,'37')
        return render(request,'download.html',{'file':file,'name':(file.filename).split('.')[0]})
    except Exception as e:
        print(e)
        return HttpResponse("Error...")

    
