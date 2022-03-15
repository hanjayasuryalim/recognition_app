import boto3
import os

class AmazonS3:
    def __init__(self):
        self.BUCKET = os.environ.get('BUCKET_NAME')
        self.REGION = os.environ.get('REGION')
        self.ACCESS_KEY = os.environ.get('ACCESS_KEY_ID')
        self.ACCESS_SECRET_KEY = os.environ.get('ACCESS_SECRET_KEY')
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=self.ACCESS_KEY,
            aws_secret_access_key=self.ACCESS_SECRET_KEY
        )

    def uploads(self,file,file_name,type):
        path = f"{type}/{file_name}"
        self.s3.upload_fileobj(file,self.BUCKET,path,ExtraArgs={'ContentType': 'image/png'})
        return f"https://{self.BUCKET}.s3.{self.REGION}.amazonaws.com/{type}/{file_name}"