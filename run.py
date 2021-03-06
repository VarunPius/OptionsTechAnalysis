#####################################################################
# Author      : Varun Pius Rodrigues                               ##
# File        : run.py                                             ##
# Description : Main program                                       ##
#####################################################################

# Standard Packages
import argparse

# Project Packages:
import lib.tracker as tracker


def main():
    arg_parser = argparse.ArgumentParser(description='List of stocks to track')
    arg_parser.add_argument('--ticker', '-t', help='Enter list of stocks', nargs='+', default=['VOO', 'VTI']) # nargs = + for variable arguments
    args = arg_parser.parse_args()
    ticker = args.ticker
    print(ticker)
    price_dict = tracker.track_market(ticker)
    print(price_dict)
