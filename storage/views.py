import base64
import re

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


def image_to_base64(image_file):
    image_data = image_file.read()
    encoded_image = base64.b64encode(image_data)
    return encoded_image.decode("utf-8")


def split_first_paragraph(text):
    match = re.search(r"([.!?])", text)
    end_index = match.end()
    first_paragraph = text[:end_index].strip()
    remaining_text = text[end_index:].strip()
    return first_paragraph, remaining_text


def fridge_by_image(request):
    context = {}

    if request.htmx:
        if request.method == "POST" and request.FILES.get("image"):
            image_file = request.FILES["image"]
            output = client.generate(
                model="llava",
                prompt="""
                Start by briefly describing the image in the first paragraph.

                Using the description of the image, determine if the item or items shown should be stored in the 
                fridge. Provide a concise answer along with a brief explanation.
                """,
                images=[image_to_base64(image_file)],
                stream=False,
            )
            full_response = output["response"]
            description, response = split_first_paragraph(full_response)
            context = {
                "response": response,
                "description": description,
            }
            return render(request, "partials/response.html", context=context)

    return render(request, "fridge_by_image.html", context)
