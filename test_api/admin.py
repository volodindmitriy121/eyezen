from django.contrib import admin

import test_api.models as m

admin.site.register(m.User)
admin.site.register(m.Sensor)
admin.site.register(m.Operator)
admin.site.register(m.ResqueTeam)
admin.site.register(m.Territory)
#admin.site.register(m.User)
#admin.site.register(m.User)