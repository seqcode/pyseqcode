"""Helper module with functions for onehot sequence encoding and generators to
to enable whole genome iteration """

from __future__ import division
import numpy as np

def map_bases(seqs,seqlen):
    """ converts a list of sequences to a one hot np array """
    fd = { 'A' : [1, 0, 0, 0], 'T' : [0,1,0,0], 'G' : [0,0,1,0],'C' : [0,0,0, 1], 'N': [0,0,0,0]}  
    # encoding
    onehot = [fd[base] for seq in seqs for base in seq]
    onehot_np = np.reshape(onehot,(-1,seqlen,4))
    return onehot_np

# generator requirements: subset, transform and return a batch of seqs/other features without loading the file, and
# allowing different transformations.

# utility for sequence: 
def seqhandler(buf,line):
    buf.append(line.strip())
    return buf

# utility for discrete features ( eg. accessibility, H3K27me3)
def arrayhandler(buf, line):
    acc = line.strip("\t")
    acc = [float(x) for x in acc]
    buf.append(acc)
    return buf

def assign_handler(dtype):
    """ chooses a data handling functionality """
    if dtype == "seq":
        # seqhandler will handle sequence features
        handler = seqhandler
        fmt = map_bases 
    else:
        # arrayhandler will handle discrete fetaures.
        handler = arrayhandler
        fmt = np.array
    return handler

def train_generator(filenanme, size, seqlen, dtype):
    """ A generator to return a batch of sites, while iterating over the file in a loop. Note: Using append repeatedly here, 
    so might not be super efficient. Alternatively, can use the inbuilt readlines function with an appox. buffer size but not quite sure how
    it'll behave at the EOF since we need looping with constant batch size. """
    handler = assign_handler(dtype)
    # iterate
    with open(filename, "r") as fp:
        line_index = 0, buf = [] # buf is my feature buffer
        while True:
            for line in fp:
                if line_index < size:
                    buf = handler(buf,line)
                    line_index +=1
                else:
                    yield fmt(buf)
                    buf = [] # clean buffer
                    buf.append(line.strip())
                    line_index += 1 # reset line index
            fp.seek(0) # reset file pointer
