# -*- coding: utf-8 -*-

import pandas as pd
import re
from nltk.corpus import stopwords # Import the stop word list
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import lda

def content_to_words(review_text):
    """ Function to convert a raw review to a string of words
     The input is a single string (a raw movie review), and 
     the output is a single string (a preprocessed movie review)  """
    # 1. Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ",review_text) 
    # 2.Convert to lower case, split into individual words
    words = letters_only.lower().split()                             
    # 3.In Python, searching a set is much faster than searching a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                   
    # 4. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    # 6. Join the words back into one string separated by space, and return the result.
    return( " ".join( meaningful_words )) 


def topic_model_lda(content,n_topics=20,n_top_words=10):
    """ runs LDA with specified number of topics  and creates most imp topic for each document and important
     keywords for each topics"""
    train_data = pd.read_csv(content)
    clean_data = [content_to_words(train_data[train_data.columns[0]][i]) for i in range(train_data[train_data.columns[0]].size)]            
    # Initialize the "CountVectorizer" object, which is scikit-learn's bag of words tool.  
    vectorizer = CountVectorizer(analyzer = "word",tokenizer = None,preprocessor = None,stop_words = None)                              
    train_data_features = vectorizer.fit_transform(clean_data)
    # Numpy arrays are easy to work with, so convert the result to an array
    train_data_features = train_data_features.toarray()   # document * terms matrix
    #words in the vocabulary
    vocab = vectorizer.get_feature_names()              
    # fitting lda model
    model = lda.LDA(n_topics,n_iter=1500, random_state=1)
    model.fit(train_data_features)
    topic_word = model.topic_word_
    titles =[i for i in range(train_data[train_data.columns[0]].size)]
    topic_details=[]
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
        topic_details.append((' '.join(topic_words)).encode('utf-8'))  
    topic_titles=["Topic "+str(i) for i in range(len(topic_details))]
    topic_keyword=pd.DataFrame({'Topics':topic_titles,'keywords':topic_details})
    pd.DataFrame.to_csv(topic_keyword,'Topic_keywords.csv')    
    doc_topic = model.doc_topic_
    max_topic=[doc_topic[i].argmax() for i in range(len(titles))]
    maxtopic=pd.Series(max_topic) 
    pd.Series.to_csv(maxtopic,'max_topic.csv') 
    return pd.Series.hist(maxtopic)

    
