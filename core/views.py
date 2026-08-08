from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Profile, SkillCategory, ProjectCategory, Project, Experience, ContactMessage
from .forms import ContactForm


def get_default_profile():
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(
            name="Alex Morgan",
            tagline="Senior Fullstack Engineer & Cloud Architect",
            bio="Passionate software engineer with over 5+ years of experience building high-scale web applications, distributed backend services, and sleek modern user interfaces.",
            email="",
            phone="+1 (555) 234-5678",
            location="San Francisco, CA"
        )
    return profile


def index_view(request):
    profile = get_default_profile()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    project_categories = ProjectCategory.objects.all()
    projects = Project.objects.select_related('category').all()
    experiences = Experience.objects.all()
    form = ContactForm()

    context = {
        'profile': profile,
        'skill_categories': skill_categories,
        'project_categories': project_categories,
        'projects': projects,
        'experiences': experiences,
        'form': form,
    }
    return render(request, 'index.html', context)


def _is_valid_email(val):
    return bool(val and isinstance(val, str) and '@' in val and '.' in val and not val.endswith('example.com') and val != 'EMAIL_HOST_USER')


@csrf_exempt
def contact_submit_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            profile = get_default_profile()

            # Determine from_email and recipient
            default_from = getattr(settings, 'DEFAULT_FROM_EMAIL', '')
            host_user = getattr(settings, 'EMAIL_HOST_USER', '')

            from_email = default_from if _is_valid_email(default_from) else (host_user if _is_valid_email(host_user) else 'webmaster@localhost')

            recipient = profile.email.strip() if (profile and _is_valid_email(profile.email)) else ''
            if not _is_valid_email(recipient):
                recipient = host_user if _is_valid_email(host_user) else (default_from if _is_valid_email(default_from) else '')

            if recipient and from_email:
                subject = f"Portfolio Contact: {contact.subject or 'New Inquiry'} from {contact.name}"
                message_body = (
                    f"You received a new message on your portfolio:\n\n"
                    f"Name: {contact.name}\n"
                    f"Email: {contact.email}\n"
                    f"Subject: {contact.subject or 'No Subject'}\n\n"
                    f"Message:\n{contact.message}\n"
                )
                try:
                    send_mail(
                        subject=subject,
                        message=message_body,
                        from_email=from_email,
                        recipient_list=[recipient],
                        fail_silently=False,
                    )
                except Exception as e:
                    print(f"Email notification error: {e}")



            return JsonResponse({
                'status': 'success',
                'message': 'Thank you! Your message has been sent successfully. I will get back to you soon.'
            })
        else:
            return JsonResponse({
                'status': 'error',
                'errors': form.errors.as_json(),
                'message': 'Please fill out all required fields properly.'
            }, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)


def download_cv_view(request):
    profile = get_default_profile()
    if profile.cv_file and hasattr(profile.cv_file, 'path'):
        try:
            with open(profile.cv_file.path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{profile.name.replace(" ", "_")}_CV.pdf"'
                return response
        except FileNotFoundError:
            pass

    # Generic fallback mock CV content
    cv_content = f"""==================================================
{profile.name.upper()} - CURRICULUM VITAE
{profile.tagline}
Email: {profile.email} | Phone: {profile.phone} | Location: {profile.location}
==================================================

SUMMARY
{profile.bio}

SKILLS & EXPERTISE
- Backend: Python, Django, PostgreSQL, FastAPI, Docker
- Frontend: HTML5, CSS3, JavaScript ES6+, React, Next.js
- Tools & Cloud: Git, Linux, AWS, CI/CD, Redis, Nginx

EXPERIENCE
- Senior Fullstack Developer (2023 - Present)
  Architected and launched multi-tenant web platforms serving 100k+ monthly active users.
- Software Engineer (2021 - 2023)
  Developed RESTful microservices, database schemas, and responsive dashboards.

EDUCATION
- B.S. in Computer Science & Software Engineering

==================================================
Generated automatically from Portfolio System.
"""
    response = HttpResponse(cv_content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{profile.name.replace(" ", "_")}_Resume.txt"'
    return response
