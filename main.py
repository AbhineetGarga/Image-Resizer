#Image Resizer
import cv2
#Confeguarable
# Specify the full path to the image file (if not in the same directory)
image_path = "E:\Lets start new journey\Py\Projects\Image-Resizer\image.jpeg"  # Replace with the actual path
destination= "Abhineet.png"
scale_percent = 50




image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

# if image is None:
#     print("Error: Could not read image file!")
# else:
#     cv2.imshow("Abhineet", image)
#     # cv2.waitKey(0)
#     #



new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)
# dim =

output=  cv2.resize(image, (new_width, new_height))


cv2.imwrite(destination, output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()