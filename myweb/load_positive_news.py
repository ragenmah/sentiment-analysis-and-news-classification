import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myweb.settings")

import django
django.setup()

from myapp.models import PositiveTraining


def save_positive_from_row(positive_row):
    positive = PositiveTraining()
    positive.s_no = positive_row[0]
    positive.title = positive_row[1]
    # positive.wine = Wine.objects.get(id=positive_row[2])
    # positive.rating = positive_row[3]
    # positive.pub_date = datetime.datetime.now()
    # positive.comment = positive_row[4]
    positive.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print("Reading from file " + str(sys.argv[1]))
        positive_df = pd.read_csv(sys.argv[1])
        print(positive_df)

        positive_df.apply(
            save_positive_from_row,
            axis=1
        )

        print("There are {} positives in DB".format(PositiveTraining.objects.count()))
        
    else:
        print("Please, provide positives file path")
