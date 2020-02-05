# coding:utf8
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, PasswordField, TextAreaField, FileField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, ValidationError
from app.models import User


class RegistForm(FlaskForm):
    name = StringField(
        label="昵称",
        validators=[
            DataRequired("请输入昵称！")
        ],
        description="昵称",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入昵称！",
            # "required": "required"
        }
    )
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("请输入邮箱！"),
            Email("邮箱格式不正确")
        ],
        description="邮箱",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入邮箱！",
            # "required": "required"
        }
    )
    phone = StringField(
        label="手机",
        validators=[
            DataRequired("请输入手机！"),
            # Regexp("d[11]", message="手机格式不正确")
        ],
        description="手机",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入手机！",
            # "required": "required"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入密码！",
            "required": "required"
        }
    )
    repwd = PasswordField(
        label="确认密码",
        validators=[
            DataRequired("请输入确认密码！"),
            EqualTo('pwd', message="两次密码不一致")
        ],
        description="确认密码",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入确认密码！",
        }
    )
    submit = SubmitField(
        '注册',
        render_kw={
            "class": "btn btn-lg btn-success btn-block"
        }

    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError("昵称已存在")

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError("邮箱已存在")

    def validate_name(self, field):
        phone = field.data
        user = User.query.filter_by(phone=phone).count()
        if user == 1:
            raise ValidationError("手机已存在")


class LoginForm(FlaskForm):
    name = StringField(
        label="账号",
        validators=[
            DataRequired("请输入账号！")
        ],
        description="账号",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入账号！",
            # "required": "required"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入密码！",
            "required": "required"
        }
    )
    submit = SubmitField(
        '登陆',
        render_kw={
            "class": "btn btn-lg btn-primary btn-block"
        }

    )


class UserdatailForm(FlaskForm):
    name = StringField(
        label="昵称",
        validators=[
            DataRequired("请输入昵称！")
        ],
        description="昵称",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入昵称！",
            # "required": "required"
        }
    )
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("请输入邮箱！"),
            Email("邮箱格式不正确")
        ],
        description="邮箱",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！",
            # "required": "required"
        }
    )
    phone = StringField(
        label="手机",
        validators=[
            DataRequired("请输入手机！"),
            # Regexp("d[11]", message="手机格式不正确")
        ],
        description="手机",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机！",
            # "required": "required"
        }
    )
    face = FileField(
        label="头像",
        validators=[
            DataRequired("请上传头像")
        ],
        description="头像"
    )
    info = TextAreaField(
        label="简介",
        validators=[
            DataRequired("请输入简介")
        ],
        description="简介",
        render_kw={
            "class": "form-control",
            "rows": 10
        }
    )
    submit = SubmitField(
        "保存修改",
        render_kw={
            "class": "btn btn-success"
        }
    )


class PwdForm(FlaskForm):
    old_pwd = PasswordField(
        label="旧密码",
        validators=[
            DataRequired("请输入旧密码")
        ],
        description="旧密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入旧密码"
        }
    )
    new_pwd = PasswordField(
        label="新密码",
        validators=[
            DataRequired("请输入新密码")
        ],
        description="新密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入新密码"
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn_success"
        }
    )


class CommentForm(FlaskForm):
    content = TextAreaField(
        label="内容",
        validators=[
            DataRequired("请输入内容")
        ],
        description="内容",
        render_kw={
            "id": "input_content"
        }
    )
    submit = SubmitField(
        '提交评论',
        render_kw={
            "class": "btn btn-success",
            "id": "btn-sub"
        }
    )