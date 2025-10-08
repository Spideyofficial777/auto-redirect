from flask import Flask, request, redirect
import datetime

app = Flask(__name__)

# Target URLs
DESKTOP_URL = "https://psychiatric-ange-spideyofficial777-f4e984ce.koyeb.app"
MOBILE_URL = "https://psychiatric-ange-spideyofficial777-f4e984ce.koyeb.app"

# Optional secret key for protected redirect
SECRET_KEY = "q9vH2KxT8WzP4fLsYj7bUeX0pRkD1nQa"

# Logging function
def log_request():
    with open("redirect_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - IP: {request.remote_addr} - UA: {request.headers.get('User-Agent')}\n")

@app.before_request
def before_request():
    log_request()  # log every user access

@app.route("/")
def home():
    user_agent = request.headers.get('User-Agent').lower()
    
    # Device-based redirect
    target_url = MOBILE_URL if "mobile" in user_agent else DESKTOP_URL
    
    # Forward query parameters if any
    if request.query_string:
        target_url += "?" + request.query_string.decode()
    
    return redirect(target_url, code=302)

@app.route("/protected")
def protected():
    key = request.args.get("key")
    if key != SECRET_KEY:
        return "Unauthorized", 403
    return redirect(DESKTOP_URL, code=302)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
  
