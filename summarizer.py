# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:55:30 2019

@author: abhis
"""

# summarizer

def get_summary_all_sections(sentences,num_sents,summarizer_name="textrank",tot_num_sents=12):
    summaries = []
    each_summ_num = tot_num_sents/len(sentences)
    for i in range(len(sentences)):
        cur_sents = sentences[i]
        num_sent_sec = num_sents[i]
        decoded = get_summary_per_section(cur_sents,each_summ_num,num_sent_sec,summarizer_name)
        summaries.append(decoded)
    return summaries

def get_ordered_summary(list_sent_sec,summary):
    ordered_summ = []
    for sent in list_sent_sec:
        for line in summary:
            if sent in line:
                if sent not in ordered_summ:
                    ordered_summ.append(sent)
                    break
    return ordered_summ

def get_ordered_summaries(list_sent,summaries):
    ordered_summs = []
    for i in range(len(list_sent)):
        list_sent_sec = list_sent[i]
        summary = summaries[i]
        ordered_summ = get_ordered_summary(list_sent_sec,summary)
        ordered_summs.append(ordered_summ)
    return ordered_summs

def summarize_url(url,summarizer_name="textrank"):
    sentences,list_sent,num_sents = parse_url_sentences(url)
    summaries = get_summary_all_sections(sentences,num_sents,summarizer_name)
    ordered_summs = get_ordered_summaries(list_sent,summaries)
    return ordered_summs
