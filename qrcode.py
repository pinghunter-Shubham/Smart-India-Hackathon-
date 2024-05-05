import cv2
from pyzbar.pyzbar import decode
def scan_qr_code():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        decoded_objects = decode(frame)
        
        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            return data  # Return the scanned QR code data
        
        key = cv2.waitKey(1)
        if key == 27:  # Press Esc to exit the camera
            break

    cap.release()
    cv2.destroyAllWindows()