import tensorflow as tf
import numpy as np
import cv2
import keras
from datetime import datetime

#audio code
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
#volume.SetMasterVolumeLevel(-25, None)


def get_extended_image(img, x, y, w, h, k=0.1):
    # The next code block checks that coordinates will be non-negative
    # (in case if desired image is located in top left corner)
    if x - k*w > 0:
        start_x = int(x - k*w)
    else:
        start_x = x
    if y - k*h > 0:
        start_y = int(y - k*h)
    else:
        start_y = y

    end_x = int(x + (1 + k)*w)
    end_y = int(y + (1 + k)*h)

    face_image = img[start_y:end_y,
                     start_x:end_x]
    face_image = tf.image.resize(face_image, [224, 224])
    # shape from (250, 250, 3) to (1, 250, 250, 3)
    face_image = np.expand_dims(face_image, axis=0)
    return face_image

video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # webcamera

if not video_capture.isOpened():
    print("\n\n\nUnable to access the camera")
else:
    print("\n\n\nAccess to the camera was successfully obtained")

print("\n\n\nStreaming started - to quit press ESC")

face_classifier = keras.models.load_model(r'C:\MyProject\397199_397209\Models\Test8_model.h5')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
class_names = ['Gozler Kapali', 'Sol Goz Kirpiliyor','Gozler Acik','Sag Goz Kirpiliyor']


sesAyarlayici = -20
sesSeviyesiTutucu = volume.GetMasterVolumeLevel()
kapalimi = False

gozYumulduktanSonraAcildiMi = True


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if not ret:
        print("\n\n\nCan't receive frame (stream end?). Exiting ...")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(100, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        # for each face on the image detected by OpenCV
        # get extended image of this face
        face_image = get_extended_image(frame, x, y, w, h, 0.5)

        # classify face and draw a rectangle around the face
        # green for positive class and red for negative
        result = face_classifier.predict(face_image)
        prediction = class_names[np.array(
            result[0]).argmax(axis=0)]  # predicted class
        confidence = np.array(result[0]).max(axis=0)  # degree of confidence

        
        if prediction == 'Gozler Kapali':
            if kapalimi==False:
                now = datetime.now()    #gözlerin kırpıldığı anı tutuyor.
                kapalimi = True         #gözler her kapatıldığında kapalımı ifadesi true değer alıyor.
                                        #gözler her açıldığında da false ifadesini alıyor.
            
            new = datetime.now()        #buda şimdiki zamanı tutuyor.
            fark = new - now
            #print(fark)
            if fark.microseconds >600000 or fark.seconds > 0: #eğer 0.6 milisaniyeden daha uzun süre göz kırpılmış ise
                
               
               




                if gozYumulduktanSonraAcildiMi:
                    if volume.GetMasterVolumeLevel() != -63:
                        gozYumulduktanSonraAcildiMi = False
                        sesSeviyesiTutucu = volume.GetMasterVolumeLevel()
                        print("burda")
                        volume.SetMasterVolumeLevel(-63, None)
                        print("Ses kapatıldı.")
                    else:
                        volume.SetMasterVolumeLevel(sesSeviyesiTutucu, None)
                        print("ses geri açıldı.")
                        gozYumulduktanSonraAcildiMi = False
                color = (0,0,255)
        
        
        
        
        
        
        
        
        
        
            else:
                color = (255,255,255)

        elif prediction == 'Sol Goz Kirpiliyor':
            volume.SetMasterVolumeLevel(sesAyarlayici, None)
            if sesAyarlayici != -65:
                sesAyarlayici -= 1
            color = (255,0,0) #blue
            if kapalimi:
                kapalimi = False
                gozYumulduktanSonraAcildiMi = True


        elif prediction == 'Gozler Acik':
            color = (255,255,255)
            if kapalimi:
                kapalimi = False
                gozYumulduktanSonraAcildiMi = True


        else:
            volume.SetMasterVolumeLevel(sesAyarlayici, None)
            if sesAyarlayici != 0:
                sesAyarlayici += 1
            color = (0,255,0)
            if kapalimi:
                kapalimi = False
                gozYumulduktanSonraAcildiMi = True




        # draw a rectangle around the face
        cv2.rectangle(frame,
                      (x, y),  # start_point
                      (x+w, y+h),  # end_point
                      color,
                      2)  # thickness in px
        cv2.putText(frame,
                    # text to put
                    "{:6} - {:.2f}%".format(prediction, confidence*100),
                    (x, y),
                    cv2.FONT_HERSHEY_PLAIN,  # font
                    2,  # fontScale
                    color,
                    2)  # thickness in px

    # display the resulting frame
    cv2.imshow("Face detector - to quit press ESC", frame)

    # Exit with ESC
    key = cv2.waitKey(1)
    if key % 256 == 27:  # ESC code
        break


# when everything done, release the capture
video_capture.release()
cv2.destroyAllWindows()
print("\n\n\nStreaming ended")