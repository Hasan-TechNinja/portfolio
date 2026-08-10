from django.core.management.base import BaseCommand
from core.models import Profile, SkillCategory, Skill, ProjectCategory, Project, Experience


class Command(BaseCommand):
    help = "Seeds the database with high quality fullstack portfolio initial data."

    def handle(self, *args, **options):
        self.stdout.write("Seeding portfolio database...")

        # 1. Seed or Update Profile
        profile, created = Profile.objects.get_or_create(id=1)
        profile.name = "Hasan Mahmud"
        profile.tagline = "Senior Fullstack Engineer & Cloud Architect"
        profile.bio = "Passionate full-stack developer with 5+ years of experience building modern scalable web applications, REST/GraphQL APIs, and high-performance microservices. Specialized in Python, Django, PostgreSQL, JavaScript, and cloud technologies."
        profile.avatar_url = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=600&auto=format&fit=crop"
        profile.cv_url = "/download-cv/"
        profile.email = "hasan.dev@example.com"
        profile.phone = "+1 (555) 987-6543"
        profile.location = "San Francisco, CA (Open to Remote)"
        profile.github_url = "https://github.com"
        profile.linkedin_url = "https://linkedin.com"
        profile.twitter_url = "https://twitter.com"
        profile.years_of_experience = 5
        profile.projects_completed = 35
        profile.satisfied_clients = 24
        profile.save()
        self.stdout.write(self.style.SUCCESS("Profile updated."))

        # 2. Skill Categories & Skills
        skills_data = [
            {
                "category": "Languages",
                "order": 1,
                "items": [
                    {"name": "Python", "icon_class": "fa-brands fa-python", "proficiency": 95, "order": 1},
                    {"name": "HTML5", "icon_class": "fa-brands fa-html5", "proficiency": 95, "order": 2},
                    {"name": "CSS3 / Sass", "icon_class": "fa-brands fa-css3-alt", "proficiency": 90, "order": 3},
                    {"name": "JavaScript (ES6+)", "icon_class": "fa-brands fa-js", "proficiency": 90, "order": 4},
                    {"name": "TypeScript", "icon_class": "fa-solid fa-code", "proficiency": 85, "order": 5},
                    {"name": "SQL", "icon_class": "fa-solid fa-database", "proficiency": 90, "order": 6},
                ]
            },
            {
                "category": "Databases",
                "order": 2,
                "items": [
                    {"name": "PostgreSQL", "icon_class": "fa-solid fa-server", "proficiency": 92, "order": 1},
                    {"name": "SQLite", "icon_class": "fa-solid fa-database", "proficiency": 95, "order": 2},
                    {"name": "Redis", "icon_class": "fa-solid fa-bolt", "proficiency": 88, "order": 3},
                    {"name": "MySQL", "icon_class": "fa-solid fa-database", "proficiency": 85, "order": 4},
                ]
            },
            {
                "category": "Frameworks & Tools",
                "order": 3,
                "items": [
                    {"name": "Django / Django REST", "icon_class": "fa-brands fa-python", "proficiency": 95, "order": 1},
                    {"name": "React.js", "icon_class": "fa-brands fa-react", "proficiency": 88, "order": 2},
                    {"name": "FastAPI", "icon_class": "fa-solid fa-feather", "proficiency": 90, "order": 3},
                    {"name": "Node.js", "icon_class": "fa-brands fa-node-js", "proficiency": 82, "order": 4},
                    {"name": "Tailwind CSS", "icon_class": "fa-solid fa-paint-brush", "proficiency": 92, "order": 5},
                ]
            },
            {
                "category": "Cloud & DevOps",
                "order": 4,
                "items": [
                    {"name": "Git & GitHub", "icon_class": "fa-brands fa-git-alt", "proficiency": 95, "order": 1},
                    {"name": "Docker", "icon_class": "fa-brands fa-docker", "proficiency": 88, "order": 2},
                    {"name": "Linux / Bash", "icon_class": "fa-brands fa-linux", "proficiency": 90, "order": 3},
                    {"name": "AWS (EC2, S3)", "icon_class": "fa-brands fa-aws", "proficiency": 84, "order": 4},
                    {"name": "Nginx & Gunicorn", "icon_class": "fa-solid fa-gears", "proficiency": 88, "order": 5},
                ]
            }
        ]

        for cat_data in skills_data:
            cat_obj, _ = SkillCategory.objects.get_or_create(
                name=cat_data["category"],
                defaults={"order": cat_data["order"]}
            )
            cat_obj.order = cat_data["order"]
            cat_obj.save()

            for item in cat_data["items"]:
                Skill.objects.update_or_create(
                    category=cat_obj,
                    name=item["name"],
                    defaults={
                        "icon_class": item["icon_class"],
                        "proficiency": item["proficiency"],
                        "order": item["order"],
                        "is_featured": True
                    }
                )
        self.stdout.write(self.style.SUCCESS("Skills seeded."))

        # 3. Project Categories & Projects
        project_cats = [
            {"name": "Fullstack", "slug": "fullstack", "order": 1},
            {"name": "Backend API", "slug": "backend", "order": 2},
            {"name": "Frontend UI", "slug": "frontend", "order": 3},
            {"name": "AI & Cloud", "slug": "ai-cloud", "order": 4},
        ]

        cat_map = {}
        for pcat in project_cats:
            c_obj, _ = ProjectCategory.objects.get_or_create(
                slug=pcat["slug"],
                defaults={"name": pcat["name"], "order": pcat["order"]}
            )
            c_obj.name = pcat["name"]
            c_obj.order = pcat["order"]
            c_obj.save()
            cat_map[pcat["slug"]] = c_obj

        projects_list = [
            {
                "title": "Enterprise Cloud SaaS Platform",
                \"description\": "Full-stack enterprise asset and workflow management dashboard with real-time telemetry and RBAC.",
                "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=800&auto=format&fit=crop",
                "category": cat_map["fullstack"],
                "live_url": "https://demo.example.com/saas",
                "github_url": "https://github.com/example/cloud-saas-platform",
                "tech_stack": "Django, PostgreSQL, React, Redis, Docker, Tailwind",
                "order": 1,
            },
            {
                "title": "AI Knowledge Base & Semantic Search API",
                \"description\": "High-speed vector similarity engine and RAG backend with FastAPI and PostgreSQL pgvector.",
                "image_url": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=800&auto=format&fit=crop",
                "category": cat_map["ai-cloud"],
                "live_url": "https://demo.example.com/ai-search",
                "github_url": "https://github.com/example/ai-semantic-search",
                "tech_stack": "Python, FastAPI, PostgreSQL, OpenAI API, Celery",
                "order": 2,
            },
            {
                "title": "Distributed Financial Gateway & Ledger",
                \"description\": "Secure payment orchestration and transaction ledger service handling micro-deposits.",
                "image_url": "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?q=80&w=800&auto=format&fit=crop",
                "category": cat_map["backend"],
                "live_url": "https://demo.example.com/finance",
                "github_url": "https://github.com/example/fintech-gateway",
                "tech_stack": "Django REST, PostgreSQL, Stripe API, JWT, Nginx",
                "order": 3,
            },
            {
                "title": "Modern Interactive Portfolio Engine",
                \"description\": "Ultra-responsive, dark-themed developer portfolio template with dynamic admin CMS.",
                "image_url": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800&auto=format&fit=crop",
                "category": cat_map["frontend"],
                "live_url": "https://demo.example.com/portfolio",
                "github_url": "https://github.com/example/portfolio-system",
                "tech_stack": "HTML5, CSS3, Vanilla JS, Django, FontAwesome",
                "order": 4,
            },
            {
                "title": "E-Commerce Micro-Storefront",
                \"description\": "Lightning fast digital store with cart drawer, checkout workflow, and inventory synchronization.",
                "image_url": "https://images.unsplash.com/photo-1472851294608-062f824d29cc?q=80&w=800&auto=format&fit=crop",
                "category": cat_map["fullstack"],
                "live_url": "https://demo.example.com/storefront",
                "github_url": "https://github.com/example/ecommerce-storefront",
                "tech_stack": "Django, SQLite/PostgreSQL, JavaScript, Glassmorphism",
                "order": 5,
            },
        ]

        for p_data in projects_list:
            Project.objects.update_or_create(
                title=p_data["title"],
                defaults=p_data
            )
        self.stdout.write(self.style.SUCCESS("Projects seeded."))

        # 4. Experiences
        experiences_list = [
            {
                "company": "TechSphere Global",
                "position": "Senior Fullstack Engineer",
                "location": "San Francisco, CA",
                "start_date": "Jan 2023",
                "end_date": "Present",
                "is_current": True,
                "company_logo_class": "fa-solid fa-rocket",
                "description": "• Spearheaded the architectural revamp of core Django REST services, cutting average API latency by 45%.\n• Designed and maintained React & Tailwind UI components serving over 150k monthly active users.\n• Implemented Docker containerization and CI/CD deployment pipelines on AWS EC2/S3.",
                "technologies": "Django, Python, PostgreSQL, React, Docker, AWS",
                "order": 1,
            },
            {
                "company": "DataWave Systems",
                "position": "Fullstack Software Developer",
                "location": "Austin, TX (Remote)",
                "start_date": "Mar 2021",
                "end_date": "Dec 2022",
                "is_current": False,
                "company_logo_class": "fa-solid fa-database",
                "description": "• Built scalable backend services in Django and FastAPI with PostgreSQL database optimizations.\n• Developed interactive data visualization dashboards and SVG reporting charts for enterprise clients.\n• Automated database migration scripts and reduced query N+1 bottlenecks.",
                "technologies": "Python, Django, FastAPI, PostgreSQL, Redis, JavaScript",
                "order": 2,
            },
            {
                "company": "Nexa Digital Agency",
                "position": "Junior Web Developer",
                "location": "New York, NY",
                "start_date": "Jun 2019",
                "end_date": "Feb 2021",
                "is_current": False,
                "company_logo_class": "fa-solid fa-laptop-code",
                "description": "• Created responsive web applications using HTML5, CSS3, JavaScript, and Python backend frameworks.\n• Integrated third-party APIs (Stripe, Twilio, SendGrid) and managed client maintenance contracts.\n• Collaborated with UI/UX designers to translate Figma mockups into pixel-perfect web interfaces.",
                "technologies": "HTML5, CSS3, JavaScript, Python, SQLite, Git",
                "order": 3,
            },
        ]

        for exp in experiences_list:
            Experience.objects.update_or_create(
                company=exp["company"],
                position=exp["position"],
                defaults=exp
            )
        self.stdout.write(self.style.SUCCESS("Experience timeline seeded."))
        self.stdout.write(self.style.SUCCESS("All portfolio data successfully seeded!"))
