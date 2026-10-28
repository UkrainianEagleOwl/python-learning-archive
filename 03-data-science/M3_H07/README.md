# MovieLens Recommender System

## Project Overview
This project aims to build and compare different recommender system algorithms using the MovieLens dataset. The goal is to predict user ratings for movies they haven't watched based on their previous ratings.

## Algorithms Explored
- Singular Value Decomposition (SVD)
- SVD++
- Non-negative Matrix Factorization (NMF)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.6+
- Poetry for dependency management

### Installation
1. Clone the repository
   ```bash
   git clone [your-repo-link]
   cd [repository-name]
   ```
2. Install dependencies using Poetry
   ```bash
   poetry install
   ```

## Running the Tests
To run the automated tests for this system:
```bash
poetry run python -m unittest discover
```

## Built With
- [Surprise](http://surpriselib.com/) - A Python scikit for building and analyzing recommender systems

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/yourusername/repository/tags).

## Authors
- **Your Name** - *Initial work* - [YourUsername](https://github.com/YourUsername)

See also the list of [contributors](https://github.com/yourusername/repository/contributors) who participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.