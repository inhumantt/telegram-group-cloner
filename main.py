from telethon import TelegramClient
import asyncio
import json
import os
import time

async def find_group_info(client):
    await client.start()
    me = await client.get_me()  # Fixed: await to get the user info
    print(f"Signed in successfully as {me.first_name}; remember to not break the ToS or you will risk an account ban!")

    group_link = input("Enter the source group username or invite link (e.g., @groupusername or https://t.me/groupusername): ").strip()

    try:
        entity = await client.get_entity(group_link)  # Get entity using link directly
        group_info = {
            'name': entity.title,
            'id': entity.id,
            'access_hash': entity.access_hash
        }

        print(f"Group Name: {group_info['name']}")
        print(f"Group ID: {group_info['id']}")
        print(f"Group Access Hash: {group_info['access_hash']}")

        # Save to JSON
        with open('group_info.json', 'w') as f:
            json.dump(group_info, f, indent=4)

        print("Group info saved to 'group_info.json'.\n")

    except Exception as e:
        print(f"Error fetching group info: {e}")

async def clone_groups(client):
    me = await client.get_me()
    print(f"Signed in successfully as {me.first_name}; ready to clone!\n")

    # Load source group info
    try:
        with open('group_info.json', 'r') as f:
            source_info = json.load(f)
    except FileNotFoundError:
        print("group_info.json not found. Please run find_group_info first.")
        return

    source_id = source_info['id']

    # Ask for destination group
    dest_link = input("Enter destination group username or link (e.g., @groupusername or https://t.me/groupusername): ").strip()

    try:
        source_entity = await client.get_entity(source_id)  # Get source group by ID directly
        dest_entity = await client.get_entity(dest_link)  # Get destination group by link

        print("Starting to forward messages...\n")

        messages = []
        async for message in client.iter_messages(source_entity, reverse=True):  # old → new
            messages.append(message)

        for msg in messages:
            try:
                await client.forward_messages(dest_entity, msg)
                await asyncio.sleep(1.5)  # sleep to avoid flood
            except Exception as e:
                print(f"Failed to forward message {msg.id}: {e}")
                time.sleep(5)

        print("\nFinished forwarding all messages!")

    except Exception as e:
        print(f"Error during cloning: {e}")

async def main():
    # Input API credentials
    api_id = int(input("Enter your API ID: "))
    api_hash = input("Enter your API Hash: ")
    phone = input("Enter your phone number (with country code, e.g., +1234567890): ")

    session_name = 'anon'
    client = TelegramClient(session_name, api_id, api_hash)

    # Start session
    await client.start(phone=lambda: phone)

    # Find group info (source)
    await find_group_info(client)

    # Clone to destination group
    await clone_groups(client)

if __name__ == "__main__":
    asyncio.run(main())
