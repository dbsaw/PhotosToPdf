# Import the required libraries
from os import listdir
from os.path import isfile, join
from PIL import Image
from fpdf import FPDF

# Create a list of photo file names from a folder named "photos"
mypath = "photos"
photos = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# Create a PDF object
pdf = FPDF("P", "mm")

# Loop through the photos
for photo in photos:
  # Open the photo as an image object
  image = Image.open(join(mypath, photo))
  # Get the width and height of the image in pixels
  width, height = image.size
  # Get the DPI of the image
  dpi = image.info.get("dpi", (96, 96))
  # Convert the width and height to millimeters using the DPI
  width_mm = width / dpi[0] * 25.4
  height_mm = height / dpi[1] * 25.4
  # Add a new page to the PDF with the same size as the image
  pdf.add_page(format=(width_mm, height_mm))
  # Set the position of the image to (0,0) which is the top left corner of the page
  pdf.image(join(mypath, photo), x=0, y=0)
  
# Save the PDF file with a name
pdf.output("photos.pdf")