#
""" collection of functions useful for preprocessing                                                               """
import os
import io


from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


stops = set(stopwords.words("english"))
wnl = WordNetLemmatizer()


def get_data(dirname):
    """ Collects all text files in the given folder   """
    if not os.listdir(dirname):
        print "Files not found-Empty Directory "
        return
    else:
        files = os.listdir(dirname)
    filenames = [dirname+"/"+files[i] for i in range(len(files))]
    train_data = [io.open(filenames[i], 'r', encoding='latin-1').read() for i in range(len(filenames))]
    return train_data

def remove_characters_after_tokenization(tokens):
    """ takes a list of teokens and removes special characters """
    pattern = re.compile('([{}])*'.format(re.escape(string.punctuation)))
    filtered_tokens = filter(None, [pattern.sub('', token) for token in tokens])
    return filtered_tokens


def text_to_list(dirname):
    """ reads text files in a directory into a  list """
    filenames = os.listdir(dirname)
    files_list = [open(dirname+"/"+filenames[i], "r").readlines() for i in range(len(filenames))]
    return files_list


def list_txt(lis,txt = 'output.txt'):
    """ writes a list to text file where each element is in separate line """
    thefile = open(txt,'w')
    for item in lis:
      thefile.write("%s\n" % item)
    thefile.close()


def preprocess_documents(file_lists):
    """ takes a list of documents as list and preprocess them """
    file_tokens =[[file_lists[i][j].lower().split() for j in range(len(file_lists[i]))] for i in range(len(file_lists))]
    file_tokens_clean = [[x for x in file_tokens[i] if x] for i in range(len(file_tokens))]
    file_tokens_clean2 = [[remove_characters_after_tokenization(file_tokens_clean[i][j]) for j in range(len(file_tokens_clean[i]))] for i in range (len(file_tokens_clean))]
    files_final = [[[w for w in file_tokens_clean2[i][j]  if not w in stops] for j in range(len(file_tokens_clean2[i]))] for i in range(len(file_tokens_clean2))]
    files_lemma = [[[wnl.lemmatize(files_final[i][j][k].decode('latin-1')) for k in range(len(files_final[i][j]))] for j in range(len(files_final[i]))] for i in range(len(files_final))]
    docs = [[[files_lemma[i][j][k].encode('ascii','ignore') for k in range(len(files_lemma[i][j]))] for j in range(len(files_lemma[i]))] for i in range(len(files_lemma))]
    docs_corpus = [[" ".join(docs[i][j]) for j in range(len(docs[i]))] for i in range(len(docs))] 
    docs_final = ["".join(docs_corpus[j]) for j in range(len(docs_corpus))] 
    return docs_final

def preprocess_query(query):
    """ takes a list of query(single line) as list and preprocess them """
    query_tokens = [query[i].lower().split() for i in range(len(query))]
    query_tokens_clean = [[x for x in query_tokens[i] if x] for i in range(len(query_tokens))]
    query_tokens_clean2 = [remove_characters_after_tokenization(query_tokens_clean[j]) for j in range(len(query_tokens_clean))] 
    query_final = [[w for w in query_tokens_clean2[i] if not w in stops] for i in range(len(query_tokens_clean2))]
    query_lemma = [[wnl.lemmatize(query_final[i][j].decode('latin-1')) for j in range(len(query_final[i]))] for i in range(len(query_final))]
    query = [[query_lemma[i][j].encode('ascii','ignore') for j in range(len(query_final[i]))] for i in range(len(query_final))]
    query_corpus = [" ".join(query[i]) for i in range(len(query))]
    return query_corpus