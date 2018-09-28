import re

txt = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"

name_list = txt.split(',')

print(name_list) # Q1

p = re.compile(r'^김|이')
kim_lee_list = [x for x in name_list if p.match(x)]

print(len(kim_lee_list)) # Q2

no_duple_list = list(set(name_list))

print(no_duple_list) # Q3

no_duple_list.sort()

print(no_duple_list) # Q4