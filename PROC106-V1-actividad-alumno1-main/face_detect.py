from traceback import format_tb
import cv2

#aqui estoy guardando en una variable el clasificador
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread("4f.jpg")

#convierte la imagen en gris
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Se llama a la función que reconoce las caras
#La funcion detectMultiScale detecta la cara(imagen en gris, escala de barritas, cuantos rasgos faciales)
faces = face_cascade.detectMultiScale(gray,1.1,4)
print(len(faces))

for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
       #foto=img[y:y+h, x:x+w]
       #cv2.imwrite("foto_de_cara.jpg",foto)
cv2.imshow('Imagen',img)
cv2.waitKey(0)



