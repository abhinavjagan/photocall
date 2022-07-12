from deepface import DeepFace

result = DeepFace.verify(img1_path = "img2.jpg", img2_path = "pdatabase/img3.jpg")
print(result)
