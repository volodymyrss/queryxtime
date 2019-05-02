import requests
import re

xtime_url="https://heasarc.gsfc.nasa.gov/cgi-bin/Tools/xTime/xTime.pl"
pattern='<tr>(.*?)</tr>'
#sub_pattern='.*?<th scope=row><label for="(.*?)">.*?</label></th>.*?<td align=center>.*?</td>.*?<td>(.*?)</td>.*?'
sub_pattern='<th scope=row><label for="(.*?)">.*?</label></th>.*?<td align=center>.*?</td>.*?<td.*?>(.*?)</td>'
#pattern='<tr>.*?<th scope=row><label for="(.*?)">.*?</label></th>.*?<td align=center>.*?</td>.*?<td>(.*?)</td>.*?</tr>'

def queryxtime(**args):
    args=dict(args.items()+dict(
            timesys_in="u",
            timesys_out="u",
            apply_clock_offset="yes").items())

    content=requests.get(xtime_url,params=args).content

    #print("content",content)

    r=[]
    
    for tr in re.findall(pattern,content,re.S):
        print("tr",tr)
        s = dict(re.findall(sub_pattern,tr,re.S))
        print("s",s)

        r+=list(s.items())

    return dict(r)
