My Projects 
==========
List of programs i have written that i found may be useful for other people 

1.word2vec.py  

Given a set of documents it trains a word2vec model on them and stores it.
It uses gensim python library for traing the model


# Training ther model 
import wordevec
# dirname = directory containing all the files 

# preprocess the data using preprocessing 
import preprocessing as pr
train_data = pr.get_data(dirname)

# Train the model
wordevec.train_word2vec(train_data)

# loading the model 

model = wordevec.load_model(path)

# calling from command prompt

python word2vec.py dirname


2. tfidf.py

Given a set of documents tfidf matrix of documents is created and stored as pickle file.
