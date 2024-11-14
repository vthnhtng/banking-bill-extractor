from PIL import Image
import pytesseract

image_path = 'bill.jpeg'
image = Image.open(image_path)

def get_roi(x, y, w, h):
    return (x, y, x + w, y + h)

amount_image = image.crop(get_roi(152, 396, 368, 90))
receiver_image = image.crop(get_roi(149, 604, 667, 58))
receiver_account_image = image.crop(get_roi(155, 655, 413, 41))
date_image = image.crop(get_roi(711, 781, 199, 72))
description_image = image.crop(get_roi(517, 897, 389, 72))
transaction_code_image = image.crop(get_roi(574, 1130, 338, 43))

print("So tien: " + pytesseract.image_to_string(amount_image))
print("Nguoi nhan: " + pytesseract.image_to_string(receiver_image))
print("STK nguoi nhan: " + pytesseract.image_to_string(receiver_account_image))
print("Ngay: " + pytesseract.image_to_string(date_image))
print("Noi dung: " + pytesseract.image_to_string(description_image))
print("Ma giao dich: " + pytesseract.image_to_string(transaction_code_image))
