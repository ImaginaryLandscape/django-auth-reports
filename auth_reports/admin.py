import csv
from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import GroupAdmin
from django.http import HttpResponse

def export_as_csv(self, request, queryset):

    meta = self.model._meta
    domain = request.get_host()
    field_names = ['Group', 'Application', 'Model', 'Permission']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}-{}.csv'.format(domain, meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        permissions = Permission.objects.filter(group__id=obj.pk)
        for perm in permissions:
            row = writer.writerow([obj.name, perm.content_type.app_label, perm.content_type.name, perm.name])

    return response

class GroupsAdmin(GroupAdmin):
    actions = [export_as_csv]

admin.site.unregister(Group)
admin.site.register(Group, GroupsAdmin)
