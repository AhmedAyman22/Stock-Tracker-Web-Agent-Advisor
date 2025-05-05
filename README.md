
# Stock-Tracker-Web-Agent-Advisor

An interactive web application that enables users to explore and select top-performing NASDAQ companies, and receive AI-driven investment advice based on their selections.

## Features
- Displays the top 100 performing companies in the NASDAQ stock market.
- Allows users to select up to 3 companies for personalized investment advice.
- Provides options to refresh data, submit selections, and clear selections.
- Responsive design using Tailwind CSS for optimal user experience.
- Dynamic data fetching and rendering using JavaScript.
- AI-powered advisor that analyzes selected companies and provides insights.

## Technologies Used
- HTML, CSS (Tailwind CSS), JavaScript for frontend development.
- Python (Flask) for backend development.
- Integration with AI models for investment advice.

## Installation

Clone the repository:

```bash
git clone https://github.com/AhmedAyman22/Stock-Tracker-Web-Agent-Advisor.git
```

Navigate to the project directory:

```bash
cd Stock-Tracker-Web-Agent-Advisor
```

Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Start the Flask application:

```bash
python app.py
```

Open your web browser and navigate to:

```arduino
http://localhost:5000
```

Interact with the application:
- View the list of top-performing NASDAQ companies.
- Select up to 3 companies to receive AI-driven investment advice.
- Use the "Refresh Data" button to update the list.
- Click "Submit Selected Tickers to Advisor" to get insights.
- Use "Clear Selected Tickers" to reset your selections.

## Project Structure
- `app/` - Contains the Flask application and route definitions.
- `templates/` - HTML templates for rendering pages.
- `static/` - Static files such as CSS, JavaScript, and images.
- `data/` - Data files and scripts for fetching and processing stock data.
- `scraper/` - Scripts for scraping stock market data.
- `api/` - API endpoints for data retrieval and submission.
- `agent/` - AI agent logic for analyzing selected companies.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Special thanks to all contributors and the open-source community for their valuable resources and support.
