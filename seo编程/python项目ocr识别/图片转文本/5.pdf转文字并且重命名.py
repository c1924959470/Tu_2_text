
import os,re
import random


#读取文件名
def eachFile(filepath):
    file_pash_list = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s\%s'%(filepath,allDir))
        file_pash_list.append(child)
    return file_pash_list



def run():

        # paths = eachFile(r'C:\Users\Administrator\Desktop\图片转文本\输出文本')
        paths = eachFile(r'C:\Users\Administrator\Desktop\PDF转文本\输出')

        for inx, m_path in enumerate(paths):
            # 文件路径
            # path=r'C:\Users\Administrator\Desktop\图片转文本\输出文本'
            path=r'C:\Users\Administrator\Desktop\PDF转文本\输出'
            # 文件名
            file_name = m_path.split("\\")[-1]

            # 先正则匹配标题,否则读取前几行作为标题
            f = open(m_path,'r',encoding='utf-8')
            read = f.readlines()
            read_str = ''.join(read)
            # rename_re = re.search(r'#.*|.*\?|.*吗|.*如何|.*怎么.*|.*什么.|.*呢?',read_str)
            rename_re = re.search(r'#.*(\s|[\r\n])|.*\?|.*吗.(\s|[\r\n])|.*呢.(\s|[\r\n])|如何.*(\s|[\r\n])|生财有术.*|#轻享# .*',read_str,re.M|re.I)

            if rename_re is None:
                # f = open(m_path, 'r', encoding='utf-8')
                # #执行读取前2行作为标题
                # read_two_lines = []
                # for i in range(20):
                #     read_two_lines.append(f.readline().strip())
                #
                # renames = ''.join(read_two_lines[12:15])
                #
                # # 正则替换renames
                # rename_re = re.sub("", "", renames)
                # rename_re2= re.search(r'[\u4e00-\u9fa5].*',rename_re).group()
                # if len(rename_re2)>12:
                #     rename = rename_re2[:12]
                # f.close()
                pass

            else:
                renames= rename_re.group()
                rename = re.sub("\*|/|\?|>|<|\n|h2|</h2>|\||\"|:| ", "", renames)
                f.close()
                print(rename)


                #打开关键词文本，随机插入关键词
                r = open(r'C:\Users\Administrator\Desktop\关键词库\比尔盖茨推荐书\比尔盖茨书.txt', 'r', encoding='utf-8').readlines()
                random_one = [x.strip() for x in random.sample(r, 1)]
                rename_zu = "【{}】{}".format(random_one[0],rename)
                os.rename(os.path.join(path, file_name ), os.path.join(path, rename_zu + ".txt"))

                print('第{}个完成..新名字:{}'.format((inx + 1),rename))



if __name__ == '__main__':
    run()