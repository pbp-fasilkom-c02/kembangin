import operator
from django.shortcuts import render
from artikel.models import Artikel, Comment
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from artikel.forms import CreateArtikel, ShareExp

# showing article
@csrf_exempt
def show_artikel(request):
    artikel = {}
    top_3 = []
    formArtikel = CreateArtikel()
    formExp = ShareExp()
    data = Artikel.objects.all()

    if (len(data) != 0):
        for i in range(0, len(data)):
            artikel[data[i]] = data[i].upvote
        
        sorted_d = dict( sorted(artikel.items(), key=operator.itemgetter(1),reverse=True))
        
        i = 1
        if (len(sorted_d) < 3):
            for key, value in sorted_d.items():
                top_3.append(key)
                     
        else:
            for key, value in sorted_d.items():
                if (i == 4):
                    break
                else:
                    top_3.append(key)
                    i += 1

    if (request.user.is_authenticated):
        context = {
                "data": top_3,
                "user" : request.user,
                "auth" : request.user.is_authenticated,
                "form" : formArtikel,
                "exp" : formExp,
            } 
        
        data = request.user
        if (data.is_doctor):
            return render(request, "artikel.html", context)
        else:
            return render(request, "artikel_pasien.html", context)
    else:
        context_anonym = {
            "data": top_3,
            "auth" : request.user.is_authenticated
        }
        return render(request, "artikel_pasien.html", context_anonym)


# data json

@login_required(login_url='/login')
@csrf_exempt
def artikel_json(request):
    data = Artikel.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
@csrf_exempt
def comment_json(request):
    data = Comment.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# create new article
@csrf_exempt
def artikel_by_id_json(request, id):
    data_artikel = Artikel.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_artikel), content_type="application/json")

@login_required(login_url='/login')
@csrf_exempt
def create_new_artikel(request):
    if request.method == "POST" and CreateArtikel(request.POST).is_valid():
        photo = request.POST.get("photo")
        title = request.POST.get("title")
        description = request.POST.get("description")
        create_new_artikel = Artikel(photo=photo,title=title, description=description, author=request.user)
        create_new_artikel.save()
     
        return JsonResponse({"pk": create_new_artikel.pk, "fields": {
            # "author" : create_new_artikel.author.username,
            "photo" :create_new_artikel.photo,
            "title": create_new_artikel.title,
            "description": create_new_artikel.description,
        }})


@login_required(login_url='/login')
@csrf_exempt
def delete_artikel(request, id):
    artikel = Artikel.objects.get(pk=id)
    artikel.delete()
    
    return redirect('artikel:show_artikel')


@login_required(login_url='/login')
def edit(request, id):
    artikel = Artikel.objects.get(id=id)
    context = {'artikel': artikel}
    return render(request, 'edit.html', context)

# belum diimplementasi


@login_required(login_url='/login')
def update(request, id):
    artikel = Artikel.objects.get(id=id)
    artikel.title = request.POST['title']
    artikel.description = request.POST['description']
    artikel.save()
    return redirect('artikel:show_artikel')


@login_required(login_url='/login')
@csrf_exempt
def handle_vote(request,id,action):
    if request.method == "POST":
        artikel = get_object_or_404(Artikel, pk= id)
        if action == "up":
            artikel.upvote += 1
        elif action == "down":
            artikel.downvote += 1
        artikel.save() 
        data = {
            'upvote': artikel.upvote,
            'downvote': artikel.downvote
        }
        return JsonResponse(data)
    return HttpResponseBadRequest()


@login_required(login_url='/login')
@csrf_exempt
def share_exp(request):
    if request.method == "POST" and ShareExp(request.POST).is_valid():
        comment = request.POST.get("comment")
        create_new_comment = Comment(comment=comment, author=request.user)
        create_new_comment.save()
        return JsonResponse({"pk": create_new_comment.pk, "fields": {
            "comment": create_new_comment.comment,
        }})
