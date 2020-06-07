from django.contrib.auth.base_user import (
    AbstractBaseUser, BaseUserManager,
)
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

###ADDED
from mkdata.models import Work
from django.contrib.postgres.fields import ArrayField


########


# User-related
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    email = models.EmailField(_('email address'), unique=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    twitter = models.CharField(_('Twitter'), max_length=50, blank=True)

    ###ADDED
    #Arrayfieldは使いにくそうだったのでTextfieldで代用しました。今後これを変更することはないと思います。
    work_like = models.TextField(default="".join(['0']*100000))

    #recommendする作品のid
    #unique:他のユーザとの被りを許すか。Falseなら許す。ユーザ名とかはTrue
    #null:空っぽでもいいか、ユーザ登録時に空っぽになるのでとりあえずTrueにしとく。Falseだとエラー
    #default=0:ということは働いてないらしいなこいつ？
    work_recommend = ArrayField(models.IntegerField(default=0), size=5,unique=False,null=True)

    #userが各idの漫画を読んだことがあるかどうかを判定。'0': 未判定, '1': 読んだことなし '2': あり '3':評価する予定（途中逃げの可能性あり） '4':isLast
    #一度'2'以上になった場合、ずっと'2'以上になる。
    work_read = models.TextField(default="".join(['0']*100000))

    ###データは入力済み？
    data_entered = models.BooleanField(default=False)
    ########

    ###過去に評価した事がある作品のidを格納
    work_evaluated = ArrayField(models.IntegerField(), size=100000,unique=False,null=True)

    ###work_evaluatedのi番目のidに対応するworkの評価値を格納
    work_evaluation = ArrayField(
        ArrayField(
            models.IntegerField(default=0),
            size=20,
            unique=False,
            null=True
        ),
        size=100000,
        default=list,
    )

    evaluation_avg = ArrayField(models.FloatField(default=0), size=20,unique=False,null=True,default=list)
    evaluation_std = ArrayField(models.FloatField(default=0), size=20,unique=False,null=True,default=list)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def __str__(self):
        return self.email

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

# for Recommendationを作りたい(あるいはUserの中に入れる)
