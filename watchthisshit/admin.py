from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile, Recommendation, MediaType, Genre, Comment

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)

admin.site.register(Recommendation)
admin.site.register(MediaType)
admin.site.register(Genre)
admin.site.register(Comment)