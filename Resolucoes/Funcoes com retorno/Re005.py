def notas(*notas, situacao = False) :
    """
    => Função para analizar notas e situações de vários alunos.
        para notas: Uma ou mais notas de alunos
        para situacao: Valor adicional, indicando se deve ou não adicionar a situação
        return: Dicionário com várias informações sobre a situação da turma.
    """
    dicionario = {}
    menor = maior = soma = 0

    for i in range(len(notas)) :
        if i == 0:
            menor = maior = notas[i]
        else:
            if notas[i] < menor:
                menor = notas[i]

            if notas[i] > maior:
                maior = notas[i]

        soma += notas[i]

    dicionario['total'] = len(notas)
    dicionario['maior'] = maior
    dicionario['menor'] = menor

    media = soma / len(notas)
    dicionario['media'] = media

    if situacao == True:
        if media >= 9 :
            dicionario['situação'] = "ÓTIMA"

        elif media <= 5:
            dicionario['situação'] = "RUIM"

        elif media < 7:
            dicionario['situação'] = "RAZOÁVEL"

        elif media <= 8:
            dicionario['situação'] = "BOA"

    return dicionario


print(notas(5.5, 9.5, 10, 6.5, situacao=True))
