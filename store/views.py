from django.shortcuts import HttpResponse,redirect
import datetime



# Create your views here.


def main(request):
    return HttpResponse ('Hello, its my project!')
def now_date(request):
    return HttpResponse(datetime.datetime.now().date())
def goodby(request):
    return HttpResponse('Goodby user!')









