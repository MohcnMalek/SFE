from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from . import ocpp_client 

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'school/index.html')

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'school/adminclick.html')

def admin_signup_view(request):
    form = forms.AdminSigupForm()
    if request.method == 'POST':
        form = forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('adminlogin')
    return render(request, 'school/adminsignup.html', {'form': form})

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    chargepoint_count = models.ChargePointExtra.objects.count()
    client_count = models.Client.objects.filter(status=True).count()
    total_client_amount = sum(client.montant for client in models.Client.objects.all())
    total_client_energy = sum(client.energy for client in models.Client.objects.all())
    charging_sessions = ocpp_client.connect_to_ocpp_server()
    # Fetch recent charging sessions
    recent_charging_sessions = models.ChargingSession.objects.order_by('-start_time')[:5]
    
    mydict = {
        'chargepoint_count': chargepoint_count,
        'client_count': client_count,
        'total_client_amount': total_client_amount,
        'total_client_energy': total_client_energy,
        'recent_charging_sessions': recent_charging_sessions,
        'charging_sessions': charging_sessions
    }

    return render(request, 'school/admin_dashboard.html', context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_chargepoint_view(request):
    return render(request, 'school/admin_chargepoint.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_chargepoint_view(request):
    form = forms.ChargePointForm()
    if request.method == 'POST':
        form = forms.ChargePointForm(request.POST)
        if form.is_valid():
            chargepoint = form.save(commit=False)
            chargepoint.status = True
            chargepoint.save()
            return HttpResponseRedirect('admin-chargepoint')
    return render(request, 'school/admin_add_chargepoint.html', {'form': form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_chargepoint_view(request):
    chargepoints = models.ChargePointExtra.objects.filter(status=True)
    return render(request, 'school/admin_view_chargepoint.html', {'chargepoints': chargepoints})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_chargepoint_view(request):
    chargepoints = models.ChargePointExtra.objects.filter(status=True)
    return render(request, 'school/admin_approve_chargepoint.html', {'chargepoints': chargepoints})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_update_chargepoint_view(request):
    chargepoints = models.ChargePointExtra.objects.filter(status=True)
    return render(request, 'school/update_chargepoint.html', {'chargepoints': chargepoints})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_chargepoint_view(request, pk):
    chargepoint = models.ChargePointExtra.objects.get(id=pk)
    chargepoint.delete()
    return redirect('admin-approve-chargepoint')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_chargepoint_view(request, pk):
    chargepoint = models.ChargePointExtra.objects.get(id=pk)
    form = forms.ChargePointForm(instance=chargepoint)

    if request.method == 'POST':
        form = forms.ChargePointForm(request.POST, instance=chargepoint)
        if form.is_valid():
            form.save()
            return redirect('admin-update-chargepoint')
    return render(request, 'school/admin_update_chargepoint.html', {'form': form})

# ------------------------------------------------------------Clients------------------------------------------------------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_client_view(request):
    return render(request, 'school/admin_client.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_client_view(request):
    form = forms.ClientForm()
    if request.method == 'POST':
        form = forms.ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.status = True
            client.save()
            # Redirect to the admin-client page after successfully adding the client
            return redirect('admin-client')
    return render(request, 'school/admin_add_client.html', {'form': form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_client_view(request):
    clients = models.Client.objects.filter(status=True)
    return render(request, 'school/admin_view_client.html', {'clients': clients})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_client_view(request):
    clients = models.Client.objects.filter(status=True)
    return render(request, 'school/admin_approve_client.html', {'clients': clients})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_update_client_view(request):
    clients = models.Client.objects.filter(status=True)
    return render(request, 'school/update_client.html', {'clients': clients})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_client_view(request, pk):
    client = models.Client.objects.get(id=pk)
    client.delete()
    return redirect('admin-approve-client')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_client_view(request, pk):
    client = models.Client.objects.get(id=pk)
    form = forms.ClientForm(instance=client)

    if request.method == 'POST':
        form = forms.ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('admin-update-client')
    return render(request, 'school/admin_update_client.html', {'form': form})

# ------------------------------------------------------------Users------------------------------------------------------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_user_view(request):
    return render(request, 'school/admin_user.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_user_view(request):
    form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            # Redirect to the admin-user page after successfully adding the user
            return redirect('admin-user')
    return render(request, 'school/admin_add_user.html', {'form': form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_user_view(request):
    users = models.Users.objects.all()  # Modification de la requête pour récupérer tous les utilisateurs
    return render(request, 'school/admin_view_user.html', {'users': users})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_user_view(request):
    users = models.Users.objects.all()
    return render(request, 'school/admin_approve_user.html', {'users': users})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_update_user_view(request):
    users = models.Users.objects.all()
    return render(request, 'school/update_user.html', {'users': users})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_user_view(request, pk):
    user = models.Users.objects.get(id=pk)
    user.delete()
    return redirect('admin-approve-user')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_user_view(request, pk):
    user = models.Users.objects.get(id=pk)
    form = forms.UserForm(instance=user)

    if request.method == 'POST':
        form = forms.UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('admin-update-user')
    return render(request, 'school/admin_update_user.html', {'form': form})