# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A learning/practice repository (GitHub: `constant-charnay/test-claude-code`) used by Constant
to get up to speed with Claude Code before a research internship. It is deliberately tiny.

Tracked content is a single script, `fibonacci.py`. There is no build system, no dependency
manifest, and no test suite.

## Running

```powershell
python fibonacci.py        # prints the first 10 Fibonacci numbers, one per line
python fibonacci.py 25     # prints the first 25
```

Use `python` (Python 3.13 is on PATH); `python3` is not available on this Windows machine.
`combien` is an optional positional int (default 10); a negative value exits via
`parseur.error(...)`.

## Conventions

- **All prose is French**: commit messages, docstrings, comments, `argparse` help and error
  strings. Match this when adding code.
- **`argparse` help/error strings are written without accented characters** (`a afficher`,
  `defaut`, `doit etre`) to stay safe in the Windows console. Docstrings and comments keep
  normal French accents. Preserve this split.
- Commit messages are short imperative-mood French sentences (e.g. "Ajoute une option en
  ligne de commande pour le nombre de termes").

## Not part of the project

`claude-code-onboarding/` is untracked personal onboarding notes (French). It is not code
and should not be committed or treated as project source.
