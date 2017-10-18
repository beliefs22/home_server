import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('vin', help='directory to search videos for.')
parser.add_argument('ftype', help='video type to search for')
parser.add_argument('-vout', help='directory to save converted video too. If blank will save in vin')
parser.add_argument('-threads', type=int, choices=range(1, 9), help='Number of threads to limit ffmpeg to')

args = parser.parse_args(sys.argv[1:])
print(args.vin, args.ftype, args.vout, args.threads)
