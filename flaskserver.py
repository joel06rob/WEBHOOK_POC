from flask import Flask, request, abort, jsonify


app = Flask(__name__)

#Managing Conversation State
conversation_STATE = {}

#Intented responses
intent_keywords = { "about": ["about", "about x", "what is X", "info", "learn"],
                   "plans": ["plans", "pricing", "subscription", "price"],
                   "support": ["help","support"],
                   "email": ["email", "contact"]
                   }

intent_responses = {"about": "X is a company that helps businesses grow through X.",
                    "plans": "Our pricing plans start at X GBP.",
                    "support": "You can contact our support here: +44 555452353",
                    "email": "We will send an auto email!"
                    }






@app.route('/webhook', methods=['POST'])
def webhook():
    if request.is_json:
        data = request.get_json()
        

        #Parse JSON
        name = data.get("name")
        phoneNumber = data.get("phone")
        message = data.get("message").lower()

        #Display Recent Message
        print(f"{phoneNumber} - {name}: \nMessage: {message}")

        step = conversation_STATE.get(name, 0)
        reply = ""

        #Initialize first response
        if step == 0:
            reply = f"Hi {name}, I am a virtual assistant to help you get started with X business. Feel free to ask me any questions."
            conversation_STATE[name] = 1
        
        else:
            matched_kw = ""
            for intent, keywords in intent_keywords.items():
                matched = False
            
                for kw in keywords:
                    if kw in message:
                        matched = True
                        matched_kw = kw
                        break
                
                #If keyword intents is matched send one of the responses - else send Couldn't Understand
                if matched:

                    if matched_kw == "email":
                        print("SENDING EMAIL...")
                        reply = "Email Sent!"
                    else:
                        reply = intent_responses[intent]
                    break
                
                else:
                    reply = "Sorry, I didn't quite catch that!"
        
        return jsonify({"status":"success", 
                        "message": reply,
                        "step": step
                        }), 200
    else:
        return jsonify({"status":"error", "message":"Request must be JSON"}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)