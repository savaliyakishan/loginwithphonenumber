from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self,phone,password =None,**extra_fields):
        if not phone:
            raise ValueError('Phone required')

        # user = self.model(email=email, **extra_fields)
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be a staff'
            )
        
        return self.create_user(phone, password, **extra_fields)