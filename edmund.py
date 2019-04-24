
def get_summary_per_section_edmund(cur_sents,each_summ_num):
    summarizer = EdmundsonSummarizer()
    parser = PlaintextParser(cur_sents, Tokenizer(LANGUAGE))
    summ = summarizer(parser.document, each_summ_num)
    decoded = []
    for line in summ:
        decoded.append(line._text)
    return decoded