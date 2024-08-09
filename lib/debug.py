#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.bucket import Bucket
from models.item import Item
import ipdb

def reset_database():
    Bucket.drop_table()
    Item.drop_table()
    Item.create_table()
    Bucket.create_table()

    travel = Bucket.create("Travel")
    job = Bucket.create("Job")

    Item.create("Austria", "Visit for a couple weeks.", travel.id)
    Item.create("Italy", "Visit for a week.", travel.id)
    Item.create("Front-End Developer", "This is one of my dream jobs", job.id)
    Item.create("Back-end Developer", "One of the jobs id like to have", job.id)
    

reset_database()
ipdb.set_trace()

