import cv2

# mở camera
cap = cv2.VideoCapture(0)

while True:
    # đọc hình ảnh từ camera
    ret, frame = cap.read()

    # hiển thị hình ảnh
    cv2.imshow('Camera', frame)

    # thoát khỏi vòng lặp khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# giải phóng camera và đóng cửa sổ hiển thị hình ảnh
cap.release()
cv2.destroyAllWindows()
#

