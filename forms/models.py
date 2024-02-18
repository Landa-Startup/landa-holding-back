from django.db import models


# Create your models here.

class StartUpsForm(models.Model):
    firstName = models.CharField(max_length=300, blank=True)
    lastName = models.CharField(max_length=300, blank=True)
    birthDate = models.DateField(blank=True)
    email = models.EmailField(blank=True)
    countryOfResidence = models.CharField(max_length=300, blank=True)
    provinceOfResidence = models.CharField(max_length=300, blank=True)
    type = models.CharField(max_length=300, blank=True)
    ideaExplanation = models.CharField(max_length=300, blank=True)
    getToKnowUs = models.CharField(max_length=300, blank=True)
    pitchDeckFile = models.FileField(upload_to='pitchdeckfile', null=True, blank=True, editable=True)
    businessPlanFile = models.FileField(upload_to='businessPlan', null=True, blank=True, editable=True)
    productName = models.CharField(max_length=500, blank=True)
    siteAddress = models.CharField(max_length=500, blank=True)
    customerProblem = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    productLevel = models.CharField(max_length=200, blank=True)
    scalable = models.TextField(blank=True)
    monetizationOfYourPlan = models.TextField(blank=True)
    structureOfYourSales = models.TextField(blank=True)
    financialModelFile = models.FileField(upload_to='financialModelFile', null=True, blank=True, editable=True)
    cooperatedWithInvestors = models.TextField(blank=True)
    financialFile = models.FileField(upload_to='financialFile', null=True, blank=True, editable=True)
    customerCharacteristic = models.TextField(blank=True)
    currentCustomers = models.TextField(blank=True)
    estimatedMarketSize = models.TextField(blank=True)
    totalTamSamSom = models.TextField(blank=True)
    startupRevenue = models.TextField(blank=True)
    monthlyIncome = models.TextField(blank=True)
    currentInterestRate = models.TextField(blank=True)
    currentRaisedFunding = models.TextField(blank=True)
    neededCapital = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True)


class ContactUs(models.Model):
    name = models.CharField('نام', max_length=250, blank=True)
    email = models.EmailField('ایمیل', blank=True)
    number = models.CharField('شماره موبایل', max_length=250, blank=True)
    subject = models.CharField('عنوان', max_length=500, blank=True)
    message = models.TextField('پیام', blank=True)
    createdAt = models.DateTimeField('ساخته شده در', auto_now_add=True, blank=True)


class PartnerMembership(models.Model):
    firstName = models.CharField('نام', max_length=500, blank=True)
    lastName = models.CharField('نام خانوادگی', max_length=500, blank=True)
    birthDate = models.DateField('تاریخ تولد', blank=True)
    email = models.EmailField('ایمیل', blank=True)
    countryOfResidence = models.CharField('کشور اقامت', max_length=500, blank=True)
    provinceOfResidence = models.CharField('استان اقامت', max_length=500, blank=True)
    companyName = models.CharField('اسم شرکت', max_length=500, blank=True)
    investmentCeiling = models.CharField('سقف سرمایه گذاری', max_length=500, blank=True)
    howDidYouKnowUs = models.CharField('چگونه با ما آشنا شدید', max_length=500, blank=True)
    createdAt = models.DateTimeField('ساخته شده در', auto_now_add=True, blank=True)
    updatedAt = models.DateTimeField('به روز شده در', auto_now=True, blank=True)


class InvestorRegistration(models.Model):
    firstName = models.CharField('نام', max_length=500, blank=True)
    lastName = models.CharField('نام خانوادگی', max_length=500, blank=True)
    email = models.EmailField('تاریخ تولد', blank=True)
    birthDate = models.DateField('ایمیل', blank=True)
    countryOfResidence = models.CharField('کشور اقامت', max_length=500, blank=True)
    provinceOfResidence = models.CharField('استان اقامت', max_length=500, blank=True)
    companyName = models.CharField('اسم شرکت', max_length=500, blank=True)
    interests = models.CharField('علاقه ها', max_length=500, blank=True)
    preferredAreas = models.CharField('زمینه موردعلاقه', max_length=500, blank=True)
    howDidYouKnowUs = models.CharField('چگونه با ما آشنا شدید', max_length=500, blank=True)
    createdAt = models.DateTimeField('ساخته شده در', auto_now_add=True)
    updatedAt = models.DateTimeField('به روز شده در', auto_now=True)


class Entrepreuneur(models.Model):
    email = models.EmailField('ایمیل')
    companyName = models.CharField('نام شرکت', max_length=300)
    phone = models.CharField('شماره موبایل', max_length=300)
    website = models.CharField('سایت', max_length=500)
    fieldOfProfessional = models.CharField('زمینه حرفه ای', max_length=500)
    createdAt = models.DateTimeField('ساخته شده در', auto_now_add=True)
    updatedAt = models.DateTimeField('به روز شده در', auto_now=True)


class ApplyJob(models.Model):
    firstName = models.CharField('نام', max_length=500)
    lastName = models.CharField('نام خانوادگی', max_length=500)
    email = models.EmailField(verbose_name='ایمیل')
    phoneNumber = models.CharField('شماره موبایل', max_length=250, blank=True)
    cvFile = models.FileField(upload_to='cv-files', editable=True, null=True, blank=True)
    createdAt = models.DateTimeField('ساخته شده در', auto_now_add=True)
    updatedAt = models.DateTimeField('به روز شده در', auto_now=True)


class Handicraft(models.Model):
    first_name = models.CharField('نام', max_length=500)
    last_name = models.CharField('نام خانوادگی', max_length=500)
    email = models.EmailField(verbose_name='ایمیل')
    organization = models.CharField('سازمان', max_length=500)
    created_at = models.DateTimeField('ساخته شده در', auto_now_add=True)


class LandaGene(models.Model):
    full_name = models.CharField('نام کامل', max_length=500)
    email = models.EmailField(verbose_name='ایمیل')
    phone_number = models.CharField('شماره موبایل', max_length=250, blank=True)
    company_name = models.CharField('نام شرکت', max_length=500, blank=True, null=True)
    created_at = models.DateTimeField('ساخته شده در', auto_now_add=True)


class WorkWithUs(models.Model):
    your_position = models.CharField(max_length=250)
    type_of_contract = models.CharField(max_length=250)
    your_first_name = models.CharField(max_length=250)
    your_last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    your_field_of_study = models.CharField(max_length=250)
    your_subfield = models.CharField(max_length=250)
    cv_file = models.FileField(upload_to='workWithUs/cv_file', null=True, blank=True, editable=True)
    email = models.EmailField('ایمیل', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

