# -- scisum --
def scisum(){
for link in new_d:
    counter=0
    #print(str(link))
    url = 'https://raw.githubusercontent.com/WING-NUS/scisumm-corpus/master/data/Test-Set-2016/C00-2123/Citance_XML/C04-1091.xml' # define XML location
    dom = minidom.parse(urllib.request.urlopen(url)) # parse the data
    summary=[]

    for i in section:
        sen=[]

        for j in i.getElementsByTagName('S'):
            sen.append(j.childNodes[0].nodeValue)
        document=tokenize(str(sen))
        sentences=term_doc_matrix(document)
        summary.append(sentences)
    #print(summary)
    counter=counter+1
    
    sum_name="Summary_"+str(counter)+".txt"
    write_summary(summary,sum_name)
}
