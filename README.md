# pre-commit-hooks [![tag](https://img.shields.io/github/tag/namelivia/pre-commit-hooks.svg)](https://github.com/namelivia/pre-commit-hooks/releases) [![Build Status](https://travis-ci.org/namelivia/pre-commit-hooks.svg?branch=master)](https://travis-ci.org/namelivia/pre-commit-hooks) [![codecov](https://codecov.io/gh/namelivia/pre-commit-hooks/branch/master/graph/badge.svg)](https://codecov.io/gh/namelivia/pre-commit-hooks)

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
<img src="https://user-images.githubusercontent.com/1571416/74920608-bb5ba280-53cc-11ea-9ee3-637a7d8db85e.gif" alt="Example GIF" />

<b>Configuration:</b>
You can add as many rules as you want like the following ones to the `repos` section of your `.pre-commit-config.yaml`:
```
- repo: https://github.com/namelivia/pre-commit-hooks
  sha: 1.0.0
  hooks:
	  - id: regex
		language_version: python3.6
		exclude: '^.pre-commit-config.yaml'
		verbose: true
		args: [
			'--critical',
			'--message', 'We dont talk about this',
			'--pattern', '(?:fight club)'
		]

	  - id: regex
		language_version: python3.6
		exclude: '^.pre-commit-config.yaml'
		verbose: true
		args: [
			'--message', 'He-Who-Must-Not-Be-Named',
			'--pattern', '(?:Voldemort)'
		]

```

<b>Arguments:</b>
 - `--critical` : If present the commit will be blocked when the pattern is found.
 - `--message` : The message that will be displayed when the pattern is found.
 - `--pattern` : The pattern to be looking for, expressed in a [regular expression](https://docs.python.org/3/howto/regex.html) form.
