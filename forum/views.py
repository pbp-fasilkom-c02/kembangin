
from django.http import JsonResponse
from django.http import HttpResponse,HttpResponseBadRequest
from django.shortcuts import render,get_object_or_404
from forum.models import Forum, ForumReply
from forum.forms import ForumForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.contrib import messages



def show_forum_index(request):
    form = ForumForm()
    return render(request, "forum_index.html",{'form':form})



def get_forums_json(request):


    list_of_forums = []
    forums = Forum.objects.all()
    replies = []
    for forum in forums:
        for reply in forum.forumreply_set.all():
            replies.append({
                'comment': reply.comment,
                'author': reply.author.username,
                'created_at': reply.created_at
            })
        list_of_forums.append({
            'question': forum.question,
            'author': forum.author.username,
            'description': forum.description,
            'created_at' : forum.created_at,
            'pk': forum.pk,
            'replies': replies,
        })


    return JsonResponse(list_of_forums,safe=False)

    
@login_required(login_url='/login')
@csrf_exempt
def add_forum(request):
    print("dsaasdas")
    if request.method == "POST":
        form = ForumForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data["question"]
            description = form.cleaned_data["description"]
            forum = Forum.objects.create(question=question,description=description,created_at=datetime.datetime.now(),author=request.user)

            data = {
            "pk": forum.pk,
            "question": forum.question,
            "description": forum.description,
            "author": forum.author.username,
            "created_at": forum.created_at
            }
            

        return JsonResponse(data)

    return HttpResponseBadRequest()

@login_required(login_url='/login')
@csrf_exempt
def delete_forum(request,id):

    

    if request.method == "DELETE":
        task = get_object_or_404(Forum, id = id)
        
        if task.author.username != request.user.username:
            response = {
                'status': 'error',
                'message': 'Kamu tidak bisa menghapus post orang lain!'
            }
            return JsonResponse(response)
        task.delete()

    return HttpResponse(status=202)

def show_forum_detail(request):

    return HttpResponse()
    # return render(request, "profile.html", context)