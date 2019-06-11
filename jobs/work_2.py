# -*- coding:utf-8 -*-
import pandas as pd
from pyecharts.options import InitOpts

__author__ = 'zhoujifeng'
__date__ = '2019/6/11 20:34'
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Scatter


def chart_1():
    path = 'H:\work\img_works\static\第二题\成交金额前20名.xlsx'
    df = pd.read_excel(path)
    df['成交金额（元）'] = df['成交金额（元）'].apply(lambda x: float(x.replace(',', '')))
    df['成交量（股）'] = df['成交量（股）'].apply(lambda x: float(x.replace(',', '')))
    attrs = list(df['证券简称'])
    #
    # Bar().add_xaxis(attrs,).add_yaxis("前收", list(df['前收']), gap='30%') \
    #     .add_yaxis("收盘", list(df['收盘']), gap='30%') \
    #     .set_global_opts(title_opts=opts.TitleOpts(title="2019年五月份成交金额前20名", subtitle="")).render('chart_1.1.html')

    Bar().add_xaxis(attrs, ) \
        .add_yaxis("成交金额（元）", list(df['成交金额（元）'])) \
        .add_yaxis("成交量（股）", list(df['成交量（股）'])) \
        .add_yaxis("前收", list(df['前收']), gap='30%') \
            .add_yaxis("收盘", list(df['收盘']), gap='30%') \
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45)),
        title_opts=opts.TitleOpts(title="2019年五月份成交金额前20名", subtitle="")) \
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False), ).render('chart_1.2.html')
    print('chart_1处理完成')


if __name__ == '__main__':
    chart_1()
