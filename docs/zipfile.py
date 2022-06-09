from io import BytesIO
import zipfile


def generate_zip(files):
    mem_zip = BytesIO()

    with zipfile.ZipFile(mem_zip, mode="w",compression=zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.writestr(f[0], f[1])

    return mem_zip.getvalue()
 
def generate_pdf():
	from reportlab.pdfgen.canvas import Canvas
	from reportlab.lib.pagesizes import A4
	buffer = BytesIO()
    canvas = Canvas(buffer, pagesize=A4)
    textobject = canvas.beginText(1.5 * cm, -2.5 * cm)
	textobject.textLine("Hello, world!")
	canvas.saveState()
	canvas.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
	
def main():
	file_names = ["test1.pdf", "test2.pdf"]
	files = []

	for f in file_names:
		pdf = generate_pdf() # your file generation method goes here
		files.append((f, pdf))

	full_zip_in_memory = generate_zip(files)


if __name__ == "__main__":
	main()






import io
import os
from PIL import Image
from pprint import pprint
from zipfile import ZipFile


def get_images(path):
    """ Returns a list of image file base name & PIL image object pairs. """

    # Harcoded with two images for testing purposes.
    IMAGES = (r"C:\vols\Files\PythonLib\Stack Overflow\cookie_cutter_background.png",
              r"C:\vols\Files\PythonLib\Stack Overflow\Flying-Eagle.png")

    images = []
    for image_path in IMAGES:
        # Get image file name without extension.
        image_name = os.path.splitext(os.path.os.path.basename(image_path))[0]
        pil_image = Image.open(image_path)
        images.append([image_name, pil_image])

    return images


def file_process_in_memory():
    """ Converts PIL image objects into BytesIO in-memory bytes buffers. """

    images = get_images('mypath')

    for i, (image_name, pil_image) in enumerate(images):
        file_object = io.BytesIO()
        pil_image.save(file_object, "PNG")
        pil_image.close()
        images[i][1] = file_object  # Replace PIL image object with BytesIO memory buffer.

    return images  # Return modified list.


images = file_process_in_memory()

# Create an in-memory zip file from the in-memory image file data.
zip_file_bytes_io = io.BytesIO()

with ZipFile(zip_file_bytes_io, 'w') as zip_file:
    for image_name, bytes_stream in images:
        zip_file.writestr(image_name+".png", bytes_stream.getvalue())

    pprint(zip_file.infolist())  # Print final contents of in memory zip file.

print('done')