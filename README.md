# Treescriptify
Get Started fast with TreeScript generated from an existing directory.

## How To Use
Run the main script in a directory to treescript-ify it.

1. Pipe program output to a file, or
2. Display it on-screen for copy-paste workflow integration.

## How To Install
You can manually install a release (if you want), or use pip.

`pip install treescriptify`

## Command Line Options

1. Hidden Files and Directories
   - `-a` or `--hide`
   - Either argument will hide.
2. Directories Only
   - `-d` or `--directories`
3. Prune Empty Directories
   - `-p` or `--prune`
4. Tree Depth
   - Example: `--depth 4`
   - The maximum number of parent directories in the tree.
5. Number Labels
   - `-n` or `--number-labels`
   - Insert Line Number DataLabels into TreeScript output.

## Features In Progress

- Gitignore Patterns
   - `--gitignore` or `--no-gitignore`
   - Either argument disables Gitignore, which is on by default.
