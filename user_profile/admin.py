from django.contrib import admin
from user_profile.models import UserProfile, DoctorProfile, Rating

admin.site.register(UserProfile)
admin.site.register(DoctorProfile)
admin.site.register(Rating)
