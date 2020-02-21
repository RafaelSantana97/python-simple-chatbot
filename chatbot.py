from answer_structure import *

structured_answers = [
  AnswerStructure('Ola, tudo bem? Eu sou o Torvaldinho.', ['Oi , tudo bem ?', 'Oi', 'E ai ?', 'beleza ?', 'blz', 'Ola']),
  AnswerStructure('Entre 4 a 6 litros.', ['quantos litros de sangue uma pessoa tem ?', 'qual a quantidade de sangue de uma pessoa adulta ?']),
  AnswerStructure('São retirados 450 mililitros.', [' Em media , quantos litros de sangue sao retirados numa doacao de sangue ?']),
  AnswerStructure('Descartes.', [' De quem e a famosa frase “ Penso , logo existo ” ?', 'famosa frase “ Penso , logo existo ” ?', ' frase “ Penso , logo existo ” ?', ' Penso , logo existo', ' Penso logo existo']),
  AnswerStructure('Brasil.', [' De onde a a invencao do chuveiro eletrico ?', ' invencao do chuveiro eletrico ?', ' onde foi inventado o chuveiro eletrico ?', ' que pais inventou o chuveiro eletrico ?']),
  AnswerStructure('Vaticano e Russia.', ['Qual o menor e o maior pais do mundo ?', 'menor e o maior pais do mundo ?', 'menor e o maior pais', ' qual menor e o maior pais ?']),
  AnswerStructure('Vaticano.', ['Qual o menor pais do mundo ?', 'Qual o menor pais ?', 'menor pais']),
  AnswerStructure('Russia.', ['Qual o maior pais do mundo ?', 'maior pais do mundo ?', 'maior pais', 'Qual o maior pais ?']),
  AnswerStructure('João Goulart.', [' Qual o nome do presidente do Brasil que ficou conhecido como Jango ?', ' Qual o nome do presidente Jango ?', ' nome do presidente Jango ?', ' Jango ?', 'presidente conhecido como Jango']),
  AnswerStructure('299 792 458 metros por segundo.', [' Qual a velocidade da luz ?', 'velocidade da luz']),
]

question = input('[Voce]: ').lower()

while question not in ['0', 'sair', 'quit', 'q', 's', 'fim', 'terminar', 'tchau', 'xau', 'vlw flw', 'flw']:
  calculated_indexes = {}

  for index, structured_answer in enumerate(structured_answers):
    actual_compatibility = structured_answer.verifyCompatibility(question)
    calculated_indexes[index] = actual_compatibility


  key_best = max(calculated_indexes, key=calculated_indexes.get)
  value_best = calculated_indexes.pop(key_best)

  key_second_best = max(calculated_indexes, key=calculated_indexes.get)
  value_second_best = calculated_indexes.pop(key_second_best)


  if value_best > 0.7:
    if (value_best - value_second_best) < 0.15:
      print('[Bot]: Pode especificar melhor?')
      print('Voce quis dizer \"', structured_answers[key_best].keys[0], '\" ou \"', structured_answers[key_second_best].keys[0], '\" ?')
    else:
      print('[Bot]: ', structured_answers[key_best].answer)

  elif value_best > 0.6:
    print ("[Bot]: [Precisao de %.0f%%]:" % (100 * value_best))
    print('[Bot]: ', structured_answers[key_best].answer)

  elif value_best > 0.4:
    print ("[Bot]: [Precisao de %.0f%%, nao tenho muita certeza sobre esta pergunta]:" % (100 * value_best))
    print('[Bot]: ', structured_answers[key_best].answer)

  else:
    print('[Bot]: Desculpe, nao entendi')

  print()
  question = input('[Voce]: ').lower()

print('[Bot]: Tchau')