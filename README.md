# PR Agent

PR Agent is a command-line tool that automatically generates well-structured GitHub pull request descriptions using GPT-4. It analyzes your git commit changes and creates a formatted PR description with sections for Goals, Key Changes, and Tests.

## Features

- Automatically generates PR titles and descriptions based on commit changes
- Creates structured PR descriptions with sections for Goals, Key Changes, and Tests
- Uses OpenAI's GPT-4 for intelligent content generation
- Integrates with GitHub CLI for seamless PR creation
- Opens PR creation in web interface for final review

## Prerequisites

- Python 3.11 or higher
- GitHub CLI (`gh`) installed and authenticated
- OpenAI API key
- Poetry (for dependency management)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd pr-agent
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Set up your OpenAI API key:
```bash
export PR_AGENT_OPENAI_API_KEY='your-api-key'
```

## Usage

Simply run the script when you're ready to create a PR:

```bash
poetry run python main.py
```

The tool will:
1. Get your current branch name
2. Fetch the latest commit changes
3. Generate a PR description using GPT-4
4. Open GitHub's PR creation page in your browser with pre-filled content

## Configuration

The tool requires the following environment variable:
- `PR_AGENT_OPENAI_API_KEY`: Your OpenAI API key

## Development

This project uses Poetry for dependency management. To set up the development environment:

```bash
poetry install --with dev
```

## License

[Insert License Information]

## Author

George Ruan (ruan.george@gmail.com)
