# pre-commit-hooks [![tag](https://img.shields.io/github/tag/namelivia/pre-commit-hooks.svg)](https://github.com/namelivia/pre-commit-hooks/releases) [![Build Status](https://travis-ci.org/namelivia/pre-commit-hooks.svg?branch=master)](https://travis-ci.org/namelivia/pre-commit-hooks)

Some custom hooks for pre-commit.

Based on: https://github.com/pre-commit/pre-commit


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

    -   repo: https://github.com/namelivia/pre-commit-hooks
        rev: 1.0.0  # Use the ref you want to point at
        hooks:
        -   id: regex


### Hooks available

#### `regex`
Look for regular expressions on the new code.
