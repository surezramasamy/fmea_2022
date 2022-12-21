from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


from django.contrib import admin






from .models import Fmea_Record
from import_export.fields import Field
from import_export import fields, resources
from Fmea.models import Add_Part,Add_Process_or_Function
from django.utils import timezone
from datetime import datetime
from import_export.widgets import ManyToManyWidget,ForeignKeyWidget

class BookResource_fmea(resources.ModelResource):
    
    Part_Name = fields.Field(column_name='Part_Name', attribute='Part_Name', widget=ManyToManyWidget(Add_Part, field='Model_name'))
    Process_OR_Function = fields.Field(
        column_name='Process_OR_Function',
        attribute='Process_OR_Function',
        widget=ForeignKeyWidget(Add_Process_or_Function, 'Process_or_function_name'))

    RPN = fields.Field(attribute = 'RPN')
    RPN_Rev = fields.Field(attribute = 'RPN_Rev')

    class Meta:

        model = Fmea_Record
        



        fields = ('id','Part_Name','date','Process_OR_Function','Potential_Failure_Mode','Potential_Effects_of_Failure',
                  'Sev','Class','Potential_causes_or_Mechanisms_of_Failure','Occ','Current_Process_Control_Prevention',
                  'Current_Process_Control_Detection','Det','RPN','Recommended_Actions','Resp_Target_Date','Actions_Taken',
                  'Sev_Rev','Occ_Rev','Det_Rev','RPN_Rev','Rev_No','Rev_Date','Rev_History')

        export_order = ('Part_Name','date','Process_OR_Function','Potential_Failure_Mode','Potential_Effects_of_Failure',
                  'Sev','Class','Potential_causes_or_Mechanisms_of_Failure','Occ','Current_Process_Control_Prevention',
                  'Current_Process_Control_Detection','Det','RPN','Recommended_Actions','Resp_Target_Date','Actions_Taken',
                  'Sev_Rev','Occ_Rev','Det_Rev','RPN_Rev','Rev_No','Rev_Date','Rev_History')





class BookAdmin_fmea(ImportExportModelAdmin,admin.ModelAdmin):

    resource_class = BookResource_fmea
    class Meta:
        model = Fmea_Record

    list_display = ['id','date','part_names','Process_OR_Function','Potential_Failure_Mode','Potential_Effects_of_Failure',
              'Sev','Class','Potential_causes_or_Mechanisms_of_Failure','Occ','Current_Process_Control_Prevention',
              'Current_Process_Control_Detection','Det','RPN','Recommended_Actions','Resp_Target_Date','Actions_Taken',
              'Sev_Rev','Occ_Rev','Det_Rev','RPN_Rev','Rev_No','Rev_Date','Rev_History']
    list_filter = ['Part_Name','Process_OR_Function','Current_Process_Control_Prevention','Current_Process_Control_Detection']
    search_fields  =['Part_Name__Model_name','Process_OR_Function__Process_or_function_name','Potential_Failure_Mode','Potential_Effects_of_Failure','Current_Process_Control_Prevention','Current_Process_Control_Detection']


admin.site.register(Add_Part)
admin.site.register(Add_Process_or_Function)
admin.site.register(Fmea_Record,BookAdmin_fmea)


