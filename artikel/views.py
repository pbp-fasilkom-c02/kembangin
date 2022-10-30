import operator
from django.shortcuts import render
from artikel.models import Artikel, Comment
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404

# showing article
# @login_required(login_url='/login')
@csrf_exempt
def show_artikel(request):
    artikel = {}
    top_3 = []

    data = Artikel.objects.all()

    if (len(data) != 0):
        for i in range(0, len(data)):
            artikel[data[i]] = data[i].upvote
        
        sorted_d = dict( sorted(artikel.items(), key=operator.itemgetter(1),reverse=True))
        
        i = 1
        print(sorted_d)
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
            
    context = {
        "data": top_3,
        "user" : request.user,
        "auth" : request.user.is_authenticated
    } 

    context_anonym = {
        "data": top_3,
        "user" : request.user.is_authenticated,
        "auth" : request.user.is_authenticated
    }

    if (request.user.is_authenticated):
        data = request.user
        if (data.is_doctor):
            print("Doctor login")
            return render(request, "artikel.html", context)

        else:
            print("Pasien login")
            return render(request, "artikel_pasien.html", context)
    else:
        return render(request, "artikel_pasien.html", context_anonym)

    

@csrf_exempt
def show_detail(request):
    context = {
        "berita": "dies natalies fasilkom",
    }
    return render(request, "detail_artikel.html", context)
    
    

@csrf_exempt
def detail_artikel(request):
    # data = Artikel.objects.filter(pk=id)
    context = {
        "berita": "dies natalies fasilkom",
        # "data" : data,
    }
    return render(request, "detail_artikel.html", context)

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
    # if (request.user.username == "halo"):
    #     print("ada")
    # else:
    #     print("gaada")
    #     print(type(request.user))
    #     print("gaada")
    if request.method == "POST":
        image = request.POST.get("image")
        title = request.POST.get("title")
        description = request.POST.get("description")
        create_new_artikel = Artikel(photo=image,title=title, description=description, author=request.user)
        create_new_artikel.save()
     
        return JsonResponse({"pk": create_new_artikel.pk, "fields": {
            "image" :create_new_artikel.photo,
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
    # if (request.user.username == "halo"):
    #     print("ada")
    # else:
    #     print("gaada")
    #     print(type(request.user))
    #     print("gaada")
    if request.method == "POST":
        comment = request.POST.get("comment")
        create_new_comment = Comment(comment=comment, author=request.user)
        create_new_comment.save()
        print("berhasil")
        return JsonResponse({"pk": create_new_comment.pk, "fields": {
            "comment": create_new_comment.comment,
        }})
