# Bantha

**[Banthas](https://starwars.fandom.com/wiki/Bantha) are sturdy and reliable, just like the schemas and models you want to build.**

## Overview

Welcome to **Bantha**, the ultimate command-line utility for those who wish to traverse the desert of data structuring with ease. Generate JSON Schemas from sample JSON inputs like a Bantha navigates the sands of Tatooine.

## Features

- **Intuitive CLI**: User-friendly command-line interface designed for quick schema generation without the need for complex configurations.  
- **JSON Schema Generation**: Instantly convert any JSON sample into a robust JSON Schema, ensuring your data structures are well-defined and validated.
- **Custom Output Control**: Specify where and how your schemas are saved with the `--destination-path` option, giving you full control over file management.
- **Schema Naming**: Allows you to name your schema directly from the command line for straightforward organization and reference.
- **Lightweight & Fast**: Optimized for performance, Bantha processes your JSON samples and generates schemas quickly, so you can keep moving at lightspeed.
- **Shell Auto-Completion**: Enhance your CLI experience with auto-completion for faster command input and fewer errors.

## Installation

Start by ensuring Poetry is installed:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Then, get Bantha up and running:

```bash
git clone https://github.com/z33DD/bantha.git
cd bantha
poetry install
```

## Usage

Enter your Poetry environment:

```bash
poetry shell
```

### Basic Usage:

- **Generate a JSON Schema:**

```bash
bantha /path/to/your/sample.json your_schema_name
```

### Optional Flags:

- `--destination-path`: Specify where to save your schema. Defaults to the current directory.

```bash
bantha /path/to/your/sample.json your_schema_name --destination-path /path/to/destination/
```

### Advanced Usage:

- **Auto-Completion:**

To enable auto-completion in your shell:

For installation:
```bash
bantha --install-completion
```

For displaying completion script:
```bash
bantha --show-completion
```

## Examples:

- Generate a schema named `user_schema` from `user.json`:

```bash
bantha user.json user_schema
```

## Contributing

Is there a disturbance in the Force? Or perhaps you have enhancements to make Bantha faster than a podracer? Open an issue or contribute with a pull request.


## License

Bantha operates under the MIT License. See [LICENSE.md](LICENSE.md) for more details.

## Acknowledgements
- Star Wars Universe: For giving us the iconic Bantha as our mascot.
- Poetry: For making Python dependency management less of a saga.
- Pydantic: For its brilliant model generation capabilities.
- datamodel-code-generator: For inspiring schema to code translations.
- Genson: For its JSON schema generation prowess.
