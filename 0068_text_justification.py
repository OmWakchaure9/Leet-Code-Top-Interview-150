class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            line_length = 0

            # Greedily select maximum words for the current line
            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            num_words = j - i
            total_spaces = maxWidth - line_length

            # Last line or line containing only one word
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                gaps = num_words - 1
                spaces = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""

                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (spaces + (1 if k - i < extra_spaces else 0))

                line += words[j - 1]

            result.append(line)
            i = j

        return result
