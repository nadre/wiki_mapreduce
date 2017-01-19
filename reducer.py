#!/usr/bin/env python3

from operator import itemgetter
import sys

def main():

    current_token = None
    current_count = 0
    token = None

    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()

        # parse the input we got from mapper.py
        token, article_id, identifier, count = line.split('\t', 3)

        if identifier == "text":
            is_text_token = True
        else:
            is_title_token = True

        # convert count (currently a string) to int
        try:
            count = int(count)
        except ValueError:
            # count was not a number, so silently
            # ignore/discard this line
            continue

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: token) before it is passed to the reducer
        if current_token == token:
            current_count += count
        else:
            if current_token:
                # write result to STDOUT
                print('%s\t%s' % (current_token, current_count))
            current_count = count
            current_token = token

    # do not forget to output the last token if needed!
    if current_token == token:
        print('%s\t%s' % (current_token, current_count))

if __name__ == '__main__':
    main()
