from flask import jsonify,request
from flask_cors import cross_origin
from app.services.upload_service import UploadService
from app import app

# initiate services
upload_service = UploadService()

@app.route('/uploads',methods=['POST'])
@cross_origin()
def uploads():
    data = request.get_json()
    b64_string = data['url'].split('data:image/jpeg;base64,')[-1]

    return upload_service.convert_base64(b64_string,data['name'])