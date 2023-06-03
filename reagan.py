"""Прочтите файл reaganomics.txt и скопируйте все до подзаголовка
«Уровни федерального подоходного налога и налога на заработную плату»."""

file = open("reaganomics.txt")
content = ""

for line in file:
        if "Federal income tax and payroll tax levels" in line:
            break

        content += line

print(content)
