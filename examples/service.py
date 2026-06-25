from flask import Flask,request,jsonify

from PIL import Image
import base64
import io


app=Flask(__name__)


#这是一个示例，定义了一个image_size接口，通过http://127.0.0.1:8080/image_size访问，仅接受 POST 请求，当该接口被调用时，执行 get_image_size() 函数
@app.route('/image_size', methods=['POST']) 
def get_image_size(): 
    img_base64 =request.json.get('image')
    if img_base64:
        img_bytes=base64.b64decode(img_base64)
        img=Image.open(io.BytesIO(img_bytes))
        w,h=img.size
        return jsonify({'width':w,'height':h})

if __name__ == '__main__':
    app.run(debug=True,port=8080)    

