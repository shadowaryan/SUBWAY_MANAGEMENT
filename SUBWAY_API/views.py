from django.shortcuts import render, HttpResponse
from .models import Record
from datetime import datetime
def swipe_in(request):
    if request.method != "POST":
        return HttpResponse('invalid response')
    
    """
    POST request for swipe_out
    """    

    user_id = request.POST.get('user_id')
    station_id = request.POST.get('station_id')
    action = 'swipe_in'
    timestamp = datetime.strptime(request.POST.get('datetime'), '%d/%m/%Y %H:%M')

    record = Record(user_id=user_id, station_id=station_id, action=action, datetime=timestamp)
    record.save()

    return HttpResponse("DONE..!!")


def swipe_out(request):
    if request.method != "POST":
        return HttpResponse('invalid response')

    """
    POST request for swipe_out
    """    
    
        
    user_id = request.POST.get('user_id')
    station_id = request.POST.get('station_id')
    action = 'swipe_out'
    timestamp = datetime.strptime(request.POST.get('datetime'), '%d/%m/%Y %H:%M')

    record = Record(user_id=user_id, station_id=station_id, action=action, datetime=timestamp)
    record.save()

    return HttpResponse("DONE..!!")