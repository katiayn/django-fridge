from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ollama import Client

client = Client(host=settings.OLLAMA_HOST)

def fridge(request):
    context = {}
    if request.htmx:
        if request.method == "POST":
            item = request.POST.get('item', '')
            output = client.generate(
                model="llama3",
                prompt=f"Should {item} be stored in the fridge? Provide a short answer with a brief explanation.",
                stream=False,
            )
            response = output["response"]
            context = {
                "response": response,
                "item": item,
            }
            return render(request, 'partials/response.html', context=context)
    return render(request, 'storage.html', context)
