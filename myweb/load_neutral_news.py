import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myweb.settings")

import django
django.setup()

from myapp.models import NeutralTraining 


def save_neutral_from_row(neutral_row):
    neutral = NeutralTraining()
    neutral.s_no = neutral_row[0]
    neutral.title = neutral_row[1]
    # neutral.wine = Wine.objects.get(id=neutral_row[2])
    # neutral.rating = neutral_row[3]
    # neutral.pub_date = datetime.datetime.now()
    # neutral.comment = neutral_row[4]
    neutral.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print("Reading from file " + str(sys.argv[1]))
        neutral_df = pd.read_csv(sys.argv[1])
        print(neutral_df)

        neutral_df.apply(
            save_neutral_from_row,
            axis=1
        )

        print("There are {} neutrals in DB".format(NeutralTraining.objects.count()))
        
    else:
        print("Please, provide neutrals file path")
