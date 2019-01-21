from django.db import models
from django.conf import settings

# Create your models here.
class Adie(models.Model):
    RACE = (
        ('Black', 'African American'),
        ('Black', 'Black'),
        ('Latinx', 'Hispanic'),
        ('Latinx', 'Latino'),
        ('Latinx', 'Latinx'),
        ('White', 'European American'),
        ('White', 'Caucasian'),
        ('White', 'White'),
        ('Asian', 'Asian American'),
        ('Asian', 'Asian'),
        ('Indigenous', 'Native'),
        ('Indigenous', 'Native American'),
        ('Indigenous', 'Alaska Native'),
        ('Pacific Islander', 'Native Hawaiian'),
        ('Pacific Islander', 'Pacific Islander'),
    )
    GENDER = (
        ('female','female'),
        ('non-binary','non-binary'),
        ('trans', 'transgender'),
        ('two-spirited', 'two-spirited'),
        ('male', 'male'),
    )
    ORIENTATION = (
        ('straight', 'straight'),
        ('queer-lesbian', 'lesbian'),
        ('queer-gay', 'gay'),
        ('queer-bisexual', 'bisexual'),
        ('asexual', 'asexual'),
    )
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER)
    race = models.CharField(max_length=20, choices=RACE)
    orientation = models.CharField(max_length=20, choices=ORIENTATION)
    transplant = models.BooleanField(default=False)
    location_city = models.CharField(max_length=20)
    location_state = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'adie'
        verbose_name_plural = 'adies'
        ordering = ['race']

    def __str__(self):
        return '\nAge: %s\nGender: %s\nRace: %s\nSexual Orientation: %s\nTransplant?: %s\nLocation: %s, %s' % (self.age, self.gender, self.race, self.orientation, self.transplant, self.location_city, self.location_state)


class Company(models.Model):
    MICROAGGRESSIONS = (
        ('NONE', 'one comment'),
        ('LOW', 'two comments'),
        ('MODERATE', 'comments and attitude'),
        ('HIGH', 'uncomfortable at the start'),
    )
    COMPANY_SIZES = (
        ('startup', 'startup company'),
        ('small', 'small company'),
        ('large', 'large company'),
    )
    company_size = models.CharField(max_length=120, choices=COMPANY_SIZES)
    org_size = models.IntegerField()
    location_city = models.CharField(max_length=120)
    location_state = models.CharField(max_length=120)
    industry = models.CharField(max_length=128)
    adies_present = models.BooleanField(default=False, null=True)
    level_of_microaggressions = models.CharField(max_length=120, choices=MICROAGGRESSIONS, null=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['level_of_microaggressions']

    def __str__(self):
        return '\nCompany Size: %s\nOrg Size: %s\nLocation: %s,  %s\nIndustry: %s\nAdies Present?: %s\nLevel of Microaggressions?: %s\n' % (self.company_size, self.org_size, self.location_city, self.location_state, self.industry, self.adies_present, self.level_of_microaggressions)


class Offer(models.Model):
    HIRE_TYPE = (
        ('INTERNAL', 'internal'),
        ('EXTERNAL', 'external'),
    )
    negotiations = models.BooleanField(default=False)
    adie_id = models.ForeignKey(Adie, on_delete=models.CASCADE)
    base_amount = models.IntegerField()
    signing_bonus = models.IntegerField(null=True)
    relocation_package = models.IntegerField(null=True)
    health_insurance = models.IntegerField(null=True)
    retirement = models.CharField(max_length=128, blank=True, default='')
    vacation_days = models.IntegerField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    hire_type = models.CharField(max_length=20, choices=HIRE_TYPE)
    stocks = models.IntegerField()

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'
        ordering = ['adie_id']

    def __str__(self):
        return '\n\tAdie: %s\nCompany: %s\nDid you negotiate?: %s\nInternal Hire/External Hire: %s\nBase Pay: %s \nSigning Bonus: %s\nHealth Insurance: %s\n # of Vacation Days: %s\n# of stock: %s\nRetirement: %s\nRelocation Compensation: %s' % (self.adie_id, self.company_id, self.hire_type, self.negotiations, self.base_amount, self.signing_bonus, self.health_insurance, self.vacation_days, self.stocks, self.retirement, self.relocation_package)
