# Import the required modules
from PIL import Image
import os

# Define the directory to check
directory = "photos"

# Create an empty list to store the photo files
photos = []

# Loop through the directory and append the photo files to the list
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jbeg"):
        photos.append(filename)

# Check if the list is empty or not
if photos:
    print("converting...")
    # Create an empty list to store the image objects
    images = []
    # Loop through the photo files and append the image objects to the list
    for photo in photos:
        image = Image.open(os.path.join(directory, photo))
        # Convert the image from RGBA to RGB mode
        image = image.convert('RGB')
        images.append(image)
    # Convert the first image to pdf and save it as photos.pdf
    images[0].save("photos.pdf", "PDF", resolution=100.0, save_all=True, append_images=images[1:])
    print("done")
else:
    print("The directory does not contain photos.")
