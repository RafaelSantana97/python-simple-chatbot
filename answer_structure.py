class AnswerStructure:

  def __init__(self, answer, keys):
    self.answer = answer
    self.keys = keys

  def verifyCompatibility(self, question):
    best_compatibility = 0
    question_words = self.handleQuestion(question)

    for key in self.keys:
      key_words = set(key.lower().split())
      
      compatibility = self.compatibility_calculator(key_words, question_words)
      best_compatibility = max(best_compatibility, compatibility)

    return best_compatibility

  def handleQuestion(self, question):
    question = question.replace('?', ' ?')
    return set(question.split())

  def compatibility_calculator(self, key_words, question_words):
    compatible_words = len(key_words.intersection(question_words))
    all_words = len(key_words.union(question_words))
    return compatible_words / all_words