with open("archivos\\leid.txt","a",encoding="UTF-8") as archivo: # en el modo append agrega sobre lo ya escrito
    archivo.write("\n")
    for i in range(5):
        archivo.writelines(["linea con for: {i} agregada\n"])