from flask import Flask, request, abort, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.is_json:
        data = request.get_json()
        
        print("RECEIVED JSON DATA")
        
        #Parse JSON
        name = data.get("name")
        phoneNumber = data.get("phone")
        message = data.get("message")

        print(f"{phoneNumber} - {name}: \nMessage: {message}")


        return jsonify({"status":"success", "message":"JSON received"}), 200
    else:
        return jsonify({"status":"error", "message":"Request must be JSON"}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)