from django.db import models


class Backend(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=50)

    def _str_(self):
        return self.name

class User(models.Model):
    username = models.CharField(default='username', max_length=45)
    password1 = models.CharField(default='password1', max_length=45)
    password2 = models.CharField(default='password2', max_length=45)
    firstname = models.CharField(default='firstname', max_length=45)
    middlename = models.CharField(default='middlename', max_length=45)
    lastname = models.CharField(default='lastname', max_length=45)
    gender = models.CharField(default='gender', max_length=45)
    type_of_user = models.CharField(default='user type', max_length=45)
    phone1 = models.IntegerField(null=True)
    phone2 = models.IntegerField(null=True)
    address1 = models.CharField(default='address1', max_length=45)
    address2 = models.CharField(default='address2', max_length=45)
    dob_day = models.CharField(default='DD', max_length=45)
    dob_month = models.CharField(default='MM', max_length=45)
    dob_year = models.CharField(default='0000', max_length=45)
    cityofbirth = models.CharField(default='city', max_length=45)
    countryofbirth = models.CharField(default='country', max_length=45)
    marital_status = models.CharField(default='relationship status', max_length=45)
    number_of_children = models.CharField(default='children?', max_length=45)
    occupation = models.CharField(default='job', max_length=45)
    employer_name = models.CharField(default='employer', max_length=45)
    employer_address = models.CharField(default='employer address', max_length=45)
    email = models.EmailField(default='email')









class Student_Hollow_Year(models.Model):
    #username = models.ForeignKey(User, on_delete=models.CASCADE)
    hollow_year = models.CharField(max_length=45)
    activities = models.CharField(max_length=45)

class School(models.Model):
    schoolID = models.CharField(max_length=45)
    school_name = models.TextField(max_length=45)
    school_address = models.CharField(max_length=45)
    type_of_school = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    country_province = models.CharField(max_length=45)
    em_contact = models.CharField(max_length=45)
    em_contact_num1 = models.IntegerField(null=True)
    em_contact_num2 = models.IntegerField(null=True)

class Tuition_Fees(models.Model):
    schoolID = models.ForeignKey(School, on_delete=models.CASCADE)
    academic_level = models.CharField(max_length=15)
    academic_year = models.IntegerField(null=True)
    tuition = models.IntegerField(null=True)
    clothing = models.CharField(max_length=45)
    furniture = models.CharField(max_length=45)
    books = models.CharField(max_length=45)
    misc = models.CharField(max_length=45)


class Student_Education(models.Model):
    schoolID = models.ForeignKey(School, on_delete=models.CASCADE)
    #username = models.ForeignKey(User, on_delete=models.CASCADE)
    year_attended = models.CharField(max_length=45)
    Class = models.CharField(max_length=45)
    grade = models.IntegerField(null=True)
    degree = models.CharField(max_length=45)
    rank = models.CharField(max_length=45)
    dismissed = models.CharField(max_length=45)
    dismissed_reason = models.CharField(max_length=45)



class Scholarship(models.Model):
    scholarshipID = models.CharField(max_length=12)
    denomination = models.TextField(max_length=40)
    referred_studies = models.CharField(max_length=25)
    amount = models.IntegerField(null=True)
    academic_year = models.DateField(max_length=10)
    description = models.CharField(max_length=20)

class Student_Scholarship(models.Model):
    scholarshipID = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    #username = models.ForeignKey(User, on_delete=models.CASCADE)
    awarded_on = models.CharField(max_length=45)
    delivery_method = models.CharField(max_length=45)
    award_justification = models.CharField(max_length=45)
    awarded_amount = models.CharField(max_length=45)

class Scholarship_Donation(models.Model):
     scholarshipID = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
     #donorID = models.ForeignKey(User, on_delete=models.CASCADE)
     amount = models.IntegerField(null=True)
     academic_year = models.IntegerField(null=True)





