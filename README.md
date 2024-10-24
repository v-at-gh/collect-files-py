# File Collector by Extension

This Python script recursively scans a given directory and collects files based on their extensions. It can print the output to the console or save it to a JSON file. The script is flexible, supporting indentation for pretty-printing the JSON output.

## Features

- **Directory Scanning**: Specify the directory to scan, including repositories.
- **File Filtering**: Automatically skips the `.git` directory but includes other hidden files and folders (e.g., `.gitpod.yml`, `.github`).
- **JSON Output**: Collects files by extension, either pretty-printed or compact, and outputs the result as JSON.
- **Flexible Output Options**: Output can be printed to the console or saved to a file.

## Requirements

- Python 3.x

## Usage

### Command-line Arguments

- `--dir`, `-d` (required): Directory of the repository to scan.
- `--outfile`, `-o`: File path where the JSON output will be saved. If not provided, output is printed to the console.
- `--stdout`, `-s`: If specified, the JSON output is printed to the console.
- `--indent`, `-i`: Indentation level for pretty-printing the JSON (optional). By default, the JSON is output in compact form (no indentation).

### Example Commands

#### Print to console with indentation:

```bash
$ collect-files.py --dir ~/data/src/github/user/repo --stdout --indent 2
```

This will scan the repository located in `~/data/src/github/user/repo`, and print the list of files organized by extension, with the JSON formatted using 2-space indentation.

#### Save to a JSON file:

```bash
$ collect-files.py -d ~/another-repo --outfile /mnt/data/another-repo.files.json
```

This will save the result as a compact JSON file (`/mnt/data/another-repo.files.json`).

#### Default behavior (prints compact JSON to console):

```bash
$ collect-files.py --dir ~/data/src/github/user/repo
```

This prints the output in a compact form to the console.

## Example Output

A sample JSON output from scanning a repository might look like this:

```json
{
    "Without_extension": [
        "/path/to/repo/Makefile"
    ],
    "py": [
        "/path/to/repo/file1.py",
        "/path/to/repo/subdir/file2.py"
    ],
    "md": [
        "/path/to/repo/README.md"
    ]
}
```

## License

This project is licensed under the MIT License.
