import os , urllib.parse , urllib.request , render_template
from app.youtube import youtube_bp

GEMINI_API_KEY = "GEMINI_API_KEY";

def home():
  return render_template (" index.html ")

def create_app():

  app = Flask(_name_)
  app.register_blueprint(youtube_bp, url_prefix="/youtube")

@app.route("/hrml")
def html():
  return render_template("index.html")

return app;
