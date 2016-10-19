import requests
import re

xtime_url="https://heasarc.gsfc.nasa.gov/cgi-bin/Tools/xTime/xTime.pl"
pattern="""<tr>.*?<th scope=row><label for="(.*?)">.*?</label></th>.*?<td align=center>.*?</td>.*?<td>(.*?)</td>.*?</tr>"""
#pattern="""<tr>.*?<th scope=row><label for="(.*?)">(.*?)</label></th>.*?<td align=center>.*?</td>.*?<td>(.*?)</td>.*?</tr>"""

def queryxtime(**args):
    args=dict(args.items()+dict(
            timesys_in="u",
            timesys_out="u",
            apply_clock_offset="yes").items())

    content=requests.get(xtime_url,params=args).content

    return dict(re.findall(pattern,content,re.S))
