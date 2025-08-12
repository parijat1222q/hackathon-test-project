from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader, select_autoescape
import tempfile
import os

def generate_pdf_report(data):
    # Load Jinja2 template
    env = Environment(
        loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('report_template.html')
    html_content = template.render(
        lab_results=data.get('lab_results', []),
        medicines=data.get('medicines', []),
        crosscheck=data.get('crosscheck', [])
    )
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_pdf:
        HTML(string=html_content).write_pdf(tmp_pdf.name)
        tmp_pdf.seek(0)
        pdf_data = tmp_pdf.read()
    return pdf_data
