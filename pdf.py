from fpdf import FPDF, HTMLMixin
from flask import Flask,request
import boto3
from botocore.client import Config
import urllib
#import psycopg2
import random
import json
app = Flask(__name__)
@app.route("/send_sms",methods=['POST'])
def index():
   class HTML2PDF(FPDF, HTMLMixin):
       pass
   pdf = HTML2PDF()
   ACCESS_KEY_ID = 'AKIAIOUH4AFAL72UJHRQ'
   ACCESS_SECRET_KEY = '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'
   BUCKET_NAME = 'infocuit-bucket001'
   '''
   pdf.add_page()
   pdf.set_xy(0, 0)
   pdf.set_font('arial', 'B', 13.0)
   pdf.cell(ln=0, h=5.0, align='L', w=0, txt="Hello_priya", border=0)
   pdf.output('test_priya1.pdf', 'F')
   '''
   new_list = []
   print('array',new_list)
   name="Aravindh"
   hotel_name = "Hilton Hotel"
   address = "No:5, First cross street,Chennai-600 001."
   mobile_no = "9677577914"
   email = "abcd96@gmail.com"
   arrival = "2019-05-10"
   departure ="2019-05-15"
   room_type = "Standard Room"
   conf_no = "8974561234"
   pdf.add_page()
   pdf.set_font("Arial",'B', size=16)
   pdf.cell(200, 10, txt="Booking Confirmation", ln=1, align="C")
   pdf.ln(10)
   pdf.set_font('Arial','B',size=14)
   pdf.cell(10)
   pdf.cell(0, 5,"%s," %hotel_name, ln=1, align="L")
   pdf.set_font('Arial',size=12)
   pdf.cell(10)
   pdf.cell(0, 5, '%s'%address, ln=1, align="L")
   pdf.cell(10)
   pdf.cell(0, 5, '%s'%mobile_no, ln=1, align="L")
   pdf.cell(10)
   pdf.cell(0, 5, '%s'%email, ln=1, align="L")
   pdf.cell(10)
   pdf.cell(200, 10, txt="Dear %s, " %name, ln=1, align="J")
   pdf.cell(10)
   pdf.output('E:/new.pdf','F')
   print('test',type(pdf.output('pdf_converson.pdf','F')))
           
   data = open('pdf_converson.pdf','rb')
   AWS_ACCESS_KEY ='AKIAILEFWKUGECA7YHWA'
   AWS_ACCESS_SECRET_KEY = '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'
   bucket_name = 'image-upload-rekognition'
   client   = boto3.resource('s3',
                              aws_access_key_id=AWS_ACCESS_KEY,
                              aws_secret_access_key=AWS_ACCESS_SECRET_KEY,
                              config=Config(signature_version='s3v4'))
    #transfer = S3Transfer(client)
   print("its came")
    #extra_args = {'ContentType': "audio/mp3"}
   client.Bucket(bucket_name).put_object(Key='pdf_converson.pdf',Body=data)
   print ('It worked!')
   print("https://s3.amazonaws.com/image-upload-rekognition/pdf_converson.pdf")
   #return(pdf.output('pdf_converson.pdf'))
print("hihlo")
index()



