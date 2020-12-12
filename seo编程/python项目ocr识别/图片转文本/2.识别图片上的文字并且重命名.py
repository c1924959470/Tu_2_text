
import os,re


#读取文件名
def eachFile(filepath):
    file_pash_list = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s\%s'%(filepath,allDir))
        file_pash_list.append(child)
    return file_pash_list





def run():
    try:
        # paths = eachFile(r'C:\Users\Administrator\Desktop\图片转文本\输出文本')
        paths = eachFile(r'C:\Users\Administrator\Desktop\PDF转文本\输出')

        for inx, m_path in enumerate(paths):
            # 文件路径
            # path=r'C:\Users\Administrator\Desktop\图片转文本\输出文本'
            path=r'C:\Users\Administrator\Desktop\PDF转文本\输出'
            # 文件名
            file_name = m_path.split("\\")[-1]
            # 读取前2行
            f = open(m_path,'r',encoding='utf-8')
            read_two_lines=[]
            for i in range(3):
                read_two_lines.append(f.readline().strip())
            f.close()
            renames = ''.join(read_two_lines)
            # 正则替换renames
            rename= re.sub("/|\?|>|<|\n|h2|</h2>|\||\"|:| ", "", renames)
            if len(rename)>6:
                # 文件重命名
                os.rename(os.path.join(path, file_name ), os.path.join(path, rename + ".txt"))
            else:
                pass

            print('第{}个完成..新名字:{}'.format((inx + 1),rename))
    except:
        pass





if __name__ == '__main__':
    run()