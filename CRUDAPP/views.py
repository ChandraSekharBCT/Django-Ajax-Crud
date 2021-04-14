import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from CRUDAPP.models import StudentData
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="",database="django_crud")
cursor=mydb.cursor()

def HomePage(request):
    students=StudentData.objects.all()
    return render(request,"homepage.html",{"students":students})

@csrf_exempt                                                                                                          
def InsertStudent(request):
    name=request.POST.get("name")
    email=request.POST.get("email")
    gender=request.POST.get("gender")

    try:
        student=StudentData(name=name,email=email,gender=gender)
        student.save()
        stuent_data={"id":student.id,"created_at":student.created_at,"error":False,"errorMessage":"Student Added Successfully"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Failed to Add Student"}
        return JsonResponse(stuent_data,safe=False)

@csrf_exempt
def update_all(request):
    data=request.POST.get("data")
    dict_data=json.loads(data)
    try:
        for dic_single in dict_data:
            student=StudentData.objects.get(id=dic_single['id'])
            student.name=dic_single['name']
            student.email=dic_single['email']
            student.gender=dic_single['gender']
            student.save()
        stuent_data={"error":False,"errorMessage":"Updated Successfully"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Failed to Update Data"}
        return JsonResponse(stuent_data,safe=False)

@csrf_exempt
def delete_data(request):
    id=request.POST.get("id")
    try:
        student=StudentData.objects.get(id=id)
        student.delete()
        stuent_data={"error":False,"errorMessage":"Deleted Successfully"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Failed to Delete Data"}
        return JsonResponse(stuent_data,safe=False)
import csv
def insert_excel(request):
    csv_data = csv.reader(open('C:/Users/MUNA/Downloads/DjangoAjaxCRUD-master/DjangoAjaxCRUD-master/CRUDAPP/crud.csv'))
    next(csv_data)
    for row in csv_data:
        print(row)
        cursor.execute('INSERT INTO crudapp_studentdata(id,name,email,gender,created_at) VALUES(%s,%s,%s,%s,%s)',row)
    mydb.commit()
    students=StudentData.objects.all()
    return render(request,'homepage.html',{'students':students})