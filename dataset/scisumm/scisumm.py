# -- scisumm --
from xml.dom import minidom
import urllib
import requests

d=['https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/C02-1050.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/C04-1091.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/E03-1007.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/E06-1004.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/H01-1062.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/J03-1005.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/J04-2003.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/J04-4002.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/C02-1050.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/C04-1091.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/E03-1007.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/E06-1004.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/H01-1062.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/J03-1005.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/J04-2003.xml',
'https://github.com/WING-NUS/scisumm-corpus/blob/master/data/Training-Set-2018/C00-2123/Citance_XML/J04-4002.xml']

new_d = []
for doc in d:
	new_d.append(doc.replace("github.com/WING-NUS/scisumm-corpus/blob/master","raw.githubusercontent.com/WING-NUS/scisumm-corpus/master"))

def parse_url_sentences(url):
    dom = minidom.parse(urllib.request.urlopen(url))
    sentences = []
    list_sent = []
    num_sents = []
    for section in dom.getElementsByTagName('SECTION'):
        sec_sent_list = []
        sec_sent = ""
        num_sent_sec = 0
        for sent in section.getElementsByTagName('S'):
            sec_sent += sent.childNodes[0].nodeValue + "\n"
            sec_sent_list.append(sent.childNodes[0].nodeValue)
            num_sent_sec += 1
        if len(sec_sent_list) > 5:
            list_sent.append(sec_sent_list)
            sentences.append(sec_sent)
            num_sents.append(num_sent_sec)
    return sentences,list_sent,num_sents

def parse_url_abstracts(url,i):
    dom = minidom.parse(urllib.request.urlopen(url))
    sentences = []
    list_sent = []
    num_sents = []
    abstract = dom.getElementsByTagName('SECTION')
    f = open('abstract/ABSTRACT'+str(i)+".txt","w",encoding="UTF-8")
    for sent in abstract[0].getElementsByTagName('S'):
        f.write(sent.childNodes[0].nodeValue+"\n")
    f.close()
	
def get_urls():
	return new_d
	