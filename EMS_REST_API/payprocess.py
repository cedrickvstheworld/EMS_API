from datetime import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMS_REST_API_project.settings')
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
from EMS_REST_API.models import GlobalConfig

class PayProcess:
    def __init__(self, income, day_of_pay):
        self.pay = income
        self.pay_day = day_of_pay
        self.global_config = GlobalConfig.objects.last()

    def tax_contrib(self):
        tax_candidate_income = self.global_config.tax_income_candidate
        tax_rate = self.global_config.tax_contrib_rate
        if self.pay_day == self.global_config.tax_pay_day:
            if self.pay > tax_candidate_income:
                return self.pay * tax_rate
            return 0
        return 0

    def sss_contrib(self):
        sss_rate = self.global_config.sss_contrib_rate
        if self.pay_day == self.global_config.sss_pay_day:
            return self.pay * sss_rate
        return 0

    def philhealth_contrib(self):
        philhealth_rate = self.global_config.philhealth_contrib_rate
        if self.pay_day == self.global_config.philhealth_pay_day:
            return self.pay * philhealth_rate
        return 0

    def pagibig_contrib(self):
        pagibig_rate = self.global_config.pagibig_contrib_rate
        if self.pay_day == self.global_config.pagibig_pay_day:
            return self.pay * pagibig_rate
        return 0

    def get_contributions(self):
        total_contrib = sum([self.tax_contrib(), self.sss_contrib(),
                             self.pagibig_contrib(), self.philhealth_contrib()])
        return total_contrib


# x = PayProcess(7000, 20)
#
# print(x.get_contributions())