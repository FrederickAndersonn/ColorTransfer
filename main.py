import cv2
import numpy as np

# Bild laden
image_path = "figures_ex5/yoshi.png"
mask_path = "figures_ex5/mask.png"
img = cv2.imread(image_path)
mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

# Breite, Höhe und Anzahl der Farbkanäle ausgeben
height, width, channels = img.shape
print(f"Breite: {width}, Höhe: {height}, Farbkanäle: {channels}")

# Bilddatenformat auf Fließkomma ändern
img_float = img.astype(np.float32) / 255.0

# Bild als uint8 anzeigen und warten, bis eine Taste gedrückt wird
cv2.imshow("Original (uint8)", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Bild als Float anzeigen und warten, bis eine Taste gedrückt wird
cv2.imshow("Float", img_float)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Rotes Quadrat in die Mitte des Bildes einzeichnen
square_size = 10
start_x = width // 2 - square_size // 2
start_y = height // 2 - square_size // 2
end_x = start_x + square_size
end_y = start_y + square_size
img[start_y:end_y, start_x:end_x, :] = [0, 0, 255]

# Jede 5. Zeile durch schwarze Pixel ersetzen
img[::5, :] = 0

# Bild auf der Festplatte speichern
cv2.imwrite("output_image.png", img)

# Übertragen Sie das Yoshi-Bild in den HSV-Farbraum
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Ändern Sie für alle weißen Pixel im Maskenbild den H-Wert im Yoshi-Bild
white_pixels = mask == 255
img_hsv[..., 0][white_pixels] = 0  # Setzt den H-Wert für weiße Pixel auf 0 (Rot)

# Konvertieren Sie das Bild zurück in den BGR-Farbraum
result_img = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

# Zeigen Sie das neue Bild auf dem Bildschirm an
cv2.imshow("Result Image", result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
