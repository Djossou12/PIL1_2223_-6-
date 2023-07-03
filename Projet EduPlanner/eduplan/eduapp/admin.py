from django.contrib import admin
from .models import IA_1
from .models import IA_2
from .models import IA_3

from .models import IM_1
from .models import IM_2
from .models import IM_3

from .models import GL_1
from .models import GL_2
from .models import GL_3

from .models import SEIOT_1
from .models import SEIOT_2
from .models import SEIOT_3

from .models import SI_1
from .models import SI_2
from .models import SI_3

from .models import Member

admin.site.register(IA_1)
admin.site.register(IA_2)
admin.site.register(IA_3)

admin.site.register(IM_1)
admin.site.register(IM_2)
admin.site.register(IM_3)

admin.site.register(GL_1)
admin.site.register(GL_2)
admin.site.register(GL_3)

admin.site.register(SEIOT_1)
admin.site.register(SEIOT_2)
admin.site.register(SEIOT_3)

admin.site.register(SI_1)
admin.site.register(SI_2)
admin.site.register(SI_3)

admin.site.register(Member)