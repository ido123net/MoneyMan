import random

import tqdm
from django.core.management.base import BaseCommand
from faker import Faker

from expenses.models import Expense


class Command(BaseCommand):
    help = 'Create fake expenses'

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int)

    def handle(self, amount, *args, **options):
        faker = Faker()
        for _ in tqdm.tqdm(range(amount)):
            Expense.objects.create(
                title=faker.sentence(),
                amount=str(random.randint(100, 10000) / 100),
                date=faker.date_this_decade(),
            )
