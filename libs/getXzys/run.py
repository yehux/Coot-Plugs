# -*- coding: utf-8 -*
import urllib2
import random
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#如果缺包 需要pip 下载所需的包
#输入你的星座
xzstr = "金牛座"
ua_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
user_agent = random.choice(ua_list)
xzNameList = ["金牛座","白羊座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座","摩羯座","水瓶座","双鱼座"]
xzUrlList = [
    "taurus/",
    "aries/",
    "gemini/",
    "cancer/",
    "leo/",
    "virgo/",
    "libra/",
    "scorpio/",
    "sagittarius/",
    "capricorn/",
    "aquarius/",
    "pisces/"
    ]
request = urllib2.Request("http://www.xzw.com/fortune/"+xzUrlList[xzNameList.index(xzstr)])
request.add_header('User-Agent',user_agent)
response = urllib2.urlopen(request)
html = response.read().decode('utf-8')
pattern = re.compile('<dl>(.*?)</dl>', re.S)
text = re.compile('<div\sclass="c_cont">(.*?)</div>',re.S)
textArr = text.findall(html)
content = pattern.findall(html)
liArr = content[1].split("<li")
star={
    "16":1,
    "32":2,
    "48":3,
    "64":4,
    "80":5
}
zhys = liArr[1][liArr[1].index("width:")+6:liArr[1].index("width:")+8]
aqys = liArr[2][liArr[2].index("width:")+6:liArr[2].index("width:")+8]
syxy = liArr[3][liArr[3].index("width:")+6:liArr[3].index("width:")+8]
cfys = liArr[4][liArr[4].index("width:")+6:liArr[4].index("width:")+8]
jkzs = liArr[5][liArr[5].index("%")-2:liArr[5].index("%")]
stzs = liArr[6][liArr[6].index("%")-2:liArr[6].index("%")]
xyys = liArr[7][liArr[7].index("</label>")+8:liArr[7].index("</label>")+10]
xysz = str(re.findall('\d+',liArr[8])[0])
spxz = liArr[9][liArr[9].index("</label>")+8:liArr[9].index("</label>")+11]
dp = liArr[10][liArr[10].index("</label>")+8:liArr[10].index("</li>")]
cwb = textArr[0].split("</")
zhpy = cwb[1][cwb[1].index("<span>")+6:]
aqpy = cwb[4][cwb[4].index("<span>")+6:]
sypy = cwb[7][cwb[7].index("<span>")+6:]
cfpy = cwb[10][cwb[10].index("<span>")+6:]
jkpy = cwb[13][cwb[13].index("<span>")+6:]
ad = "/n"
contentStr = "综合运势:"+str(star[zhys+""])+ad+"爱情运势:"+str(star[aqys+""])+ad+"事业学业:"+str(star[syxy+""])+ad+"财富运势:"+str(star[cfys+""])+ad+"健康指数:"+jkzs+ad+"商谈指数:"+stzs+ad+"幸运颜色:"+xyys+ad+"幸运数字:"+xysz+ad+"速配星座:"+spxz+ad+"短评:"+dp+ad+"综合评语:"+zhpy+ad+"爱情评语:"+aqpy+ad+"事业评语:"+sypy+ad+"财富评语:"+cfpy+ad+"健康评语:"+jkpy
print('0&&'.join(contentStr))