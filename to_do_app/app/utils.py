from io import BytesIO #A stream implementation using an in-memory bytes buffer
                       # It inherits BufferIOBase

from django.http import HttpResponse
from django.template.loader import get_template

#pisa is a html2pdf converter using the ReportLab Toolkit,
#the HTML5lib and pyPdf.

from xhtml2pdf import pisa  
#difine render_to_pdf() function

def render_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     username =context_dict['username']
     html  = template.render(context_dict)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     with open(f'media/pdf_files/task_history_pdf_{username}.pdf','w+b') as f:
        # result_file = open("test.pdf", "w+b")
        #This part will create the pdf.
        pisa_status = pisa.CreatePDF(
                html,                   # the HTML to convert
                dest=f            # file handle to recieve result
        )

     if not pdf.err:
         data =result.getvalue()
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None