from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render
from ollama import Client

client = Client(host=settings.OLLAMA_HOST)


def fridge_by_text(request):
    if request.htmx:
        if request.method == "POST" and request.POST.get("input_text"):
            description = request.POST.get("input_text")
            output = client.generate(
                model="llama3.1",
                prompt=f"Should {description} be stored in the fridge? Provide a concise answer followed by a brief "
                f"explanation.",
                stream=False,
            )
            context = {
                "response": output["response"],
                "description": description,
            }
            return render(request, "partials/response.html", context=context)
        return HttpResponseNotFound("Please provide an item.")
    return render(request, "fridge.html")
