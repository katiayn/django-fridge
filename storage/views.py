from django.conf import settings
from django.shortcuts import render
from ollama import Client


def fridge(request):
    context = {}
    client = Client(host=settings.OLLAMA_HOST)
    if request.htmx:
        if request.method == "POST":
            item = request.POST.get('item')
            output = client.generate(
                model="llama3",
                prompt=f"Should {item} be stored in the fridge? Provide a short answer with a brief explanation.",
                stream=False,
            )
            context = {
                "response": output["response"],
                "item": item,
            }
            return render(request, 'partials/response.html', context=context)
    return render(request, 'storage.html', context)
