import random

f = open(r'C:\Users\pgveg\documents\bootcampP\python-3-bootcamp\Python Basics\petnames.txt','r')
f_content = f.read()
f_content_list = f_content.split('\n')
f.close()


random_names = random.choice(f_content_list)
print(random_names)