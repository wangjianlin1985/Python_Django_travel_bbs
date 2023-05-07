# -*- coding: utf-8 -*-
import os
from django.conf import settings
#from .models.forum_sort import ForumSort


class Sort(object):
    def __init__(self, model):
        super(Sort, self).__init__()
        self.model = model
        self.node_dict = {}
        self.data = [
            {'name': '综合交流', 'url': 'exchange',
             'describe': u'自从出了冰神，死神就有些堕落了。后来兽神又来了，死神几乎无用武之地。现在天神降临，死神....还有人记得这杆枪吗？我的死神该何去何从？死神是否需要再进化？'},
            {'name': '旅行心得', 'url': 'taste',
             'describe': u'自从出了冰神，死神就有些堕落了。后来兽神又来了，死神几乎无用武之地。现在天神降临，死神....还有人记得这杆枪吗？我的死神该何去何从？死神是否需要再进化？'},
            {'name': '杂谈', 'url': 'gossip',
             'describe': u'自从出了冰神，死神就有些堕落了。后来兽神又来了，死神几乎无用武之地。现在天神降临，死神....还有人记得这杆枪吗？我的死神该何去何从？死神是否需要再进化？'},
        ]

    def write_data(self):
        data = {}
        for item in self.data:
            name = item.get('name')
            data['url'] = item.get('url')
            data['describe'] = item.get('describe')
            new_obj = self.model.objects.get_or_create(name=name, defaults=data)[0]
            new_obj.save()


def make_data():
    from .models.forum_sort import ForumSort
    Sort(ForumSort).write_data()
