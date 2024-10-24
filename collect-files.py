#!/usr/bin/env python3

from argparse import ArgumentParser
from collections import defaultdict
from json import dumps as json_dumps
from os import walk as os_walk
from pathlib import Path

def get_repo_path(path_str) -> Path:
    return Path(path_str).expanduser()

def collect_files_by_extension(repo_path):
    files = defaultdict(list)
    files['Without_extension'] = []

    for root, dirs, file_names in os_walk(repo_path):
        dirs[:] = [d for d in dirs if d != '.git']
        for file_name in file_names:
            file_path = f"{root}/{file_name}"
            if '.' in file_name:
                files[file_name.rsplit('.', 2)[-1]].append(file_path)
            else:
                files['Without_extension'].append(file_path)
    
    return files

def main():
    parser = ArgumentParser(description='Collect files by extension from a repository.')

    parser.add_argument('--dir', '-d', required=True, help='Directory of the repository to scan.')
    parser.add_argument('--outfile', '-o', help='File to write the output (default: prints to stdout).')
    parser.add_argument('--stdout', '-s', action='store_true', help='Print the result to stdout.')
    parser.add_argument('--indent', '-i', type=int, default=None, help='Indentation level for JSON output (default: no indent).')

    args = parser.parse_args()

    repo_path = get_repo_path(args.dir)

    files = collect_files_by_extension(repo_path)

    if args.indent is not None:
        json_output = json_dumps(files, indent=args.indent)
    else:
        json_output = json_dumps(files)

    if args.stdout:
        print(json_output)
    elif args.outfile:
        with open(args.outfile, 'w', encoding='utf-8') as outfile:
            outfile.write(json_output)
    else:
        print(json_output)

if __name__ == '__main__':
    main()
