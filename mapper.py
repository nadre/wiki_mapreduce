#!/usr/bin/env python3

import sys
import json
import nltk
from collections import Counter
from unidecode import unidecode

def main():
    for line in sys.stdin:
        article = json.loads(line)
        title = article['title']
        text = article['text']
        article_id = article['id']

        emit_tokens(text, article_id, 'text')
        emit_tokens(title, article_id, 'title')
        #break

def emit_tokens(text, article_id, identifier):
    tokens = nltk.word_tokenize(text)

    #try to normalize to ascii
    tokens = [check_and_return_token(token) for token in tokens]
    
    #remove False tokens from list
    tokens = [token for token in tokens if token]

    token_count = Counter(tokens)
    for token, count in token_count.most_common():
        print( '%s\t%s\t%s\t%s' % (token, article_id, identifier, count) )

def check_and_return_token(str):
    token = str.lower()

    if len(token) < 1:
        return False

    final_token = unidecode(token)
    if len(token) != len(final_token):
        return False

    if not token.isalpha():
        return False

    return final_token

if __name__ == '__main__':
    main()