# import os
# path =r'C:\Users\Administrator\Desktop\重命名'
# os.rename(os.path.join(path, '《零边际成本社会》书中的知 识点和“自动炒菜锅”.jpg'), os.path.join(path, '测试重命名' + ".jpg"))
# import os
#
#
# #读取文件名
# def eachFile(filepath):
#     file_pash_list = []
#     pathDir = os.listdir(filepath)
#     for allDir in pathDir:
#         child = os.path.join('%s\%s'%(filepath,allDir))
#         file_pash_list.append(child)
#     return file_pash_list
#
#
# # for file in os.listdir(path):
# #     os.rename(os.path.join(path,file),os.path.join(path,str(count)+".jpg"))
# #     count+=1
#
# if __name__ == '__main__':
#     path = r'C:\Users\Administrator\Desktop\PDF转文本\输出'
#     print(eachFile(path))
# import random
#
# r = open(r'C:\Users\Administrator\Desktop\关键词库\萌萌网课首页.txt', 'r', encoding='utf-8').readlines()
#
# random_one = [x.strip() for x in random.sample(r,1)]
# print(random_one[0])
import re
text = '''
<h2>20200428-20200405生财-4月合集_decrypted_部分131</h2>ou au

收起
亚马逊热词top2.5万，4月18更新版.xlsx

查看详情

富叔、子路你腿好长、knight、陈荣(小金叔叔)、斑驱、尹雪、Hellen 口钨、
Woogle、k、莫一多'周鲁鲤 等63人觉得很赞

良辰美: 感谢大佬分享，特别适合选品，同做亚马逊，这个产品上架要考验执
行力了，争取下周一这里评论汇报下

2020/4/24

柏雪梅: 谢谢分享，就是看不懂英文误

2020/4/24

JACK 回复 柏下梅: 星球赚钱的路子太多了，英文的不一定就是好的
2020/4/24

Tyler durd* : 请问关键词是用什么工具挖掘出来的?

2020/4/24
良辰美: 这个是在品牌卖家后台都可以下载的
2020/4/24

严yan: 大佬方便加wx吗

2020/4/24

谭ucky: 补充，这是VC的ARA数据
2020/4/24

Jerry炜: 感谢分享，有需求就有市场，所以热词=需求=市场。
2020/4/24

查看更多评论

波本

2020/4/24

萌新提问: 大家可能都知道股票打新及可转债打新，但是一个账户中签率很
低，看到很多大佬都是弄很多账户。

想问的就是如何弄很多个打新账户”就算加上区妈的也才3个，那么更多的账
户要怎么获取?

查看详情

Javinlee: 可转债吗”谁没几十个亲威呢2 人家不给 说明执行力不够
2020/4/24

辛小噶 回复 ]avinlee: 有个办法，租用别人账户，给别人一点佣金。这个更高
效
20201/4/24

渊杰: A股和可转债没有办法，都是根据自然人。只有港股打新可以开多户一
起打
2020/4/24

渊杰: 还有如果你有公司户的话，用公司户也可以做线上新股和可转债打新
2020/4/诗

bobo 回复 渊杰: 想请教一下，用公司账户打新有什么优势?
2020/4/24

渊杰 回复 bobo: 线上打新没喻优势 只有一个科创板不需要50w就可以打 之前
可以做线下可转债打新 但是最近没有
20201/4/24

起点终站: 借楼问一下，可转债中签最多几张呀

2020/4/24

葡萄酋长: 亲威朋友借几个，最多有个七八个就金了，多了也管理不过来，今
年打债的人特别多，中签率已经很低了，这个肉不容易捡。

2020/4/24

查看更多评论

建元

20201/4/24



大家好，这两天忙迟到了两天才发布自我介绍，与各位大佬学习，大家多多
指教!

【了昵称】奋斗

【城市】湖北-武汉 (武汉朋友请联系我)

【籍贯】湖北-黄冈

【微信ID】JY-120788，

【个人介绍]

无意之中看到生财有术的星球，据说进星球的都是层次认知比较高的，

为了认识更多牛人，结交更多朋友，于是想办法让自己出现这里
我觉想要赚钱除了自己的认知能力和综合素质外，还要善于规划和抓住机遇

大学期间我就开始搞各种"副业“了 ，卖过联通不，办过暑期培训班，在
学校里办了一个户外用品出租的小团队，搞过电脑团购，去义务进货导学校
分发去卖，各种小生意基本都尝试过，后来12年毕业了，由于我学的是士林
工程专业，毕业直接去海外事业部-卡塔尔这个国家去上班了2年多，当时由
于是实习生一年工资也有15万上下，2年后拿着在外工作赚到的钱作为启动<p>萌萌团队相关词:无水印课程众筹,卖网课的资源从哪里来,最新众筹萌萌</p>
'''


if re.search(r'#.*',text):
    result = re.search(r'(#.*)',text).group()
    print(result)

else:
    print("没有匹配")