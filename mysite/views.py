from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic.base import TemplateView
from pathlib import Path


def index(request):
    return HttpResponse("""
                        <a href="broken_template_view">broken_template_view</a><br />
                        <a href="broken_render_to_string">broken_render_to_string</a><br />
                        <a href="potentially_poisoned_view">potentially_poisoned_view</a><br />
                        <a href="working_template_view">working_template_view</a><br />
                        """)

class Broken_Template_View(TemplateView):
    template_name = Path("mysite", "broken_template_view")

class Working_Template_View(TemplateView):
    template_name = "mysite/working_template_view"

class Potentially_Poisoned_Template_View(TemplateView):
    template_name = "mysite/broken_template_view"  # Reused as it shouldn't matter

def broken_render_to_string(request):
    user_selected_template = "broken_render_to_string"  # Let's assume that is some user input and we would need to validate it
    template_name = Path("mysite", user_selected_template)
    assert template_name.is_relative_to("mysite")
    return HttpResponse(render_to_string(template_name))
