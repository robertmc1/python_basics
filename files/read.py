ipsum_file = open('ipsum.txt')

#for line in ipsum_file:
#    print(line.rstrip())
#
##el for es una forma de leer el archivo. pero como lo lee deja el cursor 
##al final de la linea y el metodo speek(0) resetea y coloca el cursor donde 
##queramos, en ete caso en el char 0
#ipsum_file.seek(0)
#
#lines = ipsum_file.readlines()
#print(lines)

ipsum_file.seek(50)
file_text = ipsum_file.read(100)
print(file_text)

ipsum_file.close()