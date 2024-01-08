import re


def remove_text(text, texts_remove, entities):
    for text_remove in texts_remove:
        formatted_remove_text = text_remove + "\n"
        formatted_remove_text_offset_start = text.find(formatted_remove_text)
        if formatted_remove_text_offset_start == -1:
            formatted_remove_text = text_remove + " "
            formatted_remove_text_offset_start = text.find(formatted_remove_text)
            if formatted_remove_text_offset_start == -1:
                formatted_remove_text = text_remove
                formatted_remove_text_offset_start = text.find(formatted_remove_text)

        if formatted_remove_text_offset_start == -1:
            continue

        formatted_text_with_removed_text = text.replace(formatted_remove_text, '')
        call_plus = len(formatted_text_with_removed_text) - len(formatted_text_with_removed_text.strip())
        formatted_remove_text_length = len(formatted_remove_text) + call_plus
        formatted_remove_text_offset_end = formatted_remove_text_offset_start + formatted_remove_text_length

        formatted_entities = []
        minus = 0
        if entities is None:
            return formatted_text_with_removed_text, None

        for entity in entities:
            entity.offset -= minus
            entity_offset_end = entity.offset + entity.length

            if entity.offset == formatted_remove_text_offset_start and entity.length == formatted_remove_text_length:
                continue

            if formatted_remove_text_offset_start < entity.offset or formatted_remove_text_offset_start > entity_offset_end:
                formatted_entities.append(entity)
                continue

            if formatted_remove_text_offset_end < entity_offset_end:
                minus = formatted_remove_text_length + 1
                entity.length -= minus
                formatted_entities.append(entity)
                continue

            minus = entity_offset_end - formatted_remove_text_offset_start + 1
            entity.length -= minus
            formatted_entities.append(entity)

        return formatted_text_with_removed_text, formatted_entities

    return text, entities


def replace_emodji(text, emoji_replacement, entities):
    formatted_entities = []
    for search_emoji, replace_emoji in emoji_replacement.items():
        search_emoji_offset = text.find(search_emoji)
        if search_emoji_offset == -1:
            continue

        search_emoji_len = len(search_emoji)
        replace_emoji_len = len(replace_emoji)

        if search_emoji_len == replace_emoji_len:
            text = text.replace(search_emoji, replace_emoji)
            continue

        if not entities:
            text = text.replace(search_emoji, replace_emoji)
            continue

        offsets = [m.start() for m in re.finditer(search_emoji, text)]
        text = text.replace(search_emoji, replace_emoji)
        razniza = search_emoji_len - replace_emoji_len
        plus = 0
        if search_emoji_len == 2:
            plus = 2
            razniza += 1
        elif search_emoji_len == 3:
            plus = 3
            razniza += 2

        minus = razniza
        for offset in offsets:
            entities_for_format = formatted_entities if formatted_entities else entities
            formatted_entities = []
            for entity in entities_for_format:
                temp_entity = entity
                entity_end = entity.offset + entity.length - plus

                if entity_end < offset:
                    formatted_entities.append(temp_entity)
                    continue

                plus += minus
                if entity.offset > offset:
                    temp_entity.offset -= minus
                    formatted_entities.append(temp_entity)
                    continue

                if entity.offset < offset < entity_end:
                    temp_entity.length -= minus
                    formatted_entities.append(temp_entity)
                    continue

                formatted_entities.append(temp_entity)

    return text, formatted_entities if formatted_entities else entities
