# -*- coding: utf-8 -*-
import json

import chardet


def main():




    with open(u"F:\\Spider-V1.0.1-BEAT_豆瓣\\Output\\20171027_2924"
              u"\\Spider-20171027-1.log") as f:
        # data = f.read()
        # print(chardet.detect(data))

        for line in f.readlines():
            line = line.decode('GB2312').encode('utf-8')
            if line.find('本地模式不需要提交数据')>=0:
                line = line[line.find('"data":'):line.find(',"param":')]
                line = '{'+line+'}'
                line = json.loads(line)
                text = line['data']
                for content in text:
                    print content['text']


if __name__ == '__main__':
    main()