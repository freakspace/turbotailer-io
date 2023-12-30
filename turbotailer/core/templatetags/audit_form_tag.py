from django import template

from turbotailer.core.forms import AuditForm

register = template.Library()


@register.inclusion_tag("core/includes/audit_form.html", takes_context=True)
def get_audit_form(context):
    return {"form": AuditForm()}
