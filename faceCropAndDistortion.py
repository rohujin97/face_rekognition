import sys
import dlib
import cv2
import openface
import glob
import os

# You can download the required pre-trained face detection model here:
# http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
predictor_model = "shape_predictor_68_face_landmarks.dat"

# Create a HOG face detector using the built-in dlib class
face_detector = dlib.get_frontal_face_detector()
face_pose_predictor = dlib.shape_predictor(predictor_model)
face_aligner = openface.AlignDlib(predictor_model)

# Get image directory
img_dir = sys.argv[1]
data_path = os.path.join(img_dir, '*g')
files = glob.glob(data_path)

# Directory for saving aligned face
align_dir_name = "aligned_faces"

root_dir = "C:/Users/rohuj/Desktop"
aligned_img_dir = root_dir + "/" + align_dir_name

try:
        if not os.path.isdir(aligned_img_dir) :
                os.mkdir(aligned_img_dir)
except OSError as e:
        if e.errno != errno.EEXIST:
                print("Failed to create directory\n")
                raise


# Face Crop & Face Distortion
for j, file_name in enumerate(files):
        # Load the image
        image = cv2.imread(file_name)

        # Run the HOG face detector on the image data
        detected_faces = face_detector(image, 1)

        print("Found {} faces in the image file {}".format(len(detected_faces), file_name))

        # Loop through each face we found in the image
        for i, face_rect in enumerate(detected_faces):

           # Detected faces are returned as an object with the coordinates 
           # of the top, left, right and bottom edges
           print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))

           # Get the the face's pose
           pose_landmarks = face_pose_predictor(image, face_rect)

           # Use openface to calculate and perform the face alignment
           alignedFace = face_aligner.align(534, image, face_rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

           # Save the aligned image to a file
           face_file_name = "aligned_face_%d_%d.jpg" % (j,i)
           cv2.imwrite(os.path.join(aligned_img_dir, face_file_name), alignedFace)
           
