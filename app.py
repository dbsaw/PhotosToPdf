import sys
from os import listdir
from os.path import isfile, join
from PIL import Image
from fpdf import FPDF, FPDFException

# Check if there are enough arguments
if len(sys.argv) != 2:
  print("Usage: python script.py file_name")
  exit()

# Get the file name from the arguments
file_name = sys.argv[1]

# Set the folder name to "photos"
mypath = "photos"

# Create a PDF object
pdf = FPDF("P", "mm")

# Try to create and save the PDF file
try:
  # Create a list of photo file names from the folder
  photos = [f for f in listdir(mypath) if isfile(join(mypath, f))]

  # Check if there are any photos in the folder
  if len(photos) == 0:
    print(f"No photos found in {mypath}")
    exit()

  # Loop through the photos
  for photo in photos:
    # Open the photo as an image object
    image = Image.open(join(mypath, photo))
    # Get the width and height of the image in pixels
    width, height = image.size
    # Get the DPI of the image
    dpi = image.info.get("dpi", (96, 96))
    # Check if the DPI is valid
    if dpi[0] <= 0 or dpi[1] <= 0:
      raise ValueError(f"Invalid DPI: {dpi}")
    # Convert the width and height to millimeters using the DPI
    width_mm = width / dpi[0] * 25.4
    height_mm = height / dpi[1] * 25.4
    # Add a new page to the PDF with the same size as the image
    pdf.add_page(format=(width_mm, height_mm))
    # Set the position of the image to (0,0) which is the top left corner of the page
    pdf.image(join(mypath, photo), x=0, y=0)
  
  # Save the PDF file with the given name
  pdf.output(file_name + ".pdf")
except ValueError as e:
  # Handle the case when the DPI is not valid
  print(f"Value error: {e}")
finally:
  # Perform some cleanup actions after trying to create and save the PDF file
  print("...")