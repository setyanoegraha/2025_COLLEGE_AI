import cv2

# Path ke file Haar Cascade untuk wajah dan senyuman
face_cascade_path = cv2.data.haarcascades + \
    'haarcascade_frontalface_default.xml'
smile_cascade_path = cv2.data.haarcascades + 'haarcascade_smile.xml'

# Load Haar Cascade untuk wajah dan senyuman
faceDetect = cv2.CascadeClassifier(face_cascade_path)
smileDetect = cv2.CascadeClassifier(smile_cascade_path)

# Jika file Haar Cascade tidak ditemukan, beri pesan error dan hentikan program
if faceDetect.empty():
    print("Error: File Haar Cascade untuk wajah tidak ditemukan!")
    exit()

if smileDetect.empty():
    print("Error: File Haar Cascade untuk senyuman tidak ditemukan!")
    exit()

# Buka kamera
camera = cv2.VideoCapture(0)

# Periksa apakah kamera berhasil dibuka
if not camera.isOpened():
    print("Error: Kamera tidak terdeteksi!")
    exit()

print("Kamera terdeteksi. Mulai mendeteksi wajah dan senyuman...")

while True:
    # Baca frame dari kamera
    ret, img = camera.read()
    if not ret:
        print("Error: Gagal mengambil frame!")
        break

    # Ubah frame ke grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah
    faces = faceDetect.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop melalui setiap wajah yang terdeteksi
    for (x, y, w, h) in faces:
        # Gambar persegi di sekitar wajah
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Ambil region of interest (ROI) untuk deteksi senyuman
        roi_gray = gray[y:y+h, x:x+w]  # Area wajah dalam grayscale
        roi_color = img[y:y+h, x:x+w]  # Area wajah dalam warna

        # Deteksi senyuman di area wajah
        smiles = smileDetect.detectMultiScale(
            roi_gray,
            scaleFactor=1.8,
            minNeighbors=25,  # Meningkatkan minNeighbors untuk mengurangi false positive
            minSize=(25, 25)
        )

        # Jika senyuman terdeteksi, gambar persegi dan tambahkan teks
        if len(smiles) > 0:
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh),
                              (255, 0, 0), 2)  # Kotak biru untuk senyuman
                cv2.putText(roi_color, 'Smiling', (sx, sy-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        else:
            # Jika tidak ada senyuman yang terdeteksi, tambahkan teks "Not Smiling"
            cv2.putText(roi_color, 'Not Smiling', (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Tampilkan frame
    cv2.imshow("Face and Smile Detection", img)

    # Hentikan program jika tombol 'q' ditekan
    if cv2.waitKey(1) == ord('q'):
        break

# Tutup kamera dan jendela
camera.release()
cv2.destroyAllWindows()
