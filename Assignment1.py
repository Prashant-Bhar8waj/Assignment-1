import tokenize
from importlib import reload
from exercise_2 import analysis
import matplotlib.pyplot as plt
#exercise_2 = reload(exercise_2.py)

# run on English text
with open("data/macbeth_en.txt", "r") as f:
    p,m = analysis("English", f.read().lower().split())
    plt.savefig('my_plot1.png')
# run on German text
with open("data/macbeth_de.txt", "r") as f:
    p,m = analysis("German", f.read().lower().split())
    plt.savefig('my_plot2.png')

# run on PIRATES OF THE CARRIBEAN: DEAD MAN'S CHEST
# TODO: Use NLTK's corpora for loading this text
# and call the function as done above

import nltk
#nltk.download('punkt')
nltk.download('gutenberg', download_dir='.')
#from nltk.corpus import gutenberg


#text = gutenberg.raw("austen-persuasion.txt")
with open("./corpora/gutenberg/austen-persuasion.txt", "r") as f:
    p,m = analysis("austen-persuasion", f.read().lower().split())
    plt.savefig('my_plot3.png')
    

#Run on Transformer's trainer module's source code
with open("data/trainer.py", "r") as f:
    tokens = [
        x.string
        for x in tokenize.generate_tokens(f.readline)
        if x.type not in {
            tokenize.COMMENT, tokenize.STRING, tokenize.INDENT, tokenize.DEDENT, tokenize.NEWLINE
        }
    ]
    p,m = analysis("Python", tokens)
    plt.savefig('my_plot4.png')
