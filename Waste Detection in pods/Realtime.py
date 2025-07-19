from ultralytics import YOLO
import cv2
model = YOLO('Waste Detection in pods\60_epochs_denoised.pt')  
results = model('polution'.mp4)  # predict on an image
res_final = results[0].plot()
cv2.imshow(res_final)