from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pdf-to-docx/', views.pdf_to_docx_view, name='pdf_to_docx'),
    path('docx-to-pdf/', views.docx_to_pdf_view, name='docx_to_pdf'),
]
