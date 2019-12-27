import os
from flask import Flask, render_template, request, make_response, jsonify
from settings import BASE_DIR


app = Flask(__name__, static_folder=os.path.join(BASE_DIR, 'static'), static_url_path='/public')


@app.route("/upload-video", methods=["GET", "POST"])
def upload_video():
    if request.method == "POST":
        file = request.files["file"]
        print("File uploaded")
        print(file)
        target_path = os.path.join(app.static_folder, file.filename)
        file.save(target_path)
        res = make_response(jsonify({"message": "File uploaded"}), 200)
        return res
    return render_template("public/upload_video.html")
