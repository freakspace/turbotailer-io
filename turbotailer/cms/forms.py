from django import forms
from django.contrib.auth.models import Group
from wagtail.admin.forms import WagtailAdminPageForm


class StandardPageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Dynamically fetch group choices from the database
        group_choices = [(group.name, group.name) for group in Group.objects.all()]
        group_choices.insert(0, ("", "---------"))  # Add a default empty choice

        # Define the role field with dynamic choices
        self.fields["role"] = forms.ChoiceField(
            choices=group_choices, required=False, help_text="Restrict access to this page by role"
        )
