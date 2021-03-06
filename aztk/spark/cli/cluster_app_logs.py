import argparse
import typing
import time
from aztk.aztklib import Aztk
from aztk import utils

def setup_parser(parser: argparse.ArgumentParser):
    parser.add_argument('--id',
                        dest='cluster_id',
                        required=True,
                        help='The unique id of your spark cluster')
    parser.add_argument('--name',
                        dest='app_name',
                        required=True,
                        help='The unique id of your job name')

    parser.add_argument('--tail', dest='tail', action='store_true')


def execute(args: typing.NamedTuple):
    aztk = Aztk()

    if args.tail:
        utils.stream_logs(client=aztk.client, cluster_id=args.cluster_id, application_name=args.app_name)
    else:
        app_logs = aztk.client.get_application_log(cluster_id=args.cluster_id, application_name=args.app_name)
        print(app_logs.log)