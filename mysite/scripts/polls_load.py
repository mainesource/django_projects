import csv #hhtps://docs.python.org/3/kibrary/csv.html

import datetime
from django.utils import timezone

from polls.models import Question, Choice

def run():
    print("=== Polls Loader")

    Choice.objects.all().delete()
    Question.objects.all().delete()
    print("=== Objects deleted")

    with open('scripts/dj4e_batch.csv') as fhand:
        reader = csv.reader(fhand)
        next(reader) # Advance past the header
        
        for row in reader:
            print(row)

            # Replace these comments to 

            # Make a new Question and save it
            q = Question(question_text=row[0], pub_date=timezone.now())
            q.save()
            #Loop through the choice strings in row[1:] and add each choice,
            for choice in row[1:]:
                # connect it to the question and save it
                q.choice_set.create(choice_text=choice, votes=0)
                q.save()

    print("=== Load Complete")
