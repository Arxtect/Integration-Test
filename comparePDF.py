from pdf2image import convert_from_path
import cv2
import numpy as np

def compare_images(img1, img2):
    return np.array_equal(img1, img2)



# if pdf identical, return True; else, return False
def compare_pdf(pdf_path1, pdf_path2):
    # 将 PDF 转换为图像
    images1 = convert_from_path(pdf_path1)
    images2 = convert_from_path(pdf_path2)

    flag = True
    # 假设 PDF 具有相同数量的页面
    for i in range(len(images1)):
        img1 = cv2.cvtColor(np.array(images1[i]), cv2.COLOR_RGB2BGR)
        img2 = cv2.cvtColor(np.array(images2[i]), cv2.COLOR_RGB2BGR)
        
        if compare_images(img1, img2) is not True:
            print(f"Page {i+1} is different.")
            flag = False
            
    if flag is False:
        return False
    return True