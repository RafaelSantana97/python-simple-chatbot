from answer_structure import AnswerStructure
from data import Data
from compatibility_checker import CompatibilityChecker
from thesaurus import Thesaurus

class ChatBot:

  structured_answers = Data.structured_answers
  question: str

  def __init__(self):

    while True:
      self.question = input('[Voce]: ').lower()
      if self.exit_is_required(self.question):
        break

      calculated_indexes = {}

      for index, structured_answer in enumerate(self.structured_answers):
        calculated_indexes[index] = CompatibilityChecker().verifyCompatibility(self.question, structured_answer)

      print(self.create_answer(calculated_indexes))


    print('[Bot]: Tchau')

  def create_answer(self, calculated_indexes) -> str:
    key_best = max(calculated_indexes, key=calculated_indexes.get)
    value_best = calculated_indexes.pop(key_best)

    key_second_best = max(calculated_indexes, key=calculated_indexes.get)
    value_second_best = calculated_indexes.pop(key_second_best)

    answer: str = ''

    if value_best > 0.7:
      if (value_best - value_second_best) < 0.15:
        answer += '[Bot]: Pode especificar melhor?'
        answer += '\n[Bot]: Voce quis dizer \"' + self.structured_answers[key_best].keys[0] + '\" ou \"' + self.structured_answers[key_second_best].keys[0] + '\" ?'
      else:
        answer += '[Bot]: ' + self.structured_answers[key_best].answer

    elif value_best > 0.6:
      answer += '[Bot]: [Precisao de %.0f%%]:' % (100 * value_best)
      answer += '\n[Bot]: ' + self.structured_answers[key_best].answer

    elif value_best > 0.4:
      answer += '[Bot]: [Precisao de %.0f%%, nao tenho muita certeza sobre esta pergunta]:' % (100 * value_best)
      answer += '\n[Bot]: ' + self.structured_answers[key_best].answer

    else:
      answer += '[Bot]: Desculpe, nao entendi'
    
    return answer + '\n'

  def exit_is_required(self, question) -> bool:
    return question in Data.thesaurus.get_all_synonyms_of('sair')

ChatBot()