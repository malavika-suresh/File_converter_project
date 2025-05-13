import os
import uuid
import subprocess
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

# Define LibreOffice executable path (set once)
LIBREOFFICE_PATH = "C:\\Program Files\\LibreOffice\\program\\soffice.exe"

# Define upload directory
UPLOAD_DIR = 'media/uploads/'
os.makedirs(UPLOAD_DIR, exist_ok=True)

def home(request):
    return render(request, 'home.html')

def pdf_to_docx_view(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        return _convert_file(
            request=request,
            input_file=request.FILES['pdf_file'],
            convert_to='docx',
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            template='pdf_to_docx.html'
        )
    return render(request, 'pdf_to_docx.html')

def docx_to_pdf_view(request):
    if request.method == 'POST' and request.FILES.get('docx_file'):
        return _convert_file(
            request=request,
            input_file=request.FILES['docx_file'],
            convert_to='pdf',
            content_type='application/pdf',
            template='docx_to_pdf.html'
        )
    return render(request, 'docx_to_pdf.html')

def _convert_file(request, input_file, convert_to, content_type, template):
    fs = FileSystemStorage(location=UPLOAD_DIR, base_url='/media/uploads/')
    filename = fs.save(f"{uuid.uuid4()}_{input_file.name}", input_file)
    input_path = fs.path(filename)
    output_dir = os.path.dirname(input_path)

    output_extension = convert_to.lower()
    output_filename = os.path.splitext(filename)[0] + f".{output_extension}"
    output_path = os.path.join(output_dir, output_filename)

    try:
        # Run LibreOffice conversion
        subprocess.run([
            LIBREOFFICE_PATH,
            "--headless",
            "--convert-to", output_extension,
            "--outdir", output_dir,
            input_path
        ], check=True)

        if not os.path.exists(output_path):
            raise Exception("Conversion failed - output file not created")

        # Serve converted file
        with open(output_path, 'rb') as out_file:
            response = HttpResponse(out_file.read(), content_type=content_type)
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(output_path)}"'
            return response

    except Exception as e:
        # Clean up if something fails
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)
        return render(request, template, {'error': str(e)})
