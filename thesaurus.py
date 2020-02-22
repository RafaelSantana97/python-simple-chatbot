class Synonym:

  def __init__(self, words: set):
    self.words = words


class Thesaurus:

  def __init__(self, synonyms_dictionary: list):
    self.synonyms_dictionary = synonyms_dictionary

  def is_synonym(self, word_1: str, word_2: str) -> bool:
    for synonyms in self.synonyms_dictionary:
      if set(word_1, word_2).issubset(synonyms):
        return True
    return False

  def get_all_synonyms_of(self, word: str) -> Synonym:
    for synonyms in self.synonyms_dictionary:
      if word in synonyms.words:
        return synonyms.words

    return []