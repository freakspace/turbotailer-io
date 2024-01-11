from django import forms
from django.utils.translation import gettext as _

from .models import Audit


class AuditForm(forms.ModelForm):
    class Meta:
        model = Audit
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs[
            "class"
        ] = "form-input rounded-xl bg-black/5 border-2 border-white/50 shadow-lg placeholder-white text-white w-full"
        self.fields["name"].widget.attrs["placeholder"] = _("Name")
        self.fields["website"].widget.attrs[
            "class"
        ] = "form-input rounded-xl bg-black/5 border-2 border-white/50 shadow-lg placeholder-white w-full"
        self.fields["website"].widget.attrs["placeholder"] = _("Website")
        self.fields["email"].widget.attrs[
            "class"
        ] = "form-input rounded-xl bg-black/5 border-2 border-white/50 shadow-lg placeholder-white w-full"
        self.fields["email"].widget.attrs["placeholder"] = _("E-mail")
