import csv
# import openpyxl
# from openpyxl.cell import get_column_letter
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied


def exportar_csv(modeladmin, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied
    opts = queryset.model._meta
    model = queryset.model.__name__
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f"attachment;filename={model}.csv"
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]
    writer.writerow(field_names)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response


exportar_csv.short_description = "Exportar a csv"


# def export_xlsx(modeladmin, request, queryset):
#     response = HttpResponse(
#         content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = f'attachment; filename={queryset.model.__name__}.xlsx'
#     wb = openpyxl.Workbook()
#     ws = wb.get_active_sheet()
#     ws.title = "MyModel"

#     row_num = 0

#     columns = [
#         (u"ID", 15),
#         (u"Title", 70),
#         (u"Description", 70),
#     ]

#     for col_num in xrange(len(columns)):
#         c = ws.cell(row=row_num + 1, column=col_num + 1)
#         c.value = columns[col_num][0]
#         c.style.font.bold = True
#         # set column width
#         ws.column_dimensions[get_column_letter(col_num+1)].width = columns[col_num][1]

#     for obj in queryset:
#         row_num += 1
#         row = [
#             obj.pk,
#             obj.title,
#             obj.description,
#         ]
#         for col_num in xrange(len(row)):
#             c = ws.cell(row=row_num + 1, column=col_num + 1)
#             c.value = row[col_num]
#             c.style.alignment.wrap_text = True

#     wb.save(response)
#     return response

# export_xlsx.short_description = u"Export XLSX"
