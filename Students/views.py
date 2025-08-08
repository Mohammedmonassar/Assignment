from django.shortcuts import render

# Create your views here.
def index(request):
    name={"fname":"Mohammed Noman"}
    return render(request,'index.html',name)

def home(request):
    return render(request,'home.html')

def show_students(request):
    return render(request,'showStudents.html')

def edit_students(request):
    students ={
        "total" : 300,
        "marks":{
            "Software Engineering":100,
            "Image Processing ":100,
            "Client and Server ":100}}
    return render(request,'editStudents.html',students)

    

def delete_students(request):
    return render(request,'deleteStudents.html')

def list_students(request):
    students ={
        "name" : "Mohammed Noman Munassar",
        "marks":[100,100,100,100],
        "subjects":{
            "Software Engineering":100,
            "Image Processing ":100,
            "Client and Server ":100}}
    return render(request,'showStudents.html',students)

    