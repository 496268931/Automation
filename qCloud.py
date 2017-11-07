# -*- coding: utf-8 -*-
import json
from numpy import *
import time

from src.QcloudApi.qcloudapi import QcloudApi

module = 'wenzhi'
action = 'LexicalSynonym'
config = {
    'Region': 'gz',
    'secretId': 'AKIDjaHqGZOdNvHTZYwyPfgdPzOdjjeRpZtB',
    'secretKey': 'LWVJvLLFyWt671DFWeaKtGzd8RYYJ1Yv',
    'method': 'post'
}

def getLexicalSynonym(text):
        params = {'text':text}
    # try:
        print len(params['text'].decode('utf-8'))
        print len(text)

        # 生成请求的URL，不发起请求
        service = QcloudApi(module, config)
        print service.generateUrl(action, params)
        # 调用接口，发起请求
        x = service.call(action, params)
        print x
        # print json.loads(x)['syns']
        # print json.loads(x)['syns'][0]['word_ori']
        # print json.loads(x)['syns'][0]['word_syns']
        print

        if None != json.loads(x)['syns']:
            for i in json.loads(x)['syns']:


                ori_text = i['word_ori']['text']
                # idx_beg = i['word_ori']['idx_beg']
                # idx_end = i['word_ori']['idx_end']
                # print idx_beg
                # print idx_end
                print ori_text

                for j in i['word_syns']:
                    print j['text']



                print '-----------------------'


        #service.setRequestMethod('get')
        #print service.call('DescribeCdnEntities', {})
    # except Exception, e:
    #     print 'exception:', e

def main():
    # x = '去年南京人购买最多的文学书籍中，有一本书也特别打眼'
    # x = x.decode('utf-8').encode('utf-8')
    # print type(x)
    getLexicalSynonym('好久都没有去去音乐会现场了')

if __name__ == '__main__':
    main()
