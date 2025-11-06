from flask import Blueprint, render_template, request

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        resume = request.files['resume']
        job_description = request.form['job_description']

        # TODO: Process resume and job description
        # 1. Extract text from resume (pdfplumber or python-docx)
        # 2. Extract skills from resume and job description (spaCy)
        # 3. Calculate ATS score (sentence-transformers)
        # 4. Perform skill gap analysis

        return "Analysis in progress..."

    return "Invalid request"
