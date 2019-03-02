from fpdf import FPDF, HTMLMixin
from flask import Flask,request
import boto3
from botocore.client import Config
import urllib
import psycopg2
import random
import json
app = Flask(__name__)
@app.route("/send_pdf",methods=['GET'])

def index():

   class HTML2PDF(FPDF, HTMLMixin):
       pass


   pdf = HTML2PDF()
   #ACCESS_KEY_ID = 'AKIAIOUH4AFAL72UJHRQ'
   #ACCESS_SECRET_KEY = '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'
   #BUCKET_NAME = 'infocuit-bucket001'
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
   hotel_name = "QualityInn"
   address = "No:5, First cross street,Chennai-600 001."
   mobile_no = "9677577914"
   email = "abcd96@gmail.com"
   room_type = "STANDARD ROOM"
   conf_no = "8974561234"
   arrival_Date = "MAR 1"
   depature_Date = "MAR 5"
   pickupdrop = "YES"
   message = "Hihlo"
   child = "2"
   adult = "2"
   no_of_nights = '2'
   phone= '9894261776'

   
   pdf.add_page()
   pdf.set_font("Arial",'B', size=18)
   pdf.cell(200, 10, txt="Booking Confirmation", ln=1, align="C")
   pdf.ln(10)
   pdf.set_font('Arial','B',size=16)
   pdf.cell(10)
   pdf.cell(0, 5,"" , ln=1, align="R")

   
   
   pdf.cell(0, 5, '', ln=1, align="R")
   
   pdf.cell(0, 5, '', ln=1, align="R")
  
   pdf.cell(0, 5, '', ln=1, align="R")
   
   pdf.set_font('Arial','B',size=14)
   pdf.cell(200, 6, txt="Dear %s, " %name, ln=1, align="J")
   pdf.cell(10)
   pdf.set_font('Arial',size=12)
   pdf.cell(0, 6, txt="        We are delighted that you have selected our QualityInn On behalf of the entire team at the" , ln=1, align="L")
   pdf.cell(0, 6, txt="QualityInn, extend you a very welcome and trust stay with us will be both enjoyable and comfortable" , ln=1, align="L")
   pdf.cell(0, 6, txt="QualityInn offers a selection of business services and facilities.which are detailed in the booklet, " , ln=1, align="L")
   pdf.cell(0, 6, txt="placed on the writing table in your room.Should you require any assistance or have any specific" , ln=1, align="L")
   pdf.cell(0, 6, txt="requirements, please do not hesitate to contact me extension(999).", ln=1, align="L")
   pdf.cell(0,2, txt=" ", ln=1, align="J")
   
   pdf.cell(0, 5, txt="Thank you for choosing to stay at QualityInn. We are pleased to confirm your accommodation", ln=1, align="L")
   pdf.cell(0, 6, txt="as follows :", ln=1, align="L")
   pdf.set_font('Arial','B',size=12)
   pdf.cell(10)
   pdf.cell(0, 5, txt="Room Type : %s"%room_type, ln=1, align="L")
   pdf.cell(10)
   pdf.cell(0, 5, 'Arrival Date : %s'%arrival_Date, ln=1, align="L")
   pdf.cell(10)
   pdf.cell(0, 5, 'Depature Date : %s'%depature_Date, ln=1, align="L")
   pdf.cell(10)
   pdf.cell(0, 5, 'No of Nights : %s'%no_of_nights, ln=1, align="L")
   pdf.cell(10)
   pdf.cell(0, 5, 'Pickupdrop : %s'%pickupdrop, ln=1, align="L")
   pdf.cell(10)
   pdf.cell(0, 5, 'Adult : %s'%adult, ln=1, align="L")
   pdf.cell(10)
   pdf.cell(0, 5, 'Child : %s'%child, ln=1, align="L")
   pdf.cell(10)
   pdf.cell(100,5, txt="Mobile Number : %s"%phone, ln=1, align="J")
   pdf.cell(10)
   pdf.cell(100,5, txt="Message : %s"%conf_no, ln=1, align="J")
   pdf.image('![room](https://user-images.githubusercontent.com/29862662/53677945-1426bc80-3cde-11e9-8efc-f5de53e0054e.jpg)', 100, 100, 70)
   pdf.image('Qualityinn.png', 10, 8, 33)
   pdf.cell(100,5, txt=" ", ln=1, align="J")
   pdf.cell(100,5, txt=" ", ln=1, align="J")
   pdf.cell(100,5, txt=" ", ln=1, align="J")
   
   pdf.set_font('Arial',size=11)
   pdf.cell(0, 10, txt="DEPOSIT:", ln=1, align="L")
   pdf.cell(10)
   pdf.cell(0, 5, txt="First night deposit will be taken prior to arrival via the Credit Card. Special Event Periods, first ", ln=1, align="L")
   pdf.cell(0, 5, txt="night deposit taken and full payment of accommodation costs is required at 28 days before arrival.", ln=1, align="L")
   pdf.set_font('Arial',size=11)
   pdf.cell(0, 10, txt="CANCELLATION:", ln=1, align="L")
   pdf.cell(10)
   pdf.cell(0, 5, txt="will be accepted up to 48hrs prior to arrival date. Should you cancel within 48hrs of arrival, you will", ln=1, align="L")
   pdf.cell(0, 5, txt="forfeit the total cost of accommodation. No Cancellation accepted during a Special Event Period 7 days before arrival.", ln=1, align="L")
   pdf.cell(0, 10, txt="CAR PARKING:", ln=1, align="L")
   pdf.cell(10)
   pdf.cell(0, 5, txt="Parking is available at 10 USD per night. This is subject to availability and will need to be confirmed", ln=1, align="L")
   pdf.cell(0, 5, txt="directly with the hotel. We recommend reserving a spot before arrival, if required contact reservations.", ln=1, align="L")
   pdf.set_font('Arial',size=10)
   pdf.cell(0, 5, txt="We look forward to welcome you to QualityInn in the near future. Should you need any further", ln=1, align="L")
   pdf.cell(0, 5, txt="information regarding your reservation please call (123) 1234 567890.", ln=1, align="L") 
   pdf.cell(0, 5, txt="Thank you", ln=1, align="L")
   pdf.cell(0, 5, txt="Warm Regards,", ln=1, align="L")
   pdf.cell(0, 5, txt="Reservations Team", ln=1, align="L")
 
  
   
   pdf.cell(0, 5,"%s," %hotel_name, ln=1, align="L")

   pdf.set_font('Arial',size=12)
   
   pdf.cell(0, 5, '%s'%address, ln=1, align="L")
  
   pdf.cell(0, 5, '%s'%mobile_no, ln=1, align="L")
  
   pdf.cell(0, 5, '%s'%email, ln=1, align="L")
   
   pdf.cell(0, 5, txt="https://www.facebook.com/qualityinnhotel", ln=1, 
align="L")
   pdf.set_font('Arial',size=9)
   pdf.cell(0, 10, txt="PS: List your hotel at Lodginglists.com to increase more direct bookings. No Commission or Fees.", ln=1, 
align="L")
   
   
   
   pdf.output('amaon_pdf_conversion_file.pdf','F')
   print('test',type(pdf.output('amaon_pdf_conversion_file.pdf','F')))
   new_list.append(pdf.output('amaon_pdf_conversion_file.pdf','F'))
   data = open('amaon_pdf_conversion_file.pdf','rb')
   AWS_ACCESS_KEY ='AKIAILEFWKUGECA7YHWA'
   AWS_ACCESS_SECRET_KEY = '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'
   bucket_name = 'image-upload-rekognition'
    #file = open('Amazonpollyvoice.mp3', 'r+')

    
   client   = boto3.resource('s3',
                              aws_access_key_id=AWS_ACCESS_KEY,
                              aws_secret_access_key=AWS_ACCESS_SECRET_KEY,
                              config=Config(signature_version='s3v4'))
    #transfer = S3Transfer(client)
   print("its came")
    #extra_args = {'ContentType': "audio/mp3"}
   client.Bucket(bucket_name).put_object(Key='amaon_pdf_conversion_file.pdf',Body=data)
   print ('It worked!')
   

print("hihlo")
index()

