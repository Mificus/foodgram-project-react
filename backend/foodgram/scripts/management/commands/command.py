import csv
import os

import psycopg2
from django.core.management.base import BaseCommand
from tags_ingr.models import Ingredient

HOST = os.getenv('DB_HOST')
NAME = os.getenv('POSTGRES_DB')
USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')


class Command(BaseCommand):
    help = 'Добавление записей в БД из файлов .csv'
    conn = psycopg2.connect(
        f'host={HOST} dbname={NAME} user={USER} password={PASSWORD}'
    )
    cur = conn.cursor()

    def add_arguments(self, parser):
        """Аргументы для пути к файлу .csv и имени таблицы."""
        parser.add_argument('path', type=str, help='Путь к файлу .csv')
        parser.add_argument(
            'tab_name', type=str, help='Имя таблицы postgresql')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        table = kwargs['tab_name']
        try:
            with open(path, 'r') as file:
                data = csv.reader(file)
                for row in data:
                    name, measurement_unit = row
                    for row in data:
                        name, measurement_unit = row
                        Ingredient.objects.get_or_create(
                            name=name,
                            measurement_unit=measurement_unit
                        )
        except FileNotFoundError:
            raise CommandError('Добавьте файл ingredients в директорию data')