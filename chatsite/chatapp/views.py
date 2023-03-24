from django.shortcuts import render
from .models import OpenAIKey
# Create your views here.


def some_view(request):
    # Get the API key from some source (e.g. environment variable)
    api_key = "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"

    # Create a new instance of the OpenAIKey model and save the API key
    key = OpenAIKey.objects.create(key=api_key)

    # Do something with the API key, such as passing it to a template
    return render(request, 'home_page.html', {'api_key': key.key})