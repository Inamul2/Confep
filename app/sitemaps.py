from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
class StaticViewSitemap(Sitemap):
    changefreq = "hourly" 
    priority = 0.9
    
    def items(self):
        return ['email_validator','email_extractor','facebook_video_downloader','youtube_video_downloader','youtube_mp3_converter','qr_code_generator','link_shortner','ip_address_finder','random_password_generator','text_translator','newsletter']
    def location(self, item):
        return reverse(item)