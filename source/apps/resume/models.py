from django.db import models
from django.utils.translation import ugettext_lazy as _
from commons.utils import PHONE_NUMBER_VALIDATOR


class Info(models.Model):
    class Meta:
        verbose_name = _("Info")
        verbose_name_plural = _("Info")

    first_name = models.CharField(_("First Name"), max_length=128)
    last_name = models.CharField(_("Last Name"), max_length=128)
    phone = models.CharField(
        _("Phone"),
        max_length=15,
        validators=[
            PHONE_NUMBER_VALIDATOR,
        ],
    )
    email = models.EmailField(_("Email"))
    bio = models.TextField(_("Bio"), max_length=512)
    linked_in = models.URLField(_("LinkedIn"), null=True, blank=True)
    github = models.URLField(_("Github"), null=True, blank=True)
    gitlab = models.URLField(_("Gitlab"), null=True, blank=True)
    telegram = models.URLField(_("Telegram"), null=True, blank=True)
    interests = models.TextField(_("Interests"), max_length=512)
    profile_photo = models.ImageField(
        _("Profile"), upload_to="profile", null=True, blank=True
    )

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)


class Experience(models.Model):
    class Meta:
        verbose_name = _("Experience")
        verbose_name_plural = _("Experiences")

    title = models.CharField(_("Title"), max_length=256)
    subtitle = models.CharField(_("Sub Title"), max_length=256)
    from_date = models.DateField(_("From"))
    to_date = models.DateField(_("To"), null=True, blank=True)
    description = models.CharField(_("Description"), max_length=512)

    def __str__(self):
        return self.title


class Education(models.Model):
    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Educations")

    title = models.CharField(_("Title"), max_length=256)
    institute = models.CharField(_("Institute"), max_length=256)
    from_date = models.DateField(_("From"))
    to_date = models.DateField(_("To"), null=True, blank=True)

    def __str__(self):
        return self.title


class SkillCategory(models.Model):
    class Meta:
        verbose_name = _("Skill Category")
        verbose_name_plural = _("Skill Categories")

    name = models.CharField(_("Name"), max_length=128)

    def __str__(self):
        return self.name


class Skill(models.Model):
    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")

    name = models.CharField(_("Name"), max_length=128)
    category = models.ForeignKey(
        "SkillCategory", models.CASCADE, "skills", verbose_name=_("Category")
    )

    def __str__(self):
        return self.name