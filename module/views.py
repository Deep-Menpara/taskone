from django.shortcuts import render, redirect
import json
from urllib.request import urlopen
from module.models import data
# Create your views here.
def home(request):


    li=data.objects.all().order_by('-popularity')

    return render(request, 'Home.html',{'list':li})

def load(request):
    url = "https://s3.amazonaws.com/open-to-cors/assignment.json"

    response = urlopen(url)

    data_json = json.loads(response.read())
    products = data_json['products']
    for temp in products:
        if data.objects.filter(subid=temp).exists():
            pass
        else:
            dict = {}
            for temp2 in products[temp]:
                dict[temp2] = products[temp][temp2]
            data.objects.create(subid=temp, subcategory=dict["subcategory"], title=dict["title"], price=dict["price"],
                                popularity=dict["popularity"])
    return redirect("/")