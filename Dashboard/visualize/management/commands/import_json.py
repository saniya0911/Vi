import json
from django.core.management.base import BaseCommand
from django.db import transaction
from visualize.models import MarketReport
from datetime import datetime
from dateutil.parser import parse

from django.conf import settings

class Command(BaseCommand):
    help= "Import external json file into django database."
    def handle(self, *args, **kwargs):
            with open(r"visualize/management/commands/json_data.json", 'r', encoding='utf8') as json_file:
                data = json.load(json_file)
            #with transaction.atomic():  # Wrap the data import in a transaction
                for entry in data:
                    # Parse date strings to datetime objects
                    published = entry.get('published', '')
                    added = entry.get('added', '')
                    intensity = entry.get('intensity', 0)
                    likelihood=entry.get('likelihood', 0)
                    relevance=entry.get('relevance', 0)
                    if published !='':
                        published = parse(published)
                    else:
                         published = None
                    if added != '':
                        added = parse(added)
                    else:
                        added = None
                    if intensity == '':
                        intensity=0
                    if relevance == '':
                        relevance=0
                    if likelihood == '':
                        likelihood=0

                    market_report = MarketReport.objects.create(
                        end_year=entry.get('end_year', ''),
                        intensity=intensity,
                        sector=entry.get('sector', ''),
                        topic=entry.get('topic', ''),
                        insight=entry.get('insight', ''),
                        url=entry.get('url', ''),
                        region=entry.get('region', ''),
                        start_year=entry.get('start_year', ''),
                        impact=entry.get('impact', ''),
                        added=added,
                        published=published,
                        country=entry.get('country', ''),
                        relevance=relevance,
                        pestle=entry.get('pestle', ''),
                        source=entry.get('source', ''),
                        title=entry.get('title', ''),
                        likelihood=likelihood,
                    )
                    market_report.save()
                    