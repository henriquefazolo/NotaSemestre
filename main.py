"""
A nota do semestre de um aluno é definida pela média das notas bimestrais.
Crie um programa que leia as notas bimestrais e mostre a média semestral de um aluno.
"""


class MediaSemestral:
    def __init__(self, bimestre_1, bimestre_2, bimestre_3):
        self.bimestre_1 = bimestre_1
        self.bimestre_2 = bimestre_2
        self.bimestre_3 = bimestre_3

    def media_semestral(self):
        media = (self.bimestre_1 + self.bimestre_2 + self.bimestre_3) / 3
        return media


m = MediaSemestral(5, 5.5, 6)

print(f'Média semestral : {m.media_semestral()}')
