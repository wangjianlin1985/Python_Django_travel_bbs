# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.shortcuts import render
from django.db.models.query_utils import Q
from community.models.topic_text import TopicText
from community.models.forum_sort import ForumSort
from base.models.sys_material import SysMaterial
from community.models.comment import Comment
from community.models.guan_zhu import Guan_Zhu
from community.models.collect_comment import CollectComment

from django.db import models
import base.views.base_views as base_view

get_user_data = base_view.UserView().get_user_data

import json, traceback, pytz, math

# Create your views here.

try:
    from django.apps import apps
except ImportError:  # django < 1.7
    from django.db import models as apps


class Community(object):
    def get_questions(self, sort_id, page, sort_field, user_id):
        page_obj = SysMaterial.objects.filter(key="comm_page_size")
        page_size = int(page_obj[0].value) if page_obj else 10
        order_field = "-write_date"
        filter_str = {'u_public': True, "a_public": True}
        try:
            page = int(page)
        except:
            pass
        if sort_id != "all":
            try:
                sort_id = int(sort_id)
                if sort_id in self.sort_ids:
                    filter_str["forum_sort_id"] = sort_id
            except:
                pass
        text_obj = TopicText.objects.filter(Q(**filter_str)).order_by("priority").order_by(order_field)[
                   page * page_size:(page + 1) * page_size]
        q_count = TopicText.objects.filter(Q(**filter_str)).count()
        page_number = int(math.ceil(float(q_count) / page_size))

        user_ids = []
        text_ids = []
        for item in text_obj:
            text_ids.append(item.id)
            user_ids.append(item.write_user_id)
        user_data = get_user_data(user_ids)

        guanzhu_obj = Guan_Zhu.objects.filter(gz_user_id=user_id, topic_id__in=text_ids)
        guanzhu_ids = []
        for item in guanzhu_obj:
            guanzhu_ids.append(item.topic_id)

        # 获取评论个数
        com_number = {}
        com_obj = Comment.objects.filter(parent_id__in=text_ids).values("parent_id").annotate(Count('parent_id'))
        for item in com_obj:
            com_number[item["parent_id"]] = item["parent_id__count"]

        # 评论数量还没有
        questions = []
        for item in text_obj:
            text_txt = item.text_txt[:150] if item.text_txt else ""
            new_date = item.write_date.astimezone(pytz.timezone('Asia/Shanghai'))
            write_date = str(new_date)[:19]
            write_user = user_data[item.write_user_id]
            show_name = write_user["show_name"] if "show_name" in write_user else write_user["username"]
            com_numb = com_number[item.id] if item.id in com_number else 0
            q_dict = {
                "id": item.id,
                "title": item.name,
                "text_htm": item.text_htm,
                "text_txt": text_txt,
                "pviews": item.pviews,
                "collection": item.collection,
                "write_date": write_date,
                "show_name": show_name,
                "com_numb": com_numb,
                "guan_zu": "yes" if item.id in guanzhu_ids else "no",
                "signatrue": write_user["signatrue"],
            }
            questions.append(q_dict)
        return questions, page_number

    def get_community(self, request, *args, **kwargs):
        sort = kwargs.get("sort")
        page = kwargs.get("page")
        request.GET.sort = sort
        request.GET.page = page
        sort_obj = ForumSort.objects.all()
        self.sort_obj = sort_obj
        edit_box = []
        default_sort = u"没有分类可以选择"
        if sort_obj:
            default_sort = sort_obj[0].id
        sort_ids = []
        for item in sort_obj:
            sort_ids.append(item.id)
            edit_dict = {
                "name": item.name,
                "id": item.id
            }
            edit_box.append(edit_dict)
        self.sort_ids = sort_ids
        if request.user.is_active:
            user_data = get_user_data(request.user)
        # questions = self.get_questions(sort, page)
        context = {
            'edit_box': edit_box,
            'default_sort': default_sort,
            # 'questions': questions
        }
        return render(request, 'community.html', context)

    def get_question_list(self, request):
        sort_id = request.GET.get("sort")
        page = request.GET.get("page")
        sort_f = request.GET.get("sort")
        u_id = request.user.id
        questions, page_number = self.get_questions(sort_id, page, sort_f, u_id)
        context = {
            'questions': questions,
            "page": page,
            "page_number": page_number if page_number != 0 else 1,
        }
        return render(request, 'question_list.html', context)

    def _get_commit_list(self, page, page_size, filter_str, order_str):
        if not order_str:
            order_str = "write_date"
        page_start = page - 1
        page_end = page_size * page + page - 2
        if not filter_str:
            comm_obj = TopicText.objects.filter(Q(**{"a_public": True})).order_by("priority").order_by(order_str)[
                       page_start: page_end]
        else:
            comm_obj = TopicText.objects.filter(Q(**filter_str) & Q(**{"a_public": True})).order_by(
                "priority").order_by(order_str)[page_start: page_end]
        comm_list = []
        icon_obj = SysMaterial.objects.get(key='user_default_icon_path')
        icon_path = icon_obj.value
        for item in comm_obj:
            comm_dict = {}
            comm_dict["user_icon"] = icon_path
            if item.write_user:
                user = item.write_user
                if isinstance(item.write_user, models.Model):
                    pass  # 如果用户头像存在则改变头像
            comm_dict["name"] = item.name
            comm_dict["text"] = item.text
            comm_dict["id"] = item.id
            comm_dict['date'] = item.write_date
            comm_dict['collection'] = item.collection
            comm_dict['pviews'] = item.pviews
            comm_dict['sort_id'] = item.forum_sort_id
            comm_dict['user'] = user
            comm_list.append(comm_dict)
        return comm_list

    def get_probem_list(self, request, *args, **kwargs):
        category = kwargs.get("category")
        action = kwargs.get("action")

    # @method_decorator(login_required)
    def create(self, request):
        method = request.method.lower()
        if method == 'post':
            result = {}
            try:
                if request.user.is_authenticated:
                    comm_sort = request.POST.get("question_sort")
                    comm_text = request.POST.get("question_main_text")
                    comm_html = request.POST.get("question_main_html")
                    comm_title = request.POST.get("question_title").strip()
                    if not comm_sort:
                        raise Exception("请选择分类")
                    if not comm_text:
                        raise Exception("请输入内容")
                    if not comm_title:
                        raise Exception("输入标题")
                    new_obj = TopicText(
                        name=comm_title,
                        text_txt=comm_text,
                        text_htm=comm_html,
                        forum_sort_id=comm_sort,
                        create_user=request.user,
                        write_user=request.user
                    )
                    TopicText.objects.bulk_create([new_obj])
                    result["successful"] = True
                    result["title"] = comm_title.encode("utf-8")
                else:
                    result['next'] = '/login/'
            except Exception as e:
                _trackback = traceback.format_exc()
                err_msg = e.message
                if not err_msg and hasattr(e, 'faultCode') and e.faultCode:
                    err_msg = e.faultCode
                result['error_msg'] = err_msg
                result['trackback'] = _trackback
            finally:
                return HttpResponse(json.dumps(result))

    def sort_comm_list(self, request, *args, **kwargs):
        result = {}
        sort = kwargs.get("sort")
        page = kwargs.get("page")
        try:
            sort = int(sort)
            page = int(page)
        except:
            return HttpResponseRedirect('404.html')
        size_obj = SysMaterial.objects.filter(key="sort_page_size")
        page_size = int(size_obj[0].value) if size_obj else 10
        filter_str = {"forum_sort_id": sort}
        comm_list = self._get_commit_list(page, page_size, filter_str, None)

        context = {
            'comm_list': comm_list,
        }
        return render(request, 'topic_text_list.html', context)

    def view_topic_text(self, request, *args, **kwargs):
        topic_id = kwargs.get("topic")
        text = {}
        text_obj = TopicText.objects.filter(id=topic_id)
        if not request:
            return HttpResponseRedirect('404.html')
        # 文章信息
        text_obj = text_obj[0]
        text["title"] = text_obj.name
        text["text"] = text_obj.text_htm
        text["collection"] = text_obj.collection  # 收藏
        if Guan_Zhu.objects.filter(topic_id=text_obj.id, gz_user_id=request.user.id).exists():
            text["action"] = "yes"
        else:
            text["action"] = "no"

        comm_obj = Comment.objects.filter(parent_id=text_obj.id, parent_type="TopicText", is_active=True,
                                          parent_comment=None).order_by("write_date")
        sc_obj = CollectComment.objects.filter(topic__in=comm_obj, user_id=request.user.id)
        collects = []
        for item in sc_obj:
            collects.append(item.topic_id)
        u_ids = [request.user.id]
        for item in comm_obj:
            u_ids.append(item.write_user_id)
        # 根据id获得关于user的数据：{2: {'username': u'test1', 'user_path': u'/static/media/icon/sysicon/yangwangtiankong.jpg', 'show_name': u'\u4f1a\u98de\u7684\u732a', 'telephone': None, 'signatrue': u'\u8fd9\u5bb6\u4f19\u5f88\u61d2\uff0c\u4ec0\u4e48\u90fd\u6ca1\u8bf4', 'send_date': None, 'auth_code': None}}
        user_data = get_user_data(u_ids)

        sum_comment = len(comm_obj)
        comm_list = []
        l1_comment_ids = []
        for item in comm_obj:
            # 通过循环组装一级评论
            u_id = item.write_user_id
            l1_comment_ids.append(item.id)
            comm_dict = {"content": item.content}
            comm_dict["id"] = item.id
            if "show_name" in user_data[u_id]:
                user_name = user_data[u_id]["show_name"]
            else:
                user_name = user_data[u_id]["username"]
            comm_dict["user_name"] = user_name
            comm_dict["user_icon"] = user_data[u_id]["user_path"]
            new_date = item.write_date.astimezone(pytz.timezone('Asia/Shanghai'))
            comm_dict["write_date"] = str(new_date)[:19]
            if item.id in collects:
                comm_dict["collects"] = True
            else:
                comm_dict["collects"] = False
            comm_list.append(comm_dict)

        count_l2_obj = Comment.objects.filter(parent_comment__in=l1_comment_ids).values("parent_comment").annotate(
            Count('parent_comment'))
        # 获取子评论数
        count_comment = {}
        for item in count_l2_obj:
            count_comment[item["parent_comment"]] = item["parent_comment__count"]
        # 把子评论数写入到模板参数中
        for item in comm_list:
            if item["id"] in count_comment:
                item["sub_number"] = count_comment[item["id"]]
            else:
                item["sub_number"] = 0

        # 当前用户的一些信息
        # TODO:当用户没有登录的时候，
        if request.user.is_active:
            u_id = request.user.id
            text["user_icon"] = user_data[u_id]["user_path"]
            text["user_name"] = user_data[u_id]["show_name"] if "show_name" in user_data[u_id] else \
                user_data[u_id][
                    "username"]

        context = {
            "text": text,
            "parent_type": "TopicText",
            "parent_id": text_obj.id,
            "comm_list": comm_list,
            "sum_comment": sum_comment,
        }
        return render(request, "topic_text_view.html", context)

    def create_focus(self, request):
        result = {}
        try:
            m_id = request.GET.get("munity_id")
            u_id = request.user.id
            obj = Guan_Zhu.objects.filter(topic_id=m_id, gz_user_id=u_id).exists()
            result["munity_id"] = m_id
            if obj:
                Guan_Zhu.objects.filter(topic_id=m_id, gz_user_id=u_id).delete()
                result["action"] = "close"
            else:
                Guan_Zhu.objects.create(topic_id=m_id, gz_user_id=u_id, create_user_id=u_id, write_user_id=u_id)
                result["action"] = "create"

        except Exception as e:
            _trackback = traceback.format_exc()
            err_msg = e.message
            if not err_msg and hasattr(e, 'faultCode') and e.faultCode:
                err_msg = e.faultCode
            result['error_msg'] = err_msg
            result['trackback'] = _trackback
        finally:
            return HttpResponse(json.dumps(result))

    def collect_comment(self, request):
        result = {}
        try:
            id = request.GET.get("id")
            u_id = request.user.id
            obj = CollectComment.objects.filter(topic_id=id, user_id=u_id).exists()
            result["id"] = id
            if obj:
                CollectComment.objects.filter(topic_id=id, user_id=u_id).delete()
                result["action"] = "closed"
            else:
                CollectComment.objects.create(topic_id=id, user_id=u_id, create_user_id=u_id, write_user_id=u_id)
                result["action"] = "created"

        except Exception as e:
            _trackback = traceback.format_exc()
            err_msg = e.message
            if not err_msg and hasattr(e, 'faultCode') and e.faultCode:
                err_msg = e.faultCode
            result['error_msg'] = err_msg
            result['trackback'] = _trackback
        finally:
            return HttpResponse(json.dumps(result))
