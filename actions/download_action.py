# -*- coding: utf-8 -*-
# @Project : upupup 
# @Time    : 2018/8/28 17:13
# @Author  : 
# @File    : download_action.py
# @Software: PyCharm
import urllib.request
import os

def cbk(a, b, c):
    '''
    下载回调函数
    :param a:
    :param b:
    :param c:
    :return:
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('{:.2f}%'.format(per))

def download(downloadLocation,file_path_final):
    '''
    :param downloadLocation: 下载的url全地址
    :param file_path_final: 文件存储路径,全路径
    :return:
    '''
    if not os.path.exists(os.path.dirname(file_path_final)):
        print('文件目录不存在,尝试创建目录')
        try:
            os.makedirs(os.path.dirname(file_path_final))
            print('目录创建成功，继续下载。')
        except Exception as e:
            exit(e)
    if os.path.exists(file_path_final):
        print('已存在同名文件！跳过')
    else:
        try:
            urllib.request.urlretrieve(downloadLocation, file_path_final, cbk)
        except Exception as err:
            print(err)