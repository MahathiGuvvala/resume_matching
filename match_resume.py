from sentence_transformers import SentenceTransformer, util
from extract_text import extract_text
from process_text import load_job_description

# Load AI Model (BERT-based for embeddings)
model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(resume_path, job_desc_path):
    """Compare resume with job description using embeddings."""
    
    # Extract text from resume
    resume_text = extract_text(resume_path)
    
    # Load and clean job description
    job_text = load_job_description(job_desc_path)

    # Convert both to embeddings
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_text, convert_to_tensor=True)

    # Compute cosine similarity
    similarity_score = util.pytorch_cos_sim(resume_embedding, job_embedding).item()
    
    return round(similarity_score * 100, 2)  # Convert to percentage

# Example usage
if __name__ == "__main__":
    resume_path = "resume/sample_resume.pdf"  # Change this to your actual resume file
    job_desc_path = "job_descriptions/sample_job.txt"  

    match_score = compute_similarity(resume_path, job_desc_path)
    print(f"Resume Match Score: {match_score}%")
