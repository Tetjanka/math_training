from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from start.views import Addition, Subtraction, Division, Multiplication
import json

def index(request):
     return render(request, "index.html")

@csrf_exempt
def start(request):
    if request.method == 'POST':
        bodyUnicode = request.body.decode('utf-8')
        body = json.loads(bodyUnicode)

        if body == "add":
            #res =  Addition()
            #result = res.action()
            #return JsonResponse({"res":result})
            train_add()
        elif body == "subtr":
            res =  Subtraction()
            result = res.action()
            return JsonResponse({"res":result})
        elif body == "divis":

            res =  Division()
            result = res.action()
            return JsonResponse({"res":result})
            return JsonResponse({"res":body})
        elif body == "multi":
            res =  Multiplication()
            result = res.action()
            return JsonResponse({"res":result})
    else:
        return render(request, "start.html")

def auth(request):
    return render(request, "auth.html")

def settings(request):
    return HttpResponse("<h2>Налаштування</h2>")

def train_add(request):
    print ("we get add request")
    res =  Addition()
    result = res.action()
    print (result[0])
    numberOne = result[0];
    numberTwo = result[1];
    summa = result[2];
    #json_res = JsonResponse({"res":result})
    #print (json_res)

    #return render (request, "train_add.html", {"json_res": json_res})

    return render (request, "train_add.html", context = {"numberOne":numberOne, "numberTwo": numberTwo, "summa": summa})
