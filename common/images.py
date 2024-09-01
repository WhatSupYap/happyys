import os
from django.urls import path
from django.http import HttpResponse, Http404
from django.conf import settings
from mimetypes import guess_type


def get_image(request, path):    
    rootpath = settings.MEDIA_ROOT
    image_path = os.path.join(rootpath, "uploads", path) 

    # Check if the image file exists
    if os.path.exists(image_path):
        # Open the image file
        with open(image_path, "rb") as file:
            # Read the image data
            image_data = file.read()
        # Guess the content type of the image
        content_type, _ = guess_type(image_path)
        # Return the image data
        return HttpResponse(image_data, content_type=content_type)
    else:
        # Raise a 404 error if the image file does not exist
        raise Http404("Image not found")
    

# def get_image(reqeust, path):
#     image_path = os.path.join("media", "upload", path) 

#     # Check if the image file exists
#     if os.path.exists(image_path):
#         # Open the image file
#         with open(image_path, "rb") as file:
#             # Read the image data
#             image_data = file.read()
#         # Return the image data
#         return HttpResponse(image_data, content_type="image/jpeg")
#     else:
#         # Return an empty string if the image file does not exist
#         raise Http404("Image not found")
