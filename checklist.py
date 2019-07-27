#!/usr/bin/env python3
import argparse
import os
import sys

__version__ = '0.2'

def main():
    args = parse_args()
    for filename in args.files:
        tasks = get_tasks_from_file(filename)
    for task in tasks:
        clear_cli()
        print(''.join(task))
        input('Press enter to continue')

def parse_args():
    parser = argparse.ArgumentParser(argument_default=None)
    parser.add_argument('files', nargs='*', default=[], help='Files to process')
    arg = parser.parse_args()
    if not arg.files:
        raise Exception('Filename required')
    return arg

def get_tasks_from_file(filename):
    lines = read_file(filename)
    tasks = detect_tasks(lines)
    return tasks

def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def detect_tasks(lines):
    tasks = []
    task_lines = []
    for line in lines:
        if line[0:2] == '# ':
            tasks.append(''.join(task_lines))
            task_lines.clear()
        task_lines.append(line)
    tasks.append('\n'.join(task_lines))
    return tasks[1:]

def clear_cli():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()