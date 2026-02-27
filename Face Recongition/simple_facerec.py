import cv2
import os
import face_recognition
import numpy as np
known_path=".\\Images\\Known_people"
Unkown_path=".\\Images\\Unknown_people"
class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

    def load_encoding_images(self, images_path):
        images = os.listdir(images_path)

        for img in images:
            img_path = os.path.join(images_path, img)
            image_data = cv2.imread(img_path)

            if image_data is None:
                continue

            rgb_img = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)

            boxes = face_recognition.face_locations(rgb_img, model="hog")
            encodings = face_recognition.face_encodings(
                rgb_img, boxes, num_jitters=1
            )

            for encoding in encodings:
                self.known_face_encodings.append(encoding)
                self.known_face_names.append(os.path.splitext(img)[0])

    def detect_known_faces(self, rgb_img_small):
        face_locations = face_recognition.face_locations(
            rgb_img_small
        )
        face_encodings = face_recognition.face_encodings(
            rgb_img_small, face_locations, num_jitters=1
        )

        face_names = []

        for face_encoding in face_encodings:
            face_distances = face_recognition.face_distance(
                self.known_face_encodings, face_encoding
            )
            best_match_index = np.argmin(face_distances)

            if face_distances[best_match_index] < 0.45:
                name = self.known_face_names[best_match_index]
            else:
                name = "Unknown"

            face_names.append(name)

        return face_locations, face_names