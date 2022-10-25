from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from forum.models import Forum, ForumReply
from forum.forms import ForumForm




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
            'replies': replies,
            
        })


    return JsonResponse(list_of_forums,safe=False)

    




def show_forum_detail(request):

    return HttpResponse()
    # return render(request, "profile.html", context)