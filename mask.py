import cv2
import numpy as np

# Bild laden
image_path = "figures_ex5/yoshi.png"
mask_path = "figures_ex5/mask.png"
img = cv2.imread(image_path)
mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

# Übertragen Sie das Yoshi-Bild in den HSV-Farbraum
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Ändern Sie für alle weißen Pixel im Maskenbild den H-Wert im Yoshi-Bild
white_pixels = mask == 255
img_hsv[..., 0][white_pixels] = 120

# Konvertieren Sie das Bild zurück in den BGR-Farbraum
result_img = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

# Zeigen Sie das neue Bild auf dem Bildschirm an
cv2.imshow("Result Image", result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
