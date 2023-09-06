from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('username')  # Utiliser l'adresse email comme nom d'utilisateur
        if not email:
            raise ValueError(_('L\'adresse email doit être renseignée.'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Un superutilisateur doit avoir is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Un superutilisateur doit avoir is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = (
        ('user', 'Utilisateur'),
        ('manager', 'Manager'),
        ('admin', 'Admin'),
    )

    email = models.EmailField(_('adresse email'), unique=True)
    username = models.CharField(_('nom d\'utilisateur'), max_length=30, unique=True)
    role = models.CharField(_('rôle'), max_length=20, choices=USER_ROLE_CHOICES, default='user')

    objects = CustomUserManager()

    def __str__(self):
        return self.email

        def save(self, *args, **kwargs):
            if not self.username:
                self.username = self.email

        super().save(*args, **kwargs)


from django.contrib.auth import get_user_model


def is_admin(CustomUser):
    return CustomUser.role == 'admin' if CustomUser else False


User = get_user_model()
User.add_to_class('is_admin', is_admin)


class CustomUserPermissions(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    can_create_equipe = models.BooleanField(default=False)
    can_read_equipe = models.BooleanField(default=False)
    can_update_equipe = models.BooleanField(default=False)
    can_delete_equipe = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


# class CustomUserPermissions(models.Model):
# user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
# can_access_manager_functionality = models.BooleanField(default=False)
# can_access_employer_functionality = models.BooleanField(default=False)


# BasedModel

class BaseModel(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    imported_by = models.CharField(max_length=50, default=' Rhimi Thouraya')

    updated_by = models.CharField(max_length=30, default=' Rhimi Thouraya')

    class Meta:
        # Django will not create a database table for this model

        abstract = True


# creating a custom model manager to apply the filter

# automatically without using filter(is_delete=False)


# SoftDeleteManager

class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


# SoftDeleteModel

class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(null=False, default=False)

    deleted_by = models.CharField(max_length=30, null=True)

    deleted_at = models.DateTimeField(auto_now_add=True, null=True)

    restored_at = models.DateTimeField(auto_now=True, null=True)

    restored_by = models.CharField(max_length=30, default='Thouraya Rhimi  ', null=True)

    objects = models.Manager()

    undeleted_objects = SoftDeleteManager()

    def soft_delete(self):
        self.is_deleted = True

        self.save()

    def restore(self):
        self.is_deleted = False

        self.save()

    class Meta:
        # Django will not create a database table for this model

        abstract = True


class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=True)
    imported_by = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.id)


class FileMs(models.Model):
    article = models.CharField(max_length=50, null=True, blank=True)
    designation_article = models.CharField(max_length=50, null=True, blank=True)
    text_article = models.CharField(max_length=50, null=True, blank=True)
    grpe_march = models.CharField(max_length=50, null=True, blank=True)
    div = models.CharField(max_length=50, null=True, blank=True)
    ctrpr = models.CharField(max_length=50, null=True, blank=True)
    typ_app = models.CharField(max_length=50, null=True, blank=True)
    a_s = models.CharField(max_length=50, null=True, blank=True)
    tcy = models.CharField(max_length=50, null=True, blank=True)
    dfi = models.CharField(max_length=50, null=True, blank=True)
    dpr = models.CharField(max_length=50, null=True, blank=True)
    horiz = models.CharField(max_length=50, null=True, blank=True)
    mp = models.CharField(max_length=50, null=True, blank=True)
    r = models.CharField(max_length=50, null=True, blank=True)
    tyar = models.CharField(max_length=50, null=True, blank=True)
    nal = models.CharField(max_length=50, null=True, blank=True)
    i_c = models.CharField(max_length=50, null=True, blank=True)
    aappr_def = models.CharField(max_length=50, null=True, blank=True)
    mgapp = models.CharField(max_length=50, null=True, blank=True)
    mag = models.CharField(max_length=50, null=True, blank=True)
    tl = models.CharField(max_length=50, null=True, blank=True)
    lot_fixe = models.CharField(max_length=50, null=True, blank=True)
    uq1 = models.CharField(max_length=50, null=True, blank=True)
    stock_securite = models.CharField(max_length=50, null=True, blank=True)
    uq0 = models.CharField(max_length=50, null=True, blank=True)

    tre = models.CharField(max_length=50, null=True, blank=True)
    gest = models.CharField(max_length=50, null=True, blank=True)
    di = models.CharField(max_length=50, null=True, blank=True)
    rebut = models.CharField(max_length=50, null=True, blank=True)
    gac = models.CharField(max_length=50, null=True, blank=True)
    Profil = models.CharField(max_length=50, null=True, blank=True)
    prpiAt = models.CharField(max_length=50, null=True, blank=True)
    cree_par = models.CharField(max_length=50, null=True, blank=True)
    langue = models.CharField(max_length=50, null=True, blank=True)
    Cree_le = models.CharField(max_length=50, null=True, blank=True)
    gcha = models.CharField(max_length=50, null=True, blank=True)
    gs = models.CharField(max_length=50, null=True, blank=True)
    mode_de_comparaison_des_besoin = models.CharField(max_length=50, null=True, blank=True)
    int_ajust_amont = models.CharField(max_length=50, null=True, blank=True)
    int_ajust_aval = models.CharField(max_length=50, null=True, blank=True)
    taille_l_min = models.CharField(max_length=50, null=True, blank=True)
    uq2 = models.CharField(max_length=50, null=True, blank=True)
    val_arrondie = models.CharField(max_length=50, null=True, blank=True)
    uq3 = models.CharField(max_length=50, null=True, blank=True)
    taille_lot_mx = models.CharField(max_length=50, null=True, blank=True)
    uq4 = models.CharField(max_length=50, null=True, blank=True)
    stock_maximum = models.CharField(max_length=50, null=True, blank=True)
    uq5 = models.CharField(max_length=50, null=True, blank=True)
    chant = models.CharField(max_length=50, null=True, blank=True)
    typ = models.CharField(max_length=50, null=True, blank=True)
    delai_sec = models.CharField(max_length=50, null=True, blank=True)
    delai_sec1 = models.CharField(max_length=50, null=True, blank=True)
    ctrl_destinataire = models.CharField(max_length=50, null=True, blank=True)
    article_rempl = models.CharField(max_length=50, null=True, blank=True)
    dv = models.CharField(max_length=50, null=True, blank=True)
    gml = models.CharField(max_length=50, null=True, blank=True)
    grpl = models.CharField(max_length=50, null=True, blank=True)
    abc = models.CharField(max_length=50, null=True, blank=True)
    uq6 = models.CharField(max_length=50, null=True, blank=True)
    element_dOTP = models.CharField(max_length=50, null=True, blank=True)
    grpa = models.CharField(max_length=50, null=True, blank=True)
    Code_pilotage = models.CharField(max_length=50, null=True, blank=True)
    hierarch_produits = models.CharField(max_length=50, null=True, blank=True)
    poids_brut = models.CharField(max_length=50, null=True, blank=True)
    unp1 = models.CharField(max_length=50, null=True, blank=True)
    poids_net = models.CharField(max_length=50, null=True, blank=True)
    unp2 = models.CharField(max_length=50, null=True, blank=True)
    pas_de_ccr = models.CharField(max_length=50, null=True, blank=True)
    Taille_de_lot_du_CCR = models.CharField(max_length=50, null=True, blank=True)
    uq7 = models.CharField(max_length=50, null=True, blank=True)
    file_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.article


class rute(BaseModel, SoftDeleteModel, models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class condition(models.Model):
    field = models.CharField(max_length=50, null=True, blank=True)
    Con = models.CharField(max_length=50, null=True, blank=True)
    id_rute = models.ForeignKey(rute, on_delete=models.CASCADE)


class resulta(models.Model):
    field = models.CharField(max_length=50, null=True, blank=True)
    Res = models.CharField(max_length=50, null=True, blank=True)
    id_condition = models.ForeignKey(condition, on_delete=models.CASCADE)


class lm(models.Model):
    field = models.CharField(max_length=50, null=True, blank=True)
    vieux = models.CharField(max_length=50, null=True, blank=True)
    nouveau = models.CharField(max_length=50, null=True, blank=True)
    id_condition = models.ForeignKey(condition, on_delete=models.CASCADE)
    id_ligne = models.ForeignKey(FileMs, null=True, on_delete=models.CASCADE)
    id_file = models.ForeignKey(File, null=True, on_delete=models.CASCADE)


class EquipeMS(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    Phone = models.IntegerField()

    def __str__(self):
        return self.name


class ChatMessage(models.Model):
    text = models.TextField()
    is_user = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
