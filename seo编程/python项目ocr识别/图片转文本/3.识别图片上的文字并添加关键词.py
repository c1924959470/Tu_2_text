
import pyocr.builders		# OCR识别
import io				# 将Wand处理结果传给给Pillow
import pprint			# 美美的打印出来
import os
import pytesseract
from PIL import Image
import random

#读取文件名
def eachFile(filepath):
    file_pash_list = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s\%s'%(filepath,allDir))
        file_pash_list.append(child)
    return file_pash_list

def ocr(path):
    img = Image.open(path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    s = pytesseract.image_to_string(img, lang='chi_sim')  #不加lang参数的话，默认进行英文识别
    return s


def save(content,file_name):
    r = open(r"C:\Users\Administrator\Desktop\关键词库\职场怎么办长尾词.txt", "r", encoding='utf-8')
    lines = r.readlines()  # 读取全部内容
    r.close()
    lines_three = [x.strip() for x in random.sample(lines, 3)]
    lines_one = [x.strip() for x in random.sample(lines, 1)]

    with open(r'C:\Users\Administrator\Desktop\图片转文本\输出文本\{}({}).txt'.format(lines_one[0],file_name),'w',encoding='utf-8') as f:
        content = "<h2>{},{}</h2>".format(lines_one[0],file_name) + content.strip() + "<p>相关词:" + ','.join(lines_three) + "</p>"
        f.write(content)
        f.close()

def run():
    paths = eachFile(r'C:\Users\Administrator\Desktop\图片转文本\输入图片')
    for inx, path in enumerate(paths):
        file_name = path.split("\\")[-1].split(".")[-2]
        print('正在处理{}'.format(file_name))
        try:
            content = ocr(path)
            save(content, file_name)
            print('第{}个文件,处理完成....'.format(inx + 1))
            # print(file_name)
        except:
            pass


if __name__ == '__main__':
    run()