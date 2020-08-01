from django.shortcuts import render
from Project2_Covid_19.settings import Covid_19_file
import json

def indexPage(request):
    data=json.loads(open(Covid_19_file).read())
    states=[state for state in data]
    states.pop(0)
    return render(request,"index.html",{"states_name":states})

s_name=None
def state_name(request):
    state_name=request.GET.get("s_name")
    global  s_name
    s_name=state_name
    data = json.loads(open(Covid_19_file).read())
    district=[]
    for x in data[state_name]["districtData"]:
        district.append(x)
    district.pop(0)
    return render(request,"statewise_district.html",{"sname":state_name,"dist_name":district})


def district_name(request):
    d_name=request.GET.get("d_name")
    global s_name
    data = json.loads(open(Covid_19_file).read())
    details=data[s_name]["districtData"][d_name]
    return render(request,"district_name.html",{"s_name":s_name,"d_name":d_name,"details":details})