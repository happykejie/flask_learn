# -*- coding: UTF-8 -*-
import  MySQLdb
from app import  db
from datetime import datetime

# 定义数据模型类
# class User(db.Model):
#     # 不指定表名，默认会将大驼峰转换为：小写+下划线
#     # 如：类名UserModel => 表名user_model
#     # 指定表名，使用__tablename__属性
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(32), unique=True)
#     email = db.Column(db.String(64), unique=True)
class ApmUsers(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    user_login =db.Column(db.String(60))
    user_pass =db.Column(db.String(255))
    user_nicename =db.Column(db.String(50))
    user_email =db.Column(db.String(100))
    user_url =db.Column(db.String(1000))
    user_registered =db.Column(db.DateTime)
    user_activation_key =db.Column(db.String(255))
    user_status =db.Column(db.INTEGER)
    display_name =db.Column(db.VARCHAR(250))

    def __init__(self, ID,user_login, user_pass, user_nicename, user_email,user_url
                 ,user_activation_key,user_status,display_name,user_registered):
        self.ID =ID
        self.user_login = user_login
        self.user_pass = user_pass
        self.user_nicename = user_nicename
        self.user_email = user_email
        self.user_url = user_url
        self.user_activation_key = user_activation_key
        self.user_status =user_status
        self.display_name = display_name
        self.user_registered = user_registered

    def __repr__(self):
        return '<Apm_Users %r>' % self.user_login


class Apmuser(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)
    user_name =db.Column(db.String)
    user_nick = db.Column(db.String)

    def __init__(self,user_id,user_name,user_nick):
        self.user_id =user_id
        self.user_name =user_name
        self.user_nick = user_nick
    def __str__(self):
        return "id:{}--name:{}--nick:{}".format(self.user_id,self.user_name,self.user_nick)


class ApmTerms(db.Model):
    term_id = db.Column(db.BIGINT,primary_key=True)
    name =db.Column(db.String)
    slug = db.Column(db.String)
    term_group = db.Column(db.BIGINT)

    def __init__(self,term_id,name,slug,term_group):
        self.term_id =term_id
        self.name =name
        self.slug = slug
        self.term_group =term_group
    def __str__(self):
        return "term_id:{}--name:{}--slug{}--term_grop{}".format(self.term_id,self.name,self.slug,self.term_group)

class ApmCommentmeta(db.Model):
    meta_id = db.Column(db.BIGINT, primary_key=True)
    comment_id = db.Column(db.BIGINT)
    meta_key = db.Column(db.String)
    meta_value = db.Column(db.Text)

    def __init__(self, meta_id, comment_id, meta_key, meta_value):
        self.meta_id = meta_id
        self.comment_id = comment_id
        self.meta_key = meta_key
        self.meta_value = meta_value

    def __str__(self):
        return "meta_id:{}--comment_id:{}--meta_key{}--meta_value{}"\
            .format(self.meta_id, self.comment_id, self.meta_key, self.meta_value)

class ApmCommens(db.Model):
    comment_ID =db.Column(db.BIGINT,primary_key=True)
    comment_post_ID =db.Column(db.BIGINT)
    comment_author =db.Column(db.String)
    comment_author_url =db.Column(db.String)
    comment_author_IP =db.Column(db.String)
    comment_data =db.Column(db.Date)
    comment_data_gmt =db.Column(db.Date)
    comment_content =db.Column(db.Text)
    comment_karma =db.Column(db.INTEGER)
    comment_approvd =db.Column(db.String)
    comment_agent =db.Column(db.String)
    comment_type =db.Column(db.String)
    comment_parent =db.Column(db.BIGINT)
    user_id =db.Column(db.INTEGER)

    def __init__(self, meta_id, comment_id, meta_key, meta_value):
        self.meta_id = meta_id
        self.comment_id = comment_id
        self.meta_key = meta_key
        self.meta_value = meta_value

class ApmLinks(db.Model):
    link_id =db.Column(db.INTEGER,primary_key=True)
    link_url =db.Column(db.String)
    link_name =db.Column(db.String)
    link_image =db.Column(db.String)
    link_target =db.Column(db.String)
    link_description =db.Column(db.String)
    link_visible =db.Column(db.String)
    link_owner =db.Column(db.INTEGER)
    link_rating =db.Column(db.INTEGER)
    link_updated =db.Column(db.Date)
    link_rel =db.Column(db.String)
    link_notes =db.Column(db.Text)
    link_rss =db.Column(db.String)
    def __init__(self):
        pass

class ApmOptions(db.Model):
    option_id =db.Column(db.BIGINT,primary_key=True)
    option_name = db.Column(db.String)
    option_value = db.Column(db.Text)
    autoload = db.Column(db.String)
    def __init__(self):
        pass

class ApmPostmeta(db.Model):
    meta_id =db.Column(db.BIGINT,primary_key=True)
    post_id = db.Column(db.BIGINT)
    meta_key = db.Column(db.String)
    meta_value = db.Column(db.Text)
    def __init__(self):
        pass

class ApmPosts(db.Model):
    ID =db.Column(db.BIGINT,primary_key=True)
    post_author = db.Column(db.BIGINT)
    post_date = db.Column(db.Date)
    post_date_gmt = db.Column(db.Date)
    post_content =db.Column(db.TEXT)
    post_title =db.Column(db.TEXT)
    post_excerpt =db.Column(db.TEXT)
    post_status =db.Column(db.String)
    post_password =db.Column(db.String)
    post_name =db.Column(db.String)
    to_ping =db.Column(db.TEXT)
    pinged =db.Column(db.TEXT)
    post_modified =db.Column(db.Date)
    post_modified_gmt =db.Column(db.Date)
    post_content_filtered =db.Column(db.Text)
    post_parent =db.Column(db.BIGINT)
    guid =db.Column(db.String)
    menu_order =db.Column(db.INTEGER)
    post_type =db.Column(db.String)
    post_mime_type =db.Column(db.String)
    comment_count =db.Column(db.INTEGER)

    def __init__(self):
        pass


class ApmSmushDirImanges(db.Model):
    id =db.Column(db.BIGINT,primary_key=True)
    path = db.Column(db.Text)
    resize = db.Column(db.String)
    lossy = db.Column(db.String)
    error =db.Column(db.String)
    image_size =db.Column(db.INTEGER)
    orig_size =db.Column(db.INTEGER)
    file_time =db.Column(db.INTEGER)
    last_scan =db.Column(db.String)
    meta =db.Column(db.Text)


    def __init__(self):
        pass

class ApmTermRelationships(db.Model):
    object_id =db.Column(db.BIGINT,primary_key=True)
    tem_taxonomy_id =db.Column(db.BIGINT,primary_key=True)
    term_order = db.Column(db.INTEGER)


    def __init__(self):
        pass


class ApmTermTaxonomy(db.Model):
    term_taxonomy_id = db.Column(db.BIGINT, primary_key=True)
    term_id = db.Column(db.INTEGER)
    taxonomy = db.Column(db.String)
    description = db.Column(db.Text)
    parent = db.Column(db.INTEGER)
    count = db.Column(db.INTEGER)
    def __init__(self):
        pass


class ApmTermmeta(db.Model):
    meta_id = db.Column(db.BIGINT, primary_key=True)
    term_id = db.Column(db.INTEGER)
    mate_key = db.Column(db.String)
    meta_value = db.Column(db.Text)

    def __init__(self):
        pass


class ApmUsermeta(db.Model):
    umeta_id = db.Column(db.BIGINT, primary_key=True)
    user_id = db.Column(db.INTEGER)
    mate_key = db.Column(db.String)
    meta_value = db.Column(db.Text)

    def __init__(self):
        pass

class MidoksWeixinRobot(db.Model):
    id = db.Column(db.BIGINT, primary_key=True)
    wxfrom = db.Column(db.String)
    to = db.Column(db.String)
    msgid = db.Column(db.String)
    msgtype = db.Column(db.String)
    createtime = db.Column(db.String)
    content = db.Column(db.String)
    picurl = db.Column(db.String)
    location_x = db.Column(db.Float)
    location_y = db.Column(db.Float)
    scale = db.Column(db.Float)
    label = db.Column(db.String)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    url = db.Column(db.String)
    event = db.Column(db.String)
    eventkey = db.Column(db.String)
    format = db.Column(db.String)
    recognition = db.Column(db.String)
    mediaid = db.Column(db.String)
    thumbmediaid = db.Column(db.String)
    response = db.Column(db.String)
    response_time = db.Column(db.String)


    def __init__(self):
        pass


class MidoksWeixinRobotExtends(db.Model):
    id =db.Column(db.INTEGER,primary_key=True)
    ext_name =db.Column(db.String)
    ext_type =db.Column(db.String)
    ext_sort =db.Column(db.INTEGER)
    ext_int = db.Column(db.INTEGER)

    def __init__(self):
        pass

class MidoksWeixinRobotMenu(db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    menu_name =db.Column(db.String)
    menu_type =db.Column(db.String)
    menu_key =db.Column(db.Text)
    menu_callback =db.Column(db.String)
    menu_sort =db.Column(db.INTEGER)
    pid =db.Column(db.INTEGER)

    def __init__(self):
        pass
class MidoksWeixinRobotReply(db.Model):
    id =db.Column(db.BIGINT,primary_key=True)
    keyword =db.Column(db.String)
    reply =db.Column(db.Text)
    status =db.Column(db.String)
    time =db.Column(db.Date)
    type =db.Column(db.String)
    sort =db.Column(db.INTEGER)
    def __init__(self):
        pass

class WechatSubscribersLiteHistory(db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    openid = db.Column(db.String)
    keyword = db.Column(db.String)
    is_match =db.Column(db.String)
    time = db.Column(db.Date)

    def __init__(self):
        pass









