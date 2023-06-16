from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Notes, Patient, ForumPost, BlogPost, JournalPost, Consultation, ConsultationComment
from django.urls import reverse_lazy
from .forms import JournalPostForm, ConsultationForm, EditProfileForm, ConsultationCommentForm,ConsultationNoteForm, CommentForm, RegistrationForm, ForgotPasswordForm, ResetPasswordForm, ChangePasswordForm
from django.contrib.auth.decorators import login_required


# for email confirmation
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django.contrib.auth import get_user_model



# Create your views here.


class StaffMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect("unauthorized")
    
class UserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("unauthorized")


def unauthorized(request):
    return render(request, "unauthorized.html")


def index(request):
    return render(request, "index.html")


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = self.model.objects.all().order_by("-date_added")
        return queryset


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"

    def get_queryset(self):
        queryset = self.model.objects.all().order_by("-date_added")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = self.get_object()
        return context


class ForumListView(ListView):
    model = ForumPost
    template_name = "forum_list.html"
    context_object_name = "forums"

    def get_queryset(self):
        queryset = self.model.objects.all().order_by("-date_added")
        return queryset

class ForumDetailView(DetailView):
    model = ForumPost
    template_name = "forum_detail.html"
    form_class = CommentForm

    def get_queryset(self):
        queryset = self.model.objects.all().order_by("-date_added")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["post"] = post
        comments = self.object.forumpost.all()
        context['comments']= comments
        if 'form' not in context:
            context['form'] = self.form_class(request=self.request, post=post)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request=request, post=self.get_object())  # Pass the request and post object to the form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('forum_detail', args=(self.get_object().pk,)))
        else:
            return self.render_to_response(self.get_context_data(form=form))

class JournalListView(ListView):
    model = JournalPost
    template_name = "journal_list.html"
    context_object_name = "journal"


class JournalDetailView(DetailView):
    model = JournalPost
    template_name = "journal_detail.html"
    context_object_name = "post"


class AddJournal(CreateView):
    model = JournalPost
    template_name = "add_journal.html"
    form_class = JournalPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditJournal(UpdateView):
    model = JournalPost
    template_name = "edit_journal.html"
    form_class = JournalPostForm


class DeleteJournal(DeleteView):
    model = JournalPost
    template_name = "delete_journal.html"
    success_url = reverse_lazy("journal_list")


# user interaction


class ProfileView(DetailView):
    model = User
    template_name = "registration/profile.html"


class EditProfileView(UpdateView):
    model = User
    template_name = "registration/edit_profile.html"
    form_class = EditProfileForm
    success_url = reverse_lazy("index")
    





#STAFF INTERACTION

class PatientProfileList(StaffMixin,ListView):
    model = Patient
    template_name = "patient_list.html"
    context_object_name ='patients'

class PatientProfileDetail(StaffMixin,DetailView):
    model = Patient
    template_name = "patient_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patients = self.get_object()
        consultation = self.object.consultation_set.all() 
        context['consultation'] = consultation
        context["patients"] = patients

        return context


class Professional(UserMixin, ListView):
    model = Consultation
    template_name = "professional_list.html"
    context_object_name = "consultations"


class ProfessionalDetail(UserMixin, DetailView):
    model = Consultation
    template_name = 'professional_detail.html'
    context_object_name = 'consultation'
    form_class = ConsultationCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = self.object.notes_set.all() #or consultation.notes.all()
        context['comments'] = self.object.comments.all()
        if 'form' not in context:
            context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            consultation = self.get_object()
            comment = ConsultationComment(
                consultation=consultation,
                author=request.user,
                body=form.cleaned_data['body']
            )
            comment.save()
            return HttpResponseRedirect(reverse('professional_detail', args=(consultation.pk,)))
        else:
            return self.render_to_response(self.get_context_data(form=form))

class AddConsultation(UserMixin, CreateView):
    model = Consultation
    template_name = "add_consultation.html"
    form_class = ConsultationForm
    success_url = reverse_lazy("professional_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs
    
class AddConsultationNotes(CreateView):
    model = Notes
    template_name = "add_notes.html"
    form_class = ConsultationNoteForm
    success_url = reverse_lazy("professional_list")

    def form_valid(self, form):
        consultation_id = self.kwargs['pk']
        consultation = get_object_or_404(Consultation, id=consultation_id)
        form.instance.consultation = consultation
        return super().form_valid(form)
    

#user registration 
# View for user registration
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('index')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = RegistrationForm()

    return render(
        request=request,
        template_name="registration/register.html",
        context={"form": form}
        )

def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('registration/activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear {user}, please go to you email {to_email} inbox and click on the received activation link to confirm and complete the registration. If not found, kindly check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated!')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid or has expired.')
        return redirect('index')
    

# Change password view
@login_required
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = ChangePasswordForm(user)
    return render(request, 'registration/change_password.html', {'form': form})



# Forgot password view
def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            User = get_user_model()
            user = User.objects.filter(email=email).first()
            if user:
                # Perform password reset steps (e.g., send reset password email)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = account_activation_token.make_token(user)
                reset_link = f"{get_current_site(request)}/reset_password/{uid}/{token}/"
                message = render_to_string('registration/reset_password_email.html', {
                    'user': user,
                    'reset_link': reset_link,
                })
                email = EmailMessage(
                    subject='Reset Password',
                    body=message,
                    to=[user.email]
                )
                email.send()
                messages.success(request, 'An email with instructions to reset your password has been sent.')
                return redirect('index')
            else:
                messages.error(request, 'The email address provided is not associated with any user account.')
    else:
        form = ForgotPasswordForm()
    return render(request, 'registration/forgot_password.html', {'form': form})





# Reset password view
def reset_password(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        return HttpResponseBadRequest("Invalid reset password link.")

    if account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = ResetPasswordForm(user=user, data=request.POST)
            if form.is_valid():
                new_password = form.cleaned_data['new_password1']
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Your password has been successfully reset. Kindly enter your new credentials to login')
                return redirect('login')  # Replace with your success URL
        else:
            form = ResetPasswordForm(user=user)
        return render(request, 'registration/reset_password.html', {'form': form})
    else:
        return HttpResponseBadRequest("Invalid reset password link.")
    


def reset_password_email(request):
    return render (request , 'reset-password_email.html')

