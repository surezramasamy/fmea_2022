from django.db import models

class Add_Part(models.Model):
    Model_name = models.CharField(max_length=256,null=False,blank=False, unique=True)
    def __str__(self):
        return self.Model_name
        #return '%s' % (self.Model_name)


class Add_Process_or_Function(models.Model):
    Process_or_function_name=models.CharField(max_length=256,blank=True,null=True)

    def __str__(self):
        return str(self.Process_or_function_name)
        

from django.utils import timezone
from django.urls import reverse




class Fmea_Record(models.Model):
    date = models.DateField(default=timezone.now)
    Part_Name=models.ManyToManyField(Add_Part,blank=True,null=True)
    Process_OR_Function = models.ForeignKey(Add_Process_or_Function,on_delete=models.CASCADE,blank=True,null=True)
    Potential_Failure_Mode = models.CharField(max_length=256)
    Potential_Effects_of_Failure=models.CharField(max_length=256)
    Sev_Choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10))
    Sev=models.PositiveIntegerField(choices=Sev_Choices,help_text="[No effect=1] [Appearance/Noise rarely noticed by customer=2] [Appearance/Noise noticed by customer=3] [Appearance/Noise noticed by most of customer=3] [Vehicle,convenience operable,Low performance=5] [Reduction in convenience and comfort function=6][Fit-issue,Reduction in primary function=7][vehicle not operate=8][Affect safety,Govt Regul NC,with warning=9][Affect safety,Govt Reg NC,without warning=10]")
    Class=models.CharField(max_length=10,blank=True,null=True)
    Potential_causes_or_Mechanisms_of_Failure=models.CharField(max_length=256)
    Occ_Choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10))
    Occ=models.PositiveIntegerField(choices=Occ_Choices,help_text="[No failure=1]   [1 in 10,00,000 =2] [1 in 100000=3] [1 in 10000=4], [1 in 2000=5] [1 in 500=5] [1 in 100=7] [1 in 50 = 8] [1 in 20=9] [1 in 10=10]")
    Current_Process_Control_Prevention=models.CharField(max_length=256)
    Current_Process_Control_Detection=models.CharField(max_length=256)
    Det_Choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10))
    Det=models.PositiveIntegerField(choices=Det_Choices,help_text="[Design prevention=1 [Error proof prevent Error=2][Automated controls during process=3][Automated controls after process=4][Variable gauge,setup,Buzzer alarm during process=5][Attribute gauge,Manual torque during process=6][Post process/Final inspection=7][Visual,Noise inspection post process=8],[Random_audit=9][No detection method=10]")
    Recommended_Actions=models.CharField(max_length=256,blank=True,null=True)
    Resp_Target_Date=models.CharField(max_length=256,blank=True,null=True)
    Actions_Taken=models.CharField(max_length=256,blank=True,null=True)
    Sev_Rev=models.IntegerField(blank=True,null=True)
    Occ_Rev=models.IntegerField(blank=True,null=True)
    Det_Rev=models.IntegerField(blank=True,null=True)
    Rev_No=models.IntegerField(blank=True,null=True)
    Rev_Date=models.DateField(default=timezone.now,blank=True,null=True)
    Rev_History=models.CharField(max_length=256,blank=True,null=True)



    def RPN(self):
        fields=[self.Sev,self.Occ,self.Det]
        for i in fields:
            if i is not None:
                return int(self.Sev*self.Occ*self.Det)
            else:
                return None




    def RPN_Rev(self):
        fields=[self.Sev_Rev,self.Occ_Rev,self.Det_Rev]
        for i in fields:
            if i is not None:
                return int(self.Sev_Rev*self.Occ_Rev*self.Det_Rev)
            else:
                return None

    def part_names(self):
        return "\n".join([p.Model_name for p in self.Part_Name.all()])