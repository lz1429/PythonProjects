#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import include
from django.urls import re_path as url
from web.views import account
from web.views import home
from web.views import project
from web.views import statistics
from web.views import wiki
from web.views import file
from web.views import setting
from web.views import issues
from web.views import dashboard

urlpatterns = [
    url(r'^register/$', account.register, name='register'),  # 注册
    url(r'^send/sms/$', account.send_sms, name='send_sms'),  # 发送短信验证码
    url(r'^login/sms/$', account.login_sms, name='login_sms'),  # 短信登录
    url(r'^login/$', account.login, name='login'),  # 密码登录
    url(r'^image/code/$', account.image_code, name='image_code'),  # 图片验证码
    url(r'^logout/$', account.logout, name='logout'),  # 注销

    url(r'^index/$', home.index, name='index'),  # 官网首页
    url(r'^price/$', home.price, name='price'),  # 价格套餐
    url(r'^payment/(?P<policy_id>\d+)/$', home.payment, name='payment'),  # 订单信息
    url(r'^pay/$', home.pay, name='pay'),  # 确认支付
    url(r'^pay/notify/$', home.pay_notify, name='pay_notify'),  # 支付成功后的跳转

    # 项目列表
    url(r'^project/list/$', project.project_list, name='project_list'),
    url(r'^project/star/(?P<project_type>\w+)/(?P<project_id>\d+)/$', project.project_star, name='project_star'),
    url(r'^project/unstar/(?P<project_type>\w+)/(?P<project_id>\d+)/$', project.project_unstar, name='project_unstar'),

    # 项目详情
    url(r'^manage/(?P<project_id>\d+)/', include([
        url(r'^wiki/$', wiki.wiki, name='wiki'),  # wiki预览
        url(r'^wiki/add/$', wiki.wiki_add, name='wiki_add'),  # 添加
        url(r'^wiki/upload/$', wiki.wiki_upload, name='wiki_upload'),  # 本地图片上传
        url(r'^wiki/catalog/$', wiki.wiki_catalog, name='wiki_catalog'),  # 获取wiki列表，前端动态新建目录
        url(r'^wiki/edit/(?P<wiki_id>\d+)/$', wiki.wiki_edit, name='wiki_edit'),  # 修改
        url(r'^wiki/delete/(?P<wiki_id>\d+)/$', wiki.wiki_delete, name='wiki_delete'),  # 删除

        url(r'^file/$', file.file, name='file'),  # 展示 & 添加 & 编辑
        url(r'^cos/credential/$', file.cos_credential, name='cos_credential'),  # 上传文件大小校验 & 获取cos上传临时凭证
        url(r'^file/post/$', file.file_post, name='file_post'),  # 上传成功后把信息存数据库 & 返回instance信息让前端新加一行表格信息
        url(r'^file/download/(?P<file_id>\d+)/$', file.file_download, name='file_download'),  # 下载文件
        url(r'^file/delete/$', file.file_delete, name='file_delete'),  # 删除文件 & 文件夹

        url(r'^setting/$', setting.setting, name='setting'),  # 系统设置
        url(r'^setting/delete/$', setting.delete, name='setting_delete'),  # 删除项目 & 删除桶

        url(r'^issues/$', issues.issues, name='issues'),  # 展示 & 添加
        url(r'^issues/detail/(?P<issues_id>\d+)/$', issues.issues_detail, name='issues_detail'),  # 问题详细 & 评论展示
        url(r'^issues/record/(?P<issues_id>\d+)/$', issues.issues_record, name='issues_record'),  # 获取评论 & 新建评论
        url(r'^issues/change/(?P<issues_id>\d+)/$', issues.issues_change, name='issues_change'),  # 问题修改 & 记录修改情况
        url(r'^issues/invite/url/$', issues.invite_url, name='invite_url'),  # 生成邀请码

        url(r'^dashboard/$', dashboard.dashboard, name='dashboard'),  # 概览
        url(r'^dashboard/issues/chart/$', dashboard.issues_chart, name='issues_chart'),  # 折线图

        url(r'^statistics/$', statistics.statistics, name='statistics'),  # 统计
        url(r'^statistics/priority/$', statistics.statistics_priority, name='statistics_priority'),  # 饼状图
        url(r'^statistics/project/user/$', statistics.statistics_project_user, name='statistics_project_user'),  # 柱状图

    ], None)),

    url(r'^invite/join/(?P<code>\w+)/$', issues.invite_join, name='invite_join'),  # 访问邀请码
]
