import cv2
# Alexandro Aguilar NC = 0007

# Cargar la imagen
imagen = cv2.imread("imagenes/leon.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(
    imagen,
    5
)

# Mostrar imágenes
cv2.imshow("Imagen original Leon-0007", imagen)
cv2.imshow("Imagen con filtro de mediana Leon-0007", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "resultado/leon_mediana.jpg",
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("resultado/leon_mediana.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Programa realizado por Alexandro Aguilar 0007")