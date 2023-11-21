from django.http import JsonResponse, HttpResponse
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout
from .models import Clients, Comptes, Mouvements, GrandLivres, Operations

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Nom d\'utilisateur ou mot de passe invalide.'})
        
def logout_view(request):
    logout(request)
    return JsonResponse({'success': True})

def get_liste_clients(request):
    clients = Clients.objects.all()
    data = []
    for client in clients:
        date_naissance = client.dateNaissanceClient.strftime('%d-%m-%Y') if client.dateNaissanceClient else None
        date_ajout = client.dateAjoutClient.strftime('%d-%m-%Y') if client.dateAjoutClient else None
        date_delivrance = client.dateDelivrancePieceIdent.strftime('%d-%m-%Y') if client.dateDelivrancePieceIdent else None
        client_data = {
            'codeAgenceClient': client.codeAgenceClient,
            'idClient': client.idClient,
            'nomClient': client.nomClient,
            'preClient': client.preClient,
            'dateNaissanceClient': date_naissance,
            'lieuNaissanceClient': client.lieuNaissanceClient,
            'nationaliteClient': client.nationaliteClient,
            'sexeClient': client.get_sexeClient_display(),
            'adresse1Client' : client.adresse1Client,
            'adresse2Client' : client.adresse2Client,
            'codePostal': client.codePostal,
            'numTelClient' : client.numTelClient,
            'pereClient' : client.pereClient,
            'mereClient' : client.mereClient,
            'situationFamiliale' : client.get_situationFamiliale_display(),
            'dateAjoutClient' : date_ajout,
            'typePersonneClient' : client.get_typePersonneClient_display(),
            'professionClient' : client.professionClient,
            'activiteClient' : client.activiteClient,
            'gerantClient' : client.gerantClient,
            'clientResideDZ' : client.clientResideDZ,
            'pieceIdentClient' : client.get_pieceIdentClient_display(),
            'dateDelivrancePieceIdent' : date_delivrance,
            'lieuDelivrancePieceIdent' : client.lieuDelivrancePieceIdent,
            'numRegistreCommerceClient' : client.numRegistreCommerceClient,
            'clientPresume' : client.clientPresume,
            'nbrModifInfoClient' : client.nbrModifInfoClient,
        }
        data.append(client_data)
    return JsonResponse(data, safe=False)

def get_clients_ordre_par_nom(request):
    clients = Clients.objects.order_by('nomClient')
    data = []
    for client in clients:
        date_naissance = client.dateNaissanceClient.strftime('%d-%m-%Y') if client.dateNaissanceClient else None
        date_ajout = client.dateAjoutClient.strftime('%d-%m-%Y') if client.dateAjoutClient else None
        date_delivrance = client.dateDelivrancePieceIdent.strftime('%d-%m-%Y') if client.dateDelivrancePieceIdent else None
        client_data = {
            'codeAgenceClient': client.codeAgenceClient,
            'idClient': client.idClient,
            'nomClient': client.nomClient,
            'preClient': client.preClient,
            'dateNaissanceClient': date_naissance,
            'lieuNaissanceClient': client.lieuNaissanceClient,
            'nationaliteClient': client.nationaliteClient,
            'sexeClient': client.get_sexeClient_display(),
            'adresse1Client' : client.adresse1Client,
            'adresse2Client' : client.adresse2Client,
            'codePostal': client.codePostal,
            'numTelClient' : client.numTelClient,
            'pereClient' : client.pereClient,
            'mereClient' : client.mereClient,
            'situationFamiliale' : client.get_situationFamiliale_display(),
            'dateAjoutClient' : date_ajout,
            'typePersonneClient' : client.get_typePersonneClient_display(),
            'professionClient' : client.professionClient,
            'activiteClient' : client.activiteClient,
            'gerantClient' : client.gerantClient,
            'clientResideDZ' : client.clientResideDZ,
            'pieceIdentClient' : client.get_pieceIdentClient_display(),
            'dateDelivrancePieceIdent' : date_delivrance,
            'lieuDelivrancePieceIdent' : client.lieuDelivrancePieceIdent,
            'numRegistreCommerceClient' : client.numRegistreCommerceClient,
            'clientPresume' : client.clientPresume,
            'nbrModifInfoClient' : client.nbrModifInfoClient,
        }
        data.append(client_data)
    return JsonResponse(data, safe=False)

def get_liste_GL(request):
    grandLivres = GrandLivres.objects.all()
    data = []
    for gl in grandLivres:
        gl_data = {
            'idGL' : gl.idGL,
            'libelleGL' : gl.libelleGL,
        }
        data.append(gl_data)
    return JsonResponse(data, safe=False)

def get_liste_operations(request):
    operations = Operations.objects.all()
    data = []
    for oper in operations:
        oper_data = {
            'numOperation' : oper.numOperation,
            'libelleOperation' : oper.libelleOperation,
        }
        data.append(oper_data)
    return JsonResponse(data, safe=False)

def get_liste_comptes(request):
    accounts = Comptes.objects.all()
    data = []
    for account in accounts:
        date_creation = account.dateCreationCompte.strftime('%d-%m-%Y') if account.dateCreationCompte else None
        date_derniere = account.dateDerniereOperation.strftime('%d-%m-%Y') if account.dateDerniereOperation else None
        date_fermeture = account.dateFermetureCompte.strftime('%d-%m-%Y') if account.dateFermetureCompte else None
        date_opposition = account.dateMiseEnOpposition.strftime('%d-%m-%Y') if account.dateMiseEnOpposition else None
        account_data = {
            'numeroCompte': account.numeroCompte,
            'client' : str(account.client.codeAgenceClient) + " - " + str(account.client.idClient) if account.client else None,
            'GL' : account.GL.idGL if account.GL else None,
            'dateCreationCompte': date_creation,
            'soldeCourant': account.soldeCourant,
            'soldeHier': account.soldeHier,
            'dateDerniereOperation' : date_derniere,
            'compteEnOpposition' : account.compteEnOpposition,
            'dateMiseEnOpposition' : date_opposition,
            'dateFermetureCompte' : date_fermeture,
        }
        data.append(account_data)
    return JsonResponse(data, safe=False)

def get_mouvements_par_numero_transaction(request, num_transaction):
    movements = Mouvements.objects.filter(numTransaction=num_transaction)
    data = []
    for movement in movements:
        date_formatted = movement.dateMouvement.strftime('%d-%m-%Y') if  movement.dateMouvement else None
        movement_data = {
            'numTransaction': movement.numTransaction,
            'montantMouvement': movement.montantMouvement,
            'dateMouvement': date_formatted,
            'heureTransaction' : movement.heureTransaction,
            'libelleTransaction' : movement.libelleTransaction,
            'RIB' : movement.RIB,
            'utilIntro' : movement.utilIntro.idUtil if movement.utilIntro else None,
            'utilValid' : movement.utilValid.idUtil if movement.utilValid else None,
            'operation' : movement.operation.numOperation,
            'compte' : movement.compte.numeroCompte if movement.compte else None,
            'GL' : movement.GL.idGL if movement.GL else None,
        }
        data.append(movement_data)
    return JsonResponse(data, safe=False)

def get_transactions_avec_filtre(request):
    num_compte = request.GET.get('num_compte', None)
    num_operation = request.GET.get('num_operation', None)
    max_amount = request.GET.get('max_amount', None)
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)
    util_intro = request.GET.get('util_intro', None)
    util_valid = request.GET.get('util_valid', None)
    gl = request.GET.get('gl', None)
    transactions = Mouvements.objects.all()

    if num_operation:
        transactions = transactions.filter(operation__numOperation=num_operation)

    if max_amount:
        transactions = transactions.filter(montantMouvement__lt=max_amount)

    if start_date and end_date:
        transactions = transactions.filter(dateMouvement__range=[start_date, end_date])

    if num_compte:
        transactions = transactions.filter(compte__numeroCompte=num_compte)

    if util_intro:
        transactions = transactions.filter(utilIntro__idUtil=util_intro)

    if util_valid:
        transactions = transactions.filter(utilValid__idUtil=util_valid)

    if gl:
        transactions = transactions.filter(GL__idGL=gl)

    data = []
    for transaction in transactions:
        date_formatted = transaction.dateMouvement.strftime('%d-%m-%Y') if  transaction.dateMouvement else None
        transaction_data = {
            'numTransaction': transaction.numTransaction,
            'compte' : transaction.compte.numeroCompte if transaction.compte else None,
            'GL' : transaction.GL.idGL if transaction.GL else None,
            'montantMouvement': transaction.montantMouvement,
            'operation' : transaction.operation.numOperation if transaction.operation else None,
            'libelleTransaction' : transaction.libelleTransaction,
            'dateMouvement': date_formatted,
            'heureTransaction' : transaction.heureTransaction,
            'utilIntro' : transaction.utilIntro.idUtil if transaction.utilIntro else None,
            'utilValid' : transaction.utilValid.idUtil if transaction.utilValid else None,
            'RIB' : transaction.RIB,
        }
        data.append(transaction_data)

    return JsonResponse(data, safe=False)
