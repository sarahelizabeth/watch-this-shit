from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile, Recommendation

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username", "password"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)

admin.site.register(Recommendation)