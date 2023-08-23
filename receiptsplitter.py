from argparse import ArgumentParser
from decimal import Decimal
from pathlib import Path
import sys

def main():
    parser = ArgumentParser(
        prog='receiptsplitter',
    )
    parser.add_argument('file')
    args = parser.parse_args()
    file = Path(args.file)
    if not file.is_file():
        print(args.file, 'is not a file', file=sys.stderr)
        return
    csv = file.read_text(encoding='utf-8').split('\n')
    people = {}
    for line in csv:
        item = line.split(',')
        payees = item[2].split(' ')
        if not payees:
            print('No payees for item', line)
            continue
        amount = Decimal(item[1]) / len(payees)
        for person in payees:
            people[person] = people.get(person, 0) + amount
    for person, amount in people.items():
        print(f'{person}:\t£{amount:.3f}')


if __name__ == '__main__':
    main()
