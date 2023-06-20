from django import forms
from django.db.models import Q
from .models import Profile, Recommendation, MediaType, Comment

MEDIA_CHOICES = (
  ("Film", "Film"),
  ("Show", "TV Show"),
  ("Book", "Book"),
)

class RecForm(forms.ModelForm):
  title = forms.CharField(widget=forms.TextInput(
    attrs={
      "class": "mb-2 input is-success"
    }
  ), required=True)
  description = forms.CharField(widget=forms.widgets.Textarea(
    attrs={
      "placeholder": "You don't have to write a description, but it would be pretty cool if you did...",
      "class": "mb-2 textarea is-success is-small",
      "rows": "3"
    }
  ), label="")
  recipients = forms.ModelMultipleChoiceField(
    queryset=None,
    widget=forms.CheckboxSelectMultiple
  )
  media_type = forms.ModelChoiceField(
    queryset=MediaType.objects.exclude(name__exact="Media"),
    widget=forms.RadioSelect(attrs={ "class": "mb-2" })
  )

  class Meta:
    model = Recommendation
    fields = ["title", "description", "media_type", "recipients"]
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    current_user_id = self.initial.get('user', None)
    self.fields["recipients"].queryset = Profile.objects.exclude(Q(pk=current_user_id) | Q(user_id=6))

class CommentForm(forms.ModelForm):
  body = forms.CharField(widget=forms.widgets.Textarea(
    attrs={
      "placeholder": "That's just, like, your opinion, man...",
      "class": "mb-2 textarea is-success is-small",
      "rows": "3"
    }
  ), label="")
  class Meta:
    model = Comment
    fields = ('body',)
