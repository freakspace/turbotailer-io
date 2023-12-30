from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from .forms import AuditForm


class AuditCreateView(View):
    template_name = "core/includes/audit_form.html"
    form_class = AuditForm
    success_url = "/"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Tak! Du vil blive kontaktet snarest"))
            return redirect(self.success_url)

        return render(request, self.template_name, {"form": form})
