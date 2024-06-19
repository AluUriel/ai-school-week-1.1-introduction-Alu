# Week 1.1: Syllabus and Reviewing LLM Essentials

## Introduction
To make the most out of this course, understand that LLMs are powerful tools for next token generation, leveraging advanced statistical analysis beyond simple models.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- You have installed Python 3.6+.

## Setup Instructions

### Step 1: Clone the Repository
First, clone the repository to your local machine using the following command:
```bash
git clone [repository-url]
cd [repository-name]
```

### Step 2: Create a Python Virtual Environment
Create a virtual environment using `venv`:
```bash
python3 -m venv venv
```

### Step 3: Activate the Virtual Environment
Activate the virtual environment:
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On MacOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### Step 4: Install Required Packages
Install the required packages using `pip`:
```bash
pip install -r requirements.txt
```

### Step 5: Create a `.env` File
Create a `.env` file in the root directory of the project. Use the `.env.sample` file as a reference:
```bash
cp .env.sample .env
```

### Step 6: Update `.env` File
Open the `.env` file and update the key values as necessary.

### Step 7: Load Environmental Variables from the `.env` File
Use the following command to export all of your environmental variables while ignoring any comments:
```bash
export $(grep -v '^#' .env | xargs)
```

In windows
$env:OPENAI_API_KEY = "your_openai_api_key"

### Alternatively - Load the Variables Inside Your Shell
If you experience problems using the `.env` file or do not wish to use one, you can load the variables directly from your shell. Use a command structured like this to load each variable:
```bash
export OPENAI_API_KEY=your-key-here
```

## Usage

#### Running In-Class Examples
To run any in-class examples, execute the server file directly from the command line. For example:

```bash
python3 in_class_examples/[file-name]
```