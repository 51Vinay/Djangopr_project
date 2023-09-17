from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .forms import EmailForm

def send_email(request):
    form = EmailForm()

    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient = form.cleaned_data['recipient']
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [recipient]

            email = EmailMessage(subject, message, from_email, recipient_list)
            
            # Attach files
            for file in request.FILES.getlist('attachments'):
                email.attach(file.name, file.read(), file.content_type)
            
            try:
                email.send()
                messages.success(request, 'Email sent successfully!')
            except Exception as e:
                messages.error(request, f'Email sending failed: {str(e)}')

    return render(request, 'email_app/send_email.html', {'form': form})








# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib import messages
# from .forms import EmailForm

# def send_email(request):
#     form = EmailForm()

#     if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             recipient = form.cleaned_data['recipient']
#             from_email = settings.EMAIL_HOST_USER
#             recipient_list = [recipient]

#             try:
#                 send_mail(subject, message, from_email, recipient_list)
#                 messages.success(request, 'Email sent successfully!')
#             except Exception as e:
#                 messages.error(request, f'Email sending failed: {str(e)}')

#     return render(request, 'email_app/send_email.html', {'form': form})
