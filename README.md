
# Telegram Group Cloner

This script allows you to clone messages from one Telegram group to another using the Telethon library. It extracts group information from the source group and forwards all messages to a destination group, preserving the message order.

## Features

- **Extract Group Information**: Get the group ID and access hash for a Telegram group.
- **Cloning**: Clone messages from one group to another.
- **Supports All Media Types**: Messages, images, videos, documents, etc., are forwarded.
- **Flood Protection**: Built-in flood protection with a 1.5-second delay between messages to prevent rate limiting.
- **Simple to Use**: User-friendly with basic inputs like API ID, API Hash, phone number, and group links.

## Requirements

- Python 3.6+
- `telethon` library
- A Telegram account

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/telegram-group-cloner.git
   cd telegram-group-cloner
   ```

2. **Install dependencies**:
   ```bash
   pip install telethon
   ```

3. **Create a Telegram Application**:
   - Visit [Telegram Developer Tools](https://my.telegram.org/auth) and create a new application to get your `API ID` and `API Hash`.

4. **Get Group Information**:
   - Run the script `main.py`, and input the necessary credentials and the source group's invite link to get the group information.
   - The script will save the group details (`group_id` and `access_hash`) in a JSON file (`group_info.json`).

## Usage

### Step 1: Run `main.py`

- Start the script by running:

  ```bash
  python main.py
  ```

- **Input the following when prompted**:
  - Your **API ID**
  - Your **API Hash**
  - Your **phone number** (with country code)
  - Source group link or username
  - Destination group link or username

### Step 2: Group Information Extraction

- The script will ask for the source group link or username (e.g., `@groupusername` or `https://t.me/groupusername`).
- It will then extract the group information and save it to `group_info.json`.

### Step 3: Cloning Messages

- After extracting the source group info, it will ask for the destination group link or username.
- The script will then start forwarding messages from the source group to the destination group.

### Note:
- Ensure you are an admin of both groups, otherwise the script won't work.
- **Rate Limiting**: The script includes a basic flood control to avoid triggering Telegram's rate limits. However, excessive message forwarding might still cause limits to trigger.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
