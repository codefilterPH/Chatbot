from django.db import models
from django.utils.translation import gettext_lazy as _

# Wagtail
from wagtail.admin.panels import (
    FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
)
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from chatapp.models import OpenAIKey


class HomePage(Page):
    template = 'home/home_page.html'
    text = RichTextField(verbose_name=_('Text'))

    content_panels = Page.content_panels + [
        FieldPanel('text'),
    ]

    class Meta:
        verbose_name = "Home"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        try:
            key = OpenAIKey.objects.get()
        except OpenAIKey.DoesNotExist:
            # If no API key exists, create a new one and save it to the database
            api_key = "Replace me with valid API KEY"
            ai_model = "text-davinci-003"
            token = 50
            key = OpenAIKey.objects.create(
                name="API KEY",
                key=api_key,
                model=ai_model,
                max_tokens=token
            )

        if key.key is not None:
            context['api_key'] = key.key
        if key.model is not None:
            context['ai_model'] = key.model
        if key.max_tokens is not None:
            context['max_tokens'] = key.max_tokens
        return context
