import asyncio
import database


async def clear_mapped_messages(links, account_name, messages_count):
    while True:
        for source, link in links.items():
            for target in link['target']:
                messages = database.get_mapped_messages_by_acc_channel(account_name, source, target)
                ids = [t[0] for t in messages]
                if len(ids) > messages_count:
                    ids = ids[:-messages_count] if len(ids) > messages_count else ids
                    database.remove_mapped_messages(ids)
        await asyncio.sleep(60 * 5)
