from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from start.views import Addition, Subtraction, Division, Multiplication, WorkDB
from start.models import SaveTask
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
    results = [[ None for y in range( 3 )] for x in range( 10 )]
    print (results)
    #numberOne = [ None for y in range( 10 )]
    #numberTwo = [ None for y in range( 10 )]
    #summa = [ None for y in range( 10 )]

    for i in range (10):
        res =  Addition()
        result = res.action()
        results[i][0] = result[0]
        results[i][1] = result[1]
        results[i][2] = result[2]
        #print (results[i][0])
        #numberOne[i] = result[0]
        #numberTwo[i] = result[1]
        #summa[i] = result[2]

    WorkDB.insertTask(results, "Addition", request)
    print (results)

    #json_res = JsonResponse({"res":result})
    #print (json_res)
    #return render (request, "train_add.html")

    #return render (request, "train_add.html", {"json_res": json_res})

    return render (request, "train_add.html", context = {"results":results})
