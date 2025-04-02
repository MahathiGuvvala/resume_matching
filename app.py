from flask import Flask, render_template, request
import os
from match_resume import compute_similarity

app = Flask(__name__)

UPLOAD_FOLDER = "resumes"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure the "resumes" folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    match_score = None
    
    if request.method == "POST":
        if "resume" not in request.files:
            return "No file uploaded", 400

        file = request.files["resume"]

        if file.filename == "":
            return "No selected file", 400

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        # Compute resume match score
        job_desc_path = "job_descriptions/sample_job.txt"
        match_score = compute_similarity(file_path, job_desc_path)

    return render_template("index.html", match_score=match_score)

if __name__ == "__main__":
    app.run(debug=True)
