from flask import Flask, request
import hashlib

app = Flask(__name__)

@app.route('/wx',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        try:
            print(request.args)
            signature = request.args.get('signature')
            timestamp = request.args.get('timestamp')
            nonce = request.args.get('nonce')
            echostr = request.args.get('echostr')
            token = '12345678'

            list1 = [token, timestamp, nonce]
            list1.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print ("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ''

        except Exception:
            return 'Argument'

