# -*- coding: utf-8 -*-
import os, smtplib, json
from django.conf import settings
from elasticsearch import Elasticsearch
from django.db import connection
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def switch_path_relative(absolute_path, keyword):
    idx = absolute_path.index(keyword)
    path = "\\" + absolute_path[idx:]
    path = '/'.join(path.split("\\"))
    return path


def write_es(data, index='travel', doc_type='note'):
    es_data = []
    es_data.append({"create": {"_index": index, "_type": doc_type}})
    es_data.append(data)
    es_host = settings.ES_HOST
    es = Elasticsearch([es_host], timeout=20)
    result = es.bulk(index=index, doc_type=doc_type, body=es_data, refresh=True)
    return result


def sql_get_es(sql):
    '''
    当用sql语句从es获取数据的时候可以使用此函数
    :param sql:传入sql语句。例：'select * from backup/backup_log ORDER BY dev_name desc limit 0,10'
    :return:{'count': 0, 'data': []}    其中count是符合条件的数据总条数，data是返回整理好的数据，是一个数组
    '''
    result = {}
    es_host_dict = settings.ES_HOST
    host = str(es_host_dict[u"host"])
    port = str(es_host_dict[u"port"])
    sql_url = "http://%s:%s/" % (host, port) + "_sql?sql=" + sql
    # 发起get请求获取数据
    es_res = requests.session().get(sql_url).content
    es_res = json.loads(es_res)
    data_res = es_res["hits"]["hits"] if es_res.has_key("hits") else {}
    result["count"] = es_res['hits']['total'] if es_res.has_key("hits") else 0
    data = []
    for item in data_res:
        data_dict = {}
        for filed in item["_source"]:
            data_dict[filed] = item["_source"][filed]
        data.append(data_dict)
    result["data"] = data
    return result


def sql_get_pgsql(sql):
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
    except:
        cursor.close()
        raise Exception(u"查询数据库失败！没有得到想要查询到的信息！")
    return data


def send_email_on_code(msg_text, to_addr, from_addr="wangjianlin1985@126.com", password="DBZTRUCHIYSUTDUG"):
    '''

    :param msg_text:发送的邮件内容
    :param from_addr:发件账号
    :param password:发件账号的密码
    :param to_addr:收件箱
    :return:成功则返回"sucessful"
    '''
    to_addr = to_addr
    #to_addr = to_addr
    #msg_text = msg_text.encode("utf-8")
    msg_text = msg_text
    #from_addr = from_addr.encode("utf-8")
    from_addr = from_addr

    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    msg = MIMEText(msg_text, 'plain', 'utf-8')
    msg['From'] = _format_addr('小方<%s>' % from_addr)
    msg['To'] = _format_addr('尊贵的VIP用户<%s>' % to_addr)
    msg['Subject'] = Header('请输入验证码修改邮箱', 'utf-8').encode()
    # smtp服务器地址
    # smtp_server = "smtp.qq.com"
    try:
        smtp_server = "smtp.126.com"
        # server = smtplib.SMTP(smtp_server, 587)
        server = smtplib.SMTP(smtp_server, 25)
        #server.starttls()
        # server.set_debuglevel(1)
        server.login(from_addr, password)
        # 发送邮件
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
    except Exception as e:
        print(e)
    return "sucessful"
