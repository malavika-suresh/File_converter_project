
# 📄 Django File Converter

A web-based file converter built with **Django** and powered by **LibreOffice**, enabling users to convert:

- ✅ PDF ➡️ DOCX
- ✅ DOCX ➡️ PDF

---

### 🚀 Features

- Convert files instantly via a simple web interface.
- Uses LibreOffice CLI for high-quality and fast conversion.
- Automatically downloads the converted file after processing.
- Upload validation (size/type), error handling, and progress feedback.

---

### 🧰 Tech Stack

- **Backend**: Django (Python)
- **Conversion Engine**: LibreOffice CLI
- **Frontend**: HTML5, CSS3, JavaScript
- **Storage**: Local file system (via Django's `FileSystemStorage`)

---

### 📦 Requirements

- Python 3.7+
- LibreOffice installed (must be available at `C:\Program Files\LibreOffice\program\soffice.exe` on Windows)

**Python packages**:
```bash
pip install -r requirements.txt
```

---

### 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/django-file-converter.git
   cd django-file-converter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Run the development server**
   ```bash
   python manage.py runserver
   ```

5. **Access the app**
   Open `http://127.0.0.1:8000/` in your browser.

---

### 📁 Folder Structure

```
file_converter_project/
├── converter/              # Main Django app
│   ├── templates/          # HTML templates
│   ├── static/             # CSS/JS/Images
│   └── views.py            # View logic (LibreOffice conversion)
├── media/uploads/          # Uploaded and converted files
├── file_converter_project/ # Django project settings
├── manage.py
└── requirements.txt
```

---

### ⚠️ Notes

- LibreOffice **must be installed** on your system.
- On Windows, make sure `soffice.exe` is accessible at:
  ```
  C:\Program Files\LibreOffice\program\soffice.exe
  ```
- You can change this path in `views.py` (`LIBREOFFICE_PATH` variable).

---

### 📸 Screenshots

> *(Optional: Add screenshots of the home page, upload form, download link, etc.)*

---

### 🤝 License

This project is licensed under the [MIT License](LICENSE).
