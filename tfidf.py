from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import sys
import preprocessing as pr


def update_documents(dirname):
    if not os.listdir(dirname):
        write_txt("Error - Files not found")
        return
    else:
        files = os.listdir(dirname)

    filenames = [dirname+"/"+files[i] for i in range(len(files))]
    list_txt(filenames, 'docnames.txt')
    file_lists = text_to_list(dirname)
    docs = preprocess_documents(file_lists)
    models = tfidf_docs(docs)
    if len(models) != 2:
        write_txt("Error - Unable to create tfidf matrix")
        return 
    else:
        pickle_dump(models[0],name = "doc_tfidf.pk")
        pickle_dump(models[1],name = "vectorizer.pk")
        write_txt("updated successfully")


def tfidf_docs(docs_corpus):
    """ given a set of documents returns tfidf matrix and model for it """
    tfidf_vectorizer = TfidfVectorizer(ngram_range = (1,2))
    try: 
        tfidf_docs = tfidf_vectorizer.fit_transform(docs_corpus)
    except (RuntimeError, TypeError, NameError,ValueError,IOError,KeyError):
        write_txt("Error - Unable to create tfidf matrix")
        return 
    return tfidf_docs,tfidf_vectorizer

def pickle_dump(model,name="picklefile.pk"):
    """  function to take a file and save it as pickle dump """
    with open(name,'wb') as f:
        pickle.dump(model,f)

def write_txt(txt,filename = 'output.txt'):
    """ writes to text file where each element is in separate line """
    thefile = open(filename,'w')
    for item in txt:
      thefile.write("%s" % item)
    thefile.close()
