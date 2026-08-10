from django.contrib import admin
from .models import Profile, SkillCategory, Skill, ProjectCategory, Project, Experience, ContactMessage


admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Admin"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'email', 'location', 'years_of_experience')


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ('name', 'proficiency', 'icon_class', 'icon_url', 'is_featured', 'order')


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'is_featured', 'order')
    list_filter = ('category', 'is_featured')
    list_editable = ('proficiency', 'is_featured', 'order')
    search_fields = ('name',)


class ProjectInline(admin.StackedInline):
    model = Project
    extra = 1
    fields = ('title', 'short_description', 'tech_stack', 'live_url', 'github_url', 'featured', 'order')


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('order',)
    inlines = [ProjectInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'order', 'created_at')
    list_filter = ('category', 'featured')
    list_editable = ('featured', 'order')
    search_fields = ('title', 'short_description', 'tech_stack')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'company', 'start_date', 'end_date', 'is_current', 'order')
    list_filter = ('is_current',)
    list_editable = ('position', 'company', 'start_date', 'end_date', 'is_current', 'order')
    search_fields = ('position', 'company', 'description')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    # readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
