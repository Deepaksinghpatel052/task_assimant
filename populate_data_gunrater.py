import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','home.settings')

import django

django.setup()

# FAKE DATA SCRIPT
import rendom

from home.models import webpage

from faker import Faker

fakegen = Faker()


def get_company_data(N=10):

    for entry in range(N):
        # crete fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        new_ins = webpage.objects.get_or_create(CompanyName=fake_name,CompanyURL=fake_url,Created_date=fake_date)[0]


if __name__ == '__main__':
    print("run script")
    get_company_data(100)
    print("run script compplate")