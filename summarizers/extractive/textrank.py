from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

def get_summary_per_section_textrank(cur_sents,each_summ_num,num_sent_sec):
    summ_ratio = each_summ_num/num_sent_sec
    decoded = summarize(str(cur_sents),ratio=summ_ratio,split=True)
    return decoded