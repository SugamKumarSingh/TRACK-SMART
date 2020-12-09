import cv2
import os
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
# 7. image saving
direc=r'D:\lol'
os.chdir(direc)
x=input("Enter your name")
result=cv2.imwrite(str(x)+ ".jpg", frame)
#print(showPic)

cam.release()

cv2.destroyAllWindows()
import face_recognition
direc=r'D:\lol'
os.chdir(direc)
picture_of_me = face_recognition.load_image_file(str(x)+ ".jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file(r'D:\lol\swapnil.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of Swapnil Pant")
else:
    print("It's not a picture of Swapnil Pant")
