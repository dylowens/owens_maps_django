from django.shortcuts import render
from .forms import ImageUploadForm
from .models import ImageUpload
from .image_processing import ocr_core, get_grayscale, remove_noise, thresholding
import cv2
import numpy as np


def upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']

            # Read the uploaded image file into a numpy array
            np_image = np.frombuffer(uploaded_image.read(), np.uint8)

            # Decode the numpy array into an OpenCV image
            cv2_image = cv2.imdecode(np_image, cv2.IMREAD_UNCHANGED)

            # Preprocess the image
            gray = get_grayscale(cv2_image)
            noise = remove_noise(gray)
            thresh = thresholding(noise)

            # Perform OCR
            text = ocr_core(thresh)

            # Check if the extracted text is empty or contains only whitespace characters
            if not text.strip():
                text = "No text could be extracted from the image."

            # Save the uploaded image and extracted text to the database
            image_upload = form.save(commit=False)
            image_upload.text = text
            image_upload.save()

            return render(request, 'imagetotext/imagetotext.html', {'form': form, 'text': text})

    else:
        form = ImageUploadForm()

    return render(request, 'imagetotext/imagetotext.html', {'form': form})
    # return render(request, 'imagetotext/imagetotext.html', {'form': form, 'text': None})
