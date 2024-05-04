from database import session, engine
from models import FaceModel, Checkin
from encoding_image import face_encoding
import models

models.Base.metadata.create_all(engine)


def add_face():
    user_name = input("Please enter your name: ")
    new_face = FaceModel(name=user_name, encoding=face_encoding())
    session.add(new_face)
    session.commit()
    return (f"new Face was added with username : {user_name}")

def compare_faces():
    
    face_to_compare = input("Please enter the name of the face to compare: ")
    face_to_compare_encoding = session.query(FaceModel).filter_by(name=face_to_compare).first().encoding
    user_face_encoding = face_encoding()


    if user_face_encoding == face_to_compare_encoding:
        print(f"BInary data is identical, you are {face_to_compare} ")
        conformation = input("Do you want to check in ? Y/N")
        if conformation.capitalize() == "Y":
            check_in()
        else:
            print("Checkin was canceled")
    else:
        print(f"The binary data wasnt a match !")
    

def check_in():
    
    new_check_in_user_name = input("Please enter your name: ")
    new_check_in_face =  Checkin(name=new_check_in_user_name, encoding=face_encoding())
    session.add(new_check_in_face)
    session.commit()
    return (f"new CheckIn was crated with usernames face binary data : {new_check_in_user_name}")


operation = input("Press C to compare faces, N to add new:")
if operation.capitalize() == "C":
    compare_faces()
elif operation.capitalize() == "N":
    add_face()
else:
    print("Invalid input")



# # Query all faces
# all_faces = session.query(Face).all()

# # Query by name
# specific_face = session.query(Face).filter_by(name='John Doe').first()
