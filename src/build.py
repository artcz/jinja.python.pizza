"""
Most of the content of the website is static and defined in pure html.
However, there are two generated elements
1. Program of the conference
2. List of Sponsors
"""

import csv
import os
from collections import namedtuple
from datetime import date, time
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


class Pizza:
    title = "Random Python Pizza"
    location = "Acme office, Office building, Street Name 13/37"
    date = date(2024, 2, 24)

    template_path = Path("../templates")

    # Sponsor Data
    Sponsor = namedtuple("Sponsor", "name logo url")
    sponsors_file = Path("../data/sponsors.csv")

    # Program Data
    ScheduleItem = namedtuple(
        "ScheduleItem", "time name speaker_name speaker_social speaker_photo css_class"
    )
    schedule_file = Path("../data/schedule.csv")


# Build Schedule
with open(Pizza.schedule_file) as fd:
    data = csv.DictReader(fd)
    Pizza.schedule = [Pizza.ScheduleItem(**row) for row in data]

# Sponsors section
with open(Pizza.sponsors_file) as fd:
    data = csv.DictReader(fd)
    Pizza.sponsors = [Pizza.Sponsor(**row) for row in data]

# Set up Jinja environment
loader = FileSystemLoader(Pizza.template_path)
env = Environment(loader=loader)
template = env.get_template("base.html")

# Here is the entire rendering, we output the file to stdout.
print(template.render({"pizza": Pizza}))
