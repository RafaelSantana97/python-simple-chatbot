from answer_structure import AnswerStructure
from data import Data

class CompatibilityChecker:

  thesaurus = Data().thesaurus

  def verifyCompatibility(self, raw_question: str, structured_answer: AnswerStructure) -> bool:
    best_compatibility = 0

    for raw_key in structured_answer.keys:     
      compatibility = self.compatibility_calculator(raw_key, raw_question)
      best_compatibility = max(best_compatibility, compatibility)

    return best_compatibility


  def handle_sentence(self, sentence) -> frozenset:
    for word in Data().words_to_be_ignored:
      sentence = sentence.replace(word, '')

    return frozenset(sentence.split())


  def compatibility_calculator(self, raw_key, raw_question) -> float:
    question_words = self.key_words_identifier(raw_question.lower())
    key_words = self.key_words_identifier(raw_key.lower())

    question_words = self.handle_sentence(question_words)
    key_words = self.handle_sentence(key_words)

    compatible_words = len(key_words.intersection(question_words))
    all_words = len(key_words.union(question_words))
    better_compatibility = compatible_words / all_words

    return better_compatibility     


  def key_words_identifier(self, sentence: str) -> [str]:
    sentence = ' ' + sentence + ' '
    synonyms_dictionary = self.thesaurus.synonyms_dictionary
    for synonyms_list in synonyms_dictionary:
      for expression in synonyms_list.expressions:
        if (' ' + expression.lower() + ' ') in sentence:
          sentence = sentence.replace(expression.lower(), str(hash(synonyms_list)))
          break

    return sentence.strip()