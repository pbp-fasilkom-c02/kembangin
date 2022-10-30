from datetime import datetime
import re
from time import timezone
from django.shortcuts import render
from artikel.models import Artikel, Comment
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from artikel.forms import ReplyThread

# showing article
# @login_required(login_url='/login')
# @csrf_exempt
def show_artikel(request):
    artikel = []
    top3 = []
    i= 0 
    data = Artikel.objects.all()

    # for j in range(0, len(data)):
    #     artikel.append(0)
    # print(len(artikel))
    # for j in range(0,len(data)):
    #     if (data[j].upvote > artikel[j]):
            
    #         artikel[i] = data[j].upvote
    #         top3.append(j)
    
    # fix = []
    # for i in range(0,3):
    #     fix.append(data[top3[i]])

    

    for i in range (0,3):
        artikel.append(data[i])

    context = {
        "data": artikel,
        "user" : request.user,
        "auth" : request.user.is_authenticated
    } 

    context_anonym = {
        "data": data,
        "user" : request.user.is_authenticated,
        "auth" : request.user.is_authenticated
    }

    print("auth")
    print(request.user.is_authenticated)

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

    # print(request.user)
    # data = request.user
    # context = {
    #         "berita": "dies natalies fasilkom",
    #         "data": data,
    # }
    

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
def post_comment(request, id):
    if request.method == "POST":
        print("bisa yey")
        form = ReplyThread(request.POST)
        if form.is_valid():
            print("hehe")
            # print(len(Comment.objects.all()), " besaran")
            artikel = Artikel.objects.filter(pk=id)[0]
            comment = form.cleaned_data["comment"]
            
            reply = Comment.objects.create(comment=comment, artikel=artikel, created_at=datetime.now(), author=request.user)
            reply.save()

            data = {
            "pk": reply.pk,
            "comment": reply.comment,
            "author": reply.author.username,
            "created_at": reply.created_at
            }
            print("risa")
            print(data)
            return JsonResponse(data)
    return HttpResponseBadRequest()

# @login_required(login_url='/login')
# @csrf_exempt
# def post_comment(request):
#     print("masukk")
#     if request.method == "POST":
#         comment = request.POST.get("comment")
#         # create_new_comment = get_object_or_404(Artikel, pk=id)
#         create_new_comment = Artikel(comment=comment)
#         create_new_comment.save()

#         return JsonResponse({"fields": {
#             "comment": create_new_comment.comment,
#         }})

# def add_comment(request, id):
#     if request.method == "POST":
#         form = ReplyForm(request.POST)
#         if form.is_valid():
#             if request.user.is_doctor:
#                 forum = Artikel.objects.filter(pk=id)[0]
#                 comment = form.cleaned_data["comment"]

#                 reply = ForumReply.objects.create(
#                     comment=comment, forum=forum, created_at=datetime.datetime.now(), author=request.user)

#                 data = {
#                     "pk": reply.pk,
#                     "comment": reply.comment,
#                     "author": reply.author.username,
#                     "created_at": reply.created_at
#                 }
#                 return JsonResponse(data)
#             else:
#                 response = {
#                     'status': 'error',
#                     'message': 'Kamu bukan dokter sehingga tidak bisa memberi komentar'
#                 }
#                 return JsonResponse(response)

#     return HttpResponseBadRequest()
