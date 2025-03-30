# Prime Numbers Checker

A Python project that provides an efficient implementation for checking prime numbers. The project includes comprehensive test coverage and follows best practices for code quality.

## Features

- Efficient prime number checking algorithm
- Comprehensive test suite
- Code quality checks (Flake8, Pylint, Bandit)
- CI/CD pipeline with GitLab
- SonarQube integration for code analysis

## Project Structure

```
.
├── src/                    # Source code directory
│   └── prime_number.py     # Main implementation
├── tst/                    # Test directory
│   └── test_prime_number.py # Test suite
├── templates/              # Template files
├── requirements.txt        # Project dependencies
├── .gitlab-ci.yml         # GitLab CI configuration
└── sonar-project.properties # SonarQube configuration
```

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd prime-numbers
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running Tests

```bash
# Run all tests
python -m pytest tst/test_prime_number.py -v

# Run tests with coverage
python -m pytest --cov=src tst/test_prime_number.py
```

### Code Quality Checks

```bash
# Run Flake8
python -m flake8 src/prime_number.py

# Run Pylint
python -m pylint src/prime_number.py

# Run Bandit (security checks)
python -m bandit -r src/prime_number.py
```

### Using the Prime Number Function

```python
from src.prime_number import is_prime_number

# Example usage
number = 17
if is_prime_number(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
```

## Algorithm Details

The prime number checking algorithm is optimized for efficiency:
- Handles edge cases (numbers ≤ 1)
- Quickly identifies 2 and 3 as prime
- Eliminates even numbers and numbers divisible by 3
- Uses an efficient loop checking up to square root of the number
- Implements the 6k±1 optimization for checking divisors

## Development

This project follows a CI/CD pipeline:
1. Code quality checks (Flake8, Pylint, Bandit)
2. Unit testing
3. Coverage reporting
4. SonarQube analysis
5. Release management

## Deployment

### CI/CD Pipeline

The project uses GitLab CI/CD for automated deployment:

1. **Pipeline Stages**:
   - Static Analysis (Flake8, Pylint, Bandit)
   - Tests (Pytest)
   - Coverage (Pytest-cov)
   - Quality Gate (SonarQube)
   - Release

2. **Deployment Environments**:
   - Test: For feature branches and development
   - Production: For main branch and hotfix releases

3. **Deployment Process**:
   - Automatic deployment on successful pipeline completion
   - Manual rollback capability available
   - Environment-specific configurations

### Deployment Requirements

- GitLab Runner with Python 3.x support
- SonarQube server access
- Environment variables:
  - `SONAR_TOKEN`: For SonarQube authentication
  - `CI_ENVIRONMENT_NAME`: Automatically set based on branch

### Manual Deployment

For manual deployment:

```bash
# 1. Ensure all tests pass
python -m pytest tst/test_prime_number.py -v

# 2. Run code quality checks
python -m flake8 src/prime_number.py
python -m pylint src/prime_number.py
python -m bandit -r src/prime_number.py

# 3. Create a release tag
git tag -a v1.x.x -m "Release version 1.x.x"
git push origin v1.x.x
```

### Rollback

In case of deployment issues:

1. Access GitLab CI/CD pipeline
2. Navigate to the failed deployment
3. Click on the "Rollback" button
4. Confirm rollback to previous stable version

## License

[Add your license information here]
