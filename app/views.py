from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def keyboard(request):
    return JsonResponse(
        {
        'type':'buttons',
        'buttons':['1','2','3']
        }
    )

@csrf_exempt
def message(request):
    return JsonResponse({
        'message':{
            'text':'Working well'
        },
        'keyboard':{
            'type':'buttons',
            'buttons':['5번','6번']
        }
    })
