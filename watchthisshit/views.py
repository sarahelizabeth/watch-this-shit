from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Recommendation, MediaType
from .forms import RecForm

def dashboard(request):
  all_recs = Recommendation.objects.all().order_by("-created_at")
  media_types = MediaType.objects.all().exclude(name__exact="Media")
  if request.method == "POST":
    form = RecForm(request.POST or None)
    if form.is_valid():
      rec = form.save(commit=False)
      rec.user = request.user
      rec.save()
      form.save_m2m()
      return redirect("watchthisshit:dashboard")
  form = RecForm(initial={"user": request.user.id})
  context = {
    "all_recs": all_recs,
    "media_types": media_types,
    "form": form
  }
  return render(request, "watchthisshit/dashboard.html", context)

def profile_list(request):
  profiles = Profile.objects.exclude(user=request.user)
  return render(request, "watchthisshit/profile_list.html", {"profiles": profiles})

@login_required
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

def recommendation(request, pk):
  rec = get_object_or_404(Recommendation, pk=pk)
  current_rec_id = rec.id
  recent_recs = rec.user.recs.all().exclude(pk=current_rec_id).order_by("-created_at")[:5]
  return render(request, "watchthisshit/recommendation.html", {
    "rec": rec,
    "recent_recs": recent_recs,
  })