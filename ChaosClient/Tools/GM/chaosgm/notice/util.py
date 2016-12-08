# coding=utf-8
import hashlib
import os
import re
import sys
import urllib
import urllib2
import uuid
import xml.etree.cElementTree as ET
from xml.dom import minidom
import paramiko
import chaosgm.settings
from gm.models import ServerGroup

path_name = "patchinfo.xml"


def get_notice_names(request):
    if hasattr(request.user, 'gm'):
        gm = request.user.gm
        out = []
        all_group = gm.manage_server_groups.all()
        for gr in all_group:
            out.append(gr.name)
        return out


def get_notice_path_by_severgroup_name(name):
    group = list(ServerGroup.objects.filter(name=name))[0]
    return group.url


def get_single_child_safe(node, name):
    children = node.getElementsByTagName(name)
    if children is None or len(children) <= 0:
        return None
    return children[0]


# 将style转化为RGB标签
# 技能特点：<&style:0xff00ff00-22-2-2-0xff0f0f14>持续AOE伤害、降低敌人命中、控制、召唤刺蛇可攻可抗<&/>!

RGB = [
    {'code': 'G', 'style': r'<&style:0xff00ff00-22-2-2-0xff0f0f14>'},
    {'code': 'R', 'style': r'<&style:0xff0000ff-22-2-2-0xff0f0f14>'},
    {'code': 'B', 'style': r'<&style:0xffff0000-22-2-2-0xff0f0f14>'},
]

style_reg = re.compile(r'<&style:.*?>')
end_reg = re.compile(r'<&/>')


def get_code_by_style(style_str):
    low_style_str = style_str.lower()
    for info in RGB:
        if info['style'] == low_style_str:
            return info['code']
    return RGB[0]['code']


def get_style_by_code(code):
    for info in RGB:
        if info['code'] == code:
            return info['style']


def sub_style_tag(m):
    title = m.group().title()
    code = get_code_by_style(title)
    return '[' + code + ']'


def sub_end_tag(m):
    return '[/]'


# style标签转为rgb
def decode_content_color(origin):
    ret = style_reg.sub(sub_style_tag, origin)
    ret = end_reg.sub(sub_end_tag, ret)
    return ret


reverse_style_reg = re.compile(r'\[[RGB]\]')
single_letter_reg = re.compile(r'\w')
reverse_end_reg = re.compile(r'\[/\]')


def sub_reverse_style_tag(m):
    title = m.group().title()
    letter = single_letter_reg.findall(title)[0]
    return get_style_by_code(letter)


def sub_reverse_end_tag(m):
    return '<&/>'


def encode_rgb_sentence(sentence):
    ret = reverse_style_reg.sub(sub_reverse_style_tag, sentence)
    ret = reverse_end_reg.sub(sub_reverse_end_tag, ret)
    return ret


def sub_rgb_sentence(m):
    title = m.group().title()
    return encode_rgb_sentence(title)


full_rgb_sentence = re.compile(r'\[[RGB]\][\s\S]*?\[/\]')


# rgb标签转为style
def encode_content_color(modify):
    return full_rgb_sentence.sub(sub_rgb_sentence, modify)


def get_notice_content(name):
    path = get_notice_path_by_severgroup_name(name) + path_name
    try:
        f = urllib2.urlopen(path)
    except:
        print("404 on url : " + path)
        return ""
    try:
        xmldoc = minidom.parse(f)
        f.close()
    except:
        print("error xml format : " + path)
        return ""

    root = xmldoc.documentElement
    announcement = get_single_child_safe(root, 'announcement')
    if announcement is None:
        return ""

    content_str = ""
    for i in range(0, 1000):
        title_node = get_single_child_safe(announcement, 'title_' + str(i))
        content_node = get_single_child_safe(announcement, 'content_' + str(i))
        if title_node == None or content_node == None:
            break

        title = title_node.firstChild.data
        content_str = content_str + title
        if not content_str.endswith('\n'):
            content_str += '\n'

        content = content_node.firstChild.data
        content = decode_content_color(content)
        content_str += content
        if not content_str.endswith('\n'):
            content_str += '\n'
            # 内容之后要再空一行
        content_str += '\n'
    return content_str


def execute_notice(server_group, content):
    if not server_group:
        raise Exception("server_group is nil")
    if not content:
        raise Exception("content is nil")
    uuid_file_path = create_uuid_temp_file_path()
    ret, reason = save_notice_str_2_xml(server_group, content, uuid_file_path)
    if ret:
        doUpPatchInfo(server_group, uuid_file_path)
        os.remove(uuid_file_path)
        return True, "ok"
    else:
        return False, reason


def create_uuid_temp_file_path():
    dir_path = os.path.join(chaosgm.settings.BASE_DIR, "tempfiles")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_name = uuid.uuid1().hex
    return os.path.join(dir_path, file_name + ".xml")


def save_notice_str_2_xml(name, notice_content, output_file_path):
    path = get_notice_path_by_severgroup_name(name) + path_name
    try:
        ret = urllib2.urlopen(path)
    except:
        print("404 on url : " + path)
        return False, "无法从" + path + "下载文件"
    try:
        tree = ET.parse(ret)
        ret.close()
    except:
        print("error xml format : " + path)
        return False, "" + path + "不是合法的xml文件"

        # 清除掉开头和结尾的空行
    notice_content = notice_content.strip()

    if len(notice_content) > chaosgm.settings.MAX_NOTICE_LEN:
        return False, "公告内容不得超过20000字"

    announcement = tree.find('announcement')
    announcement.clear()

    # 按空行分割
    tiles = re.split('\n\s*\n', notice_content)
    index = 0
    for tile in tiles:
        title_with_content = tile.split('\n', 1)
        if len(title_with_content) == 2:
            title = title_with_content[0]
            ET.SubElement(announcement, 'title_' + str(index)).text = title.strip()
            content = title_with_content[1]
            content = encode_content_color(content.strip())
            ET.SubElement(announcement, 'content_' + str(index)).text = content
            index = index + 1

    tree.write(output_file_path, encoding='utf-8', )
    return True, "ok"


USERNAME = "cdn"  # 用户名
PASSWD = "1234"  # 密码
PORT = 22


def scp(ip, port, username, passwd, src, tar):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, passwd, timeout=5)

        ftp = ssh.open_sftp()
        ftp.put(src, tar)
        ftp.close

        print '%s\tOK\n' % (ip)
        ssh.close()
    except Exception, detail:
        print '%s\tError' % (ip)
        print detail


public_key = "ucloudblueice@maplegame.cn1443493589000412522626"
private_key = "2b47e769882a3a86824cea59b456dd39e13d073d"


def _verfy_ac(params):
    items = params.items()
    # 请求参数串
    items.sort()
    # 将参数串排序

    params_data = ""
    for key, value in items:
        params_data = params_data + str(key) + str(value)
    params_data = params_data + private_key

    sign = hashlib.sha1()
    sign.update(params_data)
    signature = sign.hexdigest()
    return signature
    # 生成的Signature值


def doUpPatchInfo(dir_name, uuid_file_path):
    if dir_name is None:
        raise Exception("dir_name is None")

    src = uuid_file_path
    if not os.path.exists(src):
        raise Exception("Can not find file %s" % (src))

    tar = '/data/cdn/patches/' + dir_name + '/patchinfo.xml'
    print "Begin Up patchinfo %s ......" % (src)
    ip = '120.132.56.23'
    scp(ip, PORT, USERNAME, PASSWD, src, tar)
    refresh_url = 'http://zypatch.v5game.cn/' + dir_name + '/patchinfo.xml'
    try:
        params = {'Action': 'RefreshUcdnDomainCache', 'DomainId': 'ucdn-bwlju0',
                  'Type': 'file', 'UrlList.0': refresh_url,
                  'PublicKey': public_key,
                  }
        signature = _verfy_ac(params)
        params['Signature'] = signature
        params_url = urllib.urlencode(params)
        url = 'http://api.spark.ucloud.cn/'
        full_url = url + '?' + params_url
        data = urllib2.urlopen(full_url)
        print(data.read())
        data.close()
    except:
        import sys
        print sys.exc_info()[:2]
