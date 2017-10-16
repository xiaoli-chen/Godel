from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests
# urllib.request
import re
import json


# 找到单个job的link
#url = "http://ssl.gongyi.qq.com/m/201799/realtime.html?et=rtfx&gt=rtfx&ADTAG=rtfx"
#url = "http://ssl.gongyi.qq.com/m/201799/realtime.html?tp=2&o=1"
# 初始页
#page = urllib.request.urlopen(url)
#soup = BeautifulSoup(page, 'lxml')
#all_matches = soup.findAll(attrs={'rel':['nofollow']})
#print(len(all_matches))


#api_url = 'http://ssl.gongyi.qq.com/cgi-bin/1799_gongyi_search_fund.fcgi?limit=100'
#page = requests.get(api_url)

url_page1='http://ssl.gongyi.qq.com/cgi-bin/1799_rank_ngo?type=ngobym&pg=1&md=9&jsoncallback=_martch99_sear_fn_'

url_page2='http://ssl.gongyi.qq.com/cgi-bin/1799_rank_ngo?type=ngobym&pg=2&md=9&jsoncallback=_martch99_sear_fn_'

url_page3='http://ssl.gongyi.qq.com/cgi-bin/1799_rank_ngo?type=ngobym&pg=3&md=9&jsoncallback=_martch99_sear_fn_'

url_page4='http://ssl.gongyi.qq.com/cgi-bin/1799_rank_ngo?type=ngobym&pg=4&md=9&jsoncallback=_martch99_sear_fn_'


page1 = requests.get(url_page1).text
#page1_text = urllib.parse.unquote(page1)
#page1_text
text_20 = re.search(r'\[(.*)\]',page1)

print(text_20.group())


