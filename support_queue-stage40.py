# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: SupportQueue
def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='SupportQueue CLI')
    sub = parser.add_subparsers(dest='command')

    # create
    p = sub.add_parser('create')
    p.add_argument('--ticket-id', required=True)
    p.add_argument('--subject', required=True)
    p.add_argument('--priority', default='medium')
    p.add_argument('--status', default='open')
    p.add_argument('--description', default='')

    # update
    p = sub.add_parser('update')
    p.add_argument('--ticket-id', required=True)
    p.add_argument('--status', default=None)
    p.add_argument('--priority', default=None)
    p.add_argument('--description', default=None)
    p.add_argument('--add-tag', action='append', default=[])

    # delete
    sub.add_parser('delete').add_argument('--ticket-id', required=True)

    # list
    p = sub.add_parser('list')
    p.add_argument('--status', default=None)
    p.add_argument('--priority', default=None)

    # show
    sub.add_parser('show').add_argument('--ticket-id', required=True)

    return parser.parse_args(argv)
