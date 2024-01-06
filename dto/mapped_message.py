class MappedMessageDTO:
    def __init__(self, response):
        id, account_name, source_channel_id, source_message_id, target_channel_id, target_message_id = response
        self.id = id
        self.account_name = account_name
        self.source_channel_id = source_channel_id
        self.source_message_id = source_message_id
        self.target_channel_id = target_channel_id
        self.target_message_id = target_message_id
