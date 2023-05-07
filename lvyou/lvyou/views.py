# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from base.models.new_user import NewUser
from django.contrib.auth.models import User
from base.models.temp_tel_code import TempTelCode
from hashlib import sha1
# import urllib2
import json, random, datetime, uuid, urllib, hmac, base64, requests, urllib, sys, traceback

try:
    from django.apps import apps as models
except ImportError:  # django < 1.7
    from django.db import models


def index(request):
    return render(request, 'index.html')


def get_login(request):
    '''
    获取登陆页
    :param request:
    :return:
    '''
    return render(request, 'login.html')


def alogin(request):
    '''
    登陆页面
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    method = request.method.lower()
    if method == 'get':
        pass
    if method == 'post':
        username = request.POST['username']
        password = request.POST['password']

        # try:
        #     user1 = User.objects.get(username=username)
        #     if hasattr(user1, 'newuser'):
        #         # 说明有扩展的用户信息
        #         pass
        # except:
        #     return render(request, 'login.html', {'user_msg': u"账户不存在"})

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'login.html', {"active_msg": u'账户被禁用'})
        else:
            return render(request, 'login.html', {"psd_msg": u'密码错误'})


def loginout(request):
    '''
    退出登录页
    :param request:
    :return:
    '''
    logout(request)
    return render(request, 'index.html')


def to_register(request):
    return render(request, 'register.html')


def register(request):
    method = request.method.lower()
    if method == 'get':
        telephone = request.GET.get("telephone")
        if not telephone:
            return render(request, 'register.html', {"telephone": u"请输入手机号"})
        auth_code = str(random.randint(100000, 999999))
        time_stamp = datetime.datetime.utcnow().isoformat().split(".")[0] + "Z"
        signa_ture_nonce = str(uuid.uuid1())
        arg_dict = {
            "Action": "SingleSendSms",
            "SignName": "沐沐",
            "TemplateCode": "SMS_19770017",
            "RecNum": "13298183005",
            "ParamString": {"verifycode": auth_code},
            "Format": "JSON",
            "Version": "2016-09-27",
            "AccessKeyId": "MmU1eqySC9VE78nj",
            "SignatureMethod": "HMAC-SHA1",
            "Timestamp": time_stamp,
            "SignatureVersion": "1.0",
            "SignatureNonce": signa_ture_nonce,
        }

        def _decode_dict(data):
            rv = {}
            for key, value in data.iteritems():
                if isinstance(key, unicode):
                    key = key.encode('utf-8')
                if isinstance(value, unicode):
                    value = value.encode('utf-8')
                elif isinstance(value, list):
                    value = _decode_list(value)
                elif isinstance(value, dict):
                    value = _decode_dict(value)
                rv[key] = value
            return rv

        arg_dict = json.dumps(arg_dict).encode("utf8")
        arg_dict = json.loads(arg_dict, object_hook=_decode_dict)
        p_url = urllib.urlencode(arg_dict)
        string_to_sign = "GET" + "&" + urllib.quote("/", safe='') + "&" + p_url
        sha1_sign = hmac.new("TsyaOU7PxpCipNPwryqF9E3OpBLwAD&", string_to_sign, sha1).digest()
        signa_ture = base64.b64encode(sha1_sign)
        signa_ture = "Signature=" + urllib.quote(signa_ture, safe='')
        url_body = signa_ture + "&" + p_url
        url = "https://sms.aliyuncs.com/?" + url_body
        res = requests.session().get(url).content
        es_res = json.loads(res)
        url


    elif method == 'post':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            return render(request, 'register.html', {"password": u"两次密码不一致"})
        elif username == '' or password1 == "" or password2 == "":
            return render(request, 'register.html', {"password": u"登录名或者密码不能为空"})
        try:
            User.objects.get(username=username)
            return render(request, 'register.html', {"username": u"用户名已存在"})
        except:
            userobj = User.objects.create_user(username=username, password=password1)
            user = authenticate(username=username, password=password1)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                return render(request, 'index.html')


def get_tel_code(request):
    result = {}
    try:
        tel = request.POST.get("username")
        action = request.POST.get("action")
        try:
            tel = int(tel)
        except:
            raise Exception("手机号码有误！")
        code = int(random.uniform(100000, 999999))
        if action == "login":
            try:
                new_obj = NewUser.objects.get(telephone=tel)
                new_obj.auth_code = code
                new_obj.save()
            except:
                raise Exception("没有该手机号")
        else:
            new_obj = TempTelCode.objects.update_or_create(code=code, telphone=tel)

        method = request.method
        host = 'http://sms.market.alicloudapi.com'
        path = '/singleSendSms'
        method = 'GET'
        appcode = '95fd37d3051e4718a9c0689b5f961566'
        ParamString = '{"code":"%s"}' % str(code)
        phone = str(tel)
        SignName = '小方'
        TemplateCode = 'SMS_63795887'
        querys = 'ParamString=%s&RecNum=%s&SignName=%s&TemplateCode=%s' % (ParamString, phone, SignName, TemplateCode)
        bodys = {}
        url = host + path + '?' + querys
        req = urllib2.Request(url)
        req.add_header('Authorization', 'APPCODE ' + appcode)
        response = urllib2.urlopen(req)
        content = response.read()
        content = json.loads(content)
        if (content["success"] == True):
            result["sucess"] = True
    except Exception as e:
        _trackback = traceback.format_exc()
        err_msg = e.message
        if not err_msg and hasattr(e, 'faultCode') and e.faultCode:
            err_msg = e.faultCode
        result['error_msg'] = err_msg
        result['trackback'] = _trackback
    finally:
        return HttpResponse(json.dumps(result))
