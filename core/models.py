from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, default="Alex Morgan")
    tagline = models.CharField(max_length=200, default="Senior Fullstack Engineer & Cloud Architect")
    bio = models.TextField(default="Passionate software engineer with over 5+ years of experience building high-scale web applications, distributed backend services, and sleek modern user interfaces.")
    avatar = models.ImageField(upload_to='profile/', blank=True, null=True)
    avatar_url = models.CharField(max_length=500, blank=True, default="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=600&auto=format&fit=crop")
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)
    cv_url = models.CharField(max_length=500, blank=True, default="#")
    email = models.EmailField(default="alex.morgan.dev@example.com")
    phone = models.CharField(max_length=30, default="+1 (555) 234-5678")
    location = models.CharField(max_length=100, default="San Francisco, CA")
    github_url = models.URLField(blank=True, default="https://github.com")
    linkedin_url = models.URLField(blank=True, default="https://linkedin.com")
    twitter_url = models.URLField(blank=True, default="https://twitter.com")
    years_of_experience = models.IntegerField(default=5)
    projects_completed = models.IntegerField(default=32)
    satisfied_clients = models.IntegerField(default=18)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, blank=True, help_text="FontAwesome icon class e.g. fa-brands fa-python")
    icon_url = models.CharField(max_length=500, blank=True, help_text="SVG icon URL or logo image link")
    proficiency = models.IntegerField(default=85, help_text="Skill percentage (1-100)")
    is_featured = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Project Categories"

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True)
    live_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    featured = models.BooleanField(default=True)
    tech_stack = models.CharField(max_length=255, help_text="Comma-separated tech badges, e.g., Python, Django, PostgreSQL")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=150)
    company_logo_class = models.CharField(max_length=100, default="fa-solid fa-briefcase")
    position = models.CharField(max_length=150)
    location = models.CharField(max_length=100, blank=True, default="Remote")
    start_date = models.CharField(max_length=50, help_text="e.g. Jan 2022")
    end_date = models.CharField(max_length=50, blank=True, default="Present")
    is_current = models.BooleanField(default=False)
    description = models.TextField(help_text="Line or bullet points of key responsibilities and achievements")
    technologies = models.CharField(max_length=255, blank=True, help_text="Comma-separated tech tags")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']
        verbose_name_plural = "Experiences"

    def __str__(self):
        return f"{self.position} at {self.company}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
