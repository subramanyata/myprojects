#
""" collection of functions useful for preprocessing                                                               """

import os
import io




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
