from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect


@login_required
def dashboard(request):
    return render(
        request,
        'dashboard/dashboard.html')


def login_request(request):
    next_url = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        # datos son correctos?
        if form.is_valid():
            credentials = {
                'username': form.cleaned_data.get('username'),
                'password': form.cleaned_data.get('password')
            }
            user = authenticate(**credentials)
            # usuario existe?
            if user is not None:
                # usuario está activo?
                if user.is_active:
                    login(request, user)
                    messages.info(
                        request, f'Has ingresado como {user.username}')
                    # hay siguiente url?
                    if next_url:
                        return redirect(next_url)
                    return redirect('dashboard:dashboard')
                messages.error(request, 'Usuario inactivo.')
            else:
                messages.error(request, 'Usuario o Password inválido.')
        else:
            messages.error(request, 'Usuario o Password inválido.')
    form = AuthenticationForm()
    return render(
        request,
        'registration/login.html',
        {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, 'Hasta luego, vuelva pronto!')
    return redirect('dashboard:dashboard')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Su contraseña fue modificada exitosamente!')
            return redirect('dashboard:dashboard')
        messages.error(request, 'Verifique los datos e intente de nuevo.')
    form = PasswordChangeForm(request.user)
    return render(
        request,
        'registration/password_change_form.html',
        {'form': form})
