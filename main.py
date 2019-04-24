# -- imports --
import importer.py


summaries = []
for url in new_d:
    print("Summarizing URL : ",url)
    summary = summarize_url(url,'textrank')
    summaries.append(summary)
    
    
summ_comb = []
for summ in summaries:
    summ_comb.append(list(itertools.chain.from_iterable(summ)))

i = 0
for summ in summ_comb:
    i += 1
    f = open("textrank/RSummary_"+str(i)+".txt","w",encoding="utf-8")
    f.writelines([l+"\n" for l in summ])
    f.close()


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
    
i = 0
for url in new_d:
    i += 1
    parse_url_abstracts(url,i)
    
    
summary=[]

for i in section:
    sen=[]
    
    for j in i.getElementsByTagName('S'):
        sen.append(j.childNodes[0].nodeValue)
    document=tokenize(str(sen))
    sentences=term_doc_matrix(document)
    summary.append(sentences)
print(summary)


def write_summary(summary,name):
    with open(name, 'w',encoding='utf-8') as f:
        for item in summary:
            f.write("%s\n" % summary)