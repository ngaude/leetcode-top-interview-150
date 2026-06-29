from typing import List
from collections import Counter

class Solution:
    def findSubstring_own(self, s: str, words: List[str]) -> List[int]:
        words = sorted(words)
        ns = len(s)
        nw = len(words)
        lw = len(words[0])
        res = []
        for i in range(ns):
            valid = True
            _words = []
            for j in range(nw):
                if i+(j+1)*lw > ns:
                    valid = False
                    break
                w = s[i+j*lw:i+(j+1)*lw]
                if not w in words:
                    valid = False
                    break
                _words.append(w)
            _words = sorted(_words)
            if valid and _words == words:
                res.append(i)
            print(i,res,_words)
        return res

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Count frequency of each word in the words list
        word_count = Counter(words)
    
        # Get lengths: string length, number of words, and length of each word
        string_length = len(s)
        num_words = len(words)
        word_length = len(words[0])  # All words have the same length
    
        result = []
    
        # Try all possible starting positions within a word length
        # This ensures we check all possible alignments
        for start_pos in range(word_length):
            left = right = start_pos
            current_word_count = Counter()
        
            # Slide the window through the string
            while right + word_length <= string_length:
                # Extract the next word from the string
                current_word = s[right:right + word_length]
                right += word_length
            
                # If the word is not in our target words, reset the window
                if word_count[current_word] == 0:
                    left = right
                    current_word_count.clear()
                    continue
            
                # Add the current word to our window
                current_word_count[current_word] += 1
            
                # If we have too many of the current word, shrink window from left
                while current_word_count[current_word] > word_count[current_word]:
                    removed_word = s[left:left + word_length]
                    left += word_length
                    current_word_count[removed_word] -= 1
            
                # Check if we have found a valid concatenation
                # Window size should equal total length of all words
                if right - left == num_words * word_length:
                    result.append(left)
    
        return result


s = "barfoothefoobarman"
words = ["foo","bar"]
output = [0,9]
assert Solution().findSubstring(s, words) == output

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
output = []
assert Solution().findSubstring(s, words) == output

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
output = [6,9,12]
assert Solution().findSubstring(s, words) == output


s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
output = [8]
assert Solution().findSubstring(s, words) == output
