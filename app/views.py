from django.shortcuts import redirect, render
import requests,json
from validate_email import validate_email
import re
from django.contrib import messages
import urllib.request
import random
import instaloader
import pafy
from pytube import YouTube
import datetime
from PIL import ImageGrab,Image
import numpy as np
from translate import Translator
import pyqrcode
import pyshorteners
import socket as s
import random
import string
import random
import qrcode
import qrcode.image.svg
from io import BytesIO
import speedtest
st = speedtest.Speedtest()




def invoice_generator(request):
    if request.method == "POST":
        additional_details = request.POST.get('additional_details')
        company_3rd_name = request.POST.get('company_3rd_name')
        company_website = request.POST.get('company_website')
        buyer_email = request.POST.get('buyer_email')
        context = {
        'currency' : request.POST.get('currency'),
        'payment' : request.POST.get('payment'),
        'invoice_date' : request.POST.get('invoice_date'),
        'invoice_number' : request.POST.get('invoice_number'),
        'payment' : request.POST.get('payment'),
        'product_1' : request.POST.get('product_1'),
        'quantity_1' : request.POST.get('quantity_1'),
        'rate_1' : request.POST.get('rate_1'),
        'amount_1' : round(float(request.POST.get('rate_1')) *float(request.POST.get('quantity_1')),2),
        'product_2' : request.POST.get('product_2'),
        'quantity_2' : request.POST.get('quantity_2'),
        'rate_2' : request.POST.get('rate_2'),
        'product_3' : request.POST.get('product_3'),
        'quantity_3' : request.POST.get('quantity_3'),
        'rate_3' : request.POST.get('rate_3'),
        'result' : round(float(request.POST.get('rate_1')) * float(request.POST.get('quantity_1')),2),
        'company_name' : request.POST.get('company_name'),
        'company_address' : request.POST.get('company_address'),
        'company_contact' : request.POST.get('company_contact'),
        'buyer_name' : request.POST.get('buyer_name'),
        'buyer_address' : request.POST.get('buyer_address'),
        'buyer_contact' : request.POST.get('buyer_contact'),
        'additional_details' : request.POST.get('additional_details'),
        'company_3rd_name' : request.POST.get('company_3rd_name'),
        'company_email' : request.POST.get('company_email'),
        'company_website' : request.POST.get('company_website'),
        'buyer_email' : request.POST.get('buyer_email'),
        }
        if request.POST.get('rate_2') != None and request.POST.get('rate_3') == None:
            context['amount_2'] = round(float(request.POST.get('rate_2')) * float(request.POST.get('quantity_2')),2)
            context['result'] = context['amount_2'] + context['amount_1']
        if request.POST.get('rate_2') != None and request.POST.get('rate_3') != None:
            context['amount_2'] = round(float(request.POST.get('rate_2')) * float(request.POST.get('quantity_2')),2)
            context['amount_3'] = round(float(request.POST.get('rate_3')) * float(request.POST.get('quantity_3')),2)
            context['result'] = context['amount_2'] + context['amount_1'] + context['amount_3']
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(f"Invoice Number : {request.POST.get('invoice_number')}", image_factory=factory, box_size=8)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()
        if additional_details != None :
            return render(request,'invoice_genertor_invoice_2.html',context)
        elif company_3rd_name != None:
            return render(request,'invoice_genertor_invoice_3.html',context)
        elif company_website != None :
            return render(request,'invoice_genertor_invoice_4.html',context)
        elif buyer_email != None:
            return render(request,'invoice_genertor_invoice_5.html',context)                
        else:
            return render(request,'invoice_genertor_invoice_1.html',context)
    return render(request,'invoice_generator.html')



from django.conf import settings
from django.core.mail import EmailMessage
def feedback(request):
    if request.method == 'POST':
        feedback = request.POST['feedback']
        feedback_message = request.POST['feedback_message']
        email = EmailMessage(
        subject=f"feedback for confep {feedback_message}",
        body=f'rating Given {feedback}',
        from_email=settings.EMAIL_HOST_USER,
        to=[settings.EMAIL_HOST_USER],
        reply_to=[settings.EMAIL_HOST_USER],
        headers={'Content-Type': 'text/plain'},
        )
        email.send()                
        messages.success(request,'Your Feedback has been recieved')
        return redirect('/')    





def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)

def error_500(request,  exception):
        data = {}
        return render(request,'500.html', data)


def index(request):
    return render(request,'index.html')
    

def resume_generator(request):
    if request.method == "POST":
        skills_list = []
        achievements_list = []
        achievements_url_list = []
        languages_list = []
        for i in range(1,11):
            skills_list.append(request.POST.get(f'skill_{i}'))
        
        for i in range(1,11):
            achievements_list.append(request.POST.get(f'achievement_{i}'))
            achievements_url_list.append(request.POST.get(f'achievement_url_{i}'))

        for i in range(1,11):
            languages_list.append(request.POST.get(f'language_{i}'))
        
        context = {
            'name' : request.POST.get('name'),
            'email' : request.POST.get('email'),
            'contact' : request.POST.get('contact'),
            'linkedin' : request.POST.get('linkedin'),
            'school_name' : request.POST.get('school_name'),
            'score_secondary' : request.POST.get('score_secondary'),
            'secondary_institution' : request.POST.get('secondary_institution'),
            'pass_secondary' : request.POST.get('pass_secondary'),
            'school_name_senior' : request.POST.get('school_name_senior'),
            'score_secondary_senior' : request.POST.get('score_secondary_senior'),
            'senior_secondary_institution' : request.POST.get('senior_secondary_institution'),
            'pass_secondary_senior' : request.POST.get('pass_secondary_senior'),
            'course' : request.POST.get('course'),
            'cgpa' : request.POST.get('cgpa'),
            'college' : request.POST.get('college'),
            'university' : request.POST.get('university'),
            'timespan' : request.POST.get('timespan'),
            'project_name' : request.POST.get('project_name'),
            'project_url' : request.POST.get('project_url'),
            'project_details' : request.POST.get('project_details'),
            'project_name_2' : request.POST.get("project_name_2"),
            'project_url_2' : request.POST.get("project_url_2"),
            'project_details_2' : request.POST.get("project_details_2"),
            'project_name_3' : request.POST.get("project_name_3"),
            'project_url_3' : request.POST.get("project_url_3"),
            'project_details_3' : request.POST.get("project_details_3"),
            'skills' : skills_list,
            'ach' : zip(achievements_list,achievements_url_list),
            'languages' : languages_list,
            'experience_name' : request.POST.get('experience_name'),
            'experience_company' : request.POST.get('experience_company'),
            'experience_time' : request.POST.get('experience_time'),
            'experience_details' : request.POST.get('experience_details'),
            'experience_name_3' : request.POST.get('experience_name_3'),
            'experience_company_3' : request.POST.get('experience_company_3'),
            'experience_time_3' : request.POST.get('experience_time_3'),
            'experience_details_3' : request.POST.get('experience_details_3'),
            'experience_name_2' : request.POST.get('experience_name_2'),
            'experience_company_2' : request.POST.get('experience_company_2'),
            'experience_time_2' : request.POST.get('experience_time_2'),
            'experience_details_2' : request.POST.get('experience_details_2'),
            'github' : request.POST.get('github'),
        }
        return render(request,'resume_generator_resume.html', context)
    return render(request,'resume_generator.html')



def internet(request):
    if request.method == "POST":
        download = st.download()
        upload = st.upload()  
        servernames =[]  
        st.get_servers(servernames)  
        ping = st.results.ping  
        return render(request,"internet.html",{'download':download,'upload':upload,'ping':ping})    
    return render(request,"internet.html")
    


def email_validator(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            output = ''
            is_valid = validate_email(email)
            if is_valid == True :
	            output = "Valid"
            elif  is_valid == None:
                output = "Risky"
            else:
	            output = "Invalid"
            return render(request,'email_validator.html',{'output' : output,'input':email,'local':str(email.split("@")[0]), 'domain' : str(email.split("@")[1])}) 
    else:
        return render(request,'email_validator.html')


def email_extractor(request):
    if request.method == 'POST':
        text = request.POST.get('input')
        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", str(text))
        return render(request,'email_extractor.html',{'emails' : emails, 'text' : text}) 
    else:
        return render(request,'email_extractor.html')

def facebook_video_downloader(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        html = requests.get(link)
        try:
            url = re.search('hd_src:"(.+?)"',html.text)[1]
        except:
            url = re.search('sd_src:"(.+?)"',html.text)[1]
        return render(request,'facebook_video_downloader.html',{'embedlink':url,'link':link})
    return render(request,'facebook_video_downloader.html')


def instagram_profile_downloader(request):
    if request.method == 'POST':
        ig = instaloader.Instaloader()
        dp = request.POST.get('link')
        ig.download_profile(dp, profile_pic_only=True)
        messages.success(request,'Download Complete')
    return render(request,'instagram_profile_downloader.html')


def youtube_video_downloader(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        video = pafy.new(link)
        embedlink = link.replace("watch?v=", "embed/")
        context = {
            'video':video,
            'embedlink' : embedlink,
            'link':link,
        }
        return render(request,'youtube_video_downloader.html',context)
    return render(request,'youtube_video_downloader.html')


def youtube_mp3_converter(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        video = pafy.new(link)
        embedlink = link.replace("watch?v=", "embed/")
        context = {
            'video':video,
            'embedlink' : embedlink,
            'link':link,
        }
        return render(request,'youtube_mp3_converter.html',context)
    return render(request,'youtube_mp3_converter.html')


def youtube_shorts_downloader(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        embeds = link.split("?")
        videolink1 = embeds[0].replace("shorts/","watch?v=")
        video = pafy.new( videolink1)
        embedlink = videolink1.replace("watch?v=", "embed/")
        context = {
            'video':video,
            'embedlink' : embedlink,
            'link' : link,
        }
        return render(request,'youtube_shorts_downloader.html',context)
    return render(request,'youtube_shorts_downloader.html')



def qr_code_generator(request):
    context = {}
    if request.method == "POST":
        link = request.POST.get('qrcode')
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qrcode",""), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()
        context['link'] = link
        return render(request, "qr_code_generator.html", context=context)

    return render(request, "qr_code_generator.html")



def link_shortner(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        shortner = pyshorteners.Shortener()
        x = shortner.tinyurl.short(link)
        return render(request,'link_shortner.html',{'shortlink' : x,'link':link})       
    return render(request,'link_shortner.html')


def ip_address_finder(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        output = s.gethostbyname(link)
        return render(request,'ip_address_finder.html',{'output':output,'link':link})       
    return render(request,'ip_address_finder.html')


def random_password_generator(request):
    if request.method == 'POST':
        length = request.POST.get('link')
        letters = string.ascii_letters
        num = '0123456789'
        special = '-+*%&$!_@'
        symbols = letters+num+special
        len = int(length)
        password = ''.join(random.sample(symbols,len))
        return render(request,'random_password_generator.html',{'output':password,'len':len})    
    return render(request,'random_password_generator.html')


def text_translator(request):
    if request.method == 'POST':
        from_ = request.POST.get('from')
        to = request.POST.get('to')
        from_lang = request.POST.get('from_lang')
        s = Translator(from_lang=str(from_),to_lang=str(to))
        res = s.translate(from_lang)    
        return render(request,'text_translator.html',{'result' : res,'from_lang' : from_lang})
    return render(request,'text_translator.html')


def text_to_html(request):
    if request.method == 'POST':
        editor = request.POST.get('editor')
        return render(request,'text_to_html.html',{'editor':editor})
    return render(request,'text_to_html.html')    

