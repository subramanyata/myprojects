from preprocessing import get_data
import sys
# Import and download stopwords from NLTK.
from nltk.corpus import stopwords
from nltk import download
download('stopwords')  # Download stopwords list.
# Import word2vec model
from gensim.models import Word2Vec
# Remove stopwords.
stop_words = stopwords.words('english')

 # Download data for tokenizer.
from nltk import word_tokenize
download('punkt') 



# Pre-processing a document.
def preprocess_gensim(doc):
    """ preprocess raw text by tokenising and removing stop-words,special-charaters """
    doc = doc.lower()  # Lower the text.
    doc = word_tokenize(doc)  # Split into words.
    doc = [w for w in doc if not w in stop_words]  # Remove stopwords.
    doc = [w for w in doc if w.isalpha()]  # Remove numbers and punctuation.
    return doc

# Train a word2vec model with default vector size of 100
def train_word2vec(train_data,worker_no=3, vector_size=100,model_name="word2vec_model"):
    """ Trains a word2vec model on the preprocessed data and saves it . """
    if not train_data:
        print "no training data"
        return
    w2v_corpus = [preprocess_gensim(train_data[i]) for i in range(len(train_data))]
    model = Word2Vec(w2v_corpus, workers = worker_no, size=vector_size)
    model.save(model_name)
    print "Model Created Successfully"

# Load the Model
def load_model(path = "word2vec_model"):
    """ loads the stored  word2vec model """
    name = Word2Vec.load(path)
    return name

if __name__ == "__main__":
    train_data = get_data(sys.argv[1])
    train_word2vec(train_data)
