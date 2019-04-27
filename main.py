from textrank import get_summary_per_section_textrank
from lsa import get_summary_per_section_lsa
from luhn import get_summary_per_section_luhn
from edmund import get_summary_per_section_edmund
from scisumm import parse_url_sentences
from scisumm import get_urls
from extractive_summarizer import *
	

def get_all_extractive_summaries(summname="textrank"):
	summaries = []
	for url in get_urls():
		print("Summarizing URL : ",url)
		summary = summarize_url(url,summname)
		summaries.append(summary)
	return summaries
    
def extractive_summarizer():
	for summname in ['textrank','lsa','luhn','edmund']:
		summaries = get_all_extractive_summaries(summname)
		summ_comb = []
		for summ in summaries:
			summ_comb.append(list(itertools.chain.from_iterable(summ)))

		i = 0
		for summ in summ_comb:
			i += 1
			f = open(summname+"\RSummary_"+str(i)+".txt","w",encoding="utf-8")
			f.writelines([l+"\n" for l in summ])
			f.close()
    
	i = 0
	for url in get_urls():
		i += 1
		parse_url_abstracts(url,i)


extractive_summarizer()