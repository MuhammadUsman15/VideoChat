from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random
import time
# Create your views here.

def getToken(request):
    appId = 'You app id'
    appCertificate = 'Your Certificate'
    channelName = request.GET.get('channel')  # Use request.GET instead of request.Get
    uid=random.randint(1,230)
    expirationTimeInSeconds= 3600*24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp+expirationTimeInSeconds
    role = 1 
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token,'uid':uid},safe=False)

def lobby(request):
    return render(request, 'lobby.html')

def room(request):
    return render(request, 'room.html')