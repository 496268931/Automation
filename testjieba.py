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

def main():
    list = [
        '好美的夜景，好可爱的小姑娘，很喜欢里面的节目，希望我有一天也可以到那里去',
        '这tm的分词精确度好高啊',
        '绿草苍苍白雾茫茫有位佳人在水一方绿草萋萋白雾迷离有位佳人靠水而居我愿逆流而上依偎在她身旁无奈前有险滩道路又远又长我愿顺流而下',
        '工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作',
        '这一次的文艺晚会非常成功，希望接下来的金砖峰会也能那么成功，支持厦门！！',
        '举报您的用户已封号'
    ]
    for i in list:
        method(i)

if __name__ == '__main__':
    main()
