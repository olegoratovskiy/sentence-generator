import argparse
import pickle

from sentence_generator import is_valid_file

parser_generate = argparse.ArgumentParser()
parser_generate.add_argument('--model', type=lambda x: is_valid_file(parser_generate, x, 'rb'),
                             help='Path to the file where the model is loaded.')
parser_generate.add_argument('--prefix', type=str, default='',
                             help='Optional argument. The beginning of a sentence (one or more words). If not '
                                  'specified, '
                                  'select the initial word randomly from all words.')
parser_generate.add_argument('--length', type=int, default=5, help='Length of the generated sequence.')

parser_generate_args = parser_generate.parse_args()

loaded_model = pickle.load(parser_generate_args.model)
result = loaded_model.generate(parser_generate_args.prefix, parser_generate_args.length)
print(result)
