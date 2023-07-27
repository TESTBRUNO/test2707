from django.shortcuts import render

from django.http import HttpResponse


from myapp.models import tech, tech_img


def index(request):
    data = tech.objects.all()
    request.session["a"] = 1
    return render(request, 'index.html', {"data": data} )



def card(request,myid):
    data = tech.objects.filter(id = myid)

    if request.session["a"] == 1:
        pass

    img = tech_img.objects.filter(tech = myid)
    print(img)
    print(len(data))
    if len(data) != 0:

        return render(request, "card.html", {"id" : data, "img":img} )
    else:
        return HttpResponse("Товар не найден")


# Create your views here.
