class Synonym:

  def __init__(self, expressions: frozenset):
    self.expressions = expressions

class Thesaurus:

  def __init__(self, synonyms_dictionary: list):
    self.synonyms_dictionary = synonyms_dictionary


  def get_all_synonyms_of(self, word: str) -> Synonym:
    for synonyms in self.synonyms_dictionary:
      if word in synonyms.expressions:
        return synonyms.expressions

    return []