import cv2

cam = cv2.VideoCapture(0)

while True:
	ret, image = cam.read()
	cv2.imshow('Imagetest',image)
	k = cv2.waitKey(1)
	if k != -1:
		break
# cv2.imwrite('/home/pi/testimage.jpg', image)
cam.release()
cv2.destroyAllWindows()



# import cv2

# cam = cv2.VideoCapture(0)

# while True:
# 	ret, image = cam.read()
# 	cv2.imshow('Imagetest',image)
# 	k = cv2.waitKey(1)
# 	if k != -1:
# 		break
# # cv2.imwrite('/home/pi/testimage.jpg', image)
# cam.release()
# cv2.destroyAllWindows()

# import cv2

# # Disable the GTK backend for headless mode
# cv2.setUseOptimized(True)
# cv2.setNumThreads(4)
# cv2.ocl.setUseOpenCL(False)
# cv2.CAP_DSHOW = False

# # Open the camera
# cap = cv2.VideoCapture(0)

# # Check if the camera is opened successfully
# if not cap.isOpened():
#     print("Error: Unable to access the camera.")
#     exit()

# while True:
#     # Read a frame from the camera
#     ret, frame = cap.read()

#     # Check if the frame is valid
#     if not ret:
#         break

#     # Display the frame
#     cv2.imshow("Camera", frame)

#     # Break the loop if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the camera and close the OpenCV windows
# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import matplotlib
# matplotlib.use("Agg")
# cv2.setUseOptimized(True)
# cv2.setNumThreads(4)
# cv2.ocl.setUseOpenCL(False)
# cv2.CAP_DSHOW = False
# # Enable Video4Linux2 (V4L2) backend
# cv2.CAP_V4L2 = True

# # Open the camera
# cap = cv2.VideoCapture(0)

# # Check if the camera is opened successfully
# if not cap.isOpened():
#     print("Error: Unable to access the camera.")
#     exit()

# while True:
#     # Read a frame from the camera
#     ret, frame = cap.read()
#     # Check if the frame is valid
#     if not ret:
#         break

#     # Display the frame
#     # cv2.imshow("Camera", frame)

#     # Break the loop if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the camera and close the OpenCV windows
# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import matplotlib.pyplot as plt

# # Set the resolution for the camera
# width, height = 640, 480

# # Create a VideoCapture object to access the camera
# cap = cv2.VideoCapture(0)

# # Set the camera resolution
# cap.set(3, width)
# cap.set(4, height)

# try:
#     while True:
#         # Capture frame-by-frame
#         ret, frame = cap.read()

#         # Check if the frame is valid
#         if not ret:
#             break

#         # Convert the frame from BGR to RGB for displaying with matplotlib
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         # Display the frame using matplotlib
#         plt.imshow(frame_rgb)
#         plt.axis('off')  # Hide axes
#         plt.show(block=False)  # Show the frame without blocking the code

#         # Wait for a short time before capturing the next frame
#         plt.pause(0.1)

#         # Close the matplotlib figure to avoid memory leak
#         plt.close()

#         # Check if the user pressed 'q' to exit the loop
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

# except KeyboardInterrupt:
#     # Release the VideoCapture and close any open windows
#     cap.release()
#     cv2.destroyAllWindows()
