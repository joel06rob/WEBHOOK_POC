from flask import Flask, request, abort, jsonify

app = Flask(__name__)

conversation_STATE = {}

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.is_json:
        data = request.get_json()
        

        #Parse JSON
        name = data.get("name")
        phoneNumber = data.get("phone")
        message = data.get("message").strip().lower()

        #Display Recent Message
        print(f"{phoneNumber} - {name}: \nMessage: {message}")

        step = conversation_STATE.get(name, 0)
        reply = ""

        if step == 0:
            reply = f"Hi {name}, to understand your needs, would you like to learn more about this?"
            conversation_STATE[name] = 1
        elif step == 1:
            reply = "This is a webhook script to test your skills!"
        
        print("SENDING REPLY...")

        return jsonify({"status":"success", 
                        "message": reply,
                        "step": step
                        }), 200
    else:
        return jsonify({"status":"error", "message":"Request must be JSON"}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)