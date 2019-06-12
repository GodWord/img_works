# -*- coding:utf-8 -*-
import pandas as pd
from pyecharts.options import InitOpts

__author__ = 'zhoujifeng'
__date__ = '2019/6/11 20:34'
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Scatter


def chart_1():
    path = 'G:\work\img_works\static\第二题\成交金额前20名.xlsx'
    df = pd.read_excel(path)
    df['成交金额（元）'] = df['成交金额（元）'].apply(lambda x: float(x.replace(',', '')))
    df['成交量（股）'] = df['成交量（股）'].apply(lambda x: float(x.replace(',', '')))
    attrs = list(df['证券简称'])

    Bar().add_xaxis(attrs, ) \
        .add_yaxis("成交金额（元）", list(df['成交金额（元）'])) \
        .add_yaxis("成交量（股）", list(df['成交量（股）'])) \
        .add_yaxis("前收", list(df['前收']), gap='30%') \
        .add_yaxis("收盘", list(df['收盘']), gap='30%') \
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45)),
        title_opts=opts.TitleOpts(title="2019年五月份成交金额前20名", subtitle="")) \
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False), ).render('chart_1.html')
    print('chart_1处理完成')


def chart_2():
    path = 'G:\work\img_works\static\第二题\换手率前20名.xlsx'
    df = pd.read_excel(path)
    attrs = list(df['证券简称'])

    Bar().add_xaxis(attrs, ) \
        .add_yaxis("换手率%", list(df['换手率%']), gap='30%') \
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45)),
        title_opts=opts.TitleOpts(title="2019年五月份换手率前20名", subtitle="")) \
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False), ).render('chart_2.html')
    print('chart_2处理完成')


def chart_3():
    path = 'G:\work\img_works\static\第二题\市盈率前20名.xlsx'
    df = pd.read_excel(path)
    df.sort_values(by='市盈率', inplace=True, ascending=False)
    attrs = list(df['证券简称'])

    Bar().add_xaxis(attrs, ) \
        .add_yaxis("市盈率", list(df['市盈率']), gap='30%') \
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45)),
        title_opts=opts.TitleOpts(title="市盈率前20名.xlsx", subtitle="")) \
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False), ).render('chart_3.html')
    print('chart_3处理完成')

def chart_4():
    path = 'G:\work\img_works\static\第二题\涨幅前20名.xlsx'
    df = pd.read_excel(path)
    df.sort_values(by='涨幅%', inplace=True, ascending=False)
    attrs = list(df['证券简称'])

    Bar().add_xaxis(attrs, ) \
        .add_yaxis("涨幅%", list(df['涨幅%']), gap='30%') \
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45)),
        title_opts=opts.TitleOpts(title="涨幅前20名", subtitle="")) \
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False), ).render('chart_4.html')
    print('chart_4处理完成')


if __name__ == '__main__':
    chart_1()
    chart_2()
    chart_3()
    chart_4()
