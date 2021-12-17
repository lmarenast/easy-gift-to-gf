from code_base import *
import requests

from tkinter import filedialog
from tkinter import *


root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes=[("jpeg files","*.jpg"),
                ("png files","*.png")])

#img = PIL.Image.open(requests.get("https://www.elcomercio.com/wp-content/uploads/2021/06/Billie-700x391.jpg", stream=True).raw).convert("RGB")
img = PIL.Image.open(root.filename).convert("RGB")

face_detector = get_dlib_face_detector()
landmarks = face_detector(img)

display_facial_landmarks(img, landmarks, fig_size=[5, 5])

for landmark in landmarks:
    face = align_and_crop_face(img, landmark, expand=1.3)
    new_img = (face2paint(model=model, img=face, size=512))
    new_img.show()