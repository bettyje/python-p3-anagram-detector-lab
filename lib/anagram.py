class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        anagrams = []

        sorted_word = sorted(self.word)
        anagrams = [word for word in word_list if sorted(word) == sorted_word]
        return anagrams


# anagram_checker = Anagram("listen")
# result = anagram_checker.match(
#     ["enlist", "google", "silent", "inlets", "hello"])
# print(result)
