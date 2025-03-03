from pdf2image import convert_from_path
import cv2
import numpy as np

def compare_images(img1, img2):
    return np.array_equal(img1, img2)

def check_pdf(pdf_name, pdf_pyth, compile_type ):
    if pdf_name == "":
        with open("comparePDF.log", "a") as f:
            f.write("For " + pdf_pyth + "\n")
            f.write("The " + compile_type + "compiled PDF do not compile successfully.\n")
            f.write("\n")
        return False
    return True

# if pdf identical, return True; else, return False
def compare_pdf(pdf_path1, pdf_path2):
    # 将 PDF 转换为图像
    images1 = convert_from_path(pdf_path1)
    images2 = convert_from_path(pdf_path2)

    flag = True

    err1 = ""
    err2 = []
    if len(images1) != len(images2):
        print("The number of pages is different.")
        err1 = "The number of pages is different."
        flag = False
    else:
        err1 = "The number of pages is the same."
        # 假设 PDF 具有相同数量的页面
        for i in range(len(images1)):
            img1 = cv2.cvtColor(np.array(images1[i]), cv2.COLOR_RGB2BGR)
            img2 = cv2.cvtColor(np.array(images2[i]), cv2.COLOR_RGB2BGR)
            err2.append(f"Page {i+1} is different.")
            if compare_images(img1, img2) is not True:
                print(f"Page {i+1} is different.")
                flag = False
            
    if flag is False:
        with open("comparePDF.log", "a") as f:
            f.write("For " + pdf_path1 + " and " + pdf_path2 + "\n")
            f.write(err1)
            f.write("\n")
            for err in err2:
                f.write(err)
                f.write("\n")
        return False
    with open("comparePDF.log", "a") as f:
        f.write("For " + pdf_path1 + " and " + pdf_path2 + "\n")
        f.write("The two PDFs are identical.\n")
        f.write("\n")
    return True