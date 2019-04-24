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

def get_summary_per_section_textrank(cur_sents,each_summ_num,num_sent_sec):
    summ_ratio = each_summ_num/num_sent_sec
    decoded = summarize(str(cur_sents),ratio=summ_ratio,split=True)
    return decoded

LANGUAGE = 'english'

def get_summary_per_section(cur_sents,each_summ_num,num_sent_sec,summarizer_name="textrank"):
    if summarizer_name == "textrank":
        summary = get_summary_per_section_textrank(cur_sents,each_summ_num,num_sent_sec)
    elif summarizer_name == "lsa":
        summary = get_summary_per_section_lsa(cur_sents,each_summ_num)
    elif summarizer_name == "luhn":
        summary = get_summary_per_section_luhn(cur_sents,each_summ_num)
    elif summarizer_name == "enmund":
        summary = get_summary_per_section_edmund(cur_sents,each_summ_num)
    else:
        summary = get_summary_per_section_textrank(cur_sents,each_summ_num,num_sent_sec)
    return summary

def tokenize(document):
    doc_tokenizer = PunktSentenceTokenizer()
    sentences_list = doc_tokenizer.tokenize(document)
    return sentences_list
def term_doc_matrix(sentences_list):
    cv = CountVectorizer()
    cv_matrix = cv.fit_transform(sentences_list)
    
    normal_matrix = TfidfTransformer().fit_transform(cv_matrix)
  
    res_graph = normal_matrix * normal_matrix.T
    nx_graph = nx.from_scipy_sparse_matrix(res_graph)
    nx.draw_circular(nx_graph)
    #plt.show()
    
    ranks = nx.pagerank(nx_graph)

    for i in ranks:
        #print(i, ranks[i])
        sentence_array = sorted(((ranks[i], s) for i, s in enumerate(sentences_list)), reverse=True)
        sentence_array = np.asarray(sentence_array)
    
    rank_max = float(sentence_array[0][0])
    rank_min = float(sentence_array[len(sentence_array) - 1][0])
     
    extracted_sentences=[]  
    extracted_sentences.append(str(sentence_array[0][1]))
    if sentence_array.shape[0]>1:
        extracted_sentences.append(str(sentence_array[1][1]))
    
                
    model = extracted_sentences
    return model

