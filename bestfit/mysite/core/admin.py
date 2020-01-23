from django.contrib import admin
from .models import Test
from .models import Profile
from .models import result_db

class TestAdmin(admin.ModelAdmin):
    list_display = ('question', "option_1", "option_2", 'option_3', 'option_4', "answer")


admin.site.register(Test, TestAdmin)
admin.site.register(Profile)
admin.site.register(result_db)



