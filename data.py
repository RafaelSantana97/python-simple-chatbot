from answer_structure import AnswerStructure
from thesaurus import Thesaurus, Synonym

class Data:

  structured_answers = [
    AnswerStructure('Ola, tudo bem? Eu sou o Torvaldinho.', ['Oi , tudo bem ?']),
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

  thesaurus = Thesaurus([
    Synonym(['Ola', 'Oi', 'E ai', 'E ai ?', 'Dae']),
    Synonym(['Tudo bem', 'Tudo bem ?', 'Tudo bem com voce ?', 'Tudo bom', 'Tudo bom ?', 'Sussa', 'Sussa ?', 'De boas ?', 'De boa ?', 'Suave ?', 'Beleza ?', 'Blz ?', 'Firmeza ?' 'Fmz ?','Como vai ?', 'Como está ?', 'Na boa ?']),
    Synonym(['sair', 'fim', 'terminar', 'tchau', 'xau', 'vlw flw', 'flw'])
  ])