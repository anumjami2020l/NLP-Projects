import cv2
import pytesseract

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'"D:\Github_desktop\Data_Extraction_And_Analysis\tesseract"\tesseract.exe'

# Load and preprocess the image
image_path = 'D:\Github_desktop\Data_Extraction_And_Analysis\WhatsApp Image 2025-01-03 at 17.51.58_681f3d4d.jpg'  # Replace with your image path
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Perform OCR
text = pytesseract.image_to_string(thresh, lang='eng')
print(text)
