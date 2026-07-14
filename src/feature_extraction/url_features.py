# Used for splitting URLs into words/tokens
import re

# Import urlparse to separate URL components
from urllib.parse import urlparse

def extract_url_features(url):
    parsed=urlparse(url)
    # print(parsed)

    hostname=parsed.netloc

    path=parsed.path

    # feature1--url length
    length_url=len(url)

    #FEATURE 2-- ratio_digits_url->how many characters are digits
    digits_in_url=sum(char.isdigit() for char in url)
    ratio_digits_url=(digits_in_url)/length_url
    # print(ratio_digits_url)

    # split URL into words/token/list
    words_raw=re.split(r"[\/\.\-\_\?\=\&]+",url)
    words_raw=[word for word in words_raw if word]
    # print(words_raw)

    #FEATURE 3-- length_words_raw
    length_words_raw=len(words_raw)

    #FEATURE 4-- Longest word in URL
    longest_words_raw=max((len(word) for word in words_raw),default=0)
    
    #FEATURE 5-- hostname length
    length_hostname=len(hostname)
    
    # print(length_words_raw,longest_words_raw,length_hostname)
    #split path into words
    
    path_words=re.split(r"[\/\-\_\.\?\=\&]+",path)
    path_words=[word for word in path_words if word]
    
    # FEATURE 6: Average word length in path
    
    avg_word_path=(sum(len(word) for word in path_words)/len(path_words)
                   if path_words else 0)

    # FEATURE 7: Character Repetition
    # goooogle.com
    char_repeat=sum(1 for i in range(1,len(url))
                    if url[i]==url[i-1])
    return {

        # Total URL length
        "length_url": length_url,

        # Percentage of digits in URL
        "ratio_digits_url": ratio_digits_url,

        # Total number of tokens in URL
        "length_words_raw": length_words_raw,

        # Length of longest token
        "longest_words_raw": longest_words_raw,

        # Domain name length
        "length_hostname": length_hostname,

        # Average token length in path
        "avg_word_path": avg_word_path,

        # Consecutive repeated characters count
        "char_repeat": char_repeat,


    }

