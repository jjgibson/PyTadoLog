#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Main module for running TadoLogger from commandline.'''
import datetime as dt

from . import TadoLogger


def main():
    '''Launch the TadoLogger.'''
    #TODO: Add argument parser to let user run logging or convert csv to excel
    with TadoLogger() as tl:
        tl.start()
    print(f'Logging ended at {dt.datetime.now()}')


if __name__ == '__main__':
    main()
