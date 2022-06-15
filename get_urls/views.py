from django.http import JsonResponse
from django.shortcuts import render
import requests


def getUrls(request):
    if request.method == 'GET':
        try :
            url = 'https://www.reddit.com/r/images/new.json?limit=30'
            res = requests.get(url)
            urls = []
            if res:
                data = res.json()
                for child in data['data']['children']:
                    urls.append(child['data']['thumbnail'])
                return render(request, 'home.html', {'urls': urls})
            else:
                return render(request, 'home.html', {'urls': 'wait'})
        except: 
            return render(request, 'home.html', {'urls': 'limit exceeded'})
            
    return JsonResponse({'message': 'default'})
