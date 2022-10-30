from django.shortcuts import render
from main.models import User
from user_profile.models import DoctorProfile, UserProfile, Rating
from user_profile.forms import ChangeProfile, RatingForm
from forum.models import Forum, ForumReply
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def show_profile(request, pk):
    context = {
        "id" : pk,
        "is_doctor" : User.objects.get(pk=pk).is_doctor,
        "change_profile_form" : ChangeProfile(use_required_attribute=False),
        "rating_form" : RatingForm(),
    }
    return render(request, "profile.html", context)

def get_user(request, pk):
    if(request.method == "GET"):
        user = User.objects.get(pk = pk)
        profile = UserProfile.objects.get(user = user)
        profile.post_amount = count_questions(user)
        profile.upvote_amount = count_points(user)
        profile.save()
        response = {
            "user_id" : pk,
            "username" : user.username,
            "email" : user.email,
            "post_amount" : profile.post_amount,
            "is_doctor" : user.is_doctor,
            "bio" : profile.bio,
            "upvote_amount" : profile.upvote_amount,
            "is_logged_user" : request.user == user,
        }
        if user.is_doctor:   
            doctor = DoctorProfile.objects.get(profile = profile)
            doctor.comment_amount = count_replies(user)
            ratings_list = Rating.objects.filter(doctor = doctor)
            ratings = []
            for rating in ratings_list:
                ratings.append({
                    "author_username" : rating.author.username,
                    "author_is_doctor" : rating.author.is_doctor,
                    "author_pk" : rating.author.pk,
                    "date" : rating.date,
                    "rating" : rating.rating,
                    "comment" : rating.comment,
                    "id" : rating.id,
                })
            response.update({
                "comment_amount" : doctor.comment_amount,
                "rating_average" : doctor.rating_average,
                "ratings" : ratings,
            })
        return JsonResponse(response)

@login_required(login_url="/main/login/")
def change_profile(request, pk):
    if request.method == "POST":
        user = request.user
        profile = UserProfile.objects.get(user = user)
        new_bio = request.POST.get("bio")
        profile.bio = new_bio
        profile.save()
        return JsonResponse({"new_bio" : new_bio})

def create_rating(request, pk):
    if request.method == "POST":
        author = request.user
        doctor = DoctorProfile.objects.get(profile = UserProfile.objects.get(user = User.objects.get(pk = pk)))
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        response = {}
        if (Rating.objects.filter(author=author, doctor=doctor)):
            rating_object = Rating.objects.get(author=author, doctor=doctor)
            response.update({"old_id" : rating_object.id})
            rating_object.delete()
        rating_object = Rating.objects.create(author=author, doctor=doctor, rating=rating, comment=comment)
        rating_object.save()
        doctor.rating_average = count_average_rating(doctor)
        doctor.save()
        response.update({
            "author" : author.username,
            "rating" : rating,
            "comment" : comment,
            "date" : rating_object.date,
            "new_id" : rating_object.id,
            "is_doctor" : author.is_doctor,
            "rating_average" : doctor.rating_average,
        })
        return JsonResponse(response)

def delete_rating(request, id):
    if request.method == "DELETE":
        rating = Rating.objects.get(id = id)
        doctor = rating.doctor
        rating.delete()
        doctor.rating_average = count_average_rating(doctor)
        doctor.save()
        return JsonResponse({"rating_average" : doctor.rating_average})

# Utility
def count_questions(user):
    return Forum.objects.filter(author = user).count()

def count_points(user):
    questions = Forum.objects.filter(author = user)
    point = 0
    for question in questions:
        point += question.upvote
        point += question.downvote 
    return point
    
def count_replies(user):
    return ForumReply.objects.filter(author = user).count()

def count_average_rating(doctor):
    ratings = Rating.objects.filter(doctor = doctor)
    if ratings.count() == 0:
        return 5.0
    average_rating = 0
    for rating in ratings:
        average_rating += rating.rating
    average_rating = average_rating / ratings.count()
    return average_rating