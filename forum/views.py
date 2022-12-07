
from django.http import JsonResponse
from django.http import HttpResponse,HttpResponseBadRequest
from django.shortcuts import render,get_object_or_404
from forum.models import Forum, ForumReply
from forum.forms import ForumForm, ReplyForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime


def show_forum_index(request):
    form = ForumForm()
    return render(request, "forum_index.html",{'form':form})

@login_required(login_url='/login')
def show_forum_detail(request,pk):
    form = ReplyForm()
    return render(request, "forum_detail.html",{'form':form, 'pk':pk})

def get_forum_by_pk(request,pk):
    replies = []
    forum = Forum.objects.filter(pk=pk)[0]

    for reply in forum.forumreply_set.all():
            replies.append({
                'comment': reply.comment,
                'author': reply.author.username,
                'created_at': reply.created_at,
                'pk':reply.pk,
                'author_pk': reply.author.pk
            })
    
    data = {
            'question': forum.question,
            'author': forum.author.username,
            'description': forum.description,
            'created_at' : forum.created_at,
            'is_doctor': forum.author.is_doctor,
            'pk': forum.pk,
            'replies': replies,
            'upvote': forum.upvote,
            'downvote': forum.downvote,
            'author_pk': forum.author.pk
        }
    
    return JsonResponse(data)


def get_forums_json(request):
    list_of_forums = []
    forums = Forum.objects.all()
 
    for forum in forums:
        replies = []
        for reply in forum.forumreply_set.all():
            replies.append({
                'comment': reply.comment,
                'author': reply.author.username,
                'created_at': reply.created_at,
                'pk':reply.pk,
                'author_pk': reply.author.pk
            })
        list_of_forums.append({
            'question': forum.question,
            'author': forum.author.username,
            'description': forum.description,
            'created_at' : forum.created_at,
            'is_doctor': forum.author.is_doctor,
            'pk': forum.pk,
            'replies': replies,
            'upvote': forum.upvote,
            'downvote': forum.downvote,
            'author_pk': forum.author.pk
        })
    return JsonResponse(list_of_forums,safe=False)



    

@csrf_exempt
def add_forum(request):

    if request.method == "POST":
        form = ForumForm(request.POST)
        if form.is_valid():
            if request.user.username != "":

                question = form.cleaned_data["question"]
                description = form.cleaned_data["description"]
                forum = Forum.objects.create(question=question,description=description,created_at=datetime.datetime.now(),author=request.user)

                data = {
                "status":True,
                "pk": forum.pk,
                "question": forum.question,
                "description": forum.description,
                "author": forum.author.username,
                'is_doctor': forum.author.is_doctor,
                "created_at": forum.created_at,
                'upvote': forum.upvote,
                'downvote': forum.downvote,
                'replies': [],
                'author_pk': forum.author.pk
                }
                return JsonResponse(data)
            else:
                return JsonResponse({'status':False, 'message':'Anda harus login terlebih dahulu'})
        else:
            return JsonResponse({'status':False, 'message':"Input tidak valid!"})



    return HttpResponseBadRequest()

@login_required(login_url='/login')
@csrf_exempt
def add_comment(request,pk):

    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            if request.user.is_doctor:
                forum = Forum.objects.filter(pk=pk)[0]
                comment = form.cleaned_data["comment"]
                
                reply = ForumReply.objects.create(comment=comment,forum=forum, created_at=datetime.datetime.now(), author=request.user)
                
                data = {
                "status":True,
                "pk": reply.pk,
                "comment": reply.comment,
                "author": reply.author.username,
                "created_at": reply.created_at,
                "author_pk": reply.author.pk
                }
                return JsonResponse(data)
            else:
                response = {
                    'status': False,
                    'message': 'Kamu bukan dokter sehingga tidak bisa memberi komentar'
                }
                return JsonResponse(response)
        return JsonResponse({'status':False, 'message':"Input tidak valid!"})
    return HttpResponseBadRequest()

@csrf_exempt
def delete_forum(request,id):

    

    if request.method == "DELETE":
        post = get_object_or_404(Forum, id = id)
        
        if post.author.username != request.user.username:
            response = {
                'status': False,
                'message': 'Kamu tidak bisa menghapus post orang lain!'
            }
            return JsonResponse(response)
        else:

            post.delete()

            return JsonResponse({'status':False,'message':"Forum berhasil dihapus"})


@login_required(login_url='/login')
@csrf_exempt
def delete_comment(request,pk):

    if request.method == "DELETE":
        reply = get_object_or_404(ForumReply, id = pk)
        
        if reply.author.username != request.user.username:
            response = {
                'status': False,
                'message': 'Kamu tidak bisa menghapus komentar orang lain!'
            }
            return JsonResponse(response)
        else:
            reply.delete()
            return JsonResponse({'status':True,'message':"Forum berhasil dihapus"})
  

@csrf_exempt
def delete_forum_flutter(request,id, current_username):

      if request.method == "DELETE":
        post = get_object_or_404(Forum, id = id)
        
        if post.author.username != current_username:
            response = {
                'status': False,
                'message': 'Kamu tidak bisa menghapus post orang lain!'
            }
            return JsonResponse(response)
        else:
            post.delete()
            return JsonResponse({'status':True,'message':"Forum berhasil dihapus"})


@login_required(login_url='/login')
@csrf_exempt
def handle_vote(request,pk,action):
    replies=[]
    forum = Forum.objects.filter(pk=pk)[0]

    if request.method == "PUT":
        forum = get_object_or_404(Forum, id = pk)
        if action == "up":
            forum.upvote +=1
        elif action == "down":
            forum.downvote +=1

        forum.save()
        for reply in forum.forumreply_set.all():
            replies.append({
                'comment': reply.comment,
                'author': reply.author.username,
                'created_at': reply.created_at,
                'pk':reply.pk,
                'author_pk': reply.author.pk
            }) 
        data = {
            'question': forum.question,
            'author': forum.author.username,
            'description': forum.description,
            'created_at' : forum.created_at,
            'is_doctor': forum.author.is_doctor,
            'pk': forum.pk,
            'replies': replies,
            'upvote': forum.upvote,
            'downvote': forum.downvote,
            'author_pk': forum.author.pk
        }

        return JsonResponse(data)
    
    return HttpResponseBadRequest()

   