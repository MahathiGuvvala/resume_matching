import re

def clean_text(text):
    """Preprocess text by removing special characters and converting to lowercase."""
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    return text

def load_job_description(file_path):
    """Load job description from a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        job_text = file.read()
    return clean_text(job_text)

# Example usage:
if __name__ == "__main__":
    job_desc_path = "job_descriptions/sample_job.txt"  # Change this to your file
    job_text = load_job_description(job_desc_path)
    print("Cleaned Job Description:\n", job_text)
