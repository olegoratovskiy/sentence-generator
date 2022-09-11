import argparse
import pickle
import re
import sys

from sentence_generator import SentenceGenerator
from sentence_generator import is_valid_file

parser_train = argparse.ArgumentParser()
parser_train.add_argument('--input-dir', type=lambda x: is_valid_file(parser_train, x, 'r'), help='Path to the '
                                                                                                  'directory '
                                                                                                  'containing the '
                                                                                                  'document.')
parser_train.add_argument('--model', type=str,
                          help='Path to the file where the model is saved.')
parser_train_args = parser_train.parse_args()

text = ''
if parser_train_args.input_dir is None:
    for line in sys.stdin:
        text += line
else:
    file = parser_train_args.input_dir
    text = file.read()
    file.close()

regex = r"[\w']+|[\.]"  # regex template
tokens = re.findall(regex, text)  # list of all words (tokenized)

# fit the model on training set
model = SentenceGenerator()
model.fit(tokens)

# save the model to disk
filename = parser_train_args.model
pickle.dump(model, open(filename, 'wb'))
