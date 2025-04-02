import pdfminer.high_level
import docx2txt
import os

def extract_text(file_path):
    """Extracts text from PDF or DOCX resumes."""
    _, ext = os.path.splitext(file_path)

    if ext == ".pdf":
        return pdfminer.high_level.extract_text(file_path)
    elif ext == ".docx":
        return docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX.")

# Example usage:
if __name__ == "__main__":
    resume_path = "resume/sample_resume.pdf"  # Change this to your resume path
    text = extract_text(resume_path)
    print(text)
