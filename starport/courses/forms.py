from django import forms
from .fields import repo_url_field


class AddtoQueueForm(forms.Form):
    repo_url = repo_url_field(label="GitHub URL", max_length=50)

    def clean(self):
        cleaned_data = super(AddtoQueueForm, self).clean()
        cleaned_url = cleaned_data.get("repo_url")
        # if cleaned_url:
        #     if cleaned_url[: cleaned_url.find("/")].lower() == "onlyphantom":
        #         msg = "onlyphantom adds his own repo."
        #         self.add_error("repo_url", msg)

