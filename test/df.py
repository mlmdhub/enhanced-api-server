import requests

headers = {
 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
 'accept-language':'en-US,en;q=0.5',
 'accept-encoding':'gzip, deflate, br, zstd',
 # 'referer':'https://tieba.baidu.com/f/search/res?ie=utf-8&kw=%E6%8A%97%E5%8E%8B%E8%83%8C%E9%94%85&qw=lol',
 'upgrade-insecure-requests':'1',
 'sec-fetch-dest':'document',
 'sec-fetch-mode':'navigate',
 'sec-fetch-site':'same-origin',
 'sec-fetch-user':'?1',
 'priority':'u=0, i',
 'te':'trailers',
 # 'cookie':'XFI=d32172e0-b6e7-11ef-9dd8-1d6eaefba3a9; XFCS=67DB9062746366D8DBA426B76B7BC7471850500B08C5E36273615004A38BB5D2; XFT=GqZ8VzicdzhQPcC84IH/fqcxNmUVDJVAES0kkSpBguU=; BAIDUID=E90926E539690FA70BEE6A0C785A3CCD:FG=1; BIDUPSID=E90926E539690FA7CC83F5D8B07BF616; PSTM=1732277872; H_PS_PSSID=61027_61096_61210_61209_61215_61196_61279_60853_61327; H_WISE_SIDS=61027_61096_61210_61209_61215_61240_61196_61279_60853; ZFY=eGQ7H9KSISNKDeeqDoJA4ZRFzFMQWzTJWNsg4WaZK1Y:C; BAIDU_WISE_UID=wapp_1733828626318_429; USER_JUMP=-1; XFI=ac9eb430-b6e6-11ef-8e5b-7dd3fd598a57; XFCS=66FFA6FABCB2EED2D3D0E615C0D914635DA90B2A06C3B19D9AA69D058FEC979D; BAIDU_SSP_lcr=https://www.google.com/; Hm_lvt_292b2e1608b0823c1cb6beef7243ef34=1733828629; Hm_lpvt_292b2e1608b0823c1cb6beef7243ef34=1733829226; HMACCOUNT=17F5A1F0F6ACCC45; RT="z=1&dm=baidu.com&si=26d39dd5-acbd-479f-a12a-5ecc1893d0d0&ss=m4icslyz&sl=8&tt=bq9&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&r=47he30d4&ul=fpc0"; ab_sr=1.0.1_OWQzMzllMjc1NGY3OWI0OTkyZDk1ZmQyYTI2MmY5OGY3NjkwZDkyOWI2MDBmYjkxMzQwNmYzMmFkMGFhY2ZhZmE4M2Y1NzU0NGFhZWVhYTEzOGI2OTkzMmViOGU4YjkxNWM4NTE4Y2ZjYWY4Y2JhZTkxMTY3MDc1MjIzNDAzMzIzOTE1NzgyYTdkYjYxYWU3MjI2OTViNDkwMTEzNDc1Zg==; st_data=ad69d7b002dd5e249e211ff68b0f16917ca4b685bcbe15498420d440d96585c7dd6fa737cbe82691a0030f1d55f9dfaba062efa4b7b73d499327a924f02880f13189ee55481678c18152a6ec6c8754b500ca78e6983f4174e548b67f5608409727b4223607962aa6799fe1461910a094b433d6b9730017d69a01c89a303f6d4051d5652dd0d399daf99b8f0330a5e349; st_key_id=17; st_sign=0c19b61a; arialoadData=false; ppfuid=FOCoIC3q5fKa8fgJnwzbE67EJ49BGJeplOzf+4l4EOvDuu2RXBRv6R3A1AZMa49I27C0gDDLrJyxcIIeAeEhD3iAJZpK/vamtTTGqdKc8757oTsu/iwISZsnY/Sefe8MLY/K594STGocU9WpVBYSwkB3OalQbytO8yXCW4QN7Wgdxc0ZVK+5mkQUZbNDVX6nqti2NRQ0+jWaR/sebWvZ/5zTvct9wkZI5xq6xRiFKW2BJCmseIVKIDkHC6V7QiHkDPXYNLl/lcxE/5pk0XuA7bLVhi8nTC7D4oNeeTJaANymOxIZj5RQ+RLxHJl103SQ1iSiEnFHDsHPZfuEU1yfe85FjnYxYstXg/9EfB3EVmI+8zAmho9UyCVw0CwXswtNULXY3st+/5MpeCQPRaeM48nmXcDfihcK+Aoj3HcOTycjq1z170EyPPj5/Em4yJTI6YJrMGknHOgzVm9+IxY9F97XURNLrh7qomGuQQpRUtldEwqKyouAqG4EeNfcVml/CCiyYmjTSzkoVnWXZUDtg111cXIp8yh6lL1k2MeOY7IlFZWO/AB0BqJegiS0EPEO/ezEoZWs73UsD14CT+c9LjCafS/t8f2NhhoVubIreeZMKn53yMtHO8urhqsDgupsCddwFGoqyw1oXuUsB/n/ZMfuK4zWnUGEV2OtnLOMGur7txTYZ8dLxAh+/0Q+4zgSo5LDxX+mzjsmtpDpSGci1Oh8FVR7qC76Hz/ntGT6rZSeXoVSfMS/2gnZtJiLP/CQbAQImVakbpg6vs1d3IqznWpYI33Q5jqb6Ok7EFDjAM4vhDf6Kzef1PPb7Zbc6GieEWwHz92X9eIFRRl867qv+fQDGd33UCt5p//MBZ2u0hFZfeWmlEOHwcs42+iDuREqlaV9HFODR8BMvwaq9ZDj9b99FPxz04JzcsgS9oAn5nF1wGfBiuFo5zR2FdmVQfYI5Tv2IOghUDulefRvlX9eT7gQwEiclvXWS2pMTilyx6wORXYWMC8Ewe1rUuQprEZZNDywMI17CupLBOAx9qwTTBhEMNzi6OXbElHkA3erw56I0vmkH9G20tmAiqCABGBI1qeHlbtIIUXAPQK2AKm25kN9e++uG7KATaiQSHPJR405LDjC+5v0mQclI0YcJp8DvGLdRUpGcbUX7V27dvoxZKav+ja1hkgJRbYwJeWSxXr5EoNlrqqJb8Op38LjSNcK; XFT=itcTEs0/Ae4d0lUIw8tUWTFxqsAiBUxqdcPnIH8mGBQ=; BA_HECTOR=212l002k0kala000ag2h012h0k37so1jlg8jb1u; video_bubble0=1; wise_device=0'
}
payload=None

response0 = requests.request("GET", "https://tieba.baidu.com/p/9318171108?pid=151355055068&cid=0", headers=headers, data=payload)

with open('2.html','w',encoding='utf-8') as f:
    f.write(response0.text)