# encoding=utf-8
import jieba

# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))
#
#
# x = jieba.cut("好美的夜景，好可爱的小姑娘，很喜欢里面的节目，希望我有一天也可以到那里去")  # 默认是精确模式
# print(", ".join(x))
# x = jieba.cut("这tm的分词精确度好高啊")  # 默认是精确模式
# print(", ".join(x))
# x = jieba.cut("绿草苍苍白雾茫茫有位佳人在水一方绿草萋萋白雾迷离有位佳人靠水而居我愿逆流而上依偎在她身旁无奈前有险滩道路又远又长我愿顺流而下")  # 默认是精确模式
# print(", ".join(x))
# x = jieba.cut("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作")  # 默认是精确模式
# print(", ".join(x))


def method(x):
    xx = jieba.cut(x)  # 默认是精确模式
    print(", ".join(xx))

def xiaoYang(x):
    xx = jieba.cut(x)  # 默认是精确模式
    a = {}
    xxx = []
    for i in xx:
        xxx.append(i)
    # print xxx
    for i in xxx:
        # print i
        # print xxx.count(i)
        if xxx.count(i)>1:
            a[i] = xxx.count(i)
    print a
    for key,value in a.items():
        print key,value
def main():
    # list = [
    #     '好美的夜景，好可爱的小姑娘，很喜欢里面的节目，希望我有一天也可以到那里去',
    #     '这tm的分词精确度好高啊',
    #     '绿草苍苍白雾茫茫有位佳人在水一方绿草萋萋白雾迷离有位佳人靠水而居我愿逆流而上依偎在她身旁无奈前有险滩道路又远又长我愿顺流而下',
    #     '工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作',
    #     '这一次的文艺晚会非常成功，希望接下来的金砖峰会也能那么成功，支持厦门！！',
    #     '举报您的用户已封号',
    #     '不愧是国家领导人观看的，节目都很精彩啊，台面感很强，希望各国之间都能永远只好。',
    #     '#带着微博去旅行#　　星愿直播的A轮融资已经谈到了最后阶段, 投资机构、明星投资人、上市公司和大体量企业，四方投资方全都参与进来, 乱哄哄你方唱罢我登场, 都想要插上一脚。最终胜出的是紫荆文化基金和凤凰创投两家, A轮融资商议出的金额是两千万。'
    # ]
    # for i in list:
    #     method(i)
    article = ''
    with open('testjieba.txt','r') as f:
        for i in f.readlines():
            article = article + i
    print len(article)
    xiaoYang(article)

if __name__ == '__main__':
    main()
