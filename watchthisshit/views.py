from django.shortcuts import render, redirect
from .models import Profile, Recommendation
from .forms import RecForm

def dashboard(request):
  all_recs = Recommendation.objects.all().order_by("-created_at")
  if request.method == "POST":
    form = RecForm(request.POST or None)
    if form.is_valid():
      rec = form.save(commit=False)
      rec.user = request.user
      rec.save()
      form.save_m2m()
      return redirect("watchthisshit:dashboard")
  form = RecForm(initial={"user": request.user.id})
  return render(request, "watchthisshit/dashboard.html", {
    "all_recs": all_recs,
    "form": form
  })

def profile_list(request):
  profiles = Profile.objects.exclude(user=request.user)
  return render(request, "watchthisshit/profile_list.html", {"profiles": profiles})

def profile(request, pk):
  if not hasattr(request.user, 'profile'):
    missing_profile = Profile(user=request.user)
    missing_profile.save()
  profile = Profile.objects.get(pk=pk)
  if request.method == "POST":
    current_user_profile = request.user.profile
    data = request.POST
    action = data.get("follow")
    if action == "follow":
      current_user_profile.follows.add(profile)
    elif action == "unfollow":
      current_user_profile.follows.remove(profile)
    current_user_profile.save()
  return render(request, "watchthisshit/profile.html", {"profile": profile})