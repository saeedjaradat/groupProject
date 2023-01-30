from django.db import models
import  re
import bcrypt

class Usermanager(models.Manager):
    def employee_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        password_regex =re.compile(r'^[a-zA-Z0-9.+_-]')
        special_symbols = ['$','@','#','%','^','&']

        if len(postData['full_name']) < 2:
            errors["full_name"] = "user full_name should be at least 2characters"
        if len(postData['user_level']) < 2:
            errors["user_level"] = "user_level should be at least 2characters"
        if len(postData['experience']) < 2:
            errors["experience"] = "experience should be at least 2characters"
        if len(postData['mobile_num']) < 9:
            errors["mobile_num"] = "number should be at least 9characters"
        if len(postData['Address']) < 2:
            errors["Address"] = "Address should be at least 2characters"
        if len(postData['skill']) < 2:
            errors["skill"] = "skill should be at least 2characters"
        if len(postData['password']) < 8:
            errors["password"] = "user password should be at least 8characters"
        if len(postData['cpassword']) <8:
            errors["cpassword"] = "user cpassword should be at least 8characters"
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if not any(characters.isupper() for characters in postData['password']):
            errors['password_notInclude_upper'] = "Password must have at least one uppercase character"
        if not any(characters.islower() for characters in postData['password']):
            errors['password_notInclude_lower'] = "Password must have at least one lowercase character"
        if not any(characters.isdigit() for characters in postData['password']):
            errors['password_notInclude_number'] = "Password must have at least one numeric character."
        if not any(characters in special_symbols for characters in postData['password']):
            errors['password_symbol'] = "Password should have at least one of the symbols $@#%^&"
        return errors

    def customer_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        password_regex =re.compile(r'^[a-zA-Z0-9.+_-]')
        special_symbols = ['$','@','#','%','^','&']

        if len(postData['full_name']) < 2:
            errors["full_name"] = "name should be at least 2characters"
        if len(postData['Address']) < 2:
            errors["Address"] = "Address should be at least 2characters"
        if len(postData['mobile_num']) < 9:
            errors["mobile_num"] = "number should be at least 9characters"
        if len(postData['identity_num']) < 10:
            errors["identity_num"] = "scope of work should be at least 10characters"
        if len(postData['password']) < 8:
            errors["password"] = "user password should be at least 8characters"
        if len(postData['cpassword']) <8:
            errors["cpassword"] = "user cpassword should be at least 8characters"
        return errors





class customer(models.Model):
    full_name=models.CharField(max_length=255)
    identity_num=models.IntegerField()    
    Address=models.CharField(max_length=255)
    mobile_num=models.IntegerField()
    password=models.CharField(max_length=255)
    cpassword=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    objects = Usermanager()
    
    

class employee(models.Model):
    full_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    skill=models.CharField(max_length=255)
    experience=models.IntegerField()
    Address=models.CharField(max_length=255)
    mobile_num=models.IntegerField()
    password=models.CharField(max_length=255)
    cpassword=models.CharField(max_length=255)
    user_level=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    personal_picture=models.FieldFile()
    objects = Usermanager()
    customers=models.ManyToManyField(customer,related_name='employees')
    
class ticket(models.Model):
    service_type=models.CharField(max_length=255)
    service_description=models.CharField(max_length=255)
    employee_name=models.CharField(max_length=255)
    mobile_num=models.IntegerField()
    Address=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    customers=models.ForeignKey(customer,related_name='tickets',on_delete=models.DO_NOTHING)
    employess=models.ForeignKey(employee,related_name='tickets',on_delete=models.DO_NOTHING)

class notification (models.Model):
    description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    employess=models.ForeignKey(employee,related_name='notifications',on_delete=models.DO_NOTHING)
    customers=models.ForeignKey(customer,related_name='notifications',on_delete=models.DO_NOTHING)


class review(models.Model):
    description:models.CharField(max_length=255)
    stars=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    employess=models.ForeignKey(employee,related_name='reviews',on_delete=models.DO_NOTHING)
    customers=models.ForeignKey(customer,related_name='reviews',on_delete=models.DO_NOTHING)

class message(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    sender_employee=models.CharField(max_length=255)
    reciever_employee=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    employess=models.ForeignKey(employee,related_name='messages',on_delete=models.DO_NOTHING)






