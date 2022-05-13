This sample script uses SpaCy to generate a concordance from a text file.
A concordance is an alphabetically sorted list of all unique words occurring in 
the text along with the frequency of their appearance and the 1-based index of the 
sentences they appear in. The path to the text file is defined as the first argument
when calling the script. The script will output the concordance to stdout. 
It was written using Python 3.8.10

Example usage:

    python concordance.py my-text-file.txt

SpaCy is the only dependency needed to run the script. The version used is written in
the requirements.txt file located inside the project.
The english language model needed for spaCy to tokenize the text needs to be installed
separately. This can be done by executing the following command:

    python -m spacy download en_core_web_sm

