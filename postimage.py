from slack import WebClient
from PIL import Image
from tempfile import NamedTemporaryFile

CHANNEL='#xyzxyz'
TOKEN_FILENAME='slack_api_token'

def post_image(filename):
    with open(TOKEN_FILENAME) as tf:
        token = tf.read().strip()

    client = WebClient(token=token)

    with Image.open(filename) as img:
        img2 = img.crop((0,0,799,285))
        with NamedTemporaryFile(suffix=".png") as outfile:
            img2.save(outfile)
            print(outfile.name)
            client.files_upload(file=outfile.name, channels="#xyzxyz", 
                title="CU Coronavirus update", filetype="png", filename="corona.png")
