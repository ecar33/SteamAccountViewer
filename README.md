# Steam Account Viewer

A Python-based tool for retrieving and displaying basic information about a Steam account using the Steam Web API.  
This project demonstrates working with REST APIs, handling JSON data, and building a simple command-line interface.

## Features
- Retrieve Steam user information by SteamID or vanity URL  
- Display account details such as profile name, visibility, and game count  
- Modular structure for easy extension  
- Basic error handling for invalid input or failed API calls  

## Technologies Used
- **Python 3.11+**
- **Requests** (HTTP API communication)
- **Steam Web API**
- **JSON** parsing

## Setup

### 1) Clone the repository
```bash
git clone https://github.com/ecar33/SteamAccountViewer.git
cd SteamAccountViewer
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Add your Steam API key
Create a `.env` file in the project root and add:
```text
STEAM_API_KEY=your_api_key_here
```

### 4) Run the program
```bash
python main.py
```

## Example Output
```text
Steam Username: example_user
Account Created: 2011-04-23
Games Owned: 112
Profile Visibility: Public
```

## Future Improvements
- GUI version using **Tkinter** or **PyQt**
- Caching API results to reduce repeated calls  
- Support for additional endpoints (friends, achievements, owned games list)

## License
MIT License. See the [LICENSE](LICENSE) file for details.
