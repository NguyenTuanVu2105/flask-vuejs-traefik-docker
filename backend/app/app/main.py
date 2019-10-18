# Import installed packages
from flask import Flask, jsonify, request

# Import app code
app = Flask(__name__)

# After creating the app, so that cors can import it
from app import cors

FB_API_URL = 'https://graph.facebook.com/v4.0/me/messages'
VERIFY_TOKEN = "test12345678"
PAGE_ACCESS_TOKEN = "EAAjjuJJnoEgBAB9f87NlpokL0aZAdbrX9JYECKVbAcJZCQrZBo2cojpQCzY68h7ZAV2HzfuHOEIvrOCMhYLqjesefPaEazag6IKnPJZChs75eYZAc8MSBbhmZCk9ct3ZC6yjZCz006AMhJgv3iMFYtfXUmOm3rYpfxf9rOtwZBSp7SJuGGIlFqmUUnW7P5iMDYZB2gZD"

@app.route("/api/")
def root():
    return jsonify({"message": "Hello World"})



def get_bot_response(message):
    """This is just a dummy function, returning a variation of what
    the user said. Replace this function with one connected to chatbot."""
    return "This is a dummy response to '{}'".format(message)


def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"


# def respond(sender, message):
#     """Formulate a response to the user and
#     pass it on to a function that sends it."""
#     response = get_bot_response(message)
#     send_message(sender, response)
#
#
# def is_user_message(message):
#     """Check if the message is a message from the user"""
#     return (message.get('message') and
#             message['message'].get('text') and
#             not message['message'].get("is_echo"))


@app.route("/api/webhook")
def listen():
    """This is the main function flask uses to
    listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        return verify_webhook(request)
#
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
