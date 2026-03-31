class Solution(object):
    def compress(self, chars):
        i = 0
        index = 0

        while i < len(chars):
            j = i

            # count duplicates
            while j < len(chars) and chars[j] == chars[i]:
                j += 1

            # write character ONCE
            chars[index] = chars[i]
            index += 1

            count = j - i

            # write count if >1
            if count > 1:
                for digit in str(count):
                    chars[index] = digit
                    index += 1

            i = j

        return index