import re
import os
import cv2

num = 1

width = 800
height = 800
dim = (width, height)


for root, dirs, files in os.walk(".", topdown=False):
	for name in files:
		#print(os.path.join(root, name))
		nameImage = os.path.join(root,name)
		nameImage = str(nameImage)
		name_root = str(root)
		if re.search(r'image',name_root):
			if re.search(r'jpg',nameImage) or re.search(r'.jpeg',nameImage):
				# img = cv2.imread(nameImage)
				
				# print(len(img.shape))
				# if len(img.shape) == 3 : 
				# 	cv2.imwrite('image/'+str(num) + '.jpg', img )
				# 	num +=1
				# else : 
				# 	print('What a fuck is this ?')
				num +=1
print(num)



# 29 , 112, 148 , 405, 412, 466, 681, 993, 1253, 1377, 1492, 1640,2241