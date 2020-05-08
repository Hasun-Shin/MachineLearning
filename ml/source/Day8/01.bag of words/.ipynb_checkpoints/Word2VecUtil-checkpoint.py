import re
import nltk

import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

from multiprocessing import Pool

class Word2VecUtil(object):

    @staticmethod
    def review_to_wordlist(review, remove_stopwords=False):
        review_text = BeautifulSoup(review, "html.parser").get_text()
        review_text = re.sub('[^a-zA-Z]', ' ', review_text)
        words = review_text.lower().split()
        if remove_stopwords:
            stops = set(stopwords.words('english'))
            words = [w for w in words if not w in stops]
        stemmer = SnowballStemmer('english')
        words = [stemmer.stem(w) for w in words]
        return(words)

    @staticmethod
    def review_to_join_words( review, remove_stopwords=False ):
        words = Word2VecUtil.review_to_wordlist(\
            review, remove_stopwords=False)
        join_words = ' '.join(words)
        return join_words

    @staticmethod
    def review_to_sentences( review, remove_stopwords=False ):
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        raw_sentences = tokenizer.tokenize(review.strip())
        sentences = []
        for raw_sentence in raw_sentences:
            if len(raw_sentence) > 0:
                sentences.append(Word2VecUtil.review_to_wordlist(\
                    raw_sentence, remove_stopwords))
        return sentences

    @staticmethod
    def _apply_df(args):
        df, func, kwargs = args
        return df.apply(func, **kwargs)

    @staticmethod
    def apply_by_multiprocessing(df, func, **kwargs):
        workers = kwargs.pop('workers')
        pool = Pool(processes=workers)
        result = pool.map(Word2VecUtil._apply_df, [(d, func, kwargs)
                for d in np.array_split(df, workers)])
        pool.close()
        return pd.concat(result)