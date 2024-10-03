# AI Poker Game

Welcome to the **AI Poker Game**, a Python-based Texas Hold'em poker simulation where AI agents compete against each other using advanced strategies powered by OpenAI's GPT models.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **AI Agents**: Each player is an AI agent that makes decisions based on game state and poker theory.
- **OpenAI Integration**: Uses OpenAI's GPT models to simulate human-like decision-making and strategies.
- **Texas Hold'em Rules**: Implements the standard rules of Texas Hold'em poker.
- **Hand Evaluation**: Utilizes the `treys` library for accurate hand strength evaluation.
- **Expandable**: Designed with modularity in mind, allowing for easy expansion and customization.


## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate the virtual environment:

On macOS/Linux:
```bash
source venv/bin/activate
```

On Windows:
```cmd
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Note: Ensure that you have a `requirements.txt` file listing all the necessary packages.

## Usage

### Setting Up Environment Variables

The game requires an OpenAI API key to function. You need to set this key as an environment variable.

On macOS/Linux:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

On Windows Command Prompt:
```cmd
set OPENAI_API_KEY=your-api-key-here
```

Replace `'your-api-key-here'` with your actual OpenAI API key.

### Running the Game

```bash
python main.py
```

Note: The game runs in the console and will display the actions of each AI agent throughout the game.

## Requirements

- Python 3.7 or higher
- An OpenAI API key with access to the GPT models (e.g., gpt-3.5-turbo or gpt-4)
- Python Libraries:
  - openai
  - treys
  - python-dotenv (if you choose to use a .env file)

You can install all required libraries using the `requirements.txt` file.

## Environment Variables

The game uses the following environment variable:

- `OPENAI_API_KEY`: Your OpenAI API key.

### Using a .env File (Optional)

If you prefer to use a `.env` file to store environment variables:

1. Install python-dotenv:
   ```bash
   pip install python-dotenv
   ```

2. Create a `.env` file in the project's root directory:
   ```env
   OPENAI_API_KEY=your-api-key-here
   ```

3. Update `ai_agent.py` to load the `.env` file:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

4. Ensure `.env` is added to your `.gitignore` file to prevent it from being committed to the repository.

## Project Structure

```
├── ai_agent.py
├── card.py
├── deck.py
├── game.py
├── hand_evaluator.py
├── main.py
├── player.py
├── requirements.txt
├── README.md
└── .gitignore
```

- `ai_agent.py`: Contains the AIAgent class that uses OpenAI's API to make decisions.
- `card.py`: Defines the Card class representing a playing card.
- `deck.py`: Contains the Deck class for managing the deck of cards.
- `game.py`: Implements the PokerGame class that runs the game logic.
- `hand_evaluator.py`: Evaluates the strength of poker hands using the treys library.
- `main.py`: The entry point of the application.
- `player.py`: Defines the Player class.
- `requirements.txt`: Lists all Python dependencies.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -am 'Add new feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Create a Pull Request on GitHub.

## License

This project is licensed under the MIT License.

Note: Include a LICENSE file in your repository if you choose to use the MIT License or any other.

## Acknowledgments

- OpenAI for providing the GPT models.
- The developers of the treys library for poker hand evaluation.
- Any other resources or individuals you wish to acknowledge.
