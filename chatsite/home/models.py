from django.db import models
from django.utils.translation import gettext_lazy as _

# Wagtail
from wagtail.admin.panels import (
    FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
)
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField

import openai
from chatapp.api_key import api_key


class HomePage(Page):
    template = 'home/home_page.html'
    text = RichTextField(verbose_name=_('Text'))

    content_panels = Page.content_panels + [
        FieldPanel('text'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        openai.api_key = api_key

        user_input = request.POST.get('mytext')
        if user_input:
            #prompt = f"You said: {user_input}"
            #response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
            #context['response_text'] = response
            context["response_text"] = user_input

            return context
