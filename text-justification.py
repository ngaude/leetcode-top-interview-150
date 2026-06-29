from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line = []
        nline = 0
        for word in words:
            nword = len(word)
            if nline+nword <= maxWidth:
                line.append(word)
                nline += nword + 1
            else:
                lines.append(line)
                line = [word]
                nline = nword + 1
        if len(line):
            lines.append(line)
        text = []
        for kk,line in enumerate(lines):
            n = len(line)
            nline = sum([len(w) for w in line])
            nspace = maxWidth - nline
            if n == 1:
                text.append(line[0]+' ' * (nspace))
            elif kk == len(lines)-1:
                t = ' '.join(line)
                t += ' '*(maxWidth - len(t))
                text.append(t)
            elif n == 2:
                text.append((' '*(nspace)).join(line))
            else:          
                t = ''
                sp_size = nspace // (n-1)
                sp_extra_count = nspace % (n-1)
                for i in range(len(line)-1):
                    t += line[i]
                    if i < sp_extra_count:
                        t += ' '*(sp_size+1)
                    else:
                        t += ' '*sp_size
                t += line[-1]
                text.append(t)
        return text
    
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
text = Solution().fullJustify(words,maxWidth)
for t in text:
    print(f'|{t}|')

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
text = Solution().fullJustify(words,maxWidth)
for t in text:
    print(f'|{t}|')

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
text = Solution().fullJustify(words,maxWidth)
for t in text:
    print(f'|{t}|')


words = ["My","momma","always","said,","\"Life","was","like","a","box","of","chocolates.","You","never","know","what","you're","gonna","get."]
maxWidth = 20
text = Solution().fullJustify(words,maxWidth)
for t in text:
    print(f'|{t}|')