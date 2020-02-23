from answer_structure import AnswerStructure
from data import Data
from compatibility_checker import CompatibilityChecker
from thesaurus import Thesaurus

class ChatBot:

  structured_answers = Data.structured_answers
  question: str

  def __init__(self):
    self.info()

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
    answer: str = '\n'

    key_best = max(calculated_indexes, key=calculated_indexes.get)
    value_best = calculated_indexes.pop(key_best)

    key_second_best = max(calculated_indexes, key=calculated_indexes.get)
    value_second_best = calculated_indexes.pop(key_second_best)

    if (value_best - value_second_best) < 0.1 and value_best != 1 and value_best > 0.4:
      answer += '[Bot]: Pode especificar melhor?\n'
      answer += '[Bot]: Você quer saber \"' + self.structured_answers[key_best].keys[0] + '\" ou \"' + self.structured_answers[key_second_best].keys[0] + '\" ?'
    else:
      if value_best > 0.4:
        answer += '[Precisão de %.0f%%]:' % (100 * value_best) + '\n'
        answer += '[Bot]: ' + self.structured_answers[key_best].answer
      else:
        answer += '[Bot]: Desculpe, não entendi'
    
    return answer + '\n'


  def exit_is_required(self, question) -> bool:
    return question in Data.thesaurus.get_all_synonyms_of('sair')

  def info(self):
    x = frozenset([item.answer for item in self.structured_answers])
    print("Oi, tudo bem?\nEu sou o Torvaldinho\n")
    print("Tente adivinhar as perguntas para algumas das respostas abaixo:")
    print("Suas sentenças não precisam ser exatas nem completas:\n")
    for index, answer in enumerate(x):
      print(str(index) + '.', answer)
    print()

ChatBot()