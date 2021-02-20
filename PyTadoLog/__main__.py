#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Main module for running TadoLogger from commandline.'''

from . import TadoLogger


def main():
    '''Launch the TadoLogger.'''
    #TODO: Add argument parser to let user run logging or convert csv to excel
    tl = TadoLogger()
    try:
        tl.start()
    except KeyboardInterrupt:
        print('\nInterrupted: Cancelling next event.')
        tl.cleanup()


if __name__ == '__main__':
    main()
