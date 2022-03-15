import numpy as np
import base64
from PIL import Image
import io
import os
from app.utils.amazon_s3 import AmazonS3

s3 = AmazonS3()

class UploadService:
    def __init__(self):
        pass

    def convert_base64(self,decoded_image,image_name):
        file_name = image_name.split('.')[0]

        # for saving in static folder, preprocessing purposes
        raw_bytes = io.BytesIO(base64.b64decode(decoded_image))
        im = Image.open(raw_bytes)

        # for uploading to aws s3, development purposes
        s3_bytes = io.BytesIO(base64.b64decode(decoded_image))
        s3_bytes.seek(0)

        for f in os.listdir('./images'):
            os.remove(os.path.join('./images',f))
        im.save('./images/'+file_name+'.png','PNG')

        # img_base64 = base64.b64encode(raw_bytes.getvalue()).decode('ascii')
        # mime = "image/png"
        # uri = "data:%s;base64,%s" % (mime, img_base64)
        return s3.uploads(s3_bytes,f"{file_name}.png",'photo')