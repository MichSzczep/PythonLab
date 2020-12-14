#!/usr/bin/env python3
import os
ile0 = os.popen('ls /dev | wc -l').read()
print("W folderze /dev znajduje się " + str(ile0) + " plików")

print('Podaj ścieżkę do katalogu, który chcesz przeszukać: ')
path = input()
os.system('ls -R ' + path)

print('Podaj ścieżkę do katalogu, w którym stworzone zostaną pliki .jpg do konwersji:')
path2 = input()
for i in range (4):
    filename = path2+'/file'+str(i)+'.jpg'
    os.system('touch '+filename)
    
#os.system('mogrify -format jpg *.png')
    
for i in range (4):
    filename = path2+'/file'+str(i)+'.jpg'
    filename2 = path2+'/file'+str(i)+'.png'
    os.system('cp ' + filename + ' ' + filename2)