BETBOT - Heroku API Key Validator 🚀
betbote is a powerful Python tool that allows you to easily validate Heroku API keys. It checks the authorization status against the Heroku API, providing detailed feedback like user email and ID. With its smooth progress bar, retry logic, and error handling, betbote ensures consistent and reliable results. 🔑✅

Features ✨
🔒 Key Validation
Verifies whether your Heroku API keys are valid and authorized with clear feedback.

🔁 Retry Logic
Automatically retries failed requests with exponential backoff to ensure reliability.

📂 File Support
Extracts and validates multiple API keys from files in various formats.

📝 Detailed Feedback
Get email, user ID, and status for valid keys, along with detailed error messages for invalid keys.

⚠️ Error Handling
Gracefully handles unauthorized, forbidden, and rate-limited errors, ensuring smooth execution.

🌍 Randomized Headers
Uses randomized User-Agent headers to mimic legitimate traffic and avoid blocking.

📊 Progress Bar
Powered by tqdm, the progress bar displays real-time validation progress, making it user-friendly.

⚙️ Customizable
Easily extendable or modifiable for different use cases or feature additions.

Why Choose BETBOT? 🤔
⏱ Save Time
Quickly validate and manage your Heroku API keys without hassle.

🔒 Reliability
Built-in error handling and retry logic for consistent, accurate results.

👨‍💻 Developer-Friendly
Streamlined file input, comprehensive feedback, and easy-to-use interface for developers.

💡 Open Source
Free to use and contribute. Tailor it to your needs or add new features!

Getting Started 🛠️
Clone the repository

`git clone https://github.com/olialkibriakonok/betbote.git`

Install dependencies
Install the required Python libraries using:
`pip install -r requirements.txt`

Run the tool
Execute the following command to validate Heroku API keys:
`python betbote.py --file <path_to_file>`

License ⚖️
This project is licensed under the MIT License.

Credits 
Crafted with by Olial Kibria Konok.
