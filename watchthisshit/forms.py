from django import forms
from django.db.models.base import Model
from .models import Profile, Recommendation

class RecForm(forms.ModelForm):
  title = forms.CharField(required=True)
  description = forms.CharField(widget=forms.widgets.Textarea(
    attrs={
      "placeholder": "You don't have to write a description, but it would be pretty cool if you did...",
      "class": "textarea is-success is-medium"
    }
  ), label="",)
  recipients = forms.ModelMultipleChoiceField(
    queryset=Profile.objects.all(),
    widget=forms.CheckboxSelectMultiple
  )

  class Meta:
    model = Recommendation
    fields = ["title", "description", "recipients"]
    # exclude = ("user", )
