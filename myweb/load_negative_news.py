import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myweb.settings")

import django
django.setup()

from myapp.models import NegativeTraining 


def save_negative_from_row(negative_row):
    negative = NegativeTraining()
    negative.s_no = negative_row[0]
    negative.title = negative_row[1]
    # positive.wine = Wine.objects.get(id=positive_row[2])
    # positive.rating = positive_row[3]
    # positive.pub_date = datetime.datetime.now()
    # positive.comment = positive_row[4]
    negative.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print("Reading from file " + str(sys.argv[1]))
        negative_df = pd.read_csv(sys.argv[1])
        print(negative_df)

        negative_df.apply(
            save_negative_from_row,
            axis=1
        )

        print("There are {} negative in DB".format(NegativeTraining.objects.count()))
        
    else:
        print("Please, provide negative file path")
