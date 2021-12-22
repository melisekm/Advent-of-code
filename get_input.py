import argparse
import subprocess

with open("../session.txt") as session_file:
    SESSION = session_file.read()

parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2021)
parser.add_argument('--day', type=int, default=2)
args = parser.parse_args()

cmd = 'curl https://adventofcode.com/{}/day/{}/input --cookie "session={}"'.format(
    args.year, args.day, SESSION)
output = subprocess.check_output(cmd, shell=True)
output = output.decode('UTF-8')

with open(f"../{args.year}/day{args.day}/in.txt", 'w', encoding="UTF-8") as infile:
    infile.write(output)
