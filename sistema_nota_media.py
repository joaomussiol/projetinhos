nome_aluno = input("digite nome do seu nome:")
idade_aluno = int(input("digite idade do aluno:"))
nota_aluno_1 = float(input("digite sua nota 1:"))
nota_aluno_2 = float(input("digite sua nota 2:"))
nota_aluno_3 = float(input("digite sua nota 3:"))
media_final = (nota_aluno_1 + nota_aluno_2 + nota_aluno_3) / 3
if media_final >= 6:
    print("aluno aprovado, media final dele é: ", round(media_final, 2))
else:
    print("aluno reprovado, media final dele é:", round(media_final, 2))
