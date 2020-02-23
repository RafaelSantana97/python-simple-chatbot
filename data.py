from answer_structure import AnswerStructure
from thesaurus import Thesaurus, Synonym

class Data:

  structured_answers = [
    AnswerStructure('Ola, tudo bem?', ['Oi tudo bem', 'Oi', 'Tudo bem']),
    AnswerStructure('Um ser humano adulto possui entre 4 a 6 litros de sangue.', ['quantos litros de sangue uma pessoa tem ?', 'qual a quantidade de sangue de uma pessoa adulta ?']),
    AnswerStructure('São retirados 450 mililitros numa doação de sangue.', ['quantos litros de sangue doação ?']),
    AnswerStructure('Celebre frase de Renè Descartes.', [' De quem e a famosa frase “ Penso , logo existo ” ?', 'famosa frase “ Penso , logo existo ” ?', 'frase “ Penso , logo existo ” ?', 'Penso , logo existo', 'Penso logo existo']),
    AnswerStructure('O chuveiro elétrico foi inventado no Brasil.', ['De onde é a invenção do chuveiro elétrico ?', 'invencao do chuveiro elétrico ?', 'onde foi inventado o chuveiro elétrico ?', 'que país inventou o chuveiro elétrico ?']),
    AnswerStructure('Quem inventou o chuveiro elétrico foi o brasileiro Francisco Canho.', ['Quem inventou o chuveiro elétrico ?', 'Que pessoa inventou o chuveiro elétrico ?']),
    AnswerStructure('Vaticano e Russia são o menor e o maior país do mundo, respectivamente.', ['Qual o menor e o maior país do mundo ?', 'menor e o maior país do mundo ?', 'menor e o maior país', 'qual menor e o maior país ?', 'país', 'países']),
    AnswerStructure('Vaticano é o menor país do mundo.', ['Qual o menor país do mundo ?', 'menor país do mundo', 'menor país', 'Qual o menor país ?']),
    AnswerStructure('Russia é o maior país do mundo.', ['Qual o maior país do mundo ?', 'maior país do mundo ?', 'maior país', 'Qual o maior país ?']),
    AnswerStructure('João Goulart.', ['Qual o nome do presidente do Brasil que ficou conhecido como Jango ?', 'Qual o nome do presidente Jango ?', 'nome do presidente Jango ?', 'Jango ?', 'presidente conhecido como Jango']),
    AnswerStructure('A velocidade da luz é de 299 792 458 metros por segundo.', ['velocidade da luz em m/s']),
    AnswerStructure('A velocidade da luz é de 300.000 Km/s.', ['velocidade da luz em km/s', 'qual a velocidade da luz', 'velocidade da luz']),
    AnswerStructure('42.', ['6x9', '6 x 9', 'qual a resposta para a vida , o universo e tudo mais ?', 'vida universo e tudo mais', 'resposta para a vida', 'resposta para o universo']),
  ]

  thesaurus = Thesaurus([
    Synonym(['voce', 'vc', 'oce', 'ce', 'vs', 'vossa senhoria']),
    Synonym(['tudo bem', 'Tudo bem com voce', 'Tudo bom', 'Sussa', 'De boas', 'De boa', 'Suave', 'Beleza', 'Blz', 'Firmeza', 'Fmz','Como vai', 'Como está', 'Na boa']),
    Synonym(['Ola', 'Oi', 'E ai', 'Dae']),
    Synonym(['sair', 'fim', 'terminar', 'tchau', 'xau', 'vlw flw', 'flw']),
    Synonym(['maior', 'mais grande', 'gigante', 'grande']),
    Synonym(['menor', 'mais pequeno', 'pequeno']),
    Synonym(['doacao', 'doar', 'doação', 'doaçao', 'doacão']),
    Synonym(['a gente', 'nós']),
    Synonym(['pais', 'país']),
    Synonym(['paises', 'países']),
    Synonym(['invencao', 'invenção', 'invencão', 'invençao', 'criação', 'criacao']),
    Synonym(['inventor', 'criador']),
    Synonym(['é', 'e']),
    Synonym(['tem', 'possui']),
    Synonym(['ter', 'possuir']),
    Synonym(['quantidade', 'quantos', 'qual a quantidade', 'qual quantidade', 'quanto']),
    Synonym(['elétrico', 'eletrico']),
    Synonym(['pessoa', 'ser humano adulto', 'pessoa adulta', 'adulto']),
    Synonym(['que pessoa', 'qual pessoa', 'quem', 'qual foi a pessoa', 'quem foi que']),
    Synonym(['metros por segundo', 'm/s', 'metros/s', 'm/sec', 'metros/sec', 'mt/s']),
    Synonym(['quilometros por segundo', 'km/s', 'kilometros por segundo']),
  ])