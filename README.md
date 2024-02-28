# Python Application CI/CD with GitHub Actions

This repository contains a Python application that demonstrates CI/CD using GitHub Actions.

## CI/CD Workflow

### Triggers

- The CI/CD workflow is triggered on pushes to the `main` branch and on pull requests to `main`.

### Workflow Jobs

- **Install Dependencies**: Installs Python dependencies required by the application.
- **Run Tests**: Runs unit tests using the pytest framework.
- **Build and Deploy**: Builds and deploys the application to a test server.

### Environment

- Python version: 3.10
- Operating System: Ubuntu latest

## Running the Workflow Locally

To run the CI/CD workflow locally, follow these steps:

1. Clone this repository.
2. Install the required dependencies.
3. Set up any necessary environment variables.
4. Run the GitHub Actions workflow locally using the GitHub CLI or a third-party tool.

## Accessing Workflow Status and Logs

You can access the status and logs of the CI/CD workflow on the GitHub Actions tab of this repository.

## Secrets

This workflow requires the following secrets to be set up in the GitHub repository settings:

- `SECRET_KEY`: Secret key for the application.
- `DATABASE_URL`: URL of the database server.
