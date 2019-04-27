from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer

LANGUAGE = 'english'

def get_summary_per_section_lsa(cur_sents,each_summ_num):
    summarizer = LsaSummarizer()
    summarizer = LsaSummarizer(Stemmer(LANGUAGE))
    summarizer.stop_words = get_stop_words(LANGUAGE)
    parser = PlaintextParser(cur_sents, Tokenizer(LANGUAGE))
    summ = summarizer(parser.document, each_summ_num)
    decoded = []
    for line in summ:
        decoded.append(line._text)
    return decoded