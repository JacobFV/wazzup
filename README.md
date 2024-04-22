# Communications Assistant Backend

## Overview

The Communications Assistant Backend is a Python-based application that aggregates and analyzes user-generated content from various platforms, such as Notion, Twitter, Facebook, Quora, Reddit, and ChatGPT exports. It provides a unified interface to fetch, process, and generate personalized content based on user preferences and configurations.

## Features

- Data ingestion from multiple platforms
- Sampling and generation of personalized content
- Configuration management for user preferences
- RESTful API for seamless integration with frontend applications
- Authentication and authorization using JWT tokens
- Database integration using SQLModel and PostgreSQL
- Containerization with Docker for easy deployment

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/wazzup-ai/wazzup.git
   ```

2. Navigate to the project directory:

   ```bash
   cd wazzup
   ```

3. Install the dependencies:

   ```bash
   poetry install
   ```

4. Set up the database:
   - Create a PostgreSQL database
   - Update the database connection URL in the `.env` file

5. Run the application:

   ```bash
   poetry run wazzup run
   ```

## Usage

- Access the API documentation at  to explore the available endpoints and their usage.
- Use the provided authentication endpoints to obtain JWT tokens for authenticated requests.
- Configure user preferences and settings using the configuration endpoints.
- Fetch and process user-generated content from supported platforms using the data ingestion endpoints.
- Generate personalized content using the sampling and generation endpoints.

## Testing

Run the test suite using the following command:

```bash
poetry run pytest
```

## Deployment

The application can be deployed using Docker. Build the Docker image and run the container using the provided Dockerfile.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
