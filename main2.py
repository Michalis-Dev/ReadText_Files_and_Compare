import main

f = open("teliko.txt", mode="w", encoding="utf-8")
main.my_function('file1.txt', 'file2.txt')

#print(main.my_function('file1.txt', 'file2.txt'))
#f.write(main.my_function('file1.txt', 'file2.txt'))
f.close()