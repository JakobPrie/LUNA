import face_recognition
import numpy as np
import imutils
import pickle
import time
import cv2

PRIORITY = 6

def start(luna, profile):
    profile['LUNA_cams'] = {}
    profile['LUNA_face_boxes_names'] = {}
    profile['LUNA_cam_recognized_users'] = {}
    # load the actual face recognition model along with the label encoder
    profile['LUNA_face_recognizer'] = pickle.loads(open(profile['LUNA_PATH'] + '/resources/face_recognizer', "rb").read())
    profile['LUNA_face_label_encoder'] = pickle.loads(open(profile['LUNA_PATH'] + '/resources/face_label_encoder.pickle', "rb").read())

def run(luna, profile):
    for roomname, cams in profile['LUNA_cams'].items():
        profile['LUNA_face_boxes_names'][roomname] = {}
        profile['LUNA_cam_recognized_users'][roomname] = []

        for camname, frame in cams.items():
            profile['LUNA_face_boxes_names'][roomname][camname] = []

            # convert and resize the frame
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb = imutils.resize(frame, width=750)
            r = frame.shape[1] / float(rgb.shape[1])

            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input frame, then compute
            # the facial embeddings for each face
            boxes = face_recognition.face_locations(rgb, model='cnn')
            encodings = face_recognition.face_encodings(rgb, boxes)
            names = []

            # loop over the facial embeddings of the faces in this image
            for encoding in encodings:
                encoding = encoding.reshape(1, -1)

                # perform classification to recognize the face
                preds = profile['LUNA_face_recognizer'].predict_proba(encoding)[0]
                j = np.argmax(preds)
                proba = preds[j]
                name = profile['LUNA_face_label_encoder'].classes_[j]

                # update the list of names
                names.append((name,proba))
                profile['LUNA_cam_recognized_users'][roomname].append(name)

            # loop over the recognized faces
            for ((top, right, bottom, left), (name, proba)) in zip(boxes, names):
                # rescale the face coordinates
                top = int(top * r)
                right = int(right * r)
                bottom = int(bottom * r)
                left = int(left * r)
                if not (top, right, bottom, left, name) in profile['LUNA_face_boxes_names'][roomname][camname]:
                    profile['LUNA_face_boxes_names'][roomname][camname].append((top,right,bottom,left,name,proba))
