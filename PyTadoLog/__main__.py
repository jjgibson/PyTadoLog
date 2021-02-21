#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Main module for running TadoLogger from commandline.'''
import argparse
import datetime as dt

from . import TadoLogger


def main():
    '''Launch the TadoLogger.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--outdir', help='Path to output directory')
    parser.add_argument('--update-period', type=int,
                        help='Time in seconds between updates',
                        )
    parser.add_argument('--last-day', help='Last day of week as 3 letter string')
    parser.add_argument('-m', '--multiprocessing', action='store_true',
                        help='Use separate processed for web query and csv saving')
    args = parser.parse_args()
    with TadoLogger(args.outdir,
                    args.update_period,
                    args.last_day,
                    args.multiprocessing,
                    ) as tl:
        tl.start()
    print(f'Logging ended at {dt.datetime.now()}')


if __name__ == '__main__':
    main()
