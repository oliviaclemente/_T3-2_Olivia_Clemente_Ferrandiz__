username = input("Ingrese usuario: ")  #definimos variables
password =  input("Ingrese contraseña: ")

username1 = 3 <= len(username) < 10         #en esta parte de codigo decimos que la longitud del usuario que hemos añadidio tiene que tener un alongitud entre 3 y 10
password1 = password == "Tokio" or password == "Python"  #aqui decimos que si la contraseña es Tokio o Python dara True 

print("Username:", username1)  #imprimimos por pantalla el resultado que nos haya dado segun se haya evaluado
print("Password:", password1)