import pdfkit as pdf_gen
from flask import render_template, make_response
import base64 as make_img
from os import getenv as env
from datetime import datetime 

class obj_report():
    
    def make_img_pdf(self, img_url):
        with open(img_url, 'rb') as image_file:
            return make_img.b64encode(image_file.read()).decode()

    def proyection_pdf(self, proyection, total):
        date = datetime.now()
        template = render_template(
                'index.html',
                logo=self.make_img_pdf(env("logo")),
                bg_pdf=self.make_img_pdf(env("bg")),
                data = proyection,
                total = total, 
                date = date
                )
        css = ['templates/index.css', 'templates/main.css']
        config = pdf_gen.configuration(wkhtmltopdf=env("topdf"))
        pdf = pdf_gen.from_string(template,False,css=css,configuration=config)
        response = make_response(pdf)
        response.headers['content-type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=proyection.pdf'  
        return response



