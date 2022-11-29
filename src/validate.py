import csv
from datetime import datetime

def validate_sum(sum: str) -> bool:
    try:
        float(sum)
        return True
    except ValueError:
        raise Exception(f'wrong sum={sum}')

def validate_string(string: str) -> bool:
    clean_string = string.strip()
    if not (clean_string != '' and clean_string != '-'):
        raise Exception(f'wrong string={string}')
    return True


def validate_date(date: str) -> bool:
    try:
        date = datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        raise Exception(f'wrong date={date}')

def validate_id(id: str) -> bool:
    try:
        int(id)
        return True
    except ValueError:
        raise Exception(f'wrong Id={id}')

async def validate_csv(csv_lines: list[str]) -> list[tuple[str]]:
    bills_reader = csv.reader(csv_lines, delimiter=',')
    rows = []

    for i, row in enumerate(bills_reader):
        validate_string(row[0])
        validate_string(row[1])
        validate_id(row[2])
        validate_sum(row[3])
        validate_date(row[4])
        validate_string(row[5])

        rows.append(tuple(row))

    return rows
