# THIS FILE IS AUTO-GENERATED. DO NOT EDIT!
# Bot API 10.3 (August 24, 2026)

from typing_extensions import TypeForm

from aogami.types import (
    AcceptedGiftTypes,
    BotAccessSettings,
    BotCommand,
    BotCommandScope,
    BotDescription,
    BotName,
    BotShortDescription,
    BusinessConnection,
    ChatAdministratorRights,
    ChatFullInfo,
    ChatInviteLink,
    ChatMember,
    ChatPermissions,
    EphemeralMessageParameters,
    File,
    ForceReply,
    ForumTopic,
    GameHighScore,
    Gifts,
    InlineKeyboardMarkup,
    InlineQueryResult,
    InlineQueryResultsButton,
    InputChecklist,
    InputFile,
    InputMedia,
    InputMediaAudio,
    InputMediaDocument,
    InputMediaLivePhoto,
    InputMediaPhoto,
    InputMediaVideo,
    InputPaidMedia,
    InputPollMedia,
    InputPollOption,
    InputProfilePhoto,
    InputRichMessage,
    InputSticker,
    InputStoryContent,
    KeyboardButton,
    LabeledPrice,
    LinkPreviewOptions,
    MaskPosition,
    MenuButton,
    Message,
    MessageEntity,
    MessageId,
    OwnedGifts,
    PassportElementError,
    Poll,
    PreparedInlineMessage,
    PreparedKeyboardButton,
    ReactionType,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ReplyParameters,
    SentGuestMessage,
    SentWebAppMessage,
    ShippingOption,
    StarAmount,
    StarTransactions,
    Sticker,
    StickerSet,
    Story,
    StoryArea,
    SuggestedPostParameters,
    Update,
    User,
    UserChatBoosts,
    UserProfileAudios,
    UserProfilePhotos,
    WebhookInfo,
)


class TelegramMethods:
    async def method[T](
        self, name: str, returns: TypeForm[T], /, **params: object
    ) -> T:
        raise NotImplementedError

    async def get_updates(
        self,
        *,
        offset: int | None = None,
        limit: int | None = None,
        timeout: int | None = None,
        allowed_updates: list[str] | None = None,
    ) -> list[Update]:
        """
        Use this method to receive incoming updates using long polling (wiki). Returns
        an Array of Update objects.

        Args:
            offset (int | None): Identifier of the first update to be returned. Must be
                greater by one than the highest among the identifiers of previously
                received updates. By default, updates starting with the earliest
                unconfirmed update are returned. An update is considered confirmed as
                soon as getUpdates is called with an offset higher than its update_id.
                The negative offset can be specified to retrieve updates starting from
                -offset update from the end of the updates queue. All previous updates
                will be forgotten.
            limit (int | None): Limits the number of updates to be retrieved. Values
                between 1-100 are accepted. Defaults to 100.
            timeout (int | None): Timeout in seconds for long polling. Defaults to 0,
                i.e. usual short polling. Should be positive, short polling should be
                used for testing purposes only.
            allowed_updates (list[str] | None): A JSON-serialized list of the update
                types you want your bot to receive. For example, specify ["message",
                "edited_channel_post", "callback_query"] to only receive updates of
                these types. See Update for a complete list of available update types.
                Specify an empty list to receive all update types except chat_member,
                message_reaction, and message_reaction_count (default). If not
                specified, the previous setting will be used. Please note that this
                parameter doesn't affect updates created before the call to getUpdates,
                so unwanted updates may be received for a short period of time.
        """
        params = {
            "offset": offset,
            "limit": limit,
            "timeout": timeout,
            "allowed_updates": allowed_updates,
        }
        return await self.method("getUpdates", list[Update], **params)

    async def set_webhook(
        self,
        *,
        url: str,
        certificate: InputFile | None = None,
        ip_address: str | None = None,
        max_connections: int | None = None,
        allowed_updates: list[str] | None = None,
        drop_pending_updates: bool | None = None,
        secret_token: str | None = None,
    ) -> bool:
        """
        Use this method to specify a URL and receive incoming updates via an outgoing
        webhook. Whenever there is an update for the bot, we will send an HTTPS POST
        request to the specified URL, containing a JSON-serialized Update. In case of an
        unsuccessful request (a request with response HTTP status code different from
        2XY), we will repeat the request and give up after a reasonable amount of
        attempts. Returns True on success.
        If you'd like to make sure that the webhook was set by you, you can specify
        secret data in the parameter secret_token. If specified, the request will
        contain a header "X-Telegram-Bot-Api-Secret-Token" with the secret token as
        content.

        Args:
            url (str): HTTPS URL to send updates to. Use an empty string to remove
                webhook integration.
            certificate (InputFile | None): Upload your public key certificate so that
                the root certificate in use can be checked. See our self-signed guide
                for details.
            ip_address (str | None): The fixed IP address which will be used to send
                webhook requests instead of the IP address resolved through DNS
            max_connections (int | None): The maximum allowed number of simultaneous
                HTTPS connections to the webhook for update delivery, 1-100. Defaults to
                40. Use lower values to limit the load on your bot's server, and higher
                values to increase your bot's throughput.
            allowed_updates (list[str] | None): A JSON-serialized list of the update
                types you want your bot to receive. For example, specify ["message",
                "edited_channel_post", "callback_query"] to only receive updates of
                these types. See Update for a complete list of available update types.
                Specify an empty list to receive all update types except chat_member,
                message_reaction, and message_reaction_count (default). If not
                specified, the previous setting will be used. Please note that this
                parameter doesn't affect updates created before the call to the
                setWebhook, so unwanted updates may be received for a short period of
                time.
            drop_pending_updates (bool | None): Pass True to drop all pending updates
            secret_token (str | None): A secret token to be sent in a header
                "X-Telegram-Bot-Api-Secret-Token" in every webhook request, 1-256
                characters. Only characters A-Z, a-z, 0-9, _ and - are allowed. The
                header is useful to ensure that the request comes from a webhook set by
                you.
        """
        params = {
            "url": url,
            "certificate": certificate,
            "ip_address": ip_address,
            "max_connections": max_connections,
            "allowed_updates": allowed_updates,
            "drop_pending_updates": drop_pending_updates,
            "secret_token": secret_token,
        }
        return await self.method("setWebhook", bool, **params)

    async def delete_webhook(
        self,
        *,
        drop_pending_updates: bool | None = None,
    ) -> bool:
        """
        Use this method to remove webhook integration if you decide to switch back to
        getUpdates. Returns True on success.

        Args:
            drop_pending_updates (bool | None): Pass True to drop all pending updates
        """
        params = {
            "drop_pending_updates": drop_pending_updates,
        }
        return await self.method("deleteWebhook", bool, **params)

    async def get_webhook_info(
        self,
    ) -> WebhookInfo:
        """
        Use this method to get current webhook status. Requires no parameters. On
        success, returns a WebhookInfo object. If the bot is using getUpdates, will
        return an object with the url field empty.
        """
        params = {}
        return await self.method("getWebhookInfo", WebhookInfo, **params)

    async def get_me(
        self,
    ) -> User:
        """
        A simple method for testing your bot's authentication token. Requires no
        parameters. Returns basic information about the bot in form of a User object.
        """
        params = {}
        return await self.method("getMe", User, **params)

    async def log_out(
        self,
    ) -> bool:
        """
        Use this method to log out from the cloud Bot API server before launching the
        bot locally. You must log out the bot before running it locally, otherwise there
        is no guarantee that the bot will receive updates. After a successful call, you
        can immediately log in on a local server, but will not be able to log in back to
        the cloud Bot API server for 10 minutes. Returns True on success. Requires no
        parameters.
        """
        params = {}
        return await self.method("logOut", bool, **params)

    async def close(
        self,
    ) -> bool:
        """
        Use this method to close the bot instance before moving it from one local server
        to another. You need to delete the webhook before calling this method to ensure
        that the bot isn't launched again after server restart. The method will return
        error 429 in the first 10 minutes after the bot is launched. Returns True on
        success. Requires no parameters.
        """
        params = {}
        return await self.method("close", bool, **params)

    async def send_message(
        self,
        *,
        chat_id: int | str,
        text: str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        ephemeral_message_parameters: EphemeralMessageParameters | None = None,
        parse_mode: str | None = None,
        entities: list[MessageEntity] | None = None,
        link_preview_options: LinkPreviewOptions | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send text messages. On success, the sent Message is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            ephemeral_message_parameters (EphemeralMessageParameters | None): A JSON-
                serialized object containing the parameters of the ephemeral message to
                send
            text (str): Text of the message to be sent, 1-4096 characters after entities
                parsing
            parse_mode (str | None): Mode for parsing entities in the message text. See
                formatting options for more details.
            entities (list[MessageEntity] | None): A JSON-serialized list of special
                entities that appear in message text, which can be specified instead of
                parse_mode
            link_preview_options (LinkPreviewOptions | None): Link preview generation
                options for the message
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "ephemeral_message_parameters": ephemeral_message_parameters,
            "text": text,
            "parse_mode": parse_mode,
            "entities": entities,
            "link_preview_options": link_preview_options,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendMessage", Message, **params)

    async def forward_message(
        self,
        *,
        chat_id: int | str,
        from_chat_id: int | str,
        message_id: int,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        video_start_timestamp: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
    ) -> Message:
        """
        Use this method to forward messages of any kind. Service messages and messages
        with protected content can't be forwarded. On success, the sent Message is
        returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be forwarded; required if the message is
                forwarded to a direct messages chat
            from_chat_id (int | str): Unique identifier for the chat where the original
                message was sent (or username of the target bot, supergroup or channel
                in the format @username)
            video_start_timestamp (int | None): New start timestamp for the forwarded
                video in the message
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the forwarded
                message from forwarding and saving
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; only available when forwarding to private chats
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only
            message_id (int): Message identifier in the chat specified in from_chat_id
        """
        params = {
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "from_chat_id": from_chat_id,
            "video_start_timestamp": video_start_timestamp,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "message_id": message_id,
        }
        return await self.method("forwardMessage", Message, **params)

    async def forward_messages(
        self,
        *,
        chat_id: int | str,
        from_chat_id: int | str,
        message_ids: list[int],
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
    ) -> list[MessageId]:
        """
        Use this method to forward multiple messages of any kind. If some of the
        specified messages can't be found or forwarded, they are skipped. Service
        messages and messages with protected content can't be forwarded. Album grouping
        is kept for forwarded messages. On success, an Array of MessageId of the sent
        messages is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the messages will be forwarded; required if the messages
                are forwarded to a direct messages chat
            from_chat_id (int | str): Unique identifier for the chat where the original
                messages were sent (or username of the target bot, supergroup or channel
                in the format @username)
            message_ids (list[int]): A JSON-serialized list of 1-100 identifiers of
                messages in the chat from_chat_id to forward. The identifiers must be
                specified in a strictly increasing order.
            disable_notification (bool | None): Sends the messages silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the forwarded
                messages from forwarding and saving
        """
        params = {
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "from_chat_id": from_chat_id,
            "message_ids": message_ids,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
        }
        return await self.method("forwardMessages", list[MessageId], **params)

    async def copy_message(
        self,
        *,
        chat_id: int | str,
        from_chat_id: int | str,
        message_id: int,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        video_start_timestamp: int | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> MessageId:
        """
        Use this method to copy messages of any kind. Service messages, paid media
        messages, giveaway messages, giveaway winners messages, and invoice messages
        can't be copied. A quiz poll can be copied only if the value of the field
        correct_option_ids is known to the bot. The method is analogous to the method
        forwardMessage, but the copied message doesn't have a link to the original
        message. Returns the MessageId of the sent message on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            from_chat_id (int | str): Unique identifier for the chat where the original
                message was sent (or username of the target bot, supergroup or channel
                in the format @username)
            message_id (int): Message identifier in the chat specified in from_chat_id
            video_start_timestamp (int | None): New start timestamp for the copied video
                in the message
            caption (str | None): New caption for media, 0-1024 characters after
                entities parsing. If not specified, the original caption is kept.
            parse_mode (str | None): Mode for parsing entities in the new caption. See
                formatting options for more details.
            caption_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the new caption, which can be specified
                instead of parse_mode
            show_caption_above_media (bool | None): Pass True if the caption must be
                shown above the message media. Ignored if a new caption isn't specified.
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; only available when copying to private chats
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "from_chat_id": from_chat_id,
            "message_id": message_id,
            "video_start_timestamp": video_start_timestamp,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "show_caption_above_media": show_caption_above_media,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("copyMessage", MessageId, **params)

    async def copy_messages(
        self,
        *,
        chat_id: int | str,
        from_chat_id: int | str,
        message_ids: list[int],
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        remove_caption: bool | None = None,
    ) -> list[MessageId]:
        """
        Use this method to copy messages of any kind. If some of the specified messages
        can't be found or copied, they are skipped. Service messages, paid media
        messages, giveaway messages, giveaway winners messages, and invoice messages
        can't be copied. A quiz poll can be copied only if the value of the field
        correct_option_ids is known to the bot. The method is analogous to the method
        forwardMessages, but the copied messages don't have a link to the original
        message. Album grouping is kept for copied messages. On success, an Array of
        MessageId of the sent messages is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the messages will be sent; required if the messages are
                sent to a direct messages chat
            from_chat_id (int | str): Unique identifier for the chat where the original
                messages were sent (or username of the target bot, supergroup or channel
                in the format @username)
            message_ids (list[int]): A JSON-serialized list of 1-100 identifiers of
                messages in the chat from_chat_id to copy. The identifiers must be
                specified in a strictly increasing order.
            disable_notification (bool | None): Sends the messages silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent messages
                from forwarding and saving
            remove_caption (bool | None): Pass True to copy the messages without their
                captions
        """
        params = {
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "from_chat_id": from_chat_id,
            "message_ids": message_ids,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "remove_caption": remove_caption,
        }
        return await self.method("copyMessages", list[MessageId], **params)

    async def send_photo(
        self,
        *,
        chat_id: int | str,
        photo: InputFile | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        ephemeral_message_parameters: EphemeralMessageParameters | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        has_spoiler: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send photos. On success, the sent Message is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            ephemeral_message_parameters (EphemeralMessageParameters | None): A JSON-
                serialized object containing the parameters of the ephemeral message to
                send
            photo (InputFile | str): Photo to send. Pass a file_id as String to send a
                photo that exists on the Telegram servers (recommended), pass an HTTP
                URL as a String for Telegram to get a photo from the Internet, or upload
                a new photo using multipart/form-data. The photo must be at most 10 MB
                in size. The photo's width and height must not exceed 10000 in total.
                Width and height ratio must be at most 20. More information on Sending
                Files: https://core.telegram.org/bots/api#sending-files
            caption (str | None): Photo caption (may also be used when resending photos
                by file_id), 0-1024 characters after entities parsing
            parse_mode (str | None): Mode for parsing entities in the photo caption. See
                formatting options for more details.
            caption_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the caption, which can be specified
                instead of parse_mode
            show_caption_above_media (bool | None): Pass True if the caption must be
                shown above the message media
            has_spoiler (bool | None): Pass True if the photo needs to be covered with a
                spoiler animation
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "ephemeral_message_parameters": ephemeral_message_parameters,
            "photo": photo,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "show_caption_above_media": show_caption_above_media,
            "has_spoiler": has_spoiler,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendPhoto", Message, **params)

    async def send_live_photo(
        self,
        *,
        chat_id: int | str,
        live_photo: InputFile | str,
        photo: InputFile | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        ephemeral_message_parameters: EphemeralMessageParameters | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        has_spoiler: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send live photos. On success, the sent Message is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel (in the format @channelusername)
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            ephemeral_message_parameters (EphemeralMessageParameters | None): A JSON-
                serialized object containing the parameters of the ephemeral message to
                send
            live_photo (InputFile | str): Live photo video to send. The video must be no
                longer than 10 seconds and must not exceed 10 MB in size. Pass a file_id
                as String to send a video that exists on the Telegram servers
                (recommended) or upload a new video using multipart/form-data. More
                information on Sending Files:
                https://core.telegram.org/bots/api#sending-files. Sending live photos by
                a URL is currently unsupported.
            photo (InputFile | str): The static photo to send. Pass a file_id as String
                to send a photo that exists on the Telegram servers (recommended) or
                upload a new video using multipart/form-data. More information on
                Sending Files: https://core.telegram.org/bots/api#sending-files. Sending
                live photos by a URL is currently unsupported.
            caption (str | None): Video caption (may also be used when resending videos
                by file_id), 0-1024 characters after entities parsing
            parse_mode (str | None): Mode for parsing entities in the video caption. See
                formatting options for more details.
            caption_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the caption, which can be specified
                instead of parse_mode
            show_caption_above_media (bool | None): Pass True if the caption must be
                shown above the message media
            has_spoiler (bool | None): Pass True if the video needs to be covered with a
                spoiler animation
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "ephemeral_message_parameters": ephemeral_message_parameters,
            "live_photo": live_photo,
            "photo": photo,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "show_caption_above_media": show_caption_above_media,
            "has_spoiler": has_spoiler,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendLivePhoto", Message, **params)

    async def send_audio(
        self,
        *,
        chat_id: int | str,
        audio: InputFile | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        ephemeral_message_parameters: EphemeralMessageParameters | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        duration: int | None = None,
        performer: str | None = None,
        title: str | None = None,
        thumbnail: InputFile | str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send audio files, if you want Telegram clients to display
        them in the music player. Your audio must be in the .MP3 or .M4A format. On
        success, the sent Message is returned. Bots can currently send audio files of up
        to 50 MB in size, this limit may be changed in the future.
        For sending voice messages, use the sendVoice method instead.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            ephemeral_message_parameters (EphemeralMessageParameters | None): A JSON-
                serialized object containing the parameters of the ephemeral message to
                send
            audio (InputFile | str): Audio file to send. Pass a file_id as String to
                send an audio file that exists on the Telegram servers (recommended),
                pass an HTTP URL as a String for Telegram to get an audio file from the
                Internet, or upload a new one using multipart/form-data. More
                information on Sending Files:
                https://core.telegram.org/bots/api#sending-files
            caption (str | None): Audio caption, 0-1024 characters after entities
                parsing
            parse_mode (str | None): Mode for parsing entities in the audio caption. See
                formatting options for more details.
            caption_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the caption, which can be specified
                instead of parse_mode
            duration (int | None): Duration of the audio in seconds
            performer (str | None): Performer
            title (str | None): Track name
            thumbnail (InputFile | str | None): Thumbnail of the file sent; can be
                ignored if thumbnail generation for the file is supported server-side.
                The thumbnail should be in JPEG format and less than 200 kB in size. A
                thumbnail's width and height should not exceed 320. Ignored if the file
                is not uploaded using multipart/form-data. Thumbnails can't be reused
                and can be only uploaded as a new file, so you can pass
                "attach://<file_attach_name>" if the thumbnail was uploaded using
                multipart/form-data under <file_attach_name>. More information on
                Sending Files: https://core.telegram.org/bots/api#sending-files
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "ephemeral_message_parameters": ephemeral_message_parameters,
            "audio": audio,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "duration": duration,
            "performer": performer,
            "title": title,
            "thumbnail": thumbnail,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendAudio", Message, **params)

    async def send_document(
        self,
        *,
        chat_id: int | str,
        document: InputFile | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        ephemeral_message_parameters: EphemeralMessageParameters | None = None,
        thumbnail: InputFile | str | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        disable_content_type_detection: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send general files. On success, the sent Message is returned.
        Bots can currently send files of any type of up to 50 MB in size, this limit may
        be changed in the future.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            ephemeral_message_parameters (EphemeralMessageParameters | None): A JSON-
                serialized object containing the parameters of the ephemeral message to
                send
            document (InputFile | str): File to send. Pass a file_id as String to send a
                file that exists on the Telegram servers (recommended), pass an HTTP URL
                as a String for Telegram to get a file from the Internet, or upload a
                new one using multipart/form-data. More information on Sending Files:
                https://core.telegram.org/bots/api#sending-files
            thumbnail (InputFile | str | None): Thumbnail of the file sent; can be
                ignored if thumbnail generation for the file is supported server-side.
                The thumbnail should be in JPEG format and less than 200 kB in size. A
                thumbnail's width and height should not exceed 320. Ignored if the file
                is not uploaded using multipart/form-data. Thumbnails can't be reused
                and can be only uploaded as a new file, so you can pass
                "attach://<file_attach_name>" if the thumbnail was uploaded using
                multipart/form-data under <file_attach_name>. More information on
                Sending Files: https://core.telegram.org/bots/api#sending-files
            caption (str | None): Document caption (may also be used when resending
                documents by file_id), 0-1024 characters after entities parsing
            parse_mode (str | None): Mode for parsing entities in the document caption.
                See formatting options for more details.
            caption_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the caption, which can be specified
                instead of parse_mode
            disable_content_type_detection (bool | None): Disables automatic server-side
                content type detection for files uploaded using multipart/form-data
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "ephemeral_message_parameters": ephemeral_message_parameters,
            "document": document,
            "thumbnail": thumbnail,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "disable_content_type_detection": disable_content_type_detection,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendDocument", Message, **params)

    async def send_video(
        self,
        *,
        chat_id: int | str,
        video: InputFile | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        ephemeral_message_parameters: EphemeralMessageParameters | None = None,
        duration: int | None = None,
        width: int | None = None,
        height: int | None = None,
        thumbnail: InputFile | str | None = None,
        cover: InputFile | str | None = None,
        start_timestamp: int | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        has_spoiler: bool | None = None,
        supports_streaming: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send video files, Telegram clients support MPEG4 videos
        (other formats may be sent as Document). On success, the sent Message is
        returned. Bots can currently send video files of up to 50 MB in size, this limit
        may be changed in the future.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            ephemeral_message_parameters (EphemeralMessageParameters | None): A JSON-
                serialized object containing the parameters of the ephemeral message to
                send
            video (InputFile | str): Video to send. Pass a file_id as String to send a
                video that exists on the Telegram servers (recommended), pass an HTTP
                URL as a String for Telegram to get a video from the Internet, or upload
                a new video using multipart/form-data. More information on Sending
                Files: https://core.telegram.org/bots/api#sending-files
            duration (int | None): Duration of sent video in seconds
            width (int | None): Video width
            height (int | None): Video height
            thumbnail (InputFile | str | None): Thumbnail of the file sent; can be
                ignored if thumbnail generation for the file is supported server-side.
                The thumbnail should be in JPEG format and less than 200 kB in size. A
                thumbnail's width and height should not exceed 320. Ignored if the file
                is not uploaded using multipart/form-data. Thumbnails can't be reused
                and can be only uploaded as a new file, so you can pass
                "attach://<file_attach_name>" if the thumbnail was uploaded using
                multipart/form-data under <file_attach_name>. More information on
                Sending Files: https://core.telegram.org/bots/api#sending-files
            cover (InputFile | str | None): Cover for the video in the message. Pass a
                file_id to send a file that exists on the Telegram servers
                (recommended), pass an HTTP URL for Telegram to get a file from the
                Internet, or pass "attach://<file_attach_name>" to upload a new one
                using multipart/form-data under <file_attach_name> name. More
                information on Sending Files:
                https://core.telegram.org/bots/api#sending-files
            start_timestamp (int | None): Start timestamp for the video in the message
            caption (str | None): Video caption (may also be used when resending videos
                by file_id), 0-1024 characters after entities parsing
            parse_mode (str | None): Mode for parsing entities in the video caption. See
                formatting options for more details.
            caption_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the caption, which can be specified
                instead of parse_mode
            show_caption_above_media (bool | None): Pass True if the caption must be
                shown above the message media
            has_spoiler (bool | None): Pass True if the video needs to be covered with a
                spoiler animation
            supports_streaming (bool | None): Pass True if the uploaded video is
                suitable for streaming
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "ephemeral_message_parameters": ephemeral_message_parameters,
            "video": video,
            "duration": duration,
            "width": width,
            "height": height,
            "thumbnail": thumbnail,
            "cover": cover,
            "start_timestamp": start_timestamp,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "show_caption_above_media": show_caption_above_media,
            "has_spoiler": has_spoiler,
            "supports_streaming": supports_streaming,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendVideo", Message, **params)

    async def send_animation(
        self,
        *,
        chat_id: int | str,
        animation: InputFile | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        ephemeral_message_parameters: EphemeralMessageParameters | None = None,
        duration: int | None = None,
        width: int | None = None,
        height: int | None = None,
        thumbnail: InputFile | str | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        has_spoiler: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without
        sound). On success, the sent Message is returned. Bots can currently send
        animation files of up to 50 MB in size, this limit may be changed in the future.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            ephemeral_message_parameters (EphemeralMessageParameters | None): A JSON-
                serialized object containing the parameters of the ephemeral message to
                send
            animation (InputFile | str): Animation to send. Pass a file_id as String to
                send an animation that exists on the Telegram servers (recommended),
                pass an HTTP URL as a String for Telegram to get an animation from the
                Internet, or upload a new animation using multipart/form-data. More
                information on Sending Files:
                https://core.telegram.org/bots/api#sending-files
            duration (int | None): Duration of sent animation in seconds
            width (int | None): Animation width
            height (int | None): Animation height
            thumbnail (InputFile | str | None): Thumbnail of the file sent; can be
                ignored if thumbnail generation for the file is supported server-side.
                The thumbnail should be in JPEG format and less than 200 kB in size. A
                thumbnail's width and height should not exceed 320. Ignored if the file
                is not uploaded using multipart/form-data. Thumbnails can't be reused
                and can be only uploaded as a new file, so you can pass
                "attach://<file_attach_name>" if the thumbnail was uploaded using
                multipart/form-data under <file_attach_name>. More information on
                Sending Files: https://core.telegram.org/bots/api#sending-files
            caption (str | None): Animation caption (may also be used when resending
                animation by file_id), 0-1024 characters after entities parsing
            parse_mode (str | None): Mode for parsing entities in the animation caption.
                See formatting options for more details.
            caption_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the caption, which can be specified
                instead of parse_mode
            show_caption_above_media (bool | None): Pass True if the caption must be
                shown above the message media
            has_spoiler (bool | None): Pass True if the animation needs to be covered
                with a spoiler animation
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "ephemeral_message_parameters": ephemeral_message_parameters,
            "animation": animation,
            "duration": duration,
            "width": width,
            "height": height,
            "thumbnail": thumbnail,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "show_caption_above_media": show_caption_above_media,
            "has_spoiler": has_spoiler,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendAnimation", Message, **params)

    async def send_voice(
        self,
        *,
        chat_id: int | str,
        voice: InputFile | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        ephemeral_message_parameters: EphemeralMessageParameters | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        duration: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send audio files, if you want Telegram clients to display the
        file as a playable voice message. For this to work, your audio must be in an
        .OGG file encoded with OPUS, or in .MP3 format, or in .M4A format (other formats
        may be sent as Audio or Document). On success, the sent Message is returned.
        Bots can currently send voice messages of up to 50 MB in size, this limit may be
        changed in the future.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            ephemeral_message_parameters (EphemeralMessageParameters | None): A JSON-
                serialized object containing the parameters of the ephemeral message to
                send
            voice (InputFile | str): Audio file to send. Pass a file_id as String to
                send a file that exists on the Telegram servers (recommended), pass an
                HTTP URL as a String for Telegram to get a file from the Internet, or
                upload a new one using multipart/form-data. More information on Sending
                Files: https://core.telegram.org/bots/api#sending-files
            caption (str | None): Voice message caption, 0-1024 characters after
                entities parsing
            parse_mode (str | None): Mode for parsing entities in the voice message
                caption. See formatting options for more details.
            caption_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the caption, which can be specified
                instead of parse_mode
            duration (int | None): Duration of the voice message in seconds
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "ephemeral_message_parameters": ephemeral_message_parameters,
            "voice": voice,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "duration": duration,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendVoice", Message, **params)

    async def send_video_note(
        self,
        *,
        chat_id: int | str,
        video_note: InputFile | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        ephemeral_message_parameters: EphemeralMessageParameters | None = None,
        duration: int | None = None,
        length: int | None = None,
        thumbnail: InputFile | str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send a rounded square MPEG4 video of up to 1 minute long. On
        success, the sent Message is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            ephemeral_message_parameters (EphemeralMessageParameters | None): A JSON-
                serialized object containing the parameters of the ephemeral message to
                send
            video_note (InputFile | str): Video note to send. Pass a file_id as String
                to send a video note that exists on the Telegram servers (recommended)
                or upload a new video using multipart/form-data. More information on
                Sending Files: https://core.telegram.org/bots/api#sending-files. Sending
                video notes by a URL is currently unsupported.
            duration (int | None): Duration of sent video in seconds
            length (int | None): Video width and height, i.e. diameter of the video
                message
            thumbnail (InputFile | str | None): Thumbnail of the file sent; can be
                ignored if thumbnail generation for the file is supported server-side.
                The thumbnail should be in JPEG format and less than 200 kB in size. A
                thumbnail's width and height should not exceed 320. Ignored if the file
                is not uploaded using multipart/form-data. Thumbnails can't be reused
                and can be only uploaded as a new file, so you can pass
                "attach://<file_attach_name>" if the thumbnail was uploaded using
                multipart/form-data under <file_attach_name>. More information on
                Sending Files: https://core.telegram.org/bots/api#sending-files
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "ephemeral_message_parameters": ephemeral_message_parameters,
            "video_note": video_note,
            "duration": duration,
            "length": length,
            "thumbnail": thumbnail,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendVideoNote", Message, **params)

    async def send_paid_media(
        self,
        *,
        chat_id: int | str,
        star_count: int,
        media: list[InputPaidMedia],
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        payload: str | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send paid media. On success, the sent Message is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username. If the
                chat is a channel, all Telegram Star proceeds from this media will be
                credited to the chat's balance. Otherwise, they will be credited to the
                bot's balance.
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            star_count (int): The number of Telegram Stars that must be paid to buy
                access to the media; 1-25000
            media (list[InputPaidMedia]): A JSON-serialized Array describing the media
                to be sent; up to 10 items
            payload (str | None): Bot-defined paid media payload, 0-128 bytes. This will
                not be displayed to the user, use it for your internal processes.
            caption (str | None): Media caption, 0-1024 characters after entities
                parsing
            parse_mode (str | None): Mode for parsing entities in the media caption. See
                formatting options for more details.
            caption_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the caption, which can be specified
                instead of parse_mode
            show_caption_above_media (bool | None): Pass True if the caption must be
                shown above the message media
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "star_count": star_count,
            "media": media,
            "payload": payload,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "show_caption_above_media": show_caption_above_media,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendPaidMedia", Message, **params)

    async def send_media_group(
        self,
        *,
        chat_id: int | str,
        media: list[InputMediaAudio]
        | list[InputMediaDocument]
        | list[InputMediaLivePhoto]
        | list[InputMediaPhoto]
        | list[InputMediaVideo],
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
    ) -> list[Message]:
        """
        Use this method to send a group of photos, live photos, videos, documents or
        audios as an album. Documents and audio files can be only grouped in an album
        with messages of the same type. On success, an Array of Message objects that
        were sent is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the messages will be sent; required if the messages are
                sent to a direct messages chat
            media (list[InputMediaAudio] | list[InputMediaDocument] |
                list[InputMediaLivePhoto] | list[InputMediaPhoto] |
                list[InputMediaVideo]): A JSON-serialized Array describing messages to
                be sent, must include 2-10 items
            disable_notification (bool | None): Sends messages silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent messages
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "media": media,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
        }
        return await self.method("sendMediaGroup", list[Message], **params)

    async def send_location(
        self,
        *,
        chat_id: int | str,
        latitude: float,
        longitude: float,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        ephemeral_message_parameters: EphemeralMessageParameters | None = None,
        horizontal_accuracy: float | None = None,
        live_period: int | None = None,
        heading: int | None = None,
        proximity_alert_radius: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send point on the map. On success, the sent Message is
        returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            ephemeral_message_parameters (EphemeralMessageParameters | None): A JSON-
                serialized object containing the parameters of the ephemeral message to
                send
            latitude (float): Latitude of the location
            longitude (float): Longitude of the location
            horizontal_accuracy (float | None): The radius of uncertainty for the
                location, measured in meters; 0-1500
            live_period (int | None): Period in seconds during which the location will
                be updated (see Live Locations), must be between 60 and 86400, or
                0x7FFFFFFF for live locations that can be edited indefinitely. Must be 0
                for ephemeral messages.
            heading (int | None): For live locations, a direction in which the user is
                moving, in degrees. Must be between 1 and 360 if specified.
            proximity_alert_radius (int | None): For live locations, a maximum distance
                for proximity alerts about approaching another chat member, in meters.
                Must be between 1 and 100000 if specified.
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "ephemeral_message_parameters": ephemeral_message_parameters,
            "latitude": latitude,
            "longitude": longitude,
            "horizontal_accuracy": horizontal_accuracy,
            "live_period": live_period,
            "heading": heading,
            "proximity_alert_radius": proximity_alert_radius,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendLocation", Message, **params)

    async def send_venue(
        self,
        *,
        chat_id: int | str,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        ephemeral_message_parameters: EphemeralMessageParameters | None = None,
        foursquare_id: str | None = None,
        foursquare_type: str | None = None,
        google_place_id: str | None = None,
        google_place_type: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send information about a venue. On success, the sent Message
        is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            ephemeral_message_parameters (EphemeralMessageParameters | None): A JSON-
                serialized object containing the parameters of the ephemeral message to
                send
            latitude (float): Latitude of the venue
            longitude (float): Longitude of the venue
            title (str): Name of the venue
            address (str): Address of the venue
            foursquare_id (str | None): Foursquare identifier of the venue
            foursquare_type (str | None): Foursquare type of the venue, if known. (For
                example, "arts_entertainment/default", "arts_entertainment/aquarium" or
                "food/icecream".)
            google_place_id (str | None): Google Places identifier of the venue
            google_place_type (str | None): Google Places type of the venue. (See
                supported types.)
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "ephemeral_message_parameters": ephemeral_message_parameters,
            "latitude": latitude,
            "longitude": longitude,
            "title": title,
            "address": address,
            "foursquare_id": foursquare_id,
            "foursquare_type": foursquare_type,
            "google_place_id": google_place_id,
            "google_place_type": google_place_type,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendVenue", Message, **params)

    async def send_contact(
        self,
        *,
        chat_id: int | str,
        phone_number: str,
        first_name: str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        ephemeral_message_parameters: EphemeralMessageParameters | None = None,
        last_name: str | None = None,
        vcard: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send phone contacts. On success, the sent Message is
        returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            ephemeral_message_parameters (EphemeralMessageParameters | None): A JSON-
                serialized object containing the parameters of the ephemeral message to
                send
            phone_number (str): Contact's phone number
            first_name (str): Contact's first name
            last_name (str | None): Contact's last name
            vcard (str | None): Additional data about the contact in the form of a
                vCard, 0-2048 bytes
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "ephemeral_message_parameters": ephemeral_message_parameters,
            "phone_number": phone_number,
            "first_name": first_name,
            "last_name": last_name,
            "vcard": vcard,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendContact", Message, **params)

    async def send_poll(
        self,
        *,
        chat_id: int | str,
        question: str,
        options: list[InputPollOption],
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        question_parse_mode: str | None = None,
        question_entities: list[MessageEntity] | None = None,
        is_anonymous: bool | None = None,
        type: str | None = None,
        allows_multiple_answers: bool | None = None,
        allows_revoting: bool | None = None,
        shuffle_options: bool | None = None,
        allow_adding_options: bool | None = None,
        hide_results_until_closes: bool | None = None,
        members_only: bool | None = None,
        country_codes: list[str] | None = None,
        correct_option_ids: list[int] | None = None,
        explanation: str | None = None,
        explanation_parse_mode: str | None = None,
        explanation_entities: list[MessageEntity] | None = None,
        explanation_media: InputPollMedia | None = None,
        open_period: int | None = None,
        close_date: int | None = None,
        is_closed: bool | None = None,
        description: str | None = None,
        description_parse_mode: str | None = None,
        description_entities: list[MessageEntity] | None = None,
        media: InputPollMedia | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send a native poll. On success, the sent Message is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username. Polls
                can't be sent to channel direct messages chats.
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            question (str): Poll question, 1-300 characters
            question_parse_mode (str | None): Mode for parsing entities in the question.
                See formatting options for more details. Currently, only custom emoji
                entities are allowed.
            question_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the poll question. It can be specified
                instead of question_parse_mode.
            options (list[InputPollOption]): A JSON-serialized list of 1-12 answer
                options
            is_anonymous (bool | None): True, if the poll needs to be anonymous,
                defaults to True
            type (str | None): Poll type, "quiz" or "regular", defaults to "regular"
            allows_multiple_answers (bool | None): Pass True if the poll allows multiple
                answers, defaults to False
            allows_revoting (bool | None): Pass True if the poll allows to change chosen
                answer options, defaults to False for quizzes and to True for regular
                polls
            shuffle_options (bool | None): Pass True if the poll options must be shown
                in random order
            allow_adding_options (bool | None): Pass True if answer options can be added
                to the poll after creation; not supported for anonymous polls and
                quizzes
            hide_results_until_closes (bool | None): Pass True if poll results must be
                shown only after the poll closes
            members_only (bool | None): Pass True if voting is limited to users who have
                been members of the chat where the poll is being sent for more than 24
                hours; for channel chats only
            country_codes (list[str] | None): A JSON-serialized list of 0-12 two-letter
                ISO 3166-1 alpha-2 country codes indicating the countries from which
                users can vote in the poll; for channel chats only. Use "FT" as a
                country code to allow users with anonymous numbers to vote. If omitted
                or empty, then users from any country can participate in the poll.
            correct_option_ids (list[int] | None): A JSON-serialized list of
                monotonically increasing 0-based identifiers of the correct answer
                options, required for polls in quiz mode
            explanation (str | None): Text that is shown when a user chooses an
                incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200
                characters with at most 2 line feeds after entities parsing
            explanation_parse_mode (str | None): Mode for parsing entities in the
                explanation. See formatting options for more details.
            explanation_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the poll explanation. It can be
                specified instead of explanation_parse_mode.
            explanation_media (InputPollMedia | None): Media added to the quiz
                explanation
            open_period (int | None): Amount of time in seconds the poll will be active
                after creation, 5-2628000. Can't be used together with close_date.
            close_date (int | None): Point in time (Unix timestamp) when the poll will
                be automatically closed. Must be at least 5 and no more than 2628000
                seconds in the future. Can't be used together with open_period.
            is_closed (bool | None): Pass True if the poll needs to be immediately
                closed. This can be useful for poll preview.
            description (str | None): Description of the poll to be sent, 0-1024
                characters after entities parsing
            description_parse_mode (str | None): Mode for parsing entities in the poll
                description. See formatting options for more details.
            description_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the poll description, which can be
                specified instead of description_parse_mode
            media (InputPollMedia | None): Media added to the poll description
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "question": question,
            "question_parse_mode": question_parse_mode,
            "question_entities": question_entities,
            "options": options,
            "is_anonymous": is_anonymous,
            "type": type,
            "allows_multiple_answers": allows_multiple_answers,
            "allows_revoting": allows_revoting,
            "shuffle_options": shuffle_options,
            "allow_adding_options": allow_adding_options,
            "hide_results_until_closes": hide_results_until_closes,
            "members_only": members_only,
            "country_codes": country_codes,
            "correct_option_ids": correct_option_ids,
            "explanation": explanation,
            "explanation_parse_mode": explanation_parse_mode,
            "explanation_entities": explanation_entities,
            "explanation_media": explanation_media,
            "open_period": open_period,
            "close_date": close_date,
            "is_closed": is_closed,
            "description": description,
            "description_parse_mode": description_parse_mode,
            "description_entities": description_entities,
            "media": media,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendPoll", Message, **params)

    async def send_checklist(
        self,
        *,
        business_connection_id: str,
        chat_id: int | str,
        checklist: InputChecklist,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message:
        """
        Use this method to send a checklist on behalf of a connected business account.
        On success, the sent Message is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection
                on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot in the format @username
            checklist (InputChecklist): A JSON-serialized object for the checklist to
                send
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message
            reply_parameters (ReplyParameters | None): A JSON-serialized object for
                description of the message to reply to
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for an
                inline keyboard
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "checklist": checklist,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendChecklist", Message, **params)

    async def send_dice(
        self,
        *,
        chat_id: int | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        emoji: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send an animated emoji that will display a random value. On
        success, the sent Message is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            emoji (str | None): Emoji on which the dice throw animation is based.
                Currently, must be one of "🎲", "🎯", "🏀", "⚽", "🎳", or "🎰". Dice can have
                values 1-6 for "🎲", "🎯" and "🎳", values 1-5 for "🏀" and "⚽", and values
                1-64 for "🎰". Defaults to "🎲".
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "emoji": emoji,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendDice", Message, **params)

    async def send_message_draft(
        self,
        *,
        chat_id: int,
        draft_id: int,
        message_thread_id: int | None = None,
        text: str | None = None,
        parse_mode: str | None = None,
        entities: list[MessageEntity] | None = None,
        can_stop: bool | None = None,
        keep_on_stop: bool | None = None,
    ) -> bool:
        """
        Use this method to stream a partial message to a user while the message is being
        generated. Note that the streamed draft is ephemeral and acts as a temporary
        30-second preview - once the output is finalized, you must call sendMessage with
        the complete message to persist it in the user's chat. Returns True on success.

        Args:
            chat_id (int): Unique identifier for the target private chat
            message_thread_id (int | None): Unique identifier for the target message
                thread
            draft_id (int): Unique identifier of the message draft; must be non-zero.
                Changes to drafts with the same identifier are animated. Otherwise, the
                draft is replaced without animation.
            text (str | None): Text of the message to be sent, 0-4096 characters after
                entities parsing. Pass an empty text to show a "Thinking..."
                placeholder.
            parse_mode (str | None): Mode for parsing entities in the message text. See
                formatting options for more details.
            entities (list[MessageEntity] | None): A JSON-serialized list of special
                entities that appear in message text, which can be specified instead of
                parse_mode
            can_stop (bool | None): Pass True to show the user a button to stop further
                drafts. The bot will receive an Update "stopped_message_generation" if
                the user presses the button.
            keep_on_stop (bool | None): Pass True to keep the draft in the chat when the
                button is pressed. The draft will still disappear after a short time or
                if the bot sends a message. To fully preserve the partial draft, the bot
                should send it as a new message.
        """
        params = {
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "draft_id": draft_id,
            "text": text,
            "parse_mode": parse_mode,
            "entities": entities,
            "can_stop": can_stop,
            "keep_on_stop": keep_on_stop,
        }
        return await self.method("sendMessageDraft", bool, **params)

    async def send_chat_action(
        self,
        *,
        chat_id: int | str,
        action: str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
    ) -> bool:
        """
        Use this method when you need to tell the user that something is happening on
        the bot's side. The status is set for 5 seconds or less (when a message arrives
        from your bot, Telegram clients clear its typing status). Returns True on
        success.
        We only recommend using this method when a response from the bot will take a
        noticeable amount of time to arrive.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the action will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot or supergroup in the format @username. Channel chats and
                channel direct messages chats aren't supported.
            message_thread_id (int | None): Unique identifier for the target message
                thread or topic of a forum; for supergroups and private chats of bots
                with forum topic mode enabled only
            action (str): Type of action to broadcast. Choose one, depending on what the
                user is about to receive: typing for text messages, upload_photo for
                photos, record_video or upload_video for videos, record_voice or
                upload_voice for voice notes, upload_document for general files,
                choose_sticker for stickers, find_location for location data,
                record_video_note or upload_video_note for video notes.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "action": action,
        }
        return await self.method("sendChatAction", bool, **params)

    async def set_message_reaction(
        self,
        *,
        chat_id: int | str,
        message_id: int,
        reaction: list[ReactionType] | None = None,
        is_big: bool | None = None,
    ) -> bool:
        """
        Use this method to change the chosen reactions on a message. Service messages of
        some types can't be reacted to. Automatically forwarded messages from a channel
        to its discussion group have the same available reactions as messages in the
        channel. Bots can't use paid reactions. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_id (int): Identifier of the target message. If the message belongs
                to a media group, the reaction is set to the first non-deleted message
                in the group instead.
            reaction (list[ReactionType] | None): A JSON-serialized list of reaction
                types to set on the message. Currently, as non-premium users, bots can
                set up to one reaction per message. A custom emoji reaction can be used
                if it is either already present on the message or explicitly allowed by
                chat administrators. Paid reactions can't be used by bots.
            is_big (bool | None): Pass True to set the reaction with a big animation
        """
        params = {
            "chat_id": chat_id,
            "message_id": message_id,
            "reaction": reaction,
            "is_big": is_big,
        }
        return await self.method("setMessageReaction", bool, **params)

    async def get_user_profile_photos(
        self,
        *,
        user_id: int,
        offset: int | None = None,
        limit: int | None = None,
    ) -> UserProfilePhotos:
        """
        Use this method to get a list of profile pictures for a user. Returns a
        UserProfilePhotos object.

        Args:
            user_id (int): Unique identifier of the target user
            offset (int | None): Sequential number of the first photo to be returned. By
                default, all photos are returned.
            limit (int | None): Limits the number of photos to be retrieved. Values
                between 1-100 are accepted. Defaults to 100.
        """
        params = {
            "user_id": user_id,
            "offset": offset,
            "limit": limit,
        }
        return await self.method("getUserProfilePhotos", UserProfilePhotos, **params)

    async def get_user_profile_audios(
        self,
        *,
        user_id: int,
        offset: int | None = None,
        limit: int | None = None,
    ) -> UserProfileAudios:
        """
        Use this method to get a list of profile audios for a user. Returns a
        UserProfileAudios object.

        Args:
            user_id (int): Unique identifier of the target user
            offset (int | None): Sequential number of the first audio to be returned. By
                default, all audios are returned.
            limit (int | None): Limits the number of audios to be retrieved. Values
                between 1-100 are accepted. Defaults to 100.
        """
        params = {
            "user_id": user_id,
            "offset": offset,
            "limit": limit,
        }
        return await self.method("getUserProfileAudios", UserProfileAudios, **params)

    async def set_user_emoji_status(
        self,
        *,
        user_id: int,
        emoji_status_custom_emoji_id: str | None = None,
        emoji_status_expiration_date: int | None = None,
    ) -> bool:
        """
        Changes the emoji status for a given user that previously allowed the bot to
        manage their emoji status via the Mini App method requestEmojiStatusAccess.
        Returns True on success.

        Args:
            user_id (int): Unique identifier of the target user
            emoji_status_custom_emoji_id (str | None): Custom emoji identifier of the
                emoji status to set. Pass an empty string to remove the status.
            emoji_status_expiration_date (int | None): Expiration date of the emoji
                status, if any
        """
        params = {
            "user_id": user_id,
            "emoji_status_custom_emoji_id": emoji_status_custom_emoji_id,
            "emoji_status_expiration_date": emoji_status_expiration_date,
        }
        return await self.method("setUserEmojiStatus", bool, **params)

    async def get_file(
        self,
        *,
        file_id: str,
    ) -> File:
        """
        Use this method to get basic information about a file and prepare it for
        downloading. For the moment, bots can download files of up to 20MB in size. On
        success, a File object is returned. The file can then be downloaded via the link
        https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken
        from the response. It is guaranteed that the link will be valid for at least 1
        hour. When the link expires, a new one can be requested by calling getFile
        again.
        Note: This function may not preserve the original file name and MIME type. You
        should save the file's MIME type and name (if available) when the File object is
        received.

        Args:
            file_id (str): File identifier to get information about
        """
        params = {
            "file_id": file_id,
        }
        return await self.method("getFile", File, **params)

    async def ban_chat_member(
        self,
        *,
        chat_id: int | str,
        user_id: int,
        until_date: int | None = None,
        revoke_messages: bool | None = None,
    ) -> bool:
        """
        Use this method to ban a user in a group, a supergroup or a channel. In the case
        of supergroups and channels, the user will not be able to return to the chat on
        their own using invite links, etc., unless unbanned first. The bot must be an
        administrator in the chat for this to work and must have the appropriate
        administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target group or username of
                the target supergroup or channel in the format @username
            user_id (int): Unique identifier of the target user
            until_date (int | None): Date when the user will be unbanned; Unix time. If
                user is banned for more than 366 days or less than 30 seconds from the
                current time they are considered to be banned forever. Applied for
                supergroups and channels only.
            revoke_messages (bool | None): Pass True to delete all messages from the
                chat for the user that is being removed. If False, the user will be able
                to see messages in the group that were sent before the user was removed.
                Always True for supergroups and channels.
        """
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
            "until_date": until_date,
            "revoke_messages": revoke_messages,
        }
        return await self.method("banChatMember", bool, **params)

    async def unban_chat_member(
        self,
        *,
        chat_id: int | str,
        user_id: int,
        only_if_banned: bool | None = None,
    ) -> bool:
        """
        Use this method to unban a previously banned user in a supergroup or channel.
        The user will not return to the group or channel automatically, but will be able
        to join via link, etc. The bot must be an administrator for this to work. By
        default, this method guarantees that after the call the user is not a member of
        the chat, but will be able to join it. So if the user is a member of the chat
        they will also be removed from the chat. If you don't want this, use the
        parameter only_if_banned. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target group or username of
                the target supergroup or channel in the format @username
            user_id (int): Unique identifier of the target user
            only_if_banned (bool | None): Do nothing if the user is not banned
        """
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
            "only_if_banned": only_if_banned,
        }
        return await self.method("unbanChatMember", bool, **params)

    async def restrict_chat_member(
        self,
        *,
        chat_id: int | str,
        user_id: int,
        permissions: ChatPermissions,
        use_independent_chat_permissions: bool | None = None,
        until_date: int | None = None,
    ) -> bool:
        """
        Use this method to restrict a user in a supergroup. The bot must be an
        administrator in the supergroup for this to work and must have the appropriate
        administrator rights. Pass True for all permissions to lift restrictions from a
        user. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            user_id (int): Unique identifier of the target user
            permissions (ChatPermissions): A JSON-serialized object for new user
                permissions
            use_independent_chat_permissions (bool | None): Pass True if chat
                permissions are set independently. Otherwise, the
                can_send_other_messages and can_add_web_page_previews permissions will
                imply the can_send_messages, can_send_audios, can_send_documents,
                can_send_photos, can_send_videos, can_send_video_notes, and
                can_send_voice_notes permissions; the can_send_polls permission will
                imply the can_send_messages permission.
            until_date (int | None): Date when restrictions will be lifted for the user;
                Unix time. If user is restricted for more than 366 days or less than 30
                seconds from the current time, they are considered to be restricted
                forever.
        """
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
            "permissions": permissions,
            "use_independent_chat_permissions": use_independent_chat_permissions,
            "until_date": until_date,
        }
        return await self.method("restrictChatMember", bool, **params)

    async def promote_chat_member(
        self,
        *,
        chat_id: int | str,
        user_id: int,
        is_anonymous: bool | None = None,
        can_manage_chat: bool | None = None,
        can_delete_messages: bool | None = None,
        can_manage_video_chats: bool | None = None,
        can_restrict_members: bool | None = None,
        can_promote_members: bool | None = None,
        can_change_info: bool | None = None,
        can_invite_users: bool | None = None,
        can_post_stories: bool | None = None,
        can_edit_stories: bool | None = None,
        can_delete_stories: bool | None = None,
        can_post_messages: bool | None = None,
        can_edit_messages: bool | None = None,
        can_pin_messages: bool | None = None,
        can_manage_topics: bool | None = None,
        can_manage_direct_messages: bool | None = None,
        can_manage_tags: bool | None = None,
        can_send_welcome_messages: bool | None = None,
    ) -> bool:
        """
        Use this method to promote or demote a user in a supergroup or a channel. The
        bot must be an administrator in the chat for this to work and must have the
        appropriate administrator rights. Pass False for all boolean parameters to
        demote a user. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
            user_id (int): Unique identifier of the target user
            is_anonymous (bool | None): Pass True if the administrator's presence in the
                chat is hidden
            can_manage_chat (bool | None): Pass True if the administrator can access the
                chat event log, get boost list, see hidden supergroup and channel
                members, report spam messages, ignore slow mode, and send messages to
                the chat without paying Telegram Stars. Implied by any other
                administrator privilege.
            can_delete_messages (bool | None): Pass True if the administrator can delete
                messages of other users
            can_manage_video_chats (bool | None): Pass True if the administrator can
                manage video chats
            can_restrict_members (bool | None): Pass True if the administrator can
                restrict, ban or unban chat members, or access supergroup statistics.
                For backward compatibility, defaults to True for promotions of channel
                administrators.
            can_promote_members (bool | None): Pass True if the administrator can add
                new administrators with a subset of their own privileges or demote
                administrators that they have promoted, directly or indirectly (promoted
                by administrators that were appointed by him)
            can_change_info (bool | None): Pass True if the administrator can change
                chat title, photo and other settings
            can_invite_users (bool | None): Pass True if the administrator can invite
                new users to the chat
            can_post_stories (bool | None): Pass True if the administrator can post
                stories to the chat
            can_edit_stories (bool | None): Pass True if the administrator can edit
                stories posted by other users, post stories to the chat page, pin chat
                stories, and access the chat's story archive
            can_delete_stories (bool | None): Pass True if the administrator can delete
                stories posted by other users
            can_post_messages (bool | None): Pass True if the administrator can post
                messages in the channel, approve suggested posts, or access channel
                statistics; for channels only
            can_edit_messages (bool | None): Pass True if the administrator can edit
                messages of other users and can pin messages; for channels only
            can_pin_messages (bool | None): Pass True if the administrator can pin
                messages; for supergroups only
            can_manage_topics (bool | None): Pass True if the user is allowed to create,
                rename, close, and reopen forum topics; for supergroups only
            can_manage_direct_messages (bool | None): Pass True if the administrator can
                manage direct messages within the channel and decline suggested posts;
                for channels only
            can_manage_tags (bool | None): Pass True if the administrator can edit the
                tags of regular members; for groups and supergroups only
            can_send_welcome_messages (bool | None): Pass True if the administrator can
                manage chat welcome messages or directly send them in the case of bots
        """
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
            "is_anonymous": is_anonymous,
            "can_manage_chat": can_manage_chat,
            "can_delete_messages": can_delete_messages,
            "can_manage_video_chats": can_manage_video_chats,
            "can_restrict_members": can_restrict_members,
            "can_promote_members": can_promote_members,
            "can_change_info": can_change_info,
            "can_invite_users": can_invite_users,
            "can_post_stories": can_post_stories,
            "can_edit_stories": can_edit_stories,
            "can_delete_stories": can_delete_stories,
            "can_post_messages": can_post_messages,
            "can_edit_messages": can_edit_messages,
            "can_pin_messages": can_pin_messages,
            "can_manage_topics": can_manage_topics,
            "can_manage_direct_messages": can_manage_direct_messages,
            "can_manage_tags": can_manage_tags,
            "can_send_welcome_messages": can_send_welcome_messages,
        }
        return await self.method("promoteChatMember", bool, **params)

    async def set_chat_administrator_custom_title(
        self,
        *,
        chat_id: int | str,
        user_id: int,
        custom_title: str,
    ) -> bool:
        """
        Use this method to set a custom title for an administrator in a supergroup
        promoted by the bot. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            user_id (int): Unique identifier of the target user
            custom_title (str): New custom title for the administrator; 0-16 characters,
                emoji are not allowed
        """
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
            "custom_title": custom_title,
        }
        return await self.method("setChatAdministratorCustomTitle", bool, **params)

    async def set_chat_member_tag(
        self,
        *,
        chat_id: int | str,
        user_id: int,
        tag: str | None = None,
    ) -> bool:
        """
        Use this method to set a tag for a regular member in a group or a supergroup.
        The bot must be an administrator in the chat for this to work and must have the
        can_manage_tags administrator right. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            user_id (int): Unique identifier of the target user
            tag (str | None): New tag for the member; 0-16 characters, emoji are not
                allowed
        """
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
            "tag": tag,
        }
        return await self.method("setChatMemberTag", bool, **params)

    async def ban_chat_sender_chat(
        self,
        *,
        chat_id: int | str,
        sender_chat_id: int,
    ) -> bool:
        """
        Use this method to ban a channel chat in a supergroup or a channel. Until the
        chat is unbanned, the owner of the banned chat won't be able to send messages on
        behalf of any of their channels. The bot must be an administrator in the
        supergroup or channel for this to work and must have the appropriate
        administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
            sender_chat_id (int): Unique identifier of the target sender chat
        """
        params = {
            "chat_id": chat_id,
            "sender_chat_id": sender_chat_id,
        }
        return await self.method("banChatSenderChat", bool, **params)

    async def unban_chat_sender_chat(
        self,
        *,
        chat_id: int | str,
        sender_chat_id: int,
    ) -> bool:
        """
        Use this method to unban a previously banned channel chat in a supergroup or
        channel. The bot must be an administrator for this to work and must have the
        appropriate administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
            sender_chat_id (int): Unique identifier of the target sender chat
        """
        params = {
            "chat_id": chat_id,
            "sender_chat_id": sender_chat_id,
        }
        return await self.method("unbanChatSenderChat", bool, **params)

    async def set_chat_permissions(
        self,
        *,
        chat_id: int | str,
        permissions: ChatPermissions,
        use_independent_chat_permissions: bool | None = None,
    ) -> bool:
        """
        Use this method to set default chat permissions for all members. The bot must be
        an administrator in the group or a supergroup for this to work and must have the
        can_restrict_members administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            permissions (ChatPermissions): A JSON-serialized object for new default chat
                permissions
            use_independent_chat_permissions (bool | None): Pass True if chat
                permissions are set independently. Otherwise, the
                can_send_other_messages and can_add_web_page_previews permissions will
                imply the can_send_messages, can_send_audios, can_send_documents,
                can_send_photos, can_send_videos, can_send_video_notes, and
                can_send_voice_notes permissions; the can_send_polls permission will
                imply the can_send_messages permission.
        """
        params = {
            "chat_id": chat_id,
            "permissions": permissions,
            "use_independent_chat_permissions": use_independent_chat_permissions,
        }
        return await self.method("setChatPermissions", bool, **params)

    async def export_chat_invite_link(
        self,
        *,
        chat_id: int | str,
    ) -> str:
        """
        Use this method to generate a new primary invite link for a chat; any previously
        generated primary link is revoked. The bot must be an administrator in the chat
        for this to work and must have the appropriate administrator rights. Returns the
        new invite link as String on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
        """
        params = {
            "chat_id": chat_id,
        }
        return await self.method("exportChatInviteLink", str, **params)

    async def create_chat_invite_link(
        self,
        *,
        chat_id: int | str,
        name: str | None = None,
        expire_date: int | None = None,
        member_limit: int | None = None,
        creates_join_request: bool | None = None,
    ) -> ChatInviteLink:
        """
        Use this method to create an additional invite link for a chat. The bot must be
        an administrator in the chat for this to work and must have the appropriate
        administrator rights. The link can be revoked using the method
        revokeChatInviteLink. Returns the new invite link as ChatInviteLink object.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
            name (str | None): Invite link name; 0-32 characters
            expire_date (int | None): Point in time (Unix timestamp) when the link will
                expire
            member_limit (int | None): The maximum number of users that can be members
                of the chat simultaneously after joining the chat via this invite link;
                1-99999
            creates_join_request (bool | None): True, if users joining the chat via the
                link need to be approved by chat administrators. If True, member_limit
                can't be specified.
        """
        params = {
            "chat_id": chat_id,
            "name": name,
            "expire_date": expire_date,
            "member_limit": member_limit,
            "creates_join_request": creates_join_request,
        }
        return await self.method("createChatInviteLink", ChatInviteLink, **params)

    async def edit_chat_invite_link(
        self,
        *,
        chat_id: int | str,
        invite_link: str,
        name: str | None = None,
        expire_date: int | None = None,
        member_limit: int | None = None,
        creates_join_request: bool | None = None,
    ) -> ChatInviteLink:
        """
        Use this method to edit a non-primary invite link created by the bot. The bot
        must be an administrator in the chat for this to work and must have the
        appropriate administrator rights. Returns the edited invite link as a
        ChatInviteLink object.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
            invite_link (str): The invite link to edit
            name (str | None): Invite link name; 0-32 characters
            expire_date (int | None): Point in time (Unix timestamp) when the link will
                expire
            member_limit (int | None): The maximum number of users that can be members
                of the chat simultaneously after joining the chat via this invite link;
                1-99999
            creates_join_request (bool | None): True, if users joining the chat via the
                link need to be approved by chat administrators. If True, member_limit
                can't be specified.
        """
        params = {
            "chat_id": chat_id,
            "invite_link": invite_link,
            "name": name,
            "expire_date": expire_date,
            "member_limit": member_limit,
            "creates_join_request": creates_join_request,
        }
        return await self.method("editChatInviteLink", ChatInviteLink, **params)

    async def create_chat_subscription_invite_link(
        self,
        *,
        chat_id: int | str,
        subscription_period: int,
        subscription_price: int,
        name: str | None = None,
    ) -> ChatInviteLink:
        """
        Use this method to create a subscription invite link for a channel chat. The bot
        must have the can_invite_users administrator rights. The link can be edited
        using the method editChatSubscriptionInviteLink or revoked using the method
        revokeChatInviteLink. Returns the new invite link as a ChatInviteLink object.

        Args:
            chat_id (int | str): Unique identifier for the target channel chat or
                username of the target channel in the format @username
            name (str | None): Invite link name; 0-32 characters
            subscription_period (int): The number of seconds the subscription will be
                active for before the next payment. Currently, it must always be 2592000
                (30 days).
            subscription_price (int): The amount of Telegram Stars a user must pay
                initially and after each subsequent subscription period to be a member
                of the chat; 1-10000
        """
        params = {
            "chat_id": chat_id,
            "name": name,
            "subscription_period": subscription_period,
            "subscription_price": subscription_price,
        }
        return await self.method(
            "createChatSubscriptionInviteLink", ChatInviteLink, **params
        )

    async def edit_chat_subscription_invite_link(
        self,
        *,
        chat_id: int | str,
        invite_link: str,
        name: str | None = None,
    ) -> ChatInviteLink:
        """
        Use this method to edit a subscription invite link created by the bot. The bot
        must have the can_invite_users administrator rights. Returns the edited invite
        link as a ChatInviteLink object.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
            invite_link (str): The invite link to edit
            name (str | None): Invite link name; 0-32 characters
        """
        params = {
            "chat_id": chat_id,
            "invite_link": invite_link,
            "name": name,
        }
        return await self.method(
            "editChatSubscriptionInviteLink", ChatInviteLink, **params
        )

    async def revoke_chat_invite_link(
        self,
        *,
        chat_id: int | str,
        invite_link: str,
    ) -> ChatInviteLink:
        """
        Use this method to revoke an invite link created by the bot. If the primary link
        is revoked, a new link is automatically generated. The bot must be an
        administrator in the chat for this to work and must have the appropriate
        administrator rights. Returns the revoked invite link as ChatInviteLink object.

        Args:
            chat_id (int | str): Unique identifier of the target chat or username of the
                target channel in the format @username
            invite_link (str): The invite link to revoke
        """
        params = {
            "chat_id": chat_id,
            "invite_link": invite_link,
        }
        return await self.method("revokeChatInviteLink", ChatInviteLink, **params)

    async def approve_chat_join_request(
        self,
        *,
        chat_id: int | str,
        user_id: int,
    ) -> bool:
        """
        Use this method to approve a chat join request. The bot must be an administrator
        in the chat for this to work and must have the can_invite_users administrator
        right. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
            user_id (int): Unique identifier of the target user
        """
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
        }
        return await self.method("approveChatJoinRequest", bool, **params)

    async def decline_chat_join_request(
        self,
        *,
        chat_id: int | str,
        user_id: int,
    ) -> bool:
        """
        Use this method to decline a chat join request. The bot must be an administrator
        in the chat for this to work and must have the can_invite_users administrator
        right. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
            user_id (int): Unique identifier of the target user
        """
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
        }
        return await self.method("declineChatJoinRequest", bool, **params)

    async def answer_chat_join_request_query(
        self,
        *,
        chat_join_request_query_id: str,
        result: str,
    ) -> bool:
        """
        Use this method to process a received chat join request query. Returns True on
        success.

        Args:
            chat_join_request_query_id (str): Unique identifier of the join request
                query
            result (str): Result of the query. Must be either "approve" to allow the
                user to join the chat, "decline" to disallow the user to join the chat,
                or "queue" to leave the decision to other administrators.
        """
        params = {
            "chat_join_request_query_id": chat_join_request_query_id,
            "result": result,
        }
        return await self.method("answerChatJoinRequestQuery", bool, **params)

    async def send_chat_join_request_web_app(
        self,
        *,
        chat_join_request_query_id: str,
        web_app_url: str,
    ) -> bool:
        """
        Use this method to process a received chat join request query by showing a Mini
        App to the user before deciding the outcome. Call answerChatJoinRequestQuery to
        resolve the join request query based on the user interaction with the Mini App.
        Returns True on success.

        Args:
            chat_join_request_query_id (str): Unique identifier of the join request
                query
            web_app_url (str): An HTTPS URL of a Web App to be opened with additional
                data as specified in Initializing Web Apps
        """
        params = {
            "chat_join_request_query_id": chat_join_request_query_id,
            "web_app_url": web_app_url,
        }
        return await self.method("sendChatJoinRequestWebApp", bool, **params)

    async def set_chat_photo(
        self,
        *,
        chat_id: int | str,
        photo: InputFile,
    ) -> bool:
        """
        Use this method to set a new profile photo for the chat. Photos can't be changed
        for private chats. The bot must be an administrator in the chat for this to work
        and must have the appropriate administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
            photo (InputFile): New chat photo, uploaded using multipart/form-data
        """
        params = {
            "chat_id": chat_id,
            "photo": photo,
        }
        return await self.method("setChatPhoto", bool, **params)

    async def delete_chat_photo(
        self,
        *,
        chat_id: int | str,
    ) -> bool:
        """
        Use this method to delete a chat photo. Photos can't be changed for private
        chats. The bot must be an administrator in the chat for this to work and must
        have the appropriate administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
        """
        params = {
            "chat_id": chat_id,
        }
        return await self.method("deleteChatPhoto", bool, **params)

    async def set_chat_title(
        self,
        *,
        chat_id: int | str,
        title: str,
    ) -> bool:
        """
        Use this method to change the title of a chat. Titles can't be changed for
        private chats. The bot must be an administrator in the chat for this to work and
        must have the appropriate administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
            title (str): New chat title, 1-128 characters
        """
        params = {
            "chat_id": chat_id,
            "title": title,
        }
        return await self.method("setChatTitle", bool, **params)

    async def set_chat_description(
        self,
        *,
        chat_id: int | str,
        description: str | None = None,
    ) -> bool:
        """
        Use this method to change the description of a group, a supergroup or a channel.
        The bot must be an administrator in the chat for this to work and must have the
        appropriate administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
            description (str | None): New chat description, 0-255 characters
        """
        params = {
            "chat_id": chat_id,
            "description": description,
        }
        return await self.method("setChatDescription", bool, **params)

    async def pin_chat_message(
        self,
        *,
        chat_id: int | str,
        message_id: int,
        business_connection_id: str | None = None,
        disable_notification: bool | None = None,
    ) -> bool:
        """
        Use this method to add a message to the list of pinned messages in a chat. In
        private chats and channel direct messages chats, all non-service messages can be
        pinned. Conversely, the bot must be an administrator with the 'can_pin_messages'
        right or the 'can_edit_messages' right to pin messages in groups and channels
        respectively. Returns True on success.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be pinned
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
            message_id (int): Identifier of a message to pin
            disable_notification (bool | None): Pass True if it is not necessary to send
                a notification to all chat members about the new pinned message.
                Notifications are always disabled in channels and private chats.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_id": message_id,
            "disable_notification": disable_notification,
        }
        return await self.method("pinChatMessage", bool, **params)

    async def unpin_chat_message(
        self,
        *,
        chat_id: int | str,
        business_connection_id: str | None = None,
        message_id: int | None = None,
    ) -> bool:
        """
        Use this method to remove a message from the list of pinned messages in a chat.
        In private chats and channel direct messages chats, all messages can be
        unpinned. Conversely, the bot must be an administrator with the
        'can_pin_messages' right or the 'can_edit_messages' right to unpin messages in
        groups and channels respectively. Returns True on success.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be unpinned
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
            message_id (int | None): Identifier of the message to unpin. Required if
                business_connection_id is specified. If not specified, the most recent
                pinned message (by sending date) will be unpinned.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_id": message_id,
        }
        return await self.method("unpinChatMessage", bool, **params)

    async def unpin_all_chat_messages(
        self,
        *,
        chat_id: int | str,
    ) -> bool:
        """
        Use this method to clear the list of pinned messages in a chat. In private chats
        and channel direct messages chats, no additional rights are required to unpin
        all pinned messages. Conversely, the bot must be an administrator with the
        'can_pin_messages' right or the 'can_edit_messages' right to unpin all pinned
        messages in groups and channels respectively. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
        """
        params = {
            "chat_id": chat_id,
        }
        return await self.method("unpinAllChatMessages", bool, **params)

    async def leave_chat(
        self,
        *,
        chat_id: int | str,
    ) -> bool:
        """
        Use this method for your bot to leave a group, supergroup or channel. Returns
        True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup or channel in the format @username. Channel direct
                messages chats aren't supported; leave the corresponding channel
                instead.
        """
        params = {
            "chat_id": chat_id,
        }
        return await self.method("leaveChat", bool, **params)

    async def get_chat(
        self,
        *,
        chat_id: int | str,
    ) -> ChatFullInfo:
        """
        Use this method to get up-to-date information about the chat. Returns a
        ChatFullInfo object on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup or channel in the format @username
        """
        params = {
            "chat_id": chat_id,
        }
        return await self.method("getChat", ChatFullInfo, **params)

    async def get_chat_administrators(
        self,
        *,
        chat_id: int | str,
        return_bots: bool | None = None,
    ) -> list[ChatMember]:
        """
        Use this method to get a list of administrators in a chat. Returns an Array of
        ChatMember objects.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup or channel in the format @username
            return_bots (bool | None): Pass True to additionally receive all bots that
                are administrators of the chat. By default, bots other than the current
                bot are omitted.
        """
        params = {
            "chat_id": chat_id,
            "return_bots": return_bots,
        }
        return await self.method("getChatAdministrators", list[ChatMember], **params)

    async def get_chat_member_count(
        self,
        *,
        chat_id: int | str,
    ) -> int:
        """
        Use this method to get the number of members in a chat. Returns Integer on
        success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup or channel in the format @username
        """
        params = {
            "chat_id": chat_id,
        }
        return await self.method("getChatMemberCount", int, **params)

    async def get_chat_member(
        self,
        *,
        chat_id: int | str,
        user_id: int,
    ) -> ChatMember:
        """
        Use this method to get information about a member of a chat. The method is only
        guaranteed to work for other users if the bot is an administrator in the chat.
        Returns a ChatMember object on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup or channel in the format @username
            user_id (int): Unique identifier of the target user
        """
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
        }
        return await self.method("getChatMember", ChatMember, **params)

    async def get_user_personal_chat_messages(
        self,
        *,
        user_id: int,
        limit: int,
    ) -> list[Message]:
        """
        Use this method to get the last messages from the personal chat (i.e., the chat
        currently added to their profile) of a given user. On success, an Array of
        Message objects is returned.

        Args:
            user_id (int): Unique identifier for the target user
            limit (int): The maximum number of messages to return; 1-20
        """
        params = {
            "user_id": user_id,
            "limit": limit,
        }
        return await self.method("getUserPersonalChatMessages", list[Message], **params)

    async def set_chat_sticker_set(
        self,
        *,
        chat_id: int | str,
        sticker_set_name: str,
    ) -> bool:
        """
        Use this method to set a new group sticker set for a supergroup. The bot must be
        an administrator in the chat for this to work and must have the appropriate
        administrator rights. Use the field can_set_sticker_set optionally returned in
        getChat requests to check if the bot can use this method. Returns True on
        success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            sticker_set_name (str): Name of the sticker set to be set as the group
                sticker set
        """
        params = {
            "chat_id": chat_id,
            "sticker_set_name": sticker_set_name,
        }
        return await self.method("setChatStickerSet", bool, **params)

    async def delete_chat_sticker_set(
        self,
        *,
        chat_id: int | str,
    ) -> bool:
        """
        Use this method to delete a group sticker set from a supergroup. The bot must be
        an administrator in the chat for this to work and must have the appropriate
        administrator rights. Use the field can_set_sticker_set optionally returned in
        getChat requests to check if the bot can use this method. Returns True on
        success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
        """
        params = {
            "chat_id": chat_id,
        }
        return await self.method("deleteChatStickerSet", bool, **params)

    async def get_forum_topic_icon_stickers(
        self,
    ) -> list[Sticker]:
        """
        Use this method to get custom emoji stickers, which can be used as a forum topic
        icon by any user. Requires no parameters. Returns an Array of Sticker objects.
        """
        params = {}
        return await self.method("getForumTopicIconStickers", list[Sticker], **params)

    async def create_forum_topic(
        self,
        *,
        chat_id: int | str,
        name: str,
        icon_color: int | None = None,
        icon_custom_emoji_id: str | None = None,
    ) -> ForumTopic:
        """
        Use this method to create a topic in a forum supergroup chat or a private chat
        with a user. In the case of a supergroup chat the bot must be an administrator
        in the chat for this to work and must have the can_manage_topics administrator
        right. Returns information about the created topic as a ForumTopic object.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            name (str): Topic name, 1-128 characters
            icon_color (int | None): Color of the topic icon in RGB format. Currently,
                must be one of 7322096 (0x6FB9F0), 16766590 (0xFFD67E), 13338331
                (0xCB86DB), 9367192 (0x8EEE98), 16749490 (0xFF93B2), or 16478047
                (0xFB6F5F).
            icon_custom_emoji_id (str | None): Unique identifier of the custom emoji
                shown as the topic icon. Use getForumTopicIconStickers to get all
                allowed custom emoji identifiers.
        """
        params = {
            "chat_id": chat_id,
            "name": name,
            "icon_color": icon_color,
            "icon_custom_emoji_id": icon_custom_emoji_id,
        }
        return await self.method("createForumTopic", ForumTopic, **params)

    async def edit_forum_topic(
        self,
        *,
        chat_id: int | str,
        message_thread_id: int,
        name: str | None = None,
        icon_custom_emoji_id: str | None = None,
    ) -> bool:
        """
        Use this method to edit name and icon of a topic in a forum supergroup chat or a
        private chat with a user. In the case of a supergroup chat the bot must be an
        administrator in the chat for this to work and must have the can_manage_topics
        administrator rights, unless it is the creator of the topic. Returns True on
        success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            message_thread_id (int): Unique identifier for the target message thread of
                the forum topic
            name (str | None): New topic name, 0-128 characters. If not specified or
                empty, the current name of the topic will be kept.
            icon_custom_emoji_id (str | None): New unique identifier of the custom emoji
                shown as the topic icon. Use getForumTopicIconStickers to get all
                allowed custom emoji identifiers. Pass an empty string to remove the
                icon. If not specified, the current icon will be kept.
        """
        params = {
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "name": name,
            "icon_custom_emoji_id": icon_custom_emoji_id,
        }
        return await self.method("editForumTopic", bool, **params)

    async def close_forum_topic(
        self,
        *,
        chat_id: int | str,
        message_thread_id: int,
    ) -> bool:
        """
        Use this method to close an open topic in a forum supergroup chat. The bot must
        be an administrator in the chat for this to work and must have the
        can_manage_topics administrator rights, unless it is the creator of the topic.
        Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            message_thread_id (int): Unique identifier for the target message thread of
                the forum topic
        """
        params = {
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
        }
        return await self.method("closeForumTopic", bool, **params)

    async def reopen_forum_topic(
        self,
        *,
        chat_id: int | str,
        message_thread_id: int,
    ) -> bool:
        """
        Use this method to reopen a closed topic in a forum supergroup chat. The bot
        must be an administrator in the chat for this to work and must have the
        can_manage_topics administrator rights, unless it is the creator of the topic.
        Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            message_thread_id (int): Unique identifier for the target message thread of
                the forum topic
        """
        params = {
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
        }
        return await self.method("reopenForumTopic", bool, **params)

    async def delete_forum_topic(
        self,
        *,
        chat_id: int | str,
        message_thread_id: int,
    ) -> bool:
        """
        Use this method to delete a forum topic along with all its messages in a forum
        supergroup chat or a private chat with a user. In the case of a supergroup chat
        the bot must be an administrator in the chat for this to work and must have the
        can_delete_messages administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            message_thread_id (int): Unique identifier for the target message thread of
                the forum topic
        """
        params = {
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
        }
        return await self.method("deleteForumTopic", bool, **params)

    async def unpin_all_forum_topic_messages(
        self,
        *,
        chat_id: int | str,
        message_thread_id: int,
    ) -> bool:
        """
        Use this method to clear the list of pinned messages in a forum topic in a forum
        supergroup chat or a private chat with a user. In the case of a supergroup chat
        the bot must be an administrator in the chat for this to work and must have the
        can_pin_messages administrator right in the supergroup. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            message_thread_id (int): Unique identifier for the target message thread of
                the forum topic
        """
        params = {
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
        }
        return await self.method("unpinAllForumTopicMessages", bool, **params)

    async def edit_general_forum_topic(
        self,
        *,
        chat_id: int | str,
        name: str,
    ) -> bool:
        """
        Use this method to edit the name of the 'General' topic in a forum supergroup
        chat. The bot must be an administrator in the chat for this to work and must
        have the can_manage_topics administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            name (str): New topic name, 1-128 characters
        """
        params = {
            "chat_id": chat_id,
            "name": name,
        }
        return await self.method("editGeneralForumTopic", bool, **params)

    async def close_general_forum_topic(
        self,
        *,
        chat_id: int | str,
    ) -> bool:
        """
        Use this method to close an open 'General' topic in a forum supergroup chat. The
        bot must be an administrator in the chat for this to work and must have the
        can_manage_topics administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
        """
        params = {
            "chat_id": chat_id,
        }
        return await self.method("closeGeneralForumTopic", bool, **params)

    async def reopen_general_forum_topic(
        self,
        *,
        chat_id: int | str,
    ) -> bool:
        """
        Use this method to reopen a closed 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have the
        can_manage_topics administrator rights. The topic will be automatically unhidden
        if it was hidden. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
        """
        params = {
            "chat_id": chat_id,
        }
        return await self.method("reopenGeneralForumTopic", bool, **params)

    async def hide_general_forum_topic(
        self,
        *,
        chat_id: int | str,
    ) -> bool:
        """
        Use this method to hide the 'General' topic in a forum supergroup chat. The bot
        must be an administrator in the chat for this to work and must have the
        can_manage_topics administrator rights. The topic will be automatically closed
        if it was open. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
        """
        params = {
            "chat_id": chat_id,
        }
        return await self.method("hideGeneralForumTopic", bool, **params)

    async def unhide_general_forum_topic(
        self,
        *,
        chat_id: int | str,
    ) -> bool:
        """
        Use this method to unhide the 'General' topic in a forum supergroup chat. The
        bot must be an administrator in the chat for this to work and must have the
        can_manage_topics administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
        """
        params = {
            "chat_id": chat_id,
        }
        return await self.method("unhideGeneralForumTopic", bool, **params)

    async def unpin_all_general_forum_topic_messages(
        self,
        *,
        chat_id: int | str,
    ) -> bool:
        """
        Use this method to clear the list of pinned messages in a General forum topic.
        The bot must be an administrator in the chat for this to work and must have the
        can_pin_messages administrator right in the supergroup. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
        """
        params = {
            "chat_id": chat_id,
        }
        return await self.method("unpinAllGeneralForumTopicMessages", bool, **params)

    async def answer_callback_query(
        self,
        *,
        callback_query_id: str,
        text: str | None = None,
        show_alert: bool | None = None,
        url: str | None = None,
        cache_time: int | None = None,
    ) -> bool:
        """
        Use this method to send answers to callback queries sent from inline keyboards.
        The answer will be displayed to the user as a notification at the top of the
        chat screen or as an alert. On success, True is returned.

        Args:
            callback_query_id (str): Unique identifier for the query to be answered
            text (str | None): Text of the notification. If not specified, nothing will
                be shown to the user, 0-200 characters.
            show_alert (bool | None): If True, an alert will be shown by the client
                instead of a notification at the top of the chat screen. Defaults to
                False.
            url (str | None): URL that will be opened by the user's client. If you have
                created a Game and accepted the conditions via @BotFather, specify the
                URL that opens your game - note that this will only work if the query
                comes from a callback_game button. Otherwise, you may use links like
                t.me/your_bot?start=XXXX that open your bot with a parameter.
            cache_time (int | None): The maximum amount of time in seconds that the
                result of the callback query may be cached client-side. Defaults to 0.
        """
        params = {
            "callback_query_id": callback_query_id,
            "text": text,
            "show_alert": show_alert,
            "url": url,
            "cache_time": cache_time,
        }
        return await self.method("answerCallbackQuery", bool, **params)

    async def answer_guest_query(
        self,
        *,
        guest_query_id: str,
        result: InlineQueryResult,
    ) -> SentGuestMessage:
        """
        Use this method to reply to a received guest message. On success, a
        SentGuestMessage object is returned.

        Args:
            guest_query_id (str): Unique identifier for the query to be answered
            result (InlineQueryResult): A JSON-serialized object describing the message
                to be sent
        """
        params = {
            "guest_query_id": guest_query_id,
            "result": result,
        }
        return await self.method("answerGuestQuery", SentGuestMessage, **params)

    async def get_user_chat_boosts(
        self,
        *,
        chat_id: int | str,
        user_id: int,
    ) -> UserChatBoosts:
        """
        Use this method to get the list of boosts added to a chat by a user. Requires
        administrator rights in the chat. Returns a UserChatBoosts object.

        Args:
            chat_id (int | str): Unique identifier for the chat or username of the
                channel in the format @username
            user_id (int): Unique identifier of the target user
        """
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
        }
        return await self.method("getUserChatBoosts", UserChatBoosts, **params)

    async def get_business_connection(
        self,
        *,
        business_connection_id: str,
    ) -> BusinessConnection:
        """
        Use this method to get information about the connection of the bot with a
        business account. Returns a BusinessConnection object on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
        """
        params = {
            "business_connection_id": business_connection_id,
        }
        return await self.method("getBusinessConnection", BusinessConnection, **params)

    async def get_managed_bot_token(
        self,
        *,
        user_id: int,
    ) -> str:
        """
        Use this method to get the token of a managed bot. Returns the token as String
        on success.

        Args:
            user_id (int): User identifier of the managed bot whose token will be
                returned
        """
        params = {
            "user_id": user_id,
        }
        return await self.method("getManagedBotToken", str, **params)

    async def replace_managed_bot_token(
        self,
        *,
        user_id: int,
    ) -> str:
        """
        Use this method to revoke the current token of a managed bot and generate a new
        one. Returns the new token as String on success.

        Args:
            user_id (int): User identifier of the managed bot whose token will be
                replaced
        """
        params = {
            "user_id": user_id,
        }
        return await self.method("replaceManagedBotToken", str, **params)

    async def get_managed_bot_access_settings(
        self,
        *,
        user_id: int,
    ) -> BotAccessSettings:
        """
        Use this method to get the access settings of a managed bot. Returns a
        BotAccessSettings object on success.

        Args:
            user_id (int): User identifier of the managed bot whose access settings will
                be returned
        """
        params = {
            "user_id": user_id,
        }
        return await self.method(
            "getManagedBotAccessSettings", BotAccessSettings, **params
        )

    async def set_managed_bot_access_settings(
        self,
        *,
        user_id: int,
        is_access_restricted: bool,
        added_user_ids: list[int] | None = None,
    ) -> bool:
        """
        Use this method to change the access settings of a managed bot. Returns True on
        success.

        Args:
            user_id (int): User identifier of the managed bot whose access settings will
                be changed
            is_access_restricted (bool): Pass True if only selected users can access the
                bot. The bot's owner can always access it.
            added_user_ids (list[int] | None): A JSON-serialized list of up to 10
                identifiers of users who will have access to the bot in addition to its
                owner. Ignored if is_access_restricted is False.
        """
        params = {
            "user_id": user_id,
            "is_access_restricted": is_access_restricted,
            "added_user_ids": added_user_ids,
        }
        return await self.method("setManagedBotAccessSettings", bool, **params)

    async def set_my_commands(
        self,
        *,
        commands: list[BotCommand],
        scope: BotCommandScope | None = None,
        language_code: str | None = None,
    ) -> bool:
        """
        Use this method to change the list of the bot's commands. See this manual for
        more details about bot commands. Returns True on success.

        Args:
            commands (list[BotCommand]): A JSON-serialized list of bot commands to be
                set as the list of the bot's commands. At most 100 commands can be
                specified.
            scope (BotCommandScope | None): A JSON-serialized object, describing scope
                of users for which the commands are relevant. Defaults to
                BotCommandScopeDefault.
            language_code (str | None): A two-letter ISO 639-1 language code. If empty,
                commands will be applied to all users from the given scope, for whose
                language there are no dedicated commands.
        """
        params = {
            "commands": commands,
            "scope": scope,
            "language_code": language_code,
        }
        return await self.method("setMyCommands", bool, **params)

    async def delete_my_commands(
        self,
        *,
        scope: BotCommandScope | None = None,
        language_code: str | None = None,
    ) -> bool:
        """
        Use this method to delete the list of the bot's commands for the given scope and
        user language. After deletion, higher level commands will be shown to affected
        users. Returns True on success.

        Args:
            scope (BotCommandScope | None): A JSON-serialized object, describing scope
                of users for which the commands are relevant. Defaults to
                BotCommandScopeDefault.
            language_code (str | None): A two-letter ISO 639-1 language code. If empty,
                commands will be applied to all users from the given scope, for whose
                language there are no dedicated commands.
        """
        params = {
            "scope": scope,
            "language_code": language_code,
        }
        return await self.method("deleteMyCommands", bool, **params)

    async def get_my_commands(
        self,
        *,
        scope: BotCommandScope | None = None,
        language_code: str | None = None,
    ) -> list[BotCommand]:
        """
        Use this method to get the current list of the bot's commands for the given
        scope and user language. Returns an Array of BotCommand objects. If commands
        aren't set, an empty list is returned.

        Args:
            scope (BotCommandScope | None): A JSON-serialized object, describing scope
                of users. Defaults to BotCommandScopeDefault.
            language_code (str | None): A two-letter ISO 639-1 language code or an empty
                string
        """
        params = {
            "scope": scope,
            "language_code": language_code,
        }
        return await self.method("getMyCommands", list[BotCommand], **params)

    async def set_my_name(
        self,
        *,
        name: str | None = None,
        language_code: str | None = None,
    ) -> bool:
        """
        Use this method to change the bot's name. Returns True on success.

        Args:
            name (str | None): New bot name; 0-64 characters. Pass an empty string to
                remove the dedicated name for the given language.
            language_code (str | None): A two-letter ISO 639-1 language code. If empty,
                the name will be shown to all users for whose language there is no
                dedicated name.
        """
        params = {
            "name": name,
            "language_code": language_code,
        }
        return await self.method("setMyName", bool, **params)

    async def get_my_name(
        self,
        *,
        language_code: str | None = None,
    ) -> BotName:
        """
        Use this method to get the current bot name for the given user language. Returns
        BotName on success.

        Args:
            language_code (str | None): A two-letter ISO 639-1 language code or an empty
                string
        """
        params = {
            "language_code": language_code,
        }
        return await self.method("getMyName", BotName, **params)

    async def set_my_description(
        self,
        *,
        description: str | None = None,
        language_code: str | None = None,
    ) -> bool:
        """
        Use this method to change the bot's description, which is shown in the chat with
        the bot if the chat is empty. Returns True on success.

        Args:
            description (str | None): New bot description; 0-512 characters. Pass an
                empty string to remove the dedicated description for the given language.
            language_code (str | None): A two-letter ISO 639-1 language code. If empty,
                the description will be applied to all users for whose language there is
                no dedicated description.
        """
        params = {
            "description": description,
            "language_code": language_code,
        }
        return await self.method("setMyDescription", bool, **params)

    async def get_my_description(
        self,
        *,
        language_code: str | None = None,
    ) -> BotDescription:
        """
        Use this method to get the current bot description for the given user language.
        Returns BotDescription on success.

        Args:
            language_code (str | None): A two-letter ISO 639-1 language code or an empty
                string
        """
        params = {
            "language_code": language_code,
        }
        return await self.method("getMyDescription", BotDescription, **params)

    async def set_my_short_description(
        self,
        *,
        short_description: str | None = None,
        language_code: str | None = None,
    ) -> bool:
        """
        Use this method to change the bot's short description, which is shown on the
        bot's profile page and is sent together with the link when users share the bot.
        Returns True on success.

        Args:
            short_description (str | None): New short description for the bot; 0-120
                characters. Pass an empty string to remove the dedicated short
                description for the given language.
            language_code (str | None): A two-letter ISO 639-1 language code. If empty,
                the short description will be applied to all users for whose language
                there is no dedicated short description.
        """
        params = {
            "short_description": short_description,
            "language_code": language_code,
        }
        return await self.method("setMyShortDescription", bool, **params)

    async def get_my_short_description(
        self,
        *,
        language_code: str | None = None,
    ) -> BotShortDescription:
        """
        Use this method to get the current bot short description for the given user
        language. Returns BotShortDescription on success.

        Args:
            language_code (str | None): A two-letter ISO 639-1 language code or an empty
                string
        """
        params = {
            "language_code": language_code,
        }
        return await self.method("getMyShortDescription", BotShortDescription, **params)

    async def set_my_profile_photo(
        self,
        *,
        photo: InputProfilePhoto,
    ) -> bool:
        """
        Changes the profile photo of the bot. Returns True on success.

        Args:
            photo (InputProfilePhoto): The new profile photo to set
        """
        params = {
            "photo": photo,
        }
        return await self.method("setMyProfilePhoto", bool, **params)

    async def remove_my_profile_photo(
        self,
    ) -> bool:
        """
        Removes the profile photo of the bot. Requires no parameters. Returns True on
        success.
        """
        params = {}
        return await self.method("removeMyProfilePhoto", bool, **params)

    async def set_chat_menu_button(
        self,
        *,
        chat_id: int | None = None,
        menu_button: MenuButton | None = None,
    ) -> bool:
        """
        Use this method to change the bot's menu button in a private chat, or the
        default menu button. Returns True on success.

        Args:
            chat_id (int | None): Unique identifier for the target private chat. If not
                specified, the bot's default menu button will be changed.
            menu_button (MenuButton | None): A JSON-serialized object for the bot's new
                menu button. Defaults to MenuButtonDefault.
        """
        params = {
            "chat_id": chat_id,
            "menu_button": menu_button,
        }
        return await self.method("setChatMenuButton", bool, **params)

    async def get_chat_menu_button(
        self,
        *,
        chat_id: int | None = None,
    ) -> MenuButton:
        """
        Use this method to get the current value of the bot's menu button in a private
        chat, or the default menu button. Returns MenuButton on success.

        Args:
            chat_id (int | None): Unique identifier for the target private chat. If not
                specified, the bot's default menu button will be returned.
        """
        params = {
            "chat_id": chat_id,
        }
        return await self.method("getChatMenuButton", MenuButton, **params)

    async def set_my_default_administrator_rights(
        self,
        *,
        rights: ChatAdministratorRights | None = None,
        for_channels: bool | None = None,
    ) -> bool:
        """
        Use this method to change the default administrator rights requested by the bot
        when it's added as an administrator to groups or channels. These rights will be
        suggested to users, but they are free to modify the list before adding the bot.
        Returns True on success.

        Args:
            rights (ChatAdministratorRights | None): A JSON-serialized object describing
                new default administrator rights. If not specified, the default
                administrator rights will be cleared.
            for_channels (bool | None): Pass True to change the default administrator
                rights of the bot in channels. Otherwise, the default administrator
                rights of the bot for groups and supergroups will be changed.
        """
        params = {
            "rights": rights,
            "for_channels": for_channels,
        }
        return await self.method("setMyDefaultAdministratorRights", bool, **params)

    async def get_my_default_administrator_rights(
        self,
        *,
        for_channels: bool | None = None,
    ) -> ChatAdministratorRights:
        """
        Use this method to get the current default administrator rights of the bot.
        Returns ChatAdministratorRights on success.

        Args:
            for_channels (bool | None): Pass True to get default administrator rights of
                the bot in channels. Otherwise, default administrator rights of the bot
                for groups and supergroups will be returned.
        """
        params = {
            "for_channels": for_channels,
        }
        return await self.method(
            "getMyDefaultAdministratorRights", ChatAdministratorRights, **params
        )

    async def get_available_gifts(
        self,
    ) -> Gifts:
        """
        Returns the list of gifts that can be sent by the bot to users and channel
        chats. Requires no parameters. Returns a Gifts object.
        """
        params = {}
        return await self.method("getAvailableGifts", Gifts, **params)

    async def send_gift(
        self,
        *,
        gift_id: str,
        user_id: int | None = None,
        chat_id: int | str | None = None,
        pay_for_upgrade: bool | None = None,
        text: str | None = None,
        text_parse_mode: str | None = None,
        text_entities: list[MessageEntity] | None = None,
    ) -> bool:
        """
        Sends a gift to the given user or channel chat. The gift can't be converted to
        Telegram Stars by the receiver. Returns True on success.

        Args:
            user_id (int | None): Required if chat_id is not specified. Unique
                identifier of the target user who will receive the gift.
            chat_id (int | str | None): Required if user_id is not specified. Unique
                identifier for the chat or username of the channel (in the format
                @username) that will receive the gift.
            gift_id (str): Identifier of the gift; limited gifts can't be sent to
                channel chats
            pay_for_upgrade (bool | None): Pass True to pay for the gift upgrade from
                the bot's balance, thereby making the upgrade free for the receiver
            text (str | None): Text that will be shown along with the gift; 0-128
                characters
            text_parse_mode (str | None): Mode for parsing entities in the text. See
                formatting options for more details. Entities other than "bold",
                "italic", "underline", "strikethrough", "spoiler", "custom_emoji", and
                "date_time" are ignored.
            text_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the gift text. It can be specified
                instead of text_parse_mode. Entities other than "bold", "italic",
                "underline", "strikethrough", "spoiler", "custom_emoji", and "date_time"
                are ignored.
        """
        params = {
            "user_id": user_id,
            "chat_id": chat_id,
            "gift_id": gift_id,
            "pay_for_upgrade": pay_for_upgrade,
            "text": text,
            "text_parse_mode": text_parse_mode,
            "text_entities": text_entities,
        }
        return await self.method("sendGift", bool, **params)

    async def gift_premium_subscription(
        self,
        *,
        user_id: int,
        month_count: int,
        star_count: int,
        text: str | None = None,
        text_parse_mode: str | None = None,
        text_entities: list[MessageEntity] | None = None,
    ) -> bool:
        """
        Gifts a Telegram Premium subscription to the given user. Returns True on
        success.

        Args:
            user_id (int): Unique identifier of the target user who will receive a
                Telegram Premium subscription
            month_count (int): Number of months the Telegram Premium subscription will
                be active for the user; must be one of 3, 6, or 12
            star_count (int): Number of Telegram Stars to pay for the Telegram Premium
                subscription; must be 1000 for 3 months, 1500 for 6 months, and 2500 for
                12 months
            text (str | None): Text that will be shown along with the service message
                about the subscription; 0-128 characters
            text_parse_mode (str | None): Mode for parsing entities in the text. See
                formatting options for more details. Entities other than "bold",
                "italic", "underline", "strikethrough", "spoiler", "custom_emoji", and
                "date_time" are ignored.
            text_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the gift text. It can be specified
                instead of text_parse_mode. Entities other than "bold", "italic",
                "underline", "strikethrough", "spoiler", "custom_emoji", and "date_time"
                are ignored.
        """
        params = {
            "user_id": user_id,
            "month_count": month_count,
            "star_count": star_count,
            "text": text,
            "text_parse_mode": text_parse_mode,
            "text_entities": text_entities,
        }
        return await self.method("giftPremiumSubscription", bool, **params)

    async def verify_user(
        self,
        *,
        user_id: int,
        custom_description: str | None = None,
    ) -> bool:
        """
        Verifies a user on behalf of the organization which is represented by the bot.
        Returns True on success.

        Args:
            user_id (int): Unique identifier of the target user
            custom_description (str | None): Custom description for the verification;
                0-70 characters. Must be empty if the organization isn't allowed to
                provide a custom verification description.
        """
        params = {
            "user_id": user_id,
            "custom_description": custom_description,
        }
        return await self.method("verifyUser", bool, **params)

    async def verify_chat(
        self,
        *,
        chat_id: int | str,
        custom_description: str | None = None,
    ) -> bool:
        """
        Verifies a chat on behalf of the organization which is represented by the bot.
        Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username. Channel
                direct messages chats can't be verified.
            custom_description (str | None): Custom description for the verification;
                0-70 characters. Must be empty if the organization isn't allowed to
                provide a custom verification description.
        """
        params = {
            "chat_id": chat_id,
            "custom_description": custom_description,
        }
        return await self.method("verifyChat", bool, **params)

    async def remove_user_verification(
        self,
        *,
        user_id: int,
    ) -> bool:
        """
        Removes verification from a user who is currently verified on behalf of the
        organization represented by the bot. Returns True on success.

        Args:
            user_id (int): Unique identifier of the target user
        """
        params = {
            "user_id": user_id,
        }
        return await self.method("removeUserVerification", bool, **params)

    async def remove_chat_verification(
        self,
        *,
        chat_id: int | str,
    ) -> bool:
        """
        Removes verification from a chat that is currently verified on behalf of the
        organization represented by the bot. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot or channel in the format @username
        """
        params = {
            "chat_id": chat_id,
        }
        return await self.method("removeChatVerification", bool, **params)

    async def read_business_message(
        self,
        *,
        business_connection_id: str,
        chat_id: int,
        message_id: int,
    ) -> bool:
        """
        Marks incoming message as read on behalf of a business account. Requires the
        can_read_messages business bot right. Returns True on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
                on behalf of which to read the message
            chat_id (int): Unique identifier of the chat in which the message was
                received. The chat must have been active in the last 24 hours.
            message_id (int): Unique identifier of the message to mark as read
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_id": message_id,
        }
        return await self.method("readBusinessMessage", bool, **params)

    async def delete_business_messages(
        self,
        *,
        business_connection_id: str,
        message_ids: list[int],
    ) -> bool:
        """
        Delete messages on behalf of a business account. Requires the
        can_delete_sent_messages business bot right to delete messages sent by the bot
        itself, or the can_delete_all_messages business bot right to delete any message.
        Returns True on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
                on behalf of which to delete the messages
            message_ids (list[int]): A JSON-serialized list of 1-100 identifiers of
                messages to delete. All messages must be from the same chat. See
                deleteMessage for limitations on which messages can be deleted.
        """
        params = {
            "business_connection_id": business_connection_id,
            "message_ids": message_ids,
        }
        return await self.method("deleteBusinessMessages", bool, **params)

    async def set_business_account_name(
        self,
        *,
        business_connection_id: str,
        first_name: str,
        last_name: str | None = None,
    ) -> bool:
        """
        Changes the first and last name of a managed business account. Requires the
        can_change_name business bot right. Returns True on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            first_name (str): The new value of the first name for the business account;
                1-64 characters
            last_name (str | None): The new value of the last name for the business
                account; 0-64 characters
        """
        params = {
            "business_connection_id": business_connection_id,
            "first_name": first_name,
            "last_name": last_name,
        }
        return await self.method("setBusinessAccountName", bool, **params)

    async def set_business_account_username(
        self,
        *,
        business_connection_id: str,
        username: str | None = None,
    ) -> bool:
        """
        Changes the username of a managed business account. Requires the
        can_change_username business bot right. Returns True on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            username (str | None): The new value of the username for the business
                account; 0-32 characters
        """
        params = {
            "business_connection_id": business_connection_id,
            "username": username,
        }
        return await self.method("setBusinessAccountUsername", bool, **params)

    async def set_business_account_bio(
        self,
        *,
        business_connection_id: str,
        bio: str | None = None,
    ) -> bool:
        """
        Changes the bio of a managed business account. Requires the can_change_bio
        business bot right. Returns True on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            bio (str | None): The new value of the bio for the business account; 0-140
                characters
        """
        params = {
            "business_connection_id": business_connection_id,
            "bio": bio,
        }
        return await self.method("setBusinessAccountBio", bool, **params)

    async def set_business_account_profile_photo(
        self,
        *,
        business_connection_id: str,
        photo: InputProfilePhoto,
        is_public: bool | None = None,
    ) -> bool:
        """
        Changes the profile photo of a managed business account. Requires the
        can_edit_profile_photo business bot right. Returns True on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            photo (InputProfilePhoto): The new profile photo to set
            is_public (bool | None): Pass True to set the public photo, which will be
                visible even if the main photo is hidden by the business account's
                privacy settings. An account can have only one public photo.
        """
        params = {
            "business_connection_id": business_connection_id,
            "photo": photo,
            "is_public": is_public,
        }
        return await self.method("setBusinessAccountProfilePhoto", bool, **params)

    async def remove_business_account_profile_photo(
        self,
        *,
        business_connection_id: str,
        is_public: bool | None = None,
    ) -> bool:
        """
        Removes the current profile photo of a managed business account. Requires the
        can_edit_profile_photo business bot right. Returns True on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            is_public (bool | None): Pass True to remove the public photo, which is
                visible even if the main photo is hidden by the business account's
                privacy settings. After the main photo is removed, the previous profile
                photo (if present) becomes the main photo.
        """
        params = {
            "business_connection_id": business_connection_id,
            "is_public": is_public,
        }
        return await self.method("removeBusinessAccountProfilePhoto", bool, **params)

    async def set_business_account_gift_settings(
        self,
        *,
        business_connection_id: str,
        show_gift_button: bool,
        accepted_gift_types: AcceptedGiftTypes,
    ) -> bool:
        """
        Changes the privacy settings pertaining to incoming gifts in a managed business
        account. Requires the can_change_gift_settings business bot right. Returns True
        on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            show_gift_button (bool): Pass True if a button for sending a gift to the
                user or by the business account must always be shown in the input field
            accepted_gift_types (AcceptedGiftTypes): Types of gifts accepted by the
                business account
        """
        params = {
            "business_connection_id": business_connection_id,
            "show_gift_button": show_gift_button,
            "accepted_gift_types": accepted_gift_types,
        }
        return await self.method("setBusinessAccountGiftSettings", bool, **params)

    async def get_business_account_star_balance(
        self,
        *,
        business_connection_id: str,
    ) -> StarAmount:
        """
        Returns the amount of Telegram Stars owned by a managed business account.
        Requires the can_view_gifts_and_stars business bot right. Returns StarAmount on
        success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
        """
        params = {
            "business_connection_id": business_connection_id,
        }
        return await self.method("getBusinessAccountStarBalance", StarAmount, **params)

    async def transfer_business_account_stars(
        self,
        *,
        business_connection_id: str,
        star_count: int,
    ) -> bool:
        """
        Transfers Telegram Stars from the business account balance to the bot's balance.
        Requires the can_transfer_stars business bot right. Returns True on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            star_count (int): Number of Telegram Stars to transfer; 1-10000
        """
        params = {
            "business_connection_id": business_connection_id,
            "star_count": star_count,
        }
        return await self.method("transferBusinessAccountStars", bool, **params)

    async def get_business_account_gifts(
        self,
        *,
        business_connection_id: str,
        exclude_unsaved: bool | None = None,
        exclude_saved: bool | None = None,
        exclude_unlimited: bool | None = None,
        exclude_limited_upgradable: bool | None = None,
        exclude_limited_non_upgradable: bool | None = None,
        exclude_unique: bool | None = None,
        exclude_from_blockchain: bool | None = None,
        sort_by_price: bool | None = None,
        offset: str | None = None,
        limit: int | None = None,
    ) -> OwnedGifts:
        """
        Returns the gifts received and owned by a managed business account. Requires the
        can_view_gifts_and_stars business bot right. Returns OwnedGifts on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            exclude_unsaved (bool | None): Pass True to exclude gifts that aren't saved
                to the account's profile page
            exclude_saved (bool | None): Pass True to exclude gifts that are saved to
                the account's profile page
            exclude_unlimited (bool | None): Pass True to exclude gifts that can be
                purchased an unlimited number of times
            exclude_limited_upgradable (bool | None): Pass True to exclude gifts that
                can be purchased a limited number of times and can be upgraded to unique
            exclude_limited_non_upgradable (bool | None): Pass True to exclude gifts
                that can be purchased a limited number of times and can't be upgraded to
                unique
            exclude_unique (bool | None): Pass True to exclude unique gifts
            exclude_from_blockchain (bool | None): Pass True to exclude gifts that were
                assigned from the TON blockchain and can't be resold or transferred in
                Telegram
            sort_by_price (bool | None): Pass True to sort results by gift price instead
                of send date. Sorting is applied before pagination.
            offset (str | None): Offset of the first entry to return as received from
                the previous request; use empty string to get the first chunk of results
            limit (int | None): The maximum number of gifts to be returned; 1-100.
                Defaults to 100.
        """
        params = {
            "business_connection_id": business_connection_id,
            "exclude_unsaved": exclude_unsaved,
            "exclude_saved": exclude_saved,
            "exclude_unlimited": exclude_unlimited,
            "exclude_limited_upgradable": exclude_limited_upgradable,
            "exclude_limited_non_upgradable": exclude_limited_non_upgradable,
            "exclude_unique": exclude_unique,
            "exclude_from_blockchain": exclude_from_blockchain,
            "sort_by_price": sort_by_price,
            "offset": offset,
            "limit": limit,
        }
        return await self.method("getBusinessAccountGifts", OwnedGifts, **params)

    async def get_user_gifts(
        self,
        *,
        user_id: int,
        exclude_unlimited: bool | None = None,
        exclude_limited_upgradable: bool | None = None,
        exclude_limited_non_upgradable: bool | None = None,
        exclude_from_blockchain: bool | None = None,
        exclude_unique: bool | None = None,
        sort_by_price: bool | None = None,
        offset: str | None = None,
        limit: int | None = None,
    ) -> OwnedGifts:
        """
        Returns the gifts owned and hosted by a user. Returns OwnedGifts on success.

        Args:
            user_id (int): Unique identifier of the user
            exclude_unlimited (bool | None): Pass True to exclude gifts that can be
                purchased an unlimited number of times
            exclude_limited_upgradable (bool | None): Pass True to exclude gifts that
                can be purchased a limited number of times and can be upgraded to unique
            exclude_limited_non_upgradable (bool | None): Pass True to exclude gifts
                that can be purchased a limited number of times and can't be upgraded to
                unique
            exclude_from_blockchain (bool | None): Pass True to exclude gifts that were
                assigned from the TON blockchain and can't be resold or transferred in
                Telegram
            exclude_unique (bool | None): Pass True to exclude unique gifts
            sort_by_price (bool | None): Pass True to sort results by gift price instead
                of send date. Sorting is applied before pagination.
            offset (str | None): Offset of the first entry to return as received from
                the previous request; use an empty string to get the first chunk of
                results
            limit (int | None): The maximum number of gifts to be returned; 1-100.
                Defaults to 100.
        """
        params = {
            "user_id": user_id,
            "exclude_unlimited": exclude_unlimited,
            "exclude_limited_upgradable": exclude_limited_upgradable,
            "exclude_limited_non_upgradable": exclude_limited_non_upgradable,
            "exclude_from_blockchain": exclude_from_blockchain,
            "exclude_unique": exclude_unique,
            "sort_by_price": sort_by_price,
            "offset": offset,
            "limit": limit,
        }
        return await self.method("getUserGifts", OwnedGifts, **params)

    async def get_chat_gifts(
        self,
        *,
        chat_id: int | str,
        exclude_unsaved: bool | None = None,
        exclude_saved: bool | None = None,
        exclude_unlimited: bool | None = None,
        exclude_limited_upgradable: bool | None = None,
        exclude_limited_non_upgradable: bool | None = None,
        exclude_from_blockchain: bool | None = None,
        exclude_unique: bool | None = None,
        sort_by_price: bool | None = None,
        offset: str | None = None,
        limit: int | None = None,
    ) -> OwnedGifts:
        """
        Returns the gifts owned by a chat. Returns OwnedGifts on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target channel in the format @username
            exclude_unsaved (bool | None): Pass True to exclude gifts that aren't saved
                to the chat's profile page. Always True, unless the bot has the
                can_post_messages administrator right in the channel.
            exclude_saved (bool | None): Pass True to exclude gifts that are saved to
                the chat's profile page. Always False, unless the bot has the
                can_post_messages administrator right in the channel.
            exclude_unlimited (bool | None): Pass True to exclude gifts that can be
                purchased an unlimited number of times
            exclude_limited_upgradable (bool | None): Pass True to exclude gifts that
                can be purchased a limited number of times and can be upgraded to unique
            exclude_limited_non_upgradable (bool | None): Pass True to exclude gifts
                that can be purchased a limited number of times and can't be upgraded to
                unique
            exclude_from_blockchain (bool | None): Pass True to exclude gifts that were
                assigned from the TON blockchain and can't be resold or transferred in
                Telegram
            exclude_unique (bool | None): Pass True to exclude unique gifts
            sort_by_price (bool | None): Pass True to sort results by gift price instead
                of send date. Sorting is applied before pagination.
            offset (str | None): Offset of the first entry to return as received from
                the previous request; use an empty string to get the first chunk of
                results
            limit (int | None): The maximum number of gifts to be returned; 1-100.
                Defaults to 100.
        """
        params = {
            "chat_id": chat_id,
            "exclude_unsaved": exclude_unsaved,
            "exclude_saved": exclude_saved,
            "exclude_unlimited": exclude_unlimited,
            "exclude_limited_upgradable": exclude_limited_upgradable,
            "exclude_limited_non_upgradable": exclude_limited_non_upgradable,
            "exclude_from_blockchain": exclude_from_blockchain,
            "exclude_unique": exclude_unique,
            "sort_by_price": sort_by_price,
            "offset": offset,
            "limit": limit,
        }
        return await self.method("getChatGifts", OwnedGifts, **params)

    async def convert_gift_to_stars(
        self,
        *,
        business_connection_id: str,
        owned_gift_id: str,
    ) -> bool:
        """
        Converts a given regular gift to Telegram Stars. Requires the
        can_convert_gifts_to_stars business bot right. Returns True on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            owned_gift_id (str): Unique identifier of the regular gift that should be
                converted to Telegram Stars
        """
        params = {
            "business_connection_id": business_connection_id,
            "owned_gift_id": owned_gift_id,
        }
        return await self.method("convertGiftToStars", bool, **params)

    async def upgrade_gift(
        self,
        *,
        business_connection_id: str,
        owned_gift_id: str,
        keep_original_details: bool | None = None,
        star_count: int | None = None,
    ) -> bool:
        """
        Upgrades a given regular gift to a unique gift. Requires the
        can_transfer_and_upgrade_gifts business bot right. Additionally requires the
        can_transfer_stars business bot right if the upgrade is paid. Returns True on
        success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            owned_gift_id (str): Unique identifier of the regular gift that should be
                upgraded to a unique one
            keep_original_details (bool | None): Pass True to keep the original gift
                text, sender and receiver in the upgraded gift
            star_count (int | None): The amount of Telegram Stars that will be paid for
                the upgrade from the business account balance. If
                gift.prepaid_upgrade_star_count > 0, then pass 0, otherwise, the
                can_transfer_stars business bot right is required and
                gift.upgrade_star_count must be passed.
        """
        params = {
            "business_connection_id": business_connection_id,
            "owned_gift_id": owned_gift_id,
            "keep_original_details": keep_original_details,
            "star_count": star_count,
        }
        return await self.method("upgradeGift", bool, **params)

    async def transfer_gift(
        self,
        *,
        business_connection_id: str,
        owned_gift_id: str,
        new_owner_chat_id: int,
        star_count: int | None = None,
    ) -> bool:
        """
        Transfers an owned unique gift to another user. Requires the
        can_transfer_and_upgrade_gifts business bot right. Requires can_transfer_stars
        business bot right if the transfer is paid. Returns True on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            owned_gift_id (str): Unique identifier of the regular gift that should be
                transferred
            new_owner_chat_id (int): Unique identifier of the chat which will own the
                gift. The chat must be active in the last 24 hours.
            star_count (int | None): The amount of Telegram Stars that will be paid for
                the transfer from the business account balance. If positive, then the
                can_transfer_stars business bot right is required.
        """
        params = {
            "business_connection_id": business_connection_id,
            "owned_gift_id": owned_gift_id,
            "new_owner_chat_id": new_owner_chat_id,
            "star_count": star_count,
        }
        return await self.method("transferGift", bool, **params)

    async def post_story(
        self,
        *,
        business_connection_id: str,
        content: InputStoryContent,
        active_period: int,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        areas: list[StoryArea] | None = None,
        post_to_chat_page: bool | None = None,
        protect_content: bool | None = None,
    ) -> Story:
        """
        Posts a story on behalf of a managed business account. Requires the
        can_manage_stories business bot right. Returns Story on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            content (InputStoryContent): Content of the story
            active_period (int): Period after which the story is moved to the archive,
                in seconds; must be one of 6 * 3600, 12 * 3600, 86400, or 2 * 86400
            caption (str | None): Caption of the story, 0-2048 characters after entities
                parsing
            parse_mode (str | None): Mode for parsing entities in the story caption. See
                formatting options for more details.
            caption_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the caption, which can be specified
                instead of parse_mode
            areas (list[StoryArea] | None): A JSON-serialized list of clickable areas to
                be shown on the story
            post_to_chat_page (bool | None): Pass True to keep the story accessible
                after it expires
            protect_content (bool | None): Pass True if the content of the story must be
                protected from forwarding and screenshotting
        """
        params = {
            "business_connection_id": business_connection_id,
            "content": content,
            "active_period": active_period,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "areas": areas,
            "post_to_chat_page": post_to_chat_page,
            "protect_content": protect_content,
        }
        return await self.method("postStory", Story, **params)

    async def repost_story(
        self,
        *,
        business_connection_id: str,
        from_chat_id: int,
        from_story_id: int,
        active_period: int,
        post_to_chat_page: bool | None = None,
        protect_content: bool | None = None,
    ) -> Story:
        """
        Reposts a story on behalf of a business account from another business account.
        Both business accounts must be managed by the same bot, and the story on the
        source account must have been posted (or reposted) by the bot. Requires the
        can_manage_stories business bot right for both business accounts. Returns Story
        on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            from_chat_id (int): Unique identifier of the chat which posted the story
                that should be reposted
            from_story_id (int): Unique identifier of the story that should be reposted
            active_period (int): Period after which the story is moved to the archive,
                in seconds; must be one of 6 * 3600, 12 * 3600, 86400, or 2 * 86400
            post_to_chat_page (bool | None): Pass True to keep the story accessible
                after it expires
            protect_content (bool | None): Pass True if the content of the story must be
                protected from forwarding and screenshotting
        """
        params = {
            "business_connection_id": business_connection_id,
            "from_chat_id": from_chat_id,
            "from_story_id": from_story_id,
            "active_period": active_period,
            "post_to_chat_page": post_to_chat_page,
            "protect_content": protect_content,
        }
        return await self.method("repostStory", Story, **params)

    async def edit_story(
        self,
        *,
        business_connection_id: str,
        story_id: int,
        content: InputStoryContent,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        areas: list[StoryArea] | None = None,
    ) -> Story:
        """
        Edits a story previously posted by the bot on behalf of a managed business
        account. Requires the can_manage_stories business bot right. Returns Story on
        success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            story_id (int): Unique identifier of the story to edit
            content (InputStoryContent): Content of the story
            caption (str | None): Caption of the story, 0-2048 characters after entities
                parsing
            parse_mode (str | None): Mode for parsing entities in the story caption. See
                formatting options for more details.
            caption_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the caption, which can be specified
                instead of parse_mode
            areas (list[StoryArea] | None): A JSON-serialized list of clickable areas to
                be shown on the story
        """
        params = {
            "business_connection_id": business_connection_id,
            "story_id": story_id,
            "content": content,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "areas": areas,
        }
        return await self.method("editStory", Story, **params)

    async def delete_story(
        self,
        *,
        business_connection_id: str,
        story_id: int,
    ) -> bool:
        """
        Deletes a story previously posted by the bot on behalf of a managed business
        account. Requires the can_manage_stories business bot right. Returns True on
        success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
            story_id (int): Unique identifier of the story to delete
        """
        params = {
            "business_connection_id": business_connection_id,
            "story_id": story_id,
        }
        return await self.method("deleteStory", bool, **params)

    async def answer_web_app_query(
        self,
        *,
        web_app_query_id: str,
        result: InlineQueryResult,
    ) -> SentWebAppMessage:
        """
        Use this method to set the result of an interaction with a Web App and send a
        corresponding message on behalf of the user to the chat from which the query
        originated. On success, a SentWebAppMessage object is returned.

        Args:
            web_app_query_id (str): Unique identifier for the query to be answered
            result (InlineQueryResult): A JSON-serialized object describing the message
                to be sent
        """
        params = {
            "web_app_query_id": web_app_query_id,
            "result": result,
        }
        return await self.method("answerWebAppQuery", SentWebAppMessage, **params)

    async def save_prepared_inline_message(
        self,
        *,
        user_id: int,
        result: InlineQueryResult,
        allow_user_chats: bool | None = None,
        allow_bot_chats: bool | None = None,
        allow_group_chats: bool | None = None,
        allow_channel_chats: bool | None = None,
    ) -> PreparedInlineMessage:
        """
        Stores a message that can be sent by a user of a Mini App. Returns a
        PreparedInlineMessage object.

        Args:
            user_id (int): Unique identifier of the target user that can use the
                prepared message
            result (InlineQueryResult): A JSON-serialized object describing the message
                to be sent
            allow_user_chats (bool | None): Pass True if the message can be sent to
                private chats with users
            allow_bot_chats (bool | None): Pass True if the message can be sent to
                private chats with bots
            allow_group_chats (bool | None): Pass True if the message can be sent to
                group and supergroup chats
            allow_channel_chats (bool | None): Pass True if the message can be sent to
                channel chats
        """
        params = {
            "user_id": user_id,
            "result": result,
            "allow_user_chats": allow_user_chats,
            "allow_bot_chats": allow_bot_chats,
            "allow_group_chats": allow_group_chats,
            "allow_channel_chats": allow_channel_chats,
        }
        return await self.method(
            "savePreparedInlineMessage", PreparedInlineMessage, **params
        )

    async def save_prepared_keyboard_button(
        self,
        *,
        user_id: int,
        button: KeyboardButton,
    ) -> PreparedKeyboardButton:
        """
        Stores a keyboard button that can be used by a user within a Mini App. Returns a
        PreparedKeyboardButton object.

        Args:
            user_id (int): Unique identifier of the target user that can use the button
            button (KeyboardButton): A JSON-serialized object describing the button to
                be saved. The button must be of the type request_users, request_chat, or
                request_managed_bot.
        """
        params = {
            "user_id": user_id,
            "button": button,
        }
        return await self.method(
            "savePreparedKeyboardButton", PreparedKeyboardButton, **params
        )

    async def edit_message_text(
        self,
        *,
        business_connection_id: str | None = None,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        text: str | None = None,
        parse_mode: str | None = None,
        entities: list[MessageEntity] | None = None,
        link_preview_options: LinkPreviewOptions | None = None,
        rich_message: InputRichMessage | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message | bool:
        """
        Use this method to edit text, rich and game messages. On success, if the edited
        message is not an inline message, the edited Message is returned, otherwise True
        is returned. Note that business messages that were not sent by the bot and do
        not contain an inline keyboard can only be edited within 48 hours from the time
        they were sent.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message to be edited was sent
            chat_id (int | str | None): Required if inline_message_id is not specified.
                Unique identifier for the target chat or username of the target bot,
                supergroup or channel in the format @username.
            message_id (int | None): Required if inline_message_id is not specified.
                Identifier of the message to edit.
            inline_message_id (str | None): Required if chat_id and message_id are not
                specified. Identifier of the inline message.
            text (str | None): New text of the message, 1-4096 characters after entity
                parsing; required if rich_message isn't specified
            parse_mode (str | None): Mode for parsing entities in the message text. See
                formatting options for more details.
            entities (list[MessageEntity] | None): A JSON-serialized list of special
                entities that appear in message text, which can be specified instead of
                parse_mode
            link_preview_options (LinkPreviewOptions | None): Link preview generation
                options for the message
            rich_message (InputRichMessage | None): New rich content of the message;
                required if text isn't specified. Direct upload of new files and
                explicit upload of files by a URL isn't supported when an inline message
                is edited.
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for an
                inline keyboard
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_id": message_id,
            "inline_message_id": inline_message_id,
            "text": text,
            "parse_mode": parse_mode,
            "entities": entities,
            "link_preview_options": link_preview_options,
            "rich_message": rich_message,
            "reply_markup": reply_markup,
        }
        return await self.method("editMessageText", Message | bool, **params)

    async def edit_message_caption(
        self,
        *,
        business_connection_id: str | None = None,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message | bool:
        """
        Use this method to edit captions of messages. On success, if the edited message
        is not an inline message, the edited Message is returned, otherwise True is
        returned. Note that business messages that were not sent by the bot and do not
        contain an inline keyboard can only be edited within 48 hours from the time they
        were sent.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message to be edited was sent
            chat_id (int | str | None): Required if inline_message_id is not specified.
                Unique identifier for the target chat or username of the target bot,
                supergroup or channel in the format @username.
            message_id (int | None): Required if inline_message_id is not specified.
                Identifier of the message to edit.
            inline_message_id (str | None): Required if chat_id and message_id are not
                specified. Identifier of the inline message.
            caption (str | None): New caption of the message, 0-1024 characters after
                entities parsing
            parse_mode (str | None): Mode for parsing entities in the message caption.
                See formatting options for more details.
            caption_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the caption, which can be specified
                instead of parse_mode
            show_caption_above_media (bool | None): Pass True if the caption must be
                shown above the message media. Supported only for animation, photo and
                video messages.
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for an
                inline keyboard
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_id": message_id,
            "inline_message_id": inline_message_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "show_caption_above_media": show_caption_above_media,
            "reply_markup": reply_markup,
        }
        return await self.method("editMessageCaption", Message | bool, **params)

    async def edit_message_media(
        self,
        *,
        media: InputMedia,
        business_connection_id: str | None = None,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message | bool:
        """
        Use this method to edit animation, audio, document, live photo, photo, or video
        messages, or to replace a text or a rich message with a media. If a message is
        part of a message album, then it can be edited only to an audio for audio
        albums, only to a document for document albums and to a photo, a live photo, or
        a video otherwise. When an inline message is edited, a new file can't be
        uploaded; use a previously uploaded file via its file_id or specify a URL. On
        success, if the edited message is not an inline message, the edited Message is
        returned, otherwise True is returned. Note that business messages that were not
        sent by the bot and do not contain an inline keyboard can only be edited within
        48 hours from the time they were sent.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message to be edited was sent
            chat_id (int | str | None): Required if inline_message_id is not specified.
                Unique identifier for the target chat or username of the target bot,
                supergroup or channel in the format @username.
            message_id (int | None): Required if inline_message_id is not specified.
                Identifier of the message to edit.
            inline_message_id (str | None): Required if chat_id and message_id are not
                specified. Identifier of the inline message.
            media (InputMedia): A JSON-serialized object for the new media content of
                the message
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for a
                new inline keyboard
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_id": message_id,
            "inline_message_id": inline_message_id,
            "media": media,
            "reply_markup": reply_markup,
        }
        return await self.method("editMessageMedia", Message | bool, **params)

    async def edit_message_live_location(
        self,
        *,
        latitude: float,
        longitude: float,
        business_connection_id: str | None = None,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        live_period: int | None = None,
        horizontal_accuracy: float | None = None,
        heading: int | None = None,
        proximity_alert_radius: int | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message | bool:
        """
        Use this method to edit live location messages. A location can be edited until
        its live_period expires or editing is explicitly disabled by a call to
        stopMessageLiveLocation. On success, if the edited message is not an inline
        message, the edited Message is returned, otherwise True is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message to be edited was sent
            chat_id (int | str | None): Required if inline_message_id is not specified.
                Unique identifier for the target chat or username of the target bot,
                supergroup or channel in the format @username.
            message_id (int | None): Required if inline_message_id is not specified.
                Identifier of the message to edit.
            inline_message_id (str | None): Required if chat_id and message_id are not
                specified. Identifier of the inline message.
            latitude (float): Latitude of new location
            longitude (float): Longitude of new location
            live_period (int | None): New period in seconds during which the location
                can be updated, starting from the message send date. If 0x7FFFFFFF is
                specified, then the location can be updated forever. Otherwise, the new
                value must not exceed the current live_period by more than a day, and
                the live location expiration date must remain within the next 90 days.
                If not specified, then live_period remains unchanged.
            horizontal_accuracy (float | None): The radius of uncertainty for the
                location, measured in meters; 0-1500
            heading (int | None): Direction in which the user is moving, in degrees.
                Must be between 1 and 360 if specified.
            proximity_alert_radius (int | None): The maximum distance for proximity
                alerts about approaching another chat member, in meters. Must be between
                1 and 100000 if specified.
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for a
                new inline keyboard
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_id": message_id,
            "inline_message_id": inline_message_id,
            "latitude": latitude,
            "longitude": longitude,
            "live_period": live_period,
            "horizontal_accuracy": horizontal_accuracy,
            "heading": heading,
            "proximity_alert_radius": proximity_alert_radius,
            "reply_markup": reply_markup,
        }
        return await self.method("editMessageLiveLocation", Message | bool, **params)

    async def stop_message_live_location(
        self,
        *,
        business_connection_id: str | None = None,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message | bool:
        """
        Use this method to stop updating a live location message before live_period
        expires. On success, if the message is not an inline message, the edited Message
        is returned, otherwise True is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message to be edited was sent
            chat_id (int | str | None): Required if inline_message_id is not specified.
                Unique identifier for the target chat or username of the target bot,
                supergroup or channel in the format @username.
            message_id (int | None): Required if inline_message_id is not specified.
                Identifier of the message with live location to stop.
            inline_message_id (str | None): Required if chat_id and message_id are not
                specified. Identifier of the inline message.
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for a
                new inline keyboard
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_id": message_id,
            "inline_message_id": inline_message_id,
            "reply_markup": reply_markup,
        }
        return await self.method("stopMessageLiveLocation", Message | bool, **params)

    async def edit_message_checklist(
        self,
        *,
        business_connection_id: str,
        chat_id: int | str,
        message_id: int,
        checklist: InputChecklist,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message:
        """
        Use this method to edit a checklist on behalf of a connected business account.
        On success, the edited Message is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection
                on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot in the format @username
            message_id (int): Unique identifier for the target message
            checklist (InputChecklist): A JSON-serialized object for the new checklist
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for the
                new inline keyboard for the message
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_id": message_id,
            "checklist": checklist,
            "reply_markup": reply_markup,
        }
        return await self.method("editMessageChecklist", Message, **params)

    async def edit_message_reply_markup(
        self,
        *,
        business_connection_id: str | None = None,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message | bool:
        """
        Use this method to edit only the reply markup of messages. On success, if the
        edited message is not an inline message, the edited Message is returned,
        otherwise True is returned. Note that business messages that were not sent by
        the bot and do not contain an inline keyboard can only be edited within 48 hours
        from the time they were sent.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message to be edited was sent
            chat_id (int | str | None): Required if inline_message_id is not specified.
                Unique identifier for the target chat or username of the target bot,
                supergroup or channel in the format @username.
            message_id (int | None): Required if inline_message_id is not specified.
                Identifier of the message to edit.
            inline_message_id (str | None): Required if chat_id and message_id are not
                specified. Identifier of the inline message.
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for an
                inline keyboard
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_id": message_id,
            "inline_message_id": inline_message_id,
            "reply_markup": reply_markup,
        }
        return await self.method("editMessageReplyMarkup", Message | bool, **params)

    async def stop_poll(
        self,
        *,
        chat_id: int | str,
        message_id: int,
        business_connection_id: str | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Poll:
        """
        Use this method to stop a poll which was sent by the bot. On success, the
        stopped Poll is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message to be edited was sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_id (int): Identifier of the original message with the poll
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for a
                new message inline keyboard
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": reply_markup,
        }
        return await self.method("stopPoll", Poll, **params)

    async def edit_ephemeral_message_text(
        self,
        *,
        chat_id: int | str,
        receiver_user_id: int,
        ephemeral_message_id: int,
        text: str | None = None,
        parse_mode: str | None = None,
        entities: list[MessageEntity] | None = None,
        rich_message: InputRichMessage | None = None,
        link_preview_options: LinkPreviewOptions | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> bool:
        """
        Use this method to edit an ephemeral text or rich message. Note that it is not
        guaranteed that the user will receive the message edit event, especially if they
        are offline. On success, True is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            receiver_user_id (int): Identifier of the user who received the message
            ephemeral_message_id (int): Identifier of the ephemeral message to edit
            text (str | None): New text of the message, 1-4096 characters after entity
                parsing; required if rich_message isn't specified
            parse_mode (str | None): Mode for parsing entities in the message text. See
                formatting options for more details.
            entities (list[MessageEntity] | None): A JSON-serialized list of special
                entities that appear in message text, which can be specified instead of
                parse_mode
            rich_message (InputRichMessage | None): New rich content of the message;
                required if text isn't specified
            link_preview_options (LinkPreviewOptions | None): Link preview generation
                options for the message
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for an
                inline keyboard
        """
        params = {
            "chat_id": chat_id,
            "receiver_user_id": receiver_user_id,
            "ephemeral_message_id": ephemeral_message_id,
            "text": text,
            "parse_mode": parse_mode,
            "entities": entities,
            "rich_message": rich_message,
            "link_preview_options": link_preview_options,
            "reply_markup": reply_markup,
        }
        return await self.method("editEphemeralMessageText", bool, **params)

    async def edit_ephemeral_message_media(
        self,
        *,
        chat_id: int | str,
        receiver_user_id: int,
        ephemeral_message_id: int,
        media: InputMedia,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> bool:
        """
        Use this method to edit the media of an ephemeral message. Note that it is not
        guaranteed that the user will receive the message edit event, especially if they
        are offline. On success, True is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            receiver_user_id (int): Identifier of the user who received the message
            ephemeral_message_id (int): Identifier of the ephemeral message to edit
            media (InputMedia): A JSON-serialized object for the new media content of
                the message
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for an
                inline keyboard
        """
        params = {
            "chat_id": chat_id,
            "receiver_user_id": receiver_user_id,
            "ephemeral_message_id": ephemeral_message_id,
            "media": media,
            "reply_markup": reply_markup,
        }
        return await self.method("editEphemeralMessageMedia", bool, **params)

    async def edit_ephemeral_message_caption(
        self,
        *,
        chat_id: int | str,
        receiver_user_id: int,
        ephemeral_message_id: int,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> bool:
        """
        Use this method to edit the caption of an ephemeral message. Note that it is not
        guaranteed that the user will receive the message edit event, especially if they
        are offline. On success, True is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            receiver_user_id (int): Identifier of the user who received the message
            ephemeral_message_id (int): Identifier of the ephemeral message to edit
            caption (str | None): New caption of the message, 0-1024 characters after
                entities parsing
            parse_mode (str | None): Mode for parsing entities in the message caption.
                See formatting options for more details.
            caption_entities (list[MessageEntity] | None): A JSON-serialized list of
                special entities that appear in the caption, which can be specified
                instead of parse_mode
            show_caption_above_media (bool | None): Pass True if the caption must be
                shown above the message media. Supported only for animation, photo and
                video messages.
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for an
                inline keyboard
        """
        params = {
            "chat_id": chat_id,
            "receiver_user_id": receiver_user_id,
            "ephemeral_message_id": ephemeral_message_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "show_caption_above_media": show_caption_above_media,
            "reply_markup": reply_markup,
        }
        return await self.method("editEphemeralMessageCaption", bool, **params)

    async def edit_ephemeral_message_reply_markup(
        self,
        *,
        chat_id: int | str,
        receiver_user_id: int,
        ephemeral_message_id: int,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> bool:
        """
        Use this method to edit only the reply markup of an ephemeral message. Note that
        it is not guaranteed that the user will receive the message edit event,
        especially if they are offline. On success, True is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            receiver_user_id (int): Identifier of the user who received the message
            ephemeral_message_id (int): Identifier of the ephemeral message to edit
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for an
                inline keyboard
        """
        params = {
            "chat_id": chat_id,
            "receiver_user_id": receiver_user_id,
            "ephemeral_message_id": ephemeral_message_id,
            "reply_markup": reply_markup,
        }
        return await self.method("editEphemeralMessageReplyMarkup", bool, **params)

    async def approve_suggested_post(
        self,
        *,
        chat_id: int,
        message_id: int,
        send_date: int | None = None,
    ) -> bool:
        """
        Use this method to approve a suggested post in a direct messages chat. The bot
        must have the 'can_post_messages' administrator right in the corresponding
        channel chat. Returns True on success.

        Args:
            chat_id (int): Unique identifier for the target direct messages chat
            message_id (int): Identifier of a suggested post message to approve
            send_date (int | None): Point in time (Unix timestamp) when the post is
                expected to be published; omit if the date has already been specified
                when the suggested post was created. If specified, then the date must be
                not more than 2678400 seconds (30 days) in the future.
        """
        params = {
            "chat_id": chat_id,
            "message_id": message_id,
            "send_date": send_date,
        }
        return await self.method("approveSuggestedPost", bool, **params)

    async def decline_suggested_post(
        self,
        *,
        chat_id: int,
        message_id: int,
        comment: str | None = None,
    ) -> bool:
        """
        Use this method to decline a suggested post in a direct messages chat. The bot
        must have the 'can_manage_direct_messages' administrator right in the
        corresponding channel chat. Returns True on success.

        Args:
            chat_id (int): Unique identifier for the target direct messages chat
            message_id (int): Identifier of a suggested post message to decline
            comment (str | None): Comment for the creator of the suggested post; 0-128
                characters
        """
        params = {
            "chat_id": chat_id,
            "message_id": message_id,
            "comment": comment,
        }
        return await self.method("declineSuggestedPost", bool, **params)

    async def delete_message(
        self,
        *,
        chat_id: int | str,
        message_id: int,
    ) -> bool:
        """
        Use this method to delete a message, including service messages, with the
        following limitations:
        - A message can only be deleted if it was sent less than 48 hours ago.
        - Service messages about a supergroup, channel, or forum topic creation can't be
        deleted.
        - A dice message in a private chat can only be deleted if it was sent more than
        24 hours ago.
        - Bots can delete outgoing messages in private chats, groups, and supergroups.
        - Bots can delete incoming messages in private chats.
        - Bots granted can_post_messages permissions can delete outgoing messages in
        channels.
        - If the bot is an administrator of a group, it can delete any message there.
        - If the bot has can_delete_messages administrator right in a supergroup or a
        channel, it can delete any message there.
        - If the bot has can_manage_direct_messages administrator right in a channel, it
        can delete any message in the corresponding direct messages chat.
        Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_id (int): Identifier of the message to delete
        """
        params = {
            "chat_id": chat_id,
            "message_id": message_id,
        }
        return await self.method("deleteMessage", bool, **params)

    async def delete_messages(
        self,
        *,
        chat_id: int | str,
        message_ids: list[int],
    ) -> bool:
        """
        Use this method to delete multiple messages simultaneously. If some of the
        specified messages can't be found, they are skipped. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_ids (list[int]): A JSON-serialized list of 1-100 identifiers of
                messages to delete. See deleteMessage for limitations on which messages
                can be deleted.
        """
        params = {
            "chat_id": chat_id,
            "message_ids": message_ids,
        }
        return await self.method("deleteMessages", bool, **params)

    async def delete_ephemeral_message(
        self,
        *,
        chat_id: int | str,
        receiver_user_id: int,
        ephemeral_message_id: int,
    ) -> bool:
        """
        Use this method to delete an ephemeral message. Note that it is not guaranteed
        that the user will receive the message deletion event, especially if they are
        offline. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            receiver_user_id (int): Identifier of the user who received the message
            ephemeral_message_id (int): Identifier of the ephemeral message to delete
        """
        params = {
            "chat_id": chat_id,
            "receiver_user_id": receiver_user_id,
            "ephemeral_message_id": ephemeral_message_id,
        }
        return await self.method("deleteEphemeralMessage", bool, **params)

    async def delete_message_reaction(
        self,
        *,
        chat_id: int | str,
        message_id: int,
        user_id: int | None = None,
        actor_chat_id: int | None = None,
    ) -> bool:
        """
        Use this method to remove a reaction from a message in a group or a supergroup
        chat. The bot must have the 'can_delete_messages' administrator right in the
        chat. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            message_id (int): Identifier of the target message
            user_id (int | None): Identifier of the user whose reaction will be removed,
                if the reaction was added by a user
            actor_chat_id (int | None): Identifier of the chat whose reaction will be
                removed, if the reaction was added by a chat
        """
        params = {
            "chat_id": chat_id,
            "message_id": message_id,
            "user_id": user_id,
            "actor_chat_id": actor_chat_id,
        }
        return await self.method("deleteMessageReaction", bool, **params)

    async def delete_all_message_reactions(
        self,
        *,
        chat_id: int | str,
        user_id: int | None = None,
        actor_chat_id: int | None = None,
    ) -> bool:
        """
        Use this method to remove up to 10000 recent reactions in a group or a
        supergroup chat added by a given user or chat. The bot must have the
        'can_delete_messages' administrator right in the chat. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target supergroup in the format @username
            user_id (int | None): Identifier of the user whose reactions will be
                removed, if the reactions were added by a user
            actor_chat_id (int | None): Identifier of the chat whose reactions will be
                removed, if the reactions were added by a chat
        """
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
            "actor_chat_id": actor_chat_id,
        }
        return await self.method("deleteAllMessageReactions", bool, **params)

    async def send_sticker(
        self,
        *,
        chat_id: int | str,
        sticker: InputFile | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        ephemeral_message_parameters: EphemeralMessageParameters | None = None,
        emoji: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers. On
        success, the sent Message is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            ephemeral_message_parameters (EphemeralMessageParameters | None): A JSON-
                serialized object containing the parameters of the ephemeral message to
                send
            sticker (InputFile | str): Sticker to send. Pass a file_id as String to send
                a file that exists on the Telegram servers (recommended), pass an HTTP
                URL as a String for Telegram to get a .WEBP sticker from the Internet,
                or upload a new .WEBP, .TGS, or .WEBM sticker using multipart/form-data.
                More information on Sending Files:
                https://core.telegram.org/bots/api#sending-files. Video and animated
                stickers can't be sent via an HTTP URL.
            emoji (str | None): Emoji associated with the sticker; only for just
                uploaded stickers
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "ephemeral_message_parameters": ephemeral_message_parameters,
            "sticker": sticker,
            "emoji": emoji,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendSticker", Message, **params)

    async def get_sticker_set(
        self,
        *,
        name: str,
    ) -> StickerSet:
        """
        Use this method to get a sticker set. On success, a StickerSet object is
        returned.

        Args:
            name (str): Name of the sticker set
        """
        params = {
            "name": name,
        }
        return await self.method("getStickerSet", StickerSet, **params)

    async def get_custom_emoji_stickers(
        self,
        *,
        custom_emoji_ids: list[str],
    ) -> list[Sticker]:
        """
        Use this method to get information about custom emoji stickers by their
        identifiers. Returns an Array of Sticker objects.

        Args:
            custom_emoji_ids (list[str]): A JSON-serialized list of custom emoji
                identifiers. At most 200 custom emoji identifiers can be specified.
        """
        params = {
            "custom_emoji_ids": custom_emoji_ids,
        }
        return await self.method("getCustomEmojiStickers", list[Sticker], **params)

    async def upload_sticker_file(
        self,
        *,
        user_id: int,
        sticker: InputFile,
        sticker_format: str,
    ) -> File:
        """
        Use this method to upload a file with a sticker for later use in the
        createNewStickerSet, addStickerToSet, or replaceStickerInSet methods (the file
        can be used multiple times). Returns the uploaded File on success.

        Args:
            user_id (int): User identifier of sticker file owner
            sticker (InputFile): A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM
                format. See https://core.telegram.org/stickers for technical
                requirements. More information on Sending Files:
                https://core.telegram.org/bots/api#sending-files
            sticker_format (str): Format of the sticker, must be one of "static",
                "animated", "video"
        """
        params = {
            "user_id": user_id,
            "sticker": sticker,
            "sticker_format": sticker_format,
        }
        return await self.method("uploadStickerFile", File, **params)

    async def create_new_sticker_set(
        self,
        *,
        user_id: int,
        name: str,
        title: str,
        stickers: list[InputSticker],
        sticker_type: str | None = None,
        needs_repainting: bool | None = None,
    ) -> bool:
        """
        Use this method to create a new sticker set owned by a user. The bot will be
        able to edit the sticker set thus created. Returns True on success.

        Args:
            user_id (int): User identifier of created sticker set owner
            name (str): Short name of sticker set, to be used in t.me/addstickers/ URLs
                (e.g., animals). Can contain only English letters, digits and
                underscores. Must begin with a letter, can't contain consecutive
                underscores and must end in "_by_<bot_username>". <bot_username> is case
                insensitive. 1-64 characters.
            title (str): Sticker set title, 1-64 characters
            stickers (list[InputSticker]): A JSON-serialized list of 1-50 initial
                stickers to be added to the sticker set
            sticker_type (str | None): Type of stickers in the set, pass "regular",
                "mask", or "custom_emoji". By default, a regular sticker set is created.
            needs_repainting (bool | None): Pass True if stickers in the sticker set
                must be repainted to the color of text when used in messages, the accent
                color if used as emoji status, white on chat photos, or another
                appropriate color based on context; for custom emoji sticker sets only
        """
        params = {
            "user_id": user_id,
            "name": name,
            "title": title,
            "stickers": stickers,
            "sticker_type": sticker_type,
            "needs_repainting": needs_repainting,
        }
        return await self.method("createNewStickerSet", bool, **params)

    async def add_sticker_to_set(
        self,
        *,
        user_id: int,
        name: str,
        sticker: InputSticker,
    ) -> bool:
        """
        Use this method to add a new sticker to a set created by the bot. Emoji sticker
        sets can have up to 200 stickers. Other sticker sets can have up to 120
        stickers. Returns True on success.

        Args:
            user_id (int): User identifier of sticker set owner
            name (str): Sticker set name
            sticker (InputSticker): A JSON-serialized object with information about the
                added sticker. If exactly the same sticker had already been added to the
                set, then the set isn't changed.
        """
        params = {
            "user_id": user_id,
            "name": name,
            "sticker": sticker,
        }
        return await self.method("addStickerToSet", bool, **params)

    async def set_sticker_position_in_set(
        self,
        *,
        sticker: str,
        position: int,
    ) -> bool:
        """
        Use this method to move a sticker in a set created by the bot to a specific
        position. Returns True on success.

        Args:
            sticker (str): File identifier of the sticker
            position (int): New sticker position in the set, zero-based
        """
        params = {
            "sticker": sticker,
            "position": position,
        }
        return await self.method("setStickerPositionInSet", bool, **params)

    async def delete_sticker_from_set(
        self,
        *,
        sticker: str,
    ) -> bool:
        """
        Use this method to delete a sticker from a set created by the bot. Returns True
        on success.

        Args:
            sticker (str): File identifier of the sticker
        """
        params = {
            "sticker": sticker,
        }
        return await self.method("deleteStickerFromSet", bool, **params)

    async def replace_sticker_in_set(
        self,
        *,
        user_id: int,
        name: str,
        old_sticker: str,
        sticker: InputSticker,
    ) -> bool:
        """
        Use this method to replace an existing sticker in a sticker set with a new one.
        The method is equivalent to calling deleteStickerFromSet, then addStickerToSet,
        then setStickerPositionInSet. Returns True on success.

        Args:
            user_id (int): User identifier of the sticker set owner
            name (str): Sticker set name
            old_sticker (str): File identifier of the replaced sticker
            sticker (InputSticker): A JSON-serialized object with information about the
                added sticker. If exactly the same sticker had already been added to the
                set, then the set remains unchanged.
        """
        params = {
            "user_id": user_id,
            "name": name,
            "old_sticker": old_sticker,
            "sticker": sticker,
        }
        return await self.method("replaceStickerInSet", bool, **params)

    async def set_sticker_emoji_list(
        self,
        *,
        sticker: str,
        emoji_list: list[str],
    ) -> bool:
        """
        Use this method to change the list of emoji assigned to a regular or custom
        emoji sticker. The sticker must belong to a sticker set created by the bot.
        Returns True on success.

        Args:
            sticker (str): File identifier of the sticker
            emoji_list (list[str]): A JSON-serialized list of 1-20 emoji associated with
                the sticker
        """
        params = {
            "sticker": sticker,
            "emoji_list": emoji_list,
        }
        return await self.method("setStickerEmojiList", bool, **params)

    async def set_sticker_keywords(
        self,
        *,
        sticker: str,
        keywords: list[str] | None = None,
    ) -> bool:
        """
        Use this method to change search keywords assigned to a regular or custom emoji
        sticker. The sticker must belong to a sticker set created by the bot. Returns
        True on success.

        Args:
            sticker (str): File identifier of the sticker
            keywords (list[str] | None): A JSON-serialized list of 0-20 search keywords
                for the sticker with total length of up to 64 characters
        """
        params = {
            "sticker": sticker,
            "keywords": keywords,
        }
        return await self.method("setStickerKeywords", bool, **params)

    async def set_sticker_mask_position(
        self,
        *,
        sticker: str,
        mask_position: MaskPosition | None = None,
    ) -> bool:
        """
        Use this method to change the mask position of a mask sticker. The sticker must
        belong to a sticker set that was created by the bot. Returns True on success.

        Args:
            sticker (str): File identifier of the sticker
            mask_position (MaskPosition | None): A JSON-serialized object with the
                position where the mask should be placed on faces. Omit the parameter to
                remove the mask position.
        """
        params = {
            "sticker": sticker,
            "mask_position": mask_position,
        }
        return await self.method("setStickerMaskPosition", bool, **params)

    async def set_sticker_set_title(
        self,
        *,
        name: str,
        title: str,
    ) -> bool:
        """
        Use this method to set the title of a created sticker set. Returns True on
        success.

        Args:
            name (str): Sticker set name
            title (str): Sticker set title, 1-64 characters
        """
        params = {
            "name": name,
            "title": title,
        }
        return await self.method("setStickerSetTitle", bool, **params)

    async def set_sticker_set_thumbnail(
        self,
        *,
        name: str,
        user_id: int,
        format: str,
        thumbnail: InputFile | str | None = None,
    ) -> bool:
        """
        Use this method to set the thumbnail of a regular or mask sticker set. The
        format of the thumbnail file must match the format of the stickers in the set.
        Returns True on success.

        Args:
            name (str): Sticker set name
            user_id (int): User identifier of the sticker set owner
            thumbnail (InputFile | str | None): A .WEBP or .PNG image with the
                thumbnail, must be up to 128 kilobytes in size and have a width and
                height of exactly 100px, or a .TGS animation with a thumbnail up to 32
                kilobytes in size (see https://core.telegram.org/stickers#animation-
                requirements for animated sticker technical requirements), or a .WEBM
                video with the thumbnail up to 32 kilobytes in size; see
                https://core.telegram.org/stickers#video-requirements for video sticker
                technical requirements. Pass a file_id as a String to send a file that
                already exists on the Telegram servers, pass an HTTP URL as a String for
                Telegram to get a file from the Internet, or upload a new one using
                multipart/form-data. More information on Sending Files:
                https://core.telegram.org/bots/api#sending-files. Animated and video
                sticker set thumbnails can't be uploaded via HTTP URL. If omitted, then
                the thumbnail is dropped and the first sticker is used as the thumbnail.
            format (str): Format of the thumbnail, must be one of "static" for a .WEBP
                or .PNG image, "animated" for a .TGS animation, or "video" for a .WEBM
                video
        """
        params = {
            "name": name,
            "user_id": user_id,
            "thumbnail": thumbnail,
            "format": format,
        }
        return await self.method("setStickerSetThumbnail", bool, **params)

    async def set_custom_emoji_sticker_set_thumbnail(
        self,
        *,
        name: str,
        custom_emoji_id: str | None = None,
    ) -> bool:
        """
        Use this method to set the thumbnail of a custom emoji sticker set. Returns True
        on success.

        Args:
            name (str): Sticker set name
            custom_emoji_id (str | None): Custom emoji identifier of a sticker from the
                sticker set; pass an empty string to drop the thumbnail and use the
                first sticker as the thumbnail
        """
        params = {
            "name": name,
            "custom_emoji_id": custom_emoji_id,
        }
        return await self.method("setCustomEmojiStickerSetThumbnail", bool, **params)

    async def delete_sticker_set(
        self,
        *,
        name: str,
    ) -> bool:
        """
        Use this method to delete a sticker set that was created by the bot. Returns
        True on success.

        Args:
            name (str): Sticker set name
        """
        params = {
            "name": name,
        }
        return await self.method("deleteStickerSet", bool, **params)

    async def send_rich_message(
        self,
        *,
        chat_id: int | str,
        rich_message: InputRichMessage,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        ephemeral_message_parameters: EphemeralMessageParameters | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """
        Use this method to send rich messages. If the message contains a block with a
        media element, then the bot must have the right to send the media to the chat.
        On success, the sent Message is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent. Bot can send
                rich messages on behalf of a business account only if the corresponding
                user can send rich messages.
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            ephemeral_message_parameters (EphemeralMessageParameters | None): A JSON-
                serialized object containing the parameters of the ephemeral message to
                send
            rich_message (InputRichMessage): The message to be sent
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup |
                ReplyKeyboardRemove | ForceReply | None): Additional interface options.
                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                instructions to remove a reply keyboard or to force a reply from the
                user.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "ephemeral_message_parameters": ephemeral_message_parameters,
            "rich_message": rich_message,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendRichMessage", Message, **params)

    async def send_rich_message_draft(
        self,
        *,
        chat_id: int,
        draft_id: int,
        rich_message: InputRichMessage,
        message_thread_id: int | None = None,
        can_stop: bool | None = None,
        keep_on_stop: bool | None = None,
    ) -> bool:
        """
        Use this method to stream a partial rich message to a user while the message is
        being generated. Note that the streamed draft is ephemeral and acts as a
        temporary 30-second preview - once the output is finalized, you must call
        sendRichMessage with the complete message to persist it in the user's chat.
        Returns True on success.

        Args:
            chat_id (int): Unique identifier for the target private chat
            message_thread_id (int | None): Unique identifier for the target message
                thread
            draft_id (int): Unique identifier of the message draft; must be non-zero.
                Changes to drafts with the same identifier are animated. Otherwise, the
                draft is replaced without animation.
            rich_message (InputRichMessage): The partial message to be streamed. Direct
                upload of new files and explicit upload of files by a URL isn't
                supported.
            can_stop (bool | None): Pass True to show the user a button to stop further
                drafts. The bot will receive an Update "stopped_message_generation" if
                the user presses the button.
            keep_on_stop (bool | None): Pass True to keep the draft in the chat when the
                button is pressed. The draft will still disappear after a short time or
                if the bot sends a message. To fully preserve the partial draft, the bot
                should send it as a new message.
        """
        params = {
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "draft_id": draft_id,
            "rich_message": rich_message,
            "can_stop": can_stop,
            "keep_on_stop": keep_on_stop,
        }
        return await self.method("sendRichMessageDraft", bool, **params)

    async def answer_inline_query(
        self,
        *,
        inline_query_id: str,
        results: list[InlineQueryResult],
        cache_time: int | None = None,
        is_personal: bool | None = None,
        next_offset: str | None = None,
        button: InlineQueryResultsButton | None = None,
    ) -> bool:
        """
        Use this method to send answers to an inline query. On success, True is
        returned.
        No more than 50 results per query are allowed.

        Args:
            inline_query_id (str): Unique identifier for the answered query
            results (list[InlineQueryResult]): A JSON-serialized Array of results for
                the inline query
            cache_time (int | None): The maximum amount of time in seconds that the
                result of the inline query may be cached on the server. Defaults to 300.
            is_personal (bool | None): Pass True if results may be cached on the server
                side only for the user that sent the query. By default, results may be
                returned to any user who sends the same query.
            next_offset (str | None): Pass the offset that a client should send in the
                next query with the same text to receive more results. Pass an empty
                string if there are no more results or if you don't support pagination.
                Offset length can't exceed 64 bytes.
            button (InlineQueryResultsButton | None): A JSON-serialized object
                describing a button to be shown above inline query results
        """
        params = {
            "inline_query_id": inline_query_id,
            "results": results,
            "cache_time": cache_time,
            "is_personal": is_personal,
            "next_offset": next_offset,
            "button": button,
        }
        return await self.method("answerInlineQuery", bool, **params)

    async def send_invoice(
        self,
        *,
        chat_id: int | str,
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: list[LabeledPrice],
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        provider_token: str | None = None,
        max_tip_amount: int | None = None,
        suggested_tip_amounts: list[int] | None = None,
        start_parameter: str | None = None,
        provider_data: str | None = None,
        photo_url: str | None = None,
        photo_size: int | None = None,
        photo_width: int | None = None,
        photo_height: int | None = None,
        need_name: bool | None = None,
        need_phone_number: bool | None = None,
        need_email: bool | None = None,
        need_shipping_address: bool | None = None,
        send_phone_number_to_provider: bool | None = None,
        send_email_to_provider: bool | None = None,
        is_flexible: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        suggested_post_parameters: SuggestedPostParameters | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message:
        """
        Use this method to send invoices. On success, the sent Message is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot, supergroup or channel in the format @username
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            direct_messages_topic_id (int | None): Identifier of the direct messages
                topic to which the message will be sent; required if the message is sent
                to a direct messages chat
            title (str): Product name, 1-32 characters
            description (str): Product description, 1-255 characters
            payload (str): Bot-defined invoice payload, 1-128 bytes. This will not be
                displayed to the user, use it for your internal processes.
            provider_token (str | None): Payment provider token, obtained via
                @BotFather. Pass an empty string for payments in Telegram Stars.
            currency (str): Three-letter ISO 4217 currency code, see more on currencies.
                Pass "XTR" for payments in Telegram Stars.
            prices (list[LabeledPrice]): Price breakdown, a JSON-serialized list of
                components (e.g. product price, tax, discount, delivery cost, delivery
                tax, bonus, etc.). Must contain exactly one item for payments in
                Telegram Stars.
            max_tip_amount (int | None): The maximum accepted amount for tips in the
                smallest units of the currency (integer, not float/double). For example,
                for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp
                parameter in currencies.json, it shows the number of digits past the
                decimal point for each currency (2 for the majority of currencies).
                Defaults to 0. Not supported for payments in Telegram Stars.
            suggested_tip_amounts (list[int] | None): A JSON-serialized Array of
                suggested amounts of tips in the smallest units of the currency
                (integer, not float/double). At most 4 suggested tip amounts can be
                specified. The suggested tip amounts must be positive, passed in a
                strictly increased order and must not exceed max_tip_amount.
            start_parameter (str | None): Unique deep-linking parameter. If left empty,
                forwarded copies of the sent message will have a Pay button, allowing
                multiple users to pay directly from the forwarded message, using the
                same invoice. If non-empty, forwarded copies of the sent message will
                have a URL button with a deep link to the bot (instead of a Pay button),
                with the value used as the start parameter.
            provider_data (str | None): JSON-serialized data about the invoice, which
                will be shared with the payment provider. A detailed description of
                required fields should be provided by the payment provider.
            photo_url (str | None): URL of the product photo for the invoice. Can be a
                photo of the goods or a marketing image for a service. People like it
                better when they see what they are paying for.
            photo_size (int | None): Photo size in bytes
            photo_width (int | None): Photo width
            photo_height (int | None): Photo height
            need_name (bool | None): Pass True if you require the user's full name to
                complete the order. Ignored for payments in Telegram Stars.
            need_phone_number (bool | None): Pass True if you require the user's phone
                number to complete the order. Ignored for payments in Telegram Stars.
            need_email (bool | None): Pass True if you require the user's email address
                to complete the order. Ignored for payments in Telegram Stars.
            need_shipping_address (bool | None): Pass True if you require the user's
                shipping address to complete the order. Ignored for payments in Telegram
                Stars.
            send_phone_number_to_provider (bool | None): Pass True if the user's phone
                number should be sent to the provider. Ignored for payments in Telegram
                Stars.
            send_email_to_provider (bool | None): Pass True if the user's email address
                should be sent to the provider. Ignored for payments in Telegram Stars.
            is_flexible (bool | None): Pass True if the final price depends on the
                shipping method. Ignored for payments in Telegram Stars.
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            suggested_post_parameters (SuggestedPostParameters | None): A JSON-
                serialized object containing the parameters of the suggested post to
                send; for direct messages chats only. If the message is sent as a reply
                to another suggested post, then that suggested post is automatically
                declined.
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for an
                inline keyboard. If empty, one 'Pay total price' button will be shown.
                If not empty, the first button must be a Pay button.
        """
        params = {
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "direct_messages_topic_id": direct_messages_topic_id,
            "title": title,
            "description": description,
            "payload": payload,
            "provider_token": provider_token,
            "currency": currency,
            "prices": prices,
            "max_tip_amount": max_tip_amount,
            "suggested_tip_amounts": suggested_tip_amounts,
            "start_parameter": start_parameter,
            "provider_data": provider_data,
            "photo_url": photo_url,
            "photo_size": photo_size,
            "photo_width": photo_width,
            "photo_height": photo_height,
            "need_name": need_name,
            "need_phone_number": need_phone_number,
            "need_email": need_email,
            "need_shipping_address": need_shipping_address,
            "send_phone_number_to_provider": send_phone_number_to_provider,
            "send_email_to_provider": send_email_to_provider,
            "is_flexible": is_flexible,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "suggested_post_parameters": suggested_post_parameters,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendInvoice", Message, **params)

    async def create_invoice_link(
        self,
        *,
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: list[LabeledPrice],
        business_connection_id: str | None = None,
        provider_token: str | None = None,
        subscription_period: int | None = None,
        max_tip_amount: int | None = None,
        suggested_tip_amounts: list[int] | None = None,
        provider_data: str | None = None,
        photo_url: str | None = None,
        photo_size: int | None = None,
        photo_width: int | None = None,
        photo_height: int | None = None,
        need_name: bool | None = None,
        need_phone_number: bool | None = None,
        need_email: bool | None = None,
        need_shipping_address: bool | None = None,
        send_phone_number_to_provider: bool | None = None,
        send_email_to_provider: bool | None = None,
        is_flexible: bool | None = None,
    ) -> str:
        """
        Use this method to create a link for an invoice. Returns the created invoice
        link as String on success.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the link will be created. For payments in
                Telegram Stars only.
            title (str): Product name, 1-32 characters
            description (str): Product description, 1-255 characters
            payload (str): Bot-defined invoice payload, 1-128 bytes. This will not be
                displayed to the user, use it for your internal processes.
            provider_token (str | None): Payment provider token, obtained via
                @BotFather. Pass an empty string for payments in Telegram Stars.
            currency (str): Three-letter ISO 4217 currency code, see more on currencies.
                Pass "XTR" for payments in Telegram Stars.
            prices (list[LabeledPrice]): Price breakdown, a JSON-serialized list of
                components (e.g. product price, tax, discount, delivery cost, delivery
                tax, bonus, etc.). Must contain exactly one item for payments in
                Telegram Stars.
            subscription_period (int | None): The number of seconds the subscription
                will be active for before the next payment. The currency must be set to
                "XTR" (Telegram Stars) if the parameter is used. Currently, it must
                always be 2592000 (30 days) if specified. Any number of subscriptions
                can be active for a given bot at the same time, including multiple
                concurrent subscriptions from the same user. Subscription price must no
                exceed 10000 Telegram Stars.
            max_tip_amount (int | None): The maximum accepted amount for tips in the
                smallest units of the currency (integer, not float/double). For example,
                for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp
                parameter in currencies.json, it shows the number of digits past the
                decimal point for each currency (2 for the majority of currencies).
                Defaults to 0. Not supported for payments in Telegram Stars.
            suggested_tip_amounts (list[int] | None): A JSON-serialized Array of
                suggested amounts of tips in the smallest units of the currency
                (integer, not float/double). At most 4 suggested tip amounts can be
                specified. The suggested tip amounts must be positive, passed in a
                strictly increased order and must not exceed max_tip_amount.
            provider_data (str | None): JSON-serialized data about the invoice, which
                will be shared with the payment provider. A detailed description of
                required fields should be provided by the payment provider.
            photo_url (str | None): URL of the product photo for the invoice. Can be a
                photo of the goods or a marketing image for a service.
            photo_size (int | None): Photo size in bytes
            photo_width (int | None): Photo width
            photo_height (int | None): Photo height
            need_name (bool | None): Pass True if you require the user's full name to
                complete the order. Ignored for payments in Telegram Stars.
            need_phone_number (bool | None): Pass True if you require the user's phone
                number to complete the order. Ignored for payments in Telegram Stars.
            need_email (bool | None): Pass True if you require the user's email address
                to complete the order. Ignored for payments in Telegram Stars.
            need_shipping_address (bool | None): Pass True if you require the user's
                shipping address to complete the order. Ignored for payments in Telegram
                Stars.
            send_phone_number_to_provider (bool | None): Pass True if the user's phone
                number should be sent to the provider. Ignored for payments in Telegram
                Stars.
            send_email_to_provider (bool | None): Pass True if the user's email address
                should be sent to the provider. Ignored for payments in Telegram Stars.
            is_flexible (bool | None): Pass True if the final price depends on the
                shipping method. Ignored for payments in Telegram Stars.
        """
        params = {
            "business_connection_id": business_connection_id,
            "title": title,
            "description": description,
            "payload": payload,
            "provider_token": provider_token,
            "currency": currency,
            "prices": prices,
            "subscription_period": subscription_period,
            "max_tip_amount": max_tip_amount,
            "suggested_tip_amounts": suggested_tip_amounts,
            "provider_data": provider_data,
            "photo_url": photo_url,
            "photo_size": photo_size,
            "photo_width": photo_width,
            "photo_height": photo_height,
            "need_name": need_name,
            "need_phone_number": need_phone_number,
            "need_email": need_email,
            "need_shipping_address": need_shipping_address,
            "send_phone_number_to_provider": send_phone_number_to_provider,
            "send_email_to_provider": send_email_to_provider,
            "is_flexible": is_flexible,
        }
        return await self.method("createInvoiceLink", str, **params)

    async def answer_shipping_query(
        self,
        *,
        shipping_query_id: str,
        ok: bool,
        shipping_options: list[ShippingOption] | None = None,
        error_message: str | None = None,
    ) -> bool:
        """
        If you sent an invoice requesting a shipping address and the parameter
        is_flexible was specified, the Bot API will send an Update with a shipping_query
        field to the bot. Use this method to reply to shipping queries. On success, True
        is returned.

        Args:
            shipping_query_id (str): Unique identifier for the query to be answered
            ok (bool): Pass True if delivery to the specified address is possible and
                False if there are any problems (for example, if delivery to the
                specified address is not possible)
            shipping_options (list[ShippingOption] | None): Required if ok is True. A
                JSON-serialized Array of available shipping options.
            error_message (str | None): Required if ok is False. Error message in human
                readable form that explains why it is impossible to complete the order
                (e.g. "Sorry, delivery to your desired address is unavailable").
                Telegram will display this message to the user.
        """
        params = {
            "shipping_query_id": shipping_query_id,
            "ok": ok,
            "shipping_options": shipping_options,
            "error_message": error_message,
        }
        return await self.method("answerShippingQuery", bool, **params)

    async def answer_pre_checkout_query(
        self,
        *,
        pre_checkout_query_id: str,
        ok: bool,
        error_message: str | None = None,
    ) -> bool:
        """
        Once the user has confirmed their payment and shipping details, the Bot API
        sends the final confirmation in the form of an Update with the field
        pre_checkout_query. Use this method to respond to such pre-checkout queries. On
        success, True is returned. Note: The Bot API must receive an answer within 10
        seconds after the pre-checkout query was sent.

        Args:
            pre_checkout_query_id (str): Unique identifier for the query to be answered
            ok (bool): Specify True if everything is alright (goods are available, etc.)
                and the bot is ready to proceed with the order. Use False if there are
                any problems.
            error_message (str | None): Required if ok is False. Error message in human
                readable form that explains the reason for failure to proceed with the
                checkout (e.g. "Sorry, somebody just bought the last of our amazing
                black T-shirts while you were busy filling out your payment details.
                Please choose a different color or garment!"). Telegram will display
                this message to the user.
        """
        params = {
            "pre_checkout_query_id": pre_checkout_query_id,
            "ok": ok,
            "error_message": error_message,
        }
        return await self.method("answerPreCheckoutQuery", bool, **params)

    async def get_my_star_balance(
        self,
    ) -> StarAmount:
        """
        A method to get the current Telegram Stars balance of the bot. Requires no
        parameters. On success, returns a StarAmount object.
        """
        params = {}
        return await self.method("getMyStarBalance", StarAmount, **params)

    async def get_star_transactions(
        self,
        *,
        offset: int | None = None,
        limit: int | None = None,
    ) -> StarTransactions:
        """
        Returns the bot's Telegram Star transactions in chronological order. On success,
        returns a StarTransactions object.

        Args:
            offset (int | None): Number of transactions to skip in the response
            limit (int | None): The maximum number of transactions to be retrieved.
                Values between 1-100 are accepted. Defaults to 100.
        """
        params = {
            "offset": offset,
            "limit": limit,
        }
        return await self.method("getStarTransactions", StarTransactions, **params)

    async def refund_star_payment(
        self,
        *,
        user_id: int,
        telegram_payment_charge_id: str,
    ) -> bool:
        """
        Refunds a successful payment in Telegram Stars. Returns True on success.

        Args:
            user_id (int): Identifier of the user whose payment will be refunded
            telegram_payment_charge_id (str): Telegram payment identifier
        """
        params = {
            "user_id": user_id,
            "telegram_payment_charge_id": telegram_payment_charge_id,
        }
        return await self.method("refundStarPayment", bool, **params)

    async def edit_user_star_subscription(
        self,
        *,
        user_id: int,
        telegram_payment_charge_id: str,
        is_canceled: bool,
    ) -> bool:
        """
        Allows the bot to cancel or re-enable extension of a subscription paid in
        Telegram Stars. Returns True on success.

        Args:
            user_id (int): Identifier of the user whose subscription will be edited
            telegram_payment_charge_id (str): Telegram payment identifier for the
                subscription
            is_canceled (bool): Pass True to cancel extension of the user subscription;
                the subscription must be active up to the end of the current
                subscription period. Pass False to allow the user to re-enable a
                subscription that was previously canceled by the bot.
        """
        params = {
            "user_id": user_id,
            "telegram_payment_charge_id": telegram_payment_charge_id,
            "is_canceled": is_canceled,
        }
        return await self.method("editUserStarSubscription", bool, **params)

    async def set_passport_data_errors(
        self,
        *,
        user_id: int,
        errors: list[PassportElementError],
    ) -> bool:
        """
        Informs a user that some of the Telegram Passport elements they provided
        contains errors. The user will not be able to re-submit their Passport to you
        until the errors are fixed (the contents of the field for which you returned the
        error must change). Returns True on success.
        Use this if the data submitted by the user doesn't satisfy the standards your
        service requires for any reason. For example, if a birthday date seems invalid,
        a submitted document is blurry, a scan shows evidence of tampering, etc. Supply
        some details in the error message to make sure the user knows how to correct the
        issues.

        Args:
            user_id (int): User identifier
            errors (list[PassportElementError]): A JSON-serialized Array describing the
                errors
        """
        params = {
            "user_id": user_id,
            "errors": errors,
        }
        return await self.method("setPassportDataErrors", bool, **params)

    async def send_game(
        self,
        *,
        chat_id: int | str,
        game_short_name: str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message:
        """
        Use this method to send a game. On success, the sent Message is returned.

        Args:
            business_connection_id (str | None): Unique identifier of the business
                connection on behalf of which the message will be sent
            chat_id (int | str): Unique identifier for the target chat or username of
                the target bot in the format @username. Games can't be sent to channel
                direct messages chats and channel chats.
            message_thread_id (int | None): Unique identifier for the target message
                thread (topic) of a forum; for forum supergroups and private chats of
                bots with forum topic mode enabled only
            game_short_name (str): Short name of the game, serves as the unique
                identifier for the game. Set up your games via @BotFather.
            disable_notification (bool | None): Sends the message silently. Users will
                receive a notification with no sound.
            protect_content (bool | None): Protects the contents of the sent message
                from forwarding and saving
            allow_paid_broadcast (bool | None): Pass True to allow up to 1000 messages
                per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars
                per message. The relevant Stars will be withdrawn from the bot's
                balance.
            message_effect_id (str | None): Unique identifier of the message effect to
                be added to the message; for private chats only
            reply_parameters (ReplyParameters | None): Description of the message to
                reply to
            reply_markup (InlineKeyboardMarkup | None): A JSON-serialized object for an
                inline keyboard. If empty, one 'Play game_title' button will be shown.
                If not empty, the first button must launch the game.
        """
        params = {
            "business_connection_id": business_connection_id,
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "game_short_name": game_short_name,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        return await self.method("sendGame", Message, **params)

    async def set_game_score(
        self,
        *,
        user_id: int,
        score: int,
        force: bool | None = None,
        disable_edit_message: bool | None = None,
        chat_id: int | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
    ) -> Message | bool:
        """
        Use this method to set the score of the specified user in a game message. On
        success, if the message is not an inline message, the Message is returned,
        otherwise True is returned. Returns an error, if the new score is not greater
        than the user's current score in the chat and force is False.

        Args:
            user_id (int): User identifier
            score (int): New score, must be non-negative
            force (bool | None): Pass True if the high score is allowed to decrease.
                This can be useful when fixing mistakes or banning cheaters.
            disable_edit_message (bool | None): Pass True if the game message should not
                be automatically edited to include the current scoreboard
            chat_id (int | None): Required if inline_message_id is not specified. Unique
                identifier for the target chat.
            message_id (int | None): Required if inline_message_id is not specified.
                Identifier of the sent message.
            inline_message_id (str | None): Required if chat_id and message_id are not
                specified. Identifier of the inline message.
        """
        params = {
            "user_id": user_id,
            "score": score,
            "force": force,
            "disable_edit_message": disable_edit_message,
            "chat_id": chat_id,
            "message_id": message_id,
            "inline_message_id": inline_message_id,
        }
        return await self.method("setGameScore", Message | bool, **params)

    async def get_game_high_scores(
        self,
        *,
        user_id: int,
        chat_id: int | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
    ) -> list[GameHighScore]:
        """
        Use this method to get data for high score tables. Will return the score of the
        specified user and several of their neighbors in a game. Returns an Array of
        GameHighScore objects.

        Args:
            user_id (int): Target user id
            chat_id (int | None): Required if inline_message_id is not specified. Unique
                identifier for the target chat.
            message_id (int | None): Required if inline_message_id is not specified.
                Identifier of the sent message.
            inline_message_id (str | None): Required if chat_id and message_id are not
                specified. Identifier of the inline message.
        """
        params = {
            "user_id": user_id,
            "chat_id": chat_id,
            "message_id": message_id,
            "inline_message_id": inline_message_id,
        }
        return await self.method("getGameHighScores", list[GameHighScore], **params)
