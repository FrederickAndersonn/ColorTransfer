import cv2
import numpy as np

def color_transfer(input_image, target_image, color_space="Lab"):
    # Laden und in den Fließkommazahlen umwandeln
    input_img = cv2.imread(input_image).astype(np.float32) / 255.0
    target_img = cv2.imread(target_image).astype(np.float32) / 255.0

    # Konvertieren Sie beide Bilder in den gewünschten Farbraum
    if color_space == "Lab":
        input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2Lab)
        target_img = cv2.cvtColor(target_img, cv2.COLOR_BGR2Lab)
    elif color_space == "RGB":
        pass
    elif color_space == "HSV":
        input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2HSV)
        target_img = cv2.cvtColor(target_img, cv2.COLOR_BGR2HSV)
    else:
        raise ValueError("Ungültiger Farbraum. Verwenden Sie 'Lab', 'RGB' oder 'HSV'.")

    # Reinhardscher Farbtransfer
    for i in range(3):  # Für jeden Farbkanal separat
        input_channel = input_img[:, :, i]
        target_channel = target_img[:, :, i]

        # Berechnungen gemäß den Schritten (3i-3iv)
        input_channel = (input_channel - np.mean(input_channel)) / np.std(input_channel)
        input_channel = input_channel * np.std(target_channel) + np.mean(target_channel)

        # Setzen Sie die Ergebnisse zurück in das Bild
        input_img[:, :, i] = input_channel

    if color_space == "Lab":
        result_img = cv2.cvtColor(input_img, cv2.COLOR_Lab2BGR)
    elif color_space == "RGB":
        result_img = input_img
    elif color_space == "HSV":
        result_img = cv2.cvtColor(input_img, cv2.COLOR_HSV2BGR)

    return np.clip(result_img * 255, 0, 255).astype(np.uint8)  # Convert back to 8-bit unsigned integer

# Beispielaufruf mit Input- und Target-Bildern im Lab-Farbraum
input_image_path = "figures_ex5/FigSource.png"
target_image_path = "figures_ex5/FigTarget.png"
result_image_lab = color_transfer(input_image_path, target_image_path, color_space="Lab")

# Beispielaufruf mit Input- und Target-Bildern im RGB-Farbraum
result_image_rgb = color_transfer(input_image_path, target_image_path, color_space="RGB")

# Beispielaufruf mit Input- und Target-Bildern im HSV-Farbraum
result_image_hsv = color_transfer(input_image_path, target_image_path, color_space="HSV")

# Ergebnisbilder anzeigen
cv2.imshow("Result (Lab)", result_image_lab)
cv2.imshow("Result (RGB)", result_image_rgb)
cv2.imshow("Result (HSV)", result_image_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
