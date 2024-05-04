from deepface import DeepFace
import numpy as np
import pickle

from video_face_detect import capture_face
def face_encoding():
    image = (capture_face())
    face_encoding = DeepFace.represent(img_path=image, model_name="Facenet")
    embedding = face_encoding[0]['embedding']
    
    # Convert the list to bytes
    binary_data = pickle.dumps(embedding)
    # print(f"the binary_data is type {type(binary_data)}") 
    return binary_data


#face_encoding()