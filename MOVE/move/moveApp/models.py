from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Clients(models.Model):
    SEXE_CHOICES = (
        (0, 'Homme'),
        (1, 'Femme'),
    )

    SIT_FAM_CHOICES = (
        (0, 'Célibataire'),
        (1, 'Marié(e)'),
    )

    PERSONNE_CHOICES = (
        (0, 'Morale'),
        (1, 'Physique'),
    )

    PIECE_IDENT_CHOICES = (
        (0, 'Carte d\'identité'),
        (1, 'Permis de conduire'),
    )

    codeClient = models.AutoField(primary_key=True, blank=True)
    codeAgenceClient = models.CharField(max_length=3)
    idClient = models.IntegerField()
    nomClient = models.CharField(max_length=30)
    preClient = models.CharField(max_length=30, null=True, blank=True)
    dateNaissanceClient = models.DateField()
    lieuNaissanceClient = models.CharField(max_length=50, null=True, blank=True)
    nationaliteClient = models.CharField(max_length=50)
    sexeClient = models.IntegerField(choices=SEXE_CHOICES, null=True, blank=True)
    adresse1Client = models.CharField(max_length=100)
    adresse2Client = models.CharField(max_length=100,blank=True, null=True)
    codePostal = models.DecimalField(max_digits=10, decimal_places=0)
    numTelClient = models.CharField(max_length=20)
    pereClient = models.CharField(max_length=30, null=True, blank=True)
    mereClient = models.CharField(max_length=80, null=True, blank=True)
    dateAjoutClient = models.DateField()
    situationFamiliale = models.IntegerField(choices=SIT_FAM_CHOICES, blank=True, null=True)
    typePersonneClient = models.IntegerField(choices=PERSONNE_CHOICES)
    professionClient = models.CharField(max_length=50, null=True, blank=True)
    activiteClient = models.CharField(max_length=50, null=True, blank=True)
    gerantClient = models.CharField(max_length=80, null=True, blank=True)
    clientResideDZ = models.BooleanField()
    pieceIdentClient = models.IntegerField(choices=PIECE_IDENT_CHOICES)
    dateDelivrancePieceIdent = models.DateField()
    lieuDelivrancePieceIdent = models.CharField(max_length=100)
    numRegistreCommerceClient = models.PositiveBigIntegerField(null=True, blank=True)
    clientPresume = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    nbrModifInfoClient = models.PositiveBigIntegerField()

    class Meta:
        unique_together = ('codeAgenceClient', 'idClient')

class GrandLivres(models.Model):
    SENS_OPER_CHOICES = (
        (0, 'Débit'),
        (1, 'Crédit'),
        (2, 'Débit/Crédit'),
    )

    idGL = models.IntegerField(primary_key=True)
    libelleGL = models.CharField(max_length=200)
    sensOperation = models.IntegerField(choices=SENS_OPER_CHOICES)
    GLSusp = models.BooleanField()

class UtilisateursManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None,  **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('UtilSusp', False)

        return self.create_user(username, password, **extra_fields)


class Utilisateurs(AbstractBaseUser, PermissionsMixin):
    NIVEAU_CHOICES = (
        (0, 'Simple'),
        (1, 'Administrateur'),
    )

    idUtil = models.AutoField(primary_key=True)
    nomUtil = models.CharField(max_length=30, blank=False)
    preUtil = models.CharField(max_length=30, blank=False)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    UtilSusp = models.BooleanField(default=False)
    nivUtil = models.IntegerField(choices=NIVEAU_CHOICES, null=True, blank=False)
    serviceUtil = models.CharField(max_length=100, null=True, blank=False)
    dateCreUtil = models.DateField(null=True, blank=False)
    heureCreUtil = models.TimeField(null=True, blank=False)
    derniereOperUtil = models.DateTimeField(null=True, blank=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UtilisateursManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username


class Operations(models.Model):
    numOperation = models.IntegerField(primary_key=True)
    libelleOperation = models.CharField(max_length=200)

class Comptes(models.Model):
    numeroCompte = models.AutoField(primary_key=True)
    dateCreationCompte = models.DateField()
    soldeCourant = models.PositiveBigIntegerField(null=True)
    soldeHier = models.PositiveBigIntegerField(null=True, blank=True)
    dateDerniereOperation = models.DateField(blank=True, null=True)
    compteEnOpposition = models.BooleanField()
    dateMiseEnOpposition = models.DateField(null=True, blank=True)
    dateFermetureCompte = models.DateField(null=True, blank=True)
    client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING , related_name='comptes_client')
    GL = models.ForeignKey(GrandLivres, on_delete=models.DO_NOTHING )

class Mouvements(models.Model):
    numMouvement = models.AutoField(primary_key=True)
    numTransaction = models.IntegerField()
    montantMouvement = models.PositiveBigIntegerField()
    dateMouvement = models.DateField()
    heureTransaction = models.TimeField()
    libelleTransaction = models.CharField(max_length=200, null=True)
    RIB = models.CharField(max_length=200)
    utilIntro = models.ForeignKey(Utilisateurs, on_delete=models.DO_NOTHING, related_name='mouvements_intro')
    utilValid = models.ForeignKey(Utilisateurs, on_delete=models.DO_NOTHING, related_name='mouvements_valid', null=True, blank=True)
    operation = models.ForeignKey(Operations, on_delete=models.DO_NOTHING)
    compte = models.ForeignKey(Comptes, on_delete=models.DO_NOTHING)
    GL = models.ForeignKey(GrandLivres, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        unique_together = ('numTransaction', 'compte', 'GL')