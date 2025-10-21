import base64
import io
import PIL.Image
from IPython.core.display import HTML
from IPython.core.display_functions import display


def convert_image_to_base64(file_path):
    image = PIL.Image.open(file_path)
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    base64_image = base64.b64encode(buffered.getvalue())
    return base64_image

def visualize_base64_image(base64_image):
    image_html = f'<img src="data:image/jpeg;base64,{base64_image}"/>'
    display(HTML(image_html))

converted_image = convert_image_to_base64("niagara_falls.jpeg")

visualize_base64_image(converted_image)