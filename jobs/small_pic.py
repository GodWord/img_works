# -*- coding:utf-8 -*-
import math
import os
import time

import numpy as np
from PIL import Image

imgs_path = "G:/work/img_works/img"  # 本地图集路径

out_path = 'G:/work/img_works/output'  # 输出图片路径
out_filename = 'merge.jpg'  # 输出图片名称


def img2vector(filename):
    try:
        img = Image.open(filename)  # 读取图片文件
        img = img.resize((200, 300))  # 设置图片大小
        data = np.asarray(img, np.uint8)  # 转化成array格式，数据类型是unit8，这个很重要，防止后续报错。
        return data
    except:
        print("the " + str(filename) + "has error happen")  # 报告哪个文件发生了异常，方便后续解决bug
        return None


def merge(path):
    print('开始获取路径下所有图片')
    fileList = os.listdir(path)  # 图集路径下所有文件名

    m = len(fileList)  # 获取文件数量
    k = int(math.ceil((m + 9) / 10)) * 330  # m是整数，如果尾数不为0，则通过+9，可以推动十位数+1，做到人工取整
    # 根据文件的个数，我们调整最终缩略图的长度，以免赋值大小或太小，导致有问题或大  片空白。(255,255,255）是白色的rgb值。
    data_end = 255 * np.ones((k, 2200, 3))
    count = 0
    print('开始拼接图片')
    for filename in fileList:
        print('开始处理图片:%s' % (filename,))
        filename = os.path.join(path, filename)  # 对文件夹路径与文件名称进行拼接
        if not os.path.isfile(filename):  # 判断路径视是否为文件
            merge(filename)  # 如果不为文件继续遍历文件
            continue
        data = img2vector(filename)  # 得到单个图片array
        if data is not None:  # 如果返回值为None则读取报错，不进行下一步处理
            x = int(count / 10) * 330
            y = int(count % 10) * 220
            data_end[x:(x + 300), y:(y + 200)] = data
            count += 1
            time.sleep(0.1)
    print('开始保存图片')
    if k > 330:  # 解决递归返回值不为文件的情况。
        data_end = np.uint8(data_end)
        image = Image.fromarray(data_end)

        # 计算根据已存在文件个数当前文件名称
        file_name = "%s.%s" % (
            out_filename.split('.')[0] + str(len(os.listdir(out_path))), out_filename.split('.')[1])
        pic_path = os.path.join(out_path, file_name)  # 将文件名与输出文件路径合并
        if not os.path.exists(out_path):  # 判断输出文件路径是否存在
            os.makedirs(out_path)  # 输出文件路径不存在则创建该路径
        image.save(pic_path)  # 保存图片到本地
        print('缩略图处理完成,保存路径为:%s' % (pic_path,))


if __name__ == '__main__':
    print('开始缩略图处理')
    # 调用合并方法
    merge(imgs_path)
