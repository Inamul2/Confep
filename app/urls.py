from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('text-to-html', views.text_to_html, name='text_to_html'),
    path('email-validator', views.email_validator, name='email_validator'),
    path('email-extractor', views.email_extractor, name='email_extractor'),
    path('facebook-video-downloader', views.facebook_video_downloader, name='facebook_video_downloader'),
    path('youtube-video-downloader', views.youtube_video_downloader, name='youtube_video_downloader'),
    path('youtube-mp3-converter', views.youtube_mp3_converter, name='youtube_mp3_converter'),
    path('youtube-shorts-downloader', views.youtube_shorts_downloader, name='youtube_shorts_downloader'),
    #path('instagram-profile-downloader', views.instagram_profile_downloader, name='instagram_profile_downloader'),
    path('url-shortener', views.link_shortner, name='link_shortner'),
    path('qr-code-generator', views.qr_code_generator, name='qr_code_generator'),
    path('ip-address-finder', views.ip_address_finder, name='ip_address_finder'),
    path('random-password-generator', views.random_password_generator, name='random_password_generator'),
    path('text-translator', views.text_translator, name='text_translator'),
    path('internet-speed-test', views.internet, name='internet'),
    path('resume-generator', views.resume_generator, name='resume_generator'),
    path('invoice-generator', views.invoice_generator, name='invoice_generator'),
    path('feedback', views.feedback, name='feedback'),
]+ static(settings. STATIC_URL, document_root=settings. STATIC_ROOT)
