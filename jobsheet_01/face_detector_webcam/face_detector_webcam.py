import cv2  # type: ignore

# Pastikan file 'haarcascade_frontalface_default.xml' ada di direktori yang sama dengan script ini
# atau gunakan path lengkap ke file tersebut.
face_cascade_path = cv2.data.haarcascades + \
    'haarcascade_frontalface_default.xml'
faceDetect = cv2.CascadeClassifier(face_cascade_path)

# Jika file Haar Cascade tidak ditemukan, beri pesan error dan hentikan program
if faceDetect.empty():
    print("Error: File Haar Cascade tidak ditemukan!")
    exit()

# Buka kamera
camera = cv2.VideoCapture(0)

# Periksa apakah kamera berhasil dibuka
if not camera.isOpened():
    print("Error: Kamera tidak terdeteksi!")
    exit()

print("Kamera terdeteksi. Mulai mendeteksi wajah...")

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

    # Gambar persegi di sekitar wajah yang terdeteksi
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Tampilkan frame
    cv2.imshow("Face Detection", img)

    # Hentikan program jika tombol 'q' ditekan
    if cv2.waitKey(1) == ord('q'):
        break

# Tutup kamera dan jendela
camera.release()
cv2.destroyAllWindows()
