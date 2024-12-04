BETBOT - Heroku API Key Validator
betbote is a powerful and efficient Python tool designed to validate Heroku API keys. By checking their authorization status against the Heroku API, it provides detailed feedback, including user email and ID. It includes a dynamic progress bar for smooth validation and handles errors, retries, and more for consistent, reliable results.

Key Features:
Key Validation: Verifies if Heroku API keys are valid and authorized.
Retry Logic: Automatically retries failed requests with exponential backoff for reliable validation.
File Support: Extracts and validates multiple API keys from files, supporting various formats.
Detailed Feedback: Provides email, user ID, and key status for valid keys, and detailed error messages for invalid keys.
Error Handling: Handles unauthorized, forbidden, and rate-limited errors gracefully, ensuring a smooth experience.
Randomized Headers: Uses randomized User-Agent headers to mimic legitimate traffic and avoid blocking.
Progress Bar: Displays a dynamic progress bar powered by tqdm for a user-friendly experience.
Customizable: Easy to modify or extend for various use cases.
Why Use BETBOT?
Save Time: Quickly validate and manage your Heroku API keys.
Reliability: Includes error handling and retry logic to ensure consistent results.
Developer-Friendly: Streamlined file input and detailed feedback for developers and administrators.
Open Source: Free and open for contributions. Tailor it to your needs!
Getting Started:
Clone the repository:
(https://github.com/olialkibriakonok/betbote.git)

Install dependencies:
pip install -r requirements.txt

Run the tool to validate Heroku API keys:
python betbote.py --file <path_to_file>

License:
This tool is licensed under the MIT License.

Credits:
Crafted by Olial Kibria Konok.

