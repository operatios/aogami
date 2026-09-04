# THIS FILE IS AUTO-GENERATED. DO NOT EDIT!
# Bot API 10.3 (August 24, 2026)

from typing import Annotated, Literal

from pydantic import Field

from aogami.types_manual import InputFile, TelegramObject


class Update(TelegramObject):
    """
    This object represents an incoming update.
    At most one of the optional fields can be present in any given update.
    """

    update_id: int
    """
    The update's unique identifier. Update identifiers start from a certain positive
    number and increase sequentially. This identifier becomes especially handy if you're
    using webhooks, since it allows you to ignore repeated updates or to restore the
    correct update sequence, should they get out of order. If there are no new updates
    for at least a week, then identifier of the next update will be chosen randomly
    instead of sequentially.
    """

    message: Message | None = None
    """
    New incoming message of any kind - text, photo, sticker, etc.
    """

    edited_message: Message | None = None
    """
    New version of a message that is known to the bot and was edited. This update may at
    times be triggered by changes to message fields that are either unavailable or not
    actively used by your bot.
    """

    channel_post: Message | None = None
    """
    New incoming channel post of any kind - text, photo, sticker, etc.
    """

    edited_channel_post: Message | None = None
    """
    New version of a channel post that is known to the bot and was edited. This update
    may at times be triggered by changes to message fields that are either unavailable
    or not actively used by your bot.
    """

    business_connection: BusinessConnection | None = None
    """
    The bot was connected to or disconnected from a business account, or a user edited
    an existing connection with the bot
    """

    business_message: Message | None = None
    """
    New message from a connected business account
    """

    edited_business_message: Message | None = None
    """
    New version of a message from a connected business account
    """

    deleted_business_messages: BusinessMessagesDeleted | None = None
    """
    Messages were deleted from a connected business account
    """

    guest_message: Message | None = None
    """
    New guest message. The bot can use the field Message.guest_query_id and the method
    answerGuestQuery to send a message in response.
    """

    message_reaction: MessageReactionUpdated | None = None
    """
    A reaction to a message was changed by a user. The bot must be an administrator in
    the chat and must explicitly specify "message_reaction" in the list of
    allowed_updates to receive these updates. The update isn't received for reactions
    set by bots.
    """

    message_reaction_count: MessageReactionCountUpdated | None = None
    """
    Reactions to a message with anonymous reactions were changed. The bot must be an
    administrator in the chat and must explicitly specify "message_reaction_count" in
    the list of allowed_updates to receive these updates. The updates are grouped and
    can be sent with delay up to a few minutes.
    """

    inline_query: InlineQuery | None = None
    """
    New incoming inline query
    """

    chosen_inline_result: ChosenInlineResult | None = None
    """
    The result of an inline query that was chosen by a user and sent to their chat
    partner. Please see our documentation on the feedback collecting for details on how
    to enable these updates for your bot.
    """

    callback_query: CallbackQuery | None = None
    """
    New incoming callback query
    """

    shipping_query: ShippingQuery | None = None
    """
    New incoming shipping query. Only for invoices with flexible price.
    """

    pre_checkout_query: PreCheckoutQuery | None = None
    """
    New incoming pre-checkout query. Contains full information about checkout.
    """

    purchased_paid_media: PaidMediaPurchased | None = None
    """
    A user purchased paid media with a non-empty payload sent by the bot in a non-
    channel chat
    """

    poll: Poll | None = None
    """
    New poll state. Bots receive only updates about manually stopped polls and polls,
    which are sent by the bot.
    """

    poll_answer: PollAnswer | None = None
    """
    A user changed their answer in a non-anonymous poll. Bots receive new votes only in
    polls that were sent by the bot itself.
    """

    my_chat_member: ChatMemberUpdated | None = None
    """
    The bot's chat member status was updated in a chat. For private chats, this update
    is received only when the bot is blocked or unblocked by the user.
    """

    chat_member: ChatMemberUpdated | None = None
    """
    A chat member's status was updated in a chat. The bot must be an administrator in
    the chat and must explicitly specify "chat_member" in the list of allowed_updates to
    receive these updates.
    """

    chat_join_request: ChatJoinRequest | None = None
    """
    A request to join the chat has been sent. The bot must have the can_invite_users
    administrator right in the chat to receive these updates.
    """

    chat_boost: ChatBoostUpdated | None = None
    """
    A chat boost was added or changed. The bot must be an administrator in the chat to
    receive these updates.
    """

    removed_chat_boost: ChatBoostRemoved | None = None
    """
    A boost was removed from a chat. The bot must be an administrator in the chat to
    receive these updates.
    """

    managed_bot: ManagedBotUpdated | None = None
    """
    A new bot was created to be managed by the bot, or token or owner of a managed bot
    was changed
    """

    subscription: BotSubscriptionUpdated | None = None
    """
    User payment subscription has changed
    """

    stopped_message_generation: MessageGenerationStopped | None = None
    """
    A user asked the bot to stop the generation of a message
    """


class WebhookInfo(TelegramObject):
    """
    Describes the current status of a webhook.
    """

    url: str
    """
    Webhook URL, may be empty if webhook is not set up
    """

    has_custom_certificate: bool
    """
    True, if a custom certificate was provided for webhook certificate checks
    """

    pending_update_count: int
    """
    Number of updates awaiting delivery
    """

    ip_address: str | None = None
    """
    Currently used webhook IP address
    """

    last_error_date: int | None = None
    """
    Unix time for the most recent error that happened when trying to deliver an update
    via webhook
    """

    last_error_message: str | None = None
    """
    Error message in human-readable format for the most recent error that happened when
    trying to deliver an update via webhook
    """

    last_synchronization_error_date: int | None = None
    """
    Unix time of the most recent error that happened when trying to synchronize
    available updates with Telegram datacenters
    """

    max_connections: int | None = None
    """
    The maximum allowed number of simultaneous HTTPS connections to the webhook for
    update delivery
    """

    allowed_updates: list[str] | None = None
    """
    A list of update types the bot is subscribed to. Defaults to all update types except
    chat_member, message_reaction, and message_reaction_count.
    """


class User(TelegramObject):
    """
    This object represents a Telegram user or bot.
    """

    id: int
    """
    Unique identifier for this user or bot. This number may have more than 32
    significant bits and some programming languages may have difficulty/silent defects
    in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or
    double-precision float type are safe for storing this identifier.
    """

    is_bot: bool
    """
    True, if this user is a bot
    """

    first_name: str
    """
    User's or bot's first name
    """

    last_name: str | None = None
    """
    User's or bot's last name
    """

    username: str | None = None
    """
    User's or bot's username
    """

    language_code: str | None = None
    """
    IETF language tag of the user's language
    """

    is_premium: bool | None = None
    """
    True, if this user is a Telegram Premium user
    """

    added_to_attachment_menu: bool | None = None
    """
    True, if this user added the bot to the attachment menu
    """

    can_join_groups: bool | None = None
    """
    True, if the bot can be invited to groups. Returned only in getMe.
    """

    can_read_all_group_messages: bool | None = None
    """
    True, if privacy mode is disabled for the bot. Returned only in getMe.
    """

    supports_guest_queries: bool | None = None
    """
    True, if the bot supports guest queries from chats it is not a member of. Returned
    only in getMe.
    """

    supports_inline_queries: bool | None = None
    """
    True, if the bot supports inline queries. Returned only in getMe.
    """

    can_connect_to_business: bool | None = None
    """
    True, if the bot can be connected to a user account to manage it. Returned only in
    getMe.
    """

    has_main_web_app: bool | None = None
    """
    True, if the bot has a main Web App. Returned only in getMe.
    """

    has_topics_enabled: bool | None = None
    """
    True, if the bot has forum topic mode enabled in private chats. Returned only in
    getMe.
    """

    allows_users_to_create_topics: bool | None = None
    """
    True, if the bot allows users to create and delete topics in private chats. Returned
    only in getMe.
    """

    can_manage_bots: bool | None = None
    """
    True, if other bots can be created to be controlled by the bot. Returned only in
    getMe.
    """

    supports_join_request_queries: bool | None = None
    """
    True, if the bot supports join request queries and can be assigned to process them.
    Returned only in getMe.
    """


class Chat(TelegramObject):
    """
    This object represents a chat.
    """

    id: int
    """
    Unique identifier for this chat. This number may have more than 32 significant bits
    and some programming languages may have difficulty/silent defects in interpreting
    it. But it has at most 52 significant bits, so a signed 64-bit integer or double-
    precision float type are safe for storing this identifier.
    """

    type: str
    """
    Type of the chat, can be either "private", "group", "supergroup" or "channel"
    """

    title: str | None = None
    """
    Title, for supergroups, channels and group chats
    """

    username: str | None = None
    """
    Username, for private chats, supergroups and channels if available
    """

    first_name: str | None = None
    """
    First name of the other party in a private chat
    """

    last_name: str | None = None
    """
    Last name of the other party in a private chat
    """

    is_forum: bool | None = None
    """
    True, if the supergroup chat is a forum (has topics enabled)
    """

    is_direct_messages: bool | None = None
    """
    True, if the chat is the direct messages chat of a channel
    """


class ChatFullInfo(TelegramObject):
    """
    This object contains full information about a chat.
    """

    id: int
    """
    Unique identifier for this chat. This number may have more than 32 significant bits
    and some programming languages may have difficulty/silent defects in interpreting
    it. But it has at most 52 significant bits, so a signed 64-bit integer or double-
    precision float type are safe for storing this identifier.
    """

    type: str
    """
    Type of the chat, can be either "private", "group", "supergroup" or "channel"
    """

    title: str | None = None
    """
    Title, for supergroups, channels and group chats
    """

    username: str | None = None
    """
    Username, for private chats, supergroups and channels if available
    """

    first_name: str | None = None
    """
    First name of the other party in a private chat
    """

    last_name: str | None = None
    """
    Last name of the other party in a private chat
    """

    is_forum: bool | None = None
    """
    True, if the supergroup chat is a forum (has topics enabled)
    """

    is_direct_messages: bool | None = None
    """
    True, if the chat is the direct messages chat of a channel
    """

    accent_color_id: int
    """
    Identifier of the accent color for the chat name and backgrounds of the chat photo,
    reply header, and link preview. See accent colors for more details.
    """

    max_reaction_count: int
    """
    The maximum number of reactions that can be set on a message in the chat
    """

    photo: ChatPhoto | None = None
    """
    Chat photo
    """

    active_usernames: list[str] | None = None
    """
    If non-empty, the list of all active chat usernames; for private chats, supergroups
    and channels
    """

    birthdate: Birthdate | None = None
    """
    For private chats, the date of birth of the user
    """

    business_intro: BusinessIntro | None = None
    """
    For private chats with business accounts, the intro of the business
    """

    business_location: BusinessLocation | None = None
    """
    For private chats with business accounts, the location of the business
    """

    business_opening_hours: BusinessOpeningHours | None = None
    """
    For private chats with business accounts, the opening hours of the business
    """

    personal_chat: Chat | None = None
    """
    For private chats, the personal channel of the user
    """

    parent_chat: Chat | None = None
    """
    Information about the corresponding channel chat; for direct messages chats only
    """

    available_reactions: list[ReactionType] | None = None
    """
    List of available reactions allowed in the chat. If omitted, then all emoji
    reactions are allowed.
    """

    background_custom_emoji_id: str | None = None
    """
    Custom emoji identifier of the emoji chosen by the chat for the reply header and
    link preview background
    """

    profile_accent_color_id: int | None = None
    """
    Identifier of the accent color for the chat's profile background. See profile accent
    colors for more details.
    """

    profile_background_custom_emoji_id: str | None = None
    """
    Custom emoji identifier of the emoji chosen by the chat for its profile background
    """

    emoji_status_custom_emoji_id: str | None = None
    """
    Custom emoji identifier of the emoji status of the chat or the other party in a
    private chat
    """

    emoji_status_expiration_date: int | None = None
    """
    Expiration date of the emoji status of the chat or the other party in a private
    chat, in Unix time, if any
    """

    bio: str | None = None
    """
    Bio of the other party in a private chat
    """

    has_private_forwards: bool | None = None
    """
    True, if privacy settings of the other party in the private chat allows to use
    tg://user?id=<user_id> links only in chats with the user
    """

    has_restricted_voice_and_video_messages: bool | None = None
    """
    True, if the privacy settings of the other party restrict sending voice and video
    note messages in the private chat
    """

    join_to_send_messages: bool | None = None
    """
    True, if users need to join the supergroup before they can send messages
    """

    join_by_request: bool | None = None
    """
    True, if all users directly joining the supergroup without using an invite link need
    to be approved by supergroup administrators
    """

    description: str | None = None
    """
    Description, for groups, supergroups and channel chats
    """

    invite_link: str | None = None
    """
    Primary invite link, for groups, supergroups and channel chats
    """

    pinned_message: Message | None = None
    """
    The most recent pinned message (by sending date)
    """

    permissions: ChatPermissions | None = None
    """
    Default chat member permissions, for groups and supergroups
    """

    accepted_gift_types: AcceptedGiftTypes
    """
    Information about types of gifts that are accepted by the chat or by the
    corresponding user for private chats
    """

    can_send_paid_media: bool | None = None
    """
    True, if paid media messages can be sent or forwarded to the channel chat. The field
    is available only for channel chats.
    """

    slow_mode_delay: int | None = None
    """
    For supergroups, the minimum allowed delay between consecutive messages sent by each
    unprivileged user; in seconds
    """

    unrestrict_boost_count: int | None = None
    """
    For supergroups, the minimum number of boosts that a non-administrator user needs to
    add in order to ignore slow mode and chat permissions
    """

    message_auto_delete_time: int | None = None
    """
    The time after which all messages sent to the chat will be automatically deleted; in
    seconds
    """

    has_aggressive_anti_spam_enabled: bool | None = None
    """
    True, if aggressive anti-spam checks are enabled in the supergroup. The field is
    only available to chat administrators.
    """

    has_hidden_members: bool | None = None
    """
    True, if non-administrators can only get the list of bots and administrators in the
    chat
    """

    has_protected_content: bool | None = None
    """
    True, if messages from the chat can't be forwarded to other chats
    """

    has_visible_history: bool | None = None
    """
    True, if new chat members will have access to old messages; available only to chat
    administrators
    """

    sticker_set_name: str | None = None
    """
    For supergroups, name of the group sticker set
    """

    can_set_sticker_set: bool | None = None
    """
    True, if the bot can change the group sticker set
    """

    custom_emoji_sticker_set_name: str | None = None
    """
    For supergroups, the name of the group's custom emoji sticker set. Custom emoji from
    this set can be used by all users and bots in the group.
    """

    linked_chat_id: int | None = None
    """
    Unique identifier for the linked chat, i.e. the discussion group identifier for a
    channel and vice versa; for supergroups and channel chats. This identifier may be
    greater than 32 bits and some programming languages may have difficulty/silent
    defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit
    integer or double-precision float type are safe for storing this identifier.
    """

    location: ChatLocation | None = None
    """
    For supergroups, the location to which the supergroup is connected
    """

    rating: UserRating | None = None
    """
    For private chats, the rating of the user if any
    """

    first_profile_audio: Audio | None = None
    """
    For private chats, the first audio added to the profile of the user
    """

    unique_gift_colors: UniqueGiftColors | None = None
    """
    The color scheme based on a unique gift that must be used for the chat's name,
    message replies and link previews
    """

    paid_message_star_count: int | None = None
    """
    The number of Telegram Stars a general user has to pay to send a message to the chat
    """

    guard_bot: User | None = None
    """
    The bot that processes join request queries in the chat. The field is only available
    to chat administrators.
    """

    community: Community | None = None
    """
    The Community to which the chat belongs
    """


class Message(TelegramObject):
    """
    This object represents a message.
    """

    message_id: int
    """
    Unique message identifier inside this chat; 0 for ephemeral messages. In specific
    instances (e.g., a message containing a video sent to a big chat), the server might
    automatically schedule a message instead of sending it immediately. In such cases,
    this field will be 0 and the relevant message will be unusable until it is actually
    sent.
    """

    message_thread_id: int | None = None
    """
    Unique identifier of a message thread or forum topic to which the message belongs;
    for supergroups and private chats only
    """

    direct_messages_topic: DirectMessagesTopic | None = None
    """
    Information about the direct messages chat topic that contains the message
    """

    from_: User | None = Field(None, alias="from")
    """
    Sender of the message; may be empty for messages sent to channels. For backward
    compatibility, if the message was sent on behalf of a chat, the field contains a
    fake sender user in non-channel chats.
    """

    sender_chat: Chat | None = None
    """
    Sender of the message when sent on behalf of a chat. For example, the supergroup
    itself for messages sent by its anonymous administrators or a linked channel for
    messages automatically forwarded to the channel's discussion group. For backward
    compatibility, if the message was sent on behalf of a chat, the field from contains
    a fake sender user in non-channel chats.
    """

    sender_boost_count: int | None = None
    """
    If the sender of the message boosted the chat, the number of boosts added by the
    user
    """

    sender_business_bot: User | None = None
    """
    The bot that actually sent the message on behalf of the business account. Available
    only for outgoing messages sent on behalf of the connected business account.
    """

    sender_tag: str | None = None
    """
    Tag or custom title of the sender of the message; for supergroups only
    """

    receiver_user: User | None = None
    """
    For ephemeral messages, the user who received the message
    """

    ephemeral_message_id: int | None = None
    """
    For ephemeral messages, identifier of the ephemeral message inside this chat. The
    identifier may be reused for another ephemeral message after the message is deleted
    or expires.
    """

    date: int = Field(gt=0)
    """
    Date the message was sent in Unix time. It is always a positive number, representing
    a valid date.
    """

    guest_query_id: str | None = None
    """
    The unique identifier for the guest query. Use this identifier with the method
    answerGuestQuery to send a response message. If non-empty, the message belongs to
    the chat where the guest bot was summoned, which may not coincide with other
    existing bot chats sharing the same identifier.
    """

    business_connection_id: str | None = None
    """
    Unique identifier of the business connection from which the message was received. If
    non-empty, the message belongs to a chat of the corresponding business account that
    is independent from any potential bot chat which might share the same identifier.
    """

    chat: Chat
    """
    Chat the message belongs to
    """

    forward_origin: MessageOrigin | None = None
    """
    Information about the original message for forwarded messages
    """

    is_topic_message: bool | None = None
    """
    True, if the message is sent to a topic in a forum supergroup or a private chat with
    the bot
    """

    is_automatic_forward: bool | None = None
    """
    True, if the message is a channel post that was automatically forwarded to the
    connected discussion group
    """

    reply_to_message: Message | None = None
    """
    For replies in the same chat and message thread, the original message. Note that the
    Message object in this field will not contain further reply_to_message fields even
    if it itself is a reply. If the message is a reply to an ephemeral message, then
    this field may be omitted.
    """

    external_reply: ExternalReplyInfo | None = None
    """
    Information about the message that is being replied to, which may come from another
    chat or forum topic
    """

    quote: TextQuote | None = None
    """
    For replies that quote part of the original message, the quoted part of the message
    """

    reply_to_story: Story | None = None
    """
    For replies to a story, the original story
    """

    reply_to_checklist_task_id: int | None = None
    """
    Identifier of the specific checklist task that is being replied to
    """

    reply_to_poll_option_id: str | None = None
    """
    Persistent identifier of the specific poll option that is being replied to
    """

    via_bot: User | None = None
    """
    Bot through which the message was sent
    """

    guest_bot_caller_user: User | None = None
    """
    For a message sent by a guest bot, this is the user whose original message triggered
    the bot's response
    """

    guest_bot_caller_chat: Chat | None = None
    """
    For a message sent by a guest bot, this is the chat whose original message triggered
    the bot's response
    """

    edit_date: int | None = None
    """
    Date the message was last edited in Unix time
    """

    has_protected_content: bool | None = None
    """
    True, if the message can't be forwarded
    """

    is_from_offline: bool | None = None
    """
    True, if the message was sent by an implicit action, for example, as an away or a
    greeting business message, or as a scheduled message
    """

    is_paid_post: bool | None = None
    """
    True, if the message is a paid post. Note that such posts must not be deleted for 24
    hours to receive the payment and can't be edited.
    """

    media_group_id: str | None = None
    """
    The unique identifier inside this chat of a media message group this message belongs
    to
    """

    author_signature: str | None = None
    """
    Signature of the post author for messages in channels, or the custom title of an
    anonymous group administrator
    """

    paid_star_count: int | None = None
    """
    The number of Telegram Stars that were paid by the sender of the message to send it
    """

    text: str | None = None
    """
    For text messages, the actual UTF-8 text of the message
    """

    entities: list[MessageEntity] | None = None
    """
    For text messages, special entities like usernames, URLs, bot commands, etc. that
    appear in the text
    """

    link_preview_options: LinkPreviewOptions | None = None
    """
    Options used for link preview generation for the message, if it is a text message
    and link preview options were changed
    """

    suggested_post_info: SuggestedPostInfo | None = None
    """
    Information about suggested post parameters if the message is a suggested post in a
    channel direct messages chat. If the message is an approved or declined suggested
    post, then it can't be edited.
    """

    effect_id: str | None = None
    """
    Unique identifier of the message effect added to the message
    """

    rich_message: RichMessage | None = None
    """
    Message is a rich formatted message
    """

    animation: Animation | None = None
    """
    Message is an animation, information about the animation. For backward
    compatibility, when this field is set, the document field will also be set.
    """

    audio: Audio | None = None
    """
    Message is an audio file, information about the file
    """

    document: Document | None = None
    """
    Message is a general file, information about the file
    """

    live_photo: LivePhoto | None = None
    """
    Message is a live photo, information about the live photo. For backward
    compatibility, when this field is set, the photo field will also be set.
    """

    paid_media: PaidMediaInfo | None = None
    """
    Message contains paid media; information about the paid media
    """

    photo: list[PhotoSize] | None = None
    """
    Message is a photo, available sizes of the photo
    """

    sticker: Sticker | None = None
    """
    Message is a sticker, information about the sticker
    """

    story: Story | None = None
    """
    Message is a forwarded story
    """

    video: Video | None = None
    """
    Message is a video, information about the video
    """

    video_note: VideoNote | None = None
    """
    Message is a video note, information about the video message
    """

    voice: Voice | None = None
    """
    Message is a voice message, information about the file
    """

    caption: str | None = None
    """
    Caption for the animation, audio, document, paid media, photo, video or voice
    """

    caption_entities: list[MessageEntity] | None = None
    """
    For messages with a caption, special entities like usernames, URLs, bot commands,
    etc. that appear in the caption
    """

    show_caption_above_media: bool | None = None
    """
    True, if the caption must be shown above the message media
    """

    has_media_spoiler: bool | None = None
    """
    True, if the message media is covered by a spoiler animation
    """

    checklist: Checklist | None = None
    """
    Message is a checklist
    """

    contact: Contact | None = None
    """
    Message is a shared contact, information about the contact
    """

    dice: Dice | None = None
    """
    Message is a dice with random value
    """

    game: Game | None = None
    """
    Message is a game, information about the game. More about games:
    https://core.telegram.org/bots/api#games
    """

    poll: Poll | None = None
    """
    Message is a native poll, information about the poll
    """

    venue: Venue | None = None
    """
    Message is a venue, information about the venue. For backward compatibility, when
    this field is set, the location field will also be set.
    """

    location: Location | None = None
    """
    Message is a shared location, information about the location
    """

    new_chat_members: list[User] | None = None
    """
    New members that were added to the group or supergroup and information about them
    (the bot itself may be one of these members)
    """

    left_chat_member: User | None = None
    """
    A member was removed from the group, information about them (this member may be the
    bot itself)
    """

    chat_owner_left: ChatOwnerLeft | None = None
    """
    Service message: chat owner has left
    """

    chat_owner_changed: ChatOwnerChanged | None = None
    """
    Service message: chat owner has changed
    """

    new_chat_title: str | None = None
    """
    A chat title was changed to this value
    """

    new_chat_photo: list[PhotoSize] | None = None
    """
    A chat photo was change to this value
    """

    delete_chat_photo: bool | None = None
    """
    Service message: the chat photo was deleted
    """

    group_chat_created: bool | None = None
    """
    Service message: the group has been created
    """

    supergroup_chat_created: bool | None = None
    """
    Service message: the supergroup has been created. This field can't be received in a
    message coming through updates, because bot can't be a member of a supergroup when
    it is created. It can only be found in reply_to_message if someone replies to a very
    first message in a directly created supergroup.
    """

    channel_chat_created: bool | None = None
    """
    Service message: the channel has been created. This field can't be received in a
    message coming through updates, because bot can't be a member of a channel when it
    is created. It can only be found in reply_to_message if someone replies to a very
    first message in a channel.
    """

    message_auto_delete_timer_changed: MessageAutoDeleteTimerChanged | None = None
    """
    Service message: auto-delete timer settings changed in the chat
    """

    migrate_to_chat_id: int | None = None
    """
    The group has been migrated to a supergroup with the specified identifier. This
    number may have more than 32 significant bits and some programming languages may
    have difficulty/silent defects in interpreting it. But it has at most 52 significant
    bits, so a signed 64-bit integer or double-precision float type are safe for storing
    this identifier.
    """

    migrate_from_chat_id: int | None = None
    """
    The supergroup has been migrated from a group with the specified identifier. This
    number may have more than 32 significant bits and some programming languages may
    have difficulty/silent defects in interpreting it. But it has at most 52 significant
    bits, so a signed 64-bit integer or double-precision float type are safe for storing
    this identifier.
    """

    pinned_message: MaybeInaccessibleMessage | None = None
    """
    Specified message was pinned. Note that the Message object in this field will not
    contain further reply_to_message fields even if it itself is a reply.
    """

    invoice: Invoice | None = None
    """
    Message is an invoice for a payment, information about the invoice. More about
    payments: https://core.telegram.org/bots/api#payments
    """

    successful_payment: SuccessfulPayment | None = None
    """
    Message is a service message about a successful payment, information about the
    payment. More about payments: https://core.telegram.org/bots/api#payments
    """

    refunded_payment: RefundedPayment | None = None
    """
    Message is a service message about a refunded payment, information about the
    payment. More about payments: https://core.telegram.org/bots/api#payments
    """

    users_shared: UsersShared | None = None
    """
    Service message: users were shared with the bot
    """

    chat_shared: ChatShared | None = None
    """
    Service message: a chat was shared with the bot
    """

    gift: GiftInfo | None = None
    """
    Service message: a regular gift was sent or received
    """

    unique_gift: UniqueGiftInfo | None = None
    """
    Service message: a unique gift was sent or received
    """

    gift_upgrade_sent: GiftInfo | None = None
    """
    Service message: upgrade of a gift was purchased after the gift was sent
    """

    connected_website: str | None = None
    """
    The domain name of the website on which the user has logged in. More about Telegram
    Login: https://core.telegram.org/widgets/login
    """

    write_access_allowed: WriteAccessAllowed | None = None
    """
    Service message: the user allowed the bot to write messages after adding it to the
    attachment or side menu, launching a Web App from a link, or accepting an explicit
    request from a Web App sent by the method requestWriteAccess
    """

    passport_data: PassportData | None = None
    """
    Telegram Passport data
    """

    proximity_alert_triggered: ProximityAlertTriggered | None = None
    """
    Service message: a user in the chat triggered another user's proximity alert while
    sharing Live Location
    """

    boost_added: ChatBoostAdded | None = None
    """
    Service message: user boosted the chat
    """

    chat_background_set: ChatBackground | None = None
    """
    Service message: chat background set
    """

    checklist_tasks_done: ChecklistTasksDone | None = None
    """
    Service message: some tasks in a checklist were marked as done or not done
    """

    checklist_tasks_added: ChecklistTasksAdded | None = None
    """
    Service message: tasks were added to a checklist
    """

    community_chat_added: CommunityChatAdded | None = None
    """
    Service message: chat or bot added to a Community
    """

    community_chat_joined: CommunityChatJoined | None = None
    """
    Service message: chat was joined by a user from a Community
    """

    community_chat_removed: CommunityChatRemoved | None = None
    """
    Service message: chat or bot removed from a Community
    """

    direct_message_price_changed: DirectMessagePriceChanged | None = None
    """
    Service message: the price for paid messages in the corresponding direct messages
    chat of a channel has changed
    """

    forum_topic_created: ForumTopicCreated | None = None
    """
    Service message: forum topic created
    """

    forum_topic_edited: ForumTopicEdited | None = None
    """
    Service message: forum topic edited
    """

    forum_topic_closed: ForumTopicClosed | None = None
    """
    Service message: forum topic closed
    """

    forum_topic_reopened: ForumTopicReopened | None = None
    """
    Service message: forum topic reopened
    """

    general_forum_topic_hidden: GeneralForumTopicHidden | None = None
    """
    Service message: the 'General' forum topic hidden
    """

    general_forum_topic_unhidden: GeneralForumTopicUnhidden | None = None
    """
    Service message: the 'General' forum topic unhidden
    """

    giveaway_created: GiveawayCreated | None = None
    """
    Service message: a scheduled giveaway was created
    """

    giveaway: Giveaway | None = None
    """
    The message is a scheduled giveaway message
    """

    giveaway_winners: GiveawayWinners | None = None
    """
    A giveaway with public winners was completed
    """

    giveaway_completed: GiveawayCompleted | None = None
    """
    Service message: a giveaway without public winners was completed
    """

    managed_bot_created: ManagedBotCreated | None = None
    """
    Service message: user created a bot that will be managed by the current bot
    """

    paid_message_price_changed: PaidMessagePriceChanged | None = None
    """
    Service message: the price for paid messages has changed in the chat
    """

    poll_option_added: PollOptionAdded | None = None
    """
    Service message: answer option was added to a poll
    """

    poll_option_deleted: PollOptionDeleted | None = None
    """
    Service message: answer option was deleted from a poll
    """

    suggested_post_approved: SuggestedPostApproved | None = None
    """
    Service message: a suggested post was approved
    """

    suggested_post_approval_failed: SuggestedPostApprovalFailed | None = None
    """
    Service message: approval of a suggested post has failed
    """

    suggested_post_declined: SuggestedPostDeclined | None = None
    """
    Service message: a suggested post was declined
    """

    suggested_post_paid: SuggestedPostPaid | None = None
    """
    Service message: payment for a suggested post was received
    """

    suggested_post_refunded: SuggestedPostRefunded | None = None
    """
    Service message: payment for a suggested post was refunded
    """

    video_chat_scheduled: VideoChatScheduled | None = None
    """
    Service message: video chat scheduled
    """

    video_chat_started: VideoChatStarted | None = None
    """
    Service message: video chat started
    """

    video_chat_ended: VideoChatEnded | None = None
    """
    Service message: video chat ended
    """

    video_chat_participants_invited: VideoChatParticipantsInvited | None = None
    """
    Service message: new participants invited to a video chat
    """

    web_app_data: WebAppData | None = None
    """
    Service message: data sent by a Web App
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message. login_url buttons are represented as
    ordinary url buttons.
    """


class MessageId(TelegramObject):
    """
    This object represents a unique message identifier.
    """

    message_id: int
    """
    Unique message identifier. In specific instances (e.g., message containing a video
    sent to a big chat), the server might automatically schedule a message instead of
    sending it immediately. In such cases, this field will be 0 and the relevant message
    will be unusable until it is actually sent.
    """


class InaccessibleMessage(TelegramObject):
    """
    This object describes a message that was deleted or is otherwise inaccessible to the
    bot.
    """

    chat: Chat
    """
    Chat the message belonged to
    """

    message_id: int
    """
    Unique message identifier inside the chat
    """

    date: Literal[0] = 0
    """
    Always 0. The field can be used to differentiate regular and inaccessible messages.
    """


type MaybeInaccessibleMessage = Message | InaccessibleMessage


class MessageEntity(TelegramObject):
    """
    This object represents one special entity in a text message. For example, hashtags,
    usernames, URLs, etc.
    """

    type: str
    """
    Type of the entity. Currently, can be "mention" (@username), "hashtag" (#hashtag or
    #hashtag@chatusername), "cashtag" ($USD or $USD@chatusername), "bot_command"
    (/start@jobs_bot), "url" (https://telegram.org), "email" (do-not-
    reply@telegram.org), "phone_number" (+1-212-555-0123), "bold" (bold text), "italic"
    (italic text), "underline" (underlined text), "strikethrough" (strikethrough text),
    "spoiler" (spoiler message), "blockquote" (block quotation), "expandable_blockquote"
    (collapsed-by-default block quotation), "code" (monowidth string), "pre" (monowidth
    block), "text_link" (for clickable text URLs), "text_mention" (for users without
    usernames), "custom_emoji" (for inline custom emoji stickers), or "date_time" (for
    formatted date and time).
    """

    offset: int
    """
    Offset in UTF-16 code units to the start of the entity
    """

    length: int
    """
    Length of the entity in UTF-16 code units
    """

    url: str | None = None
    """
    For "text_link" only, URL that will be opened after user taps on the text
    """

    user: User | None = None
    """
    For "text_mention" only, the mentioned user
    """

    language: str | None = None
    """
    For "pre" only, the programming language of the entity text
    """

    custom_emoji_id: str | None = None
    """
    For "custom_emoji" only, unique identifier of the custom emoji. Use
    getCustomEmojiStickers to get full information about the sticker.
    """

    unix_time: int | None = None
    """
    For "date_time" only, the Unix time associated with the entity
    """

    date_time_format: str | None = None
    """
    For "date_time" only, the string that defines the formatting of the date and time.
    See date-time entity formatting for more details.
    """


class TextQuote(TelegramObject):
    """
    This object contains information about the quoted part of a message that is replied
    to by the given message.
    """

    text: str
    """
    Text of the quoted part of a message that is replied to by the given message
    """

    entities: list[MessageEntity] | None = None
    """
    Special entities that appear in the quote. Currently, only bold, italic, underline,
    strikethrough, spoiler, custom_emoji, and date_time entities are kept in quotes.
    """

    position: int
    """
    Approximate quote position in the original message in UTF-16 code units as specified
    by the sender
    """

    is_manual: bool | None = None
    """
    True, if the quote was chosen manually by the message sender. Otherwise, the quote
    was added automatically by the server.
    """


class ExternalReplyInfo(TelegramObject):
    """
    This object contains information about a message that is being replied to, which may
    come from another chat or forum topic.
    """

    origin: MessageOrigin
    """
    Origin of the message replied to by the given message
    """

    chat: Chat | None = None
    """
    Chat the original message belongs to. Available only if the chat is a supergroup or
    a channel.
    """

    message_id: int | None = None
    """
    Unique message identifier inside the original chat. Available only if the original
    chat is a supergroup or a channel.
    """

    link_preview_options: LinkPreviewOptions | None = None
    """
    Options used for link preview generation for the original message, if it is a text
    message
    """

    animation: Animation | None = None
    """
    Message is an animation, information about the animation
    """

    audio: Audio | None = None
    """
    Message is an audio file, information about the file
    """

    document: Document | None = None
    """
    Message is a general file, information about the file
    """

    live_photo: LivePhoto | None = None
    """
    Message is a live photo, information about the live photo
    """

    paid_media: PaidMediaInfo | None = None
    """
    Message contains paid media; information about the paid media
    """

    photo: list[PhotoSize] | None = None
    """
    Message is a photo, available sizes of the photo
    """

    sticker: Sticker | None = None
    """
    Message is a sticker, information about the sticker
    """

    story: Story | None = None
    """
    Message is a forwarded story
    """

    video: Video | None = None
    """
    Message is a video, information about the video
    """

    video_note: VideoNote | None = None
    """
    Message is a video note, information about the video message
    """

    voice: Voice | None = None
    """
    Message is a voice message, information about the file
    """

    has_media_spoiler: bool | None = None
    """
    True, if the message media is covered by a spoiler animation
    """

    checklist: Checklist | None = None
    """
    Message is a checklist
    """

    contact: Contact | None = None
    """
    Message is a shared contact, information about the contact
    """

    dice: Dice | None = None
    """
    Message is a dice with random value
    """

    game: Game | None = None
    """
    Message is a game, information about the game. More about games:
    https://core.telegram.org/bots/api#games
    """

    giveaway: Giveaway | None = None
    """
    Message is a scheduled giveaway, information about the giveaway
    """

    giveaway_winners: GiveawayWinners | None = None
    """
    A giveaway with public winners was completed
    """

    invoice: Invoice | None = None
    """
    Message is an invoice for a payment, information about the invoice. More about
    payments: https://core.telegram.org/bots/api#payments
    """

    location: Location | None = None
    """
    Message is a shared location, information about the location
    """

    poll: Poll | None = None
    """
    Message is a native poll, information about the poll
    """

    venue: Venue | None = None
    """
    Message is a venue, information about the venue
    """


class ReplyParameters(TelegramObject):
    """
    Describes reply parameters for the message that is being sent.
    """

    message_id: int | None = None
    """
    Identifier of the message that will be replied to in the current chat, or in the
    chat chat_id if it is specified. Required if ephemeral_message_id isn't specified.
    """

    chat_id: int | str | None = None
    """
    If the message to be replied to is from a different chat, unique identifier for the
    chat or username of the bot, supergroup or channel in the format @username. Not
    supported for messages sent on behalf of a business account, messages from channel
    direct messages chats and ephemeral messages.
    """

    ephemeral_message_id: int | None = None
    """
    Identifier of the incoming ephemeral message that will be replied to in the current
    chat. A reply to an ephemeral message must itself be an ephemeral message. An
    ephemeral message may only be replied to within 15 seconds of being sent. Required
    if message_id isn't specified.
    """

    allow_sending_without_reply: bool | None = None
    """
    Pass True if the message should be sent even if the specified message to be replied
    to is not found. Always False for replies in another chat or forum topic, and sent
    ephemeral messages. Always True for messages sent on behalf of a business account.
    """

    quote: str | None = None
    """
    Quoted part of the message to be replied to; 0-1024 characters after entities
    parsing. The quote must be an exact substring of the message to be replied to,
    including bold, italic, underline, strikethrough, spoiler, custom_emoji, and
    date_time entities. The message will fail to send if the quote isn't found in the
    original message. Ignored for ephemeral messages.
    """

    quote_parse_mode: str | None = None
    """
    Mode for parsing entities in the quote. See formatting options for more details.
    """

    quote_entities: list[MessageEntity] | None = None
    """
    A JSON-serialized list of special entities that appear in the quote. It can be
    specified instead of quote_parse_mode.
    """

    quote_position: int | None = None
    """
    Position of the quote in the original message in UTF-16 code units
    """

    checklist_task_id: int | None = None
    """
    Identifier of the specific checklist task to be replied to
    """

    poll_option_id: str | None = None
    """
    Persistent identifier of the specific poll option to be replied to
    """


class EphemeralMessageParameters(TelegramObject):
    """
    No description
    """

    receiver_user_id: int
    """
    Identifier of the user who will receive the message. It is not guaranteed that the
    user will receive the message, especially if they are offline. See here for more
    details.
    """

    callback_query_id: str | None = None
    """
    Identifier of the callback query which triggered the message, if any
    """

    replace_callback_query_message: bool | None = None
    """
    Pass True if the ephemeral message must be shown in place of the original message.
    Must be False for callback queries from ephemeral messages, which must be edited
    using regular editEphemeralMessage... methods.
    """


type MessageOrigin = Annotated[
    MessageOriginUser
    | MessageOriginHiddenUser
    | MessageOriginChat
    | MessageOriginChannel,
    Field(discriminator="type"),
]


class MessageOriginUser(TelegramObject):
    """
    The message was originally sent by a known user.
    """

    type: Literal["user"] = "user"
    """
    Type of the message origin, always "user"
    """

    date: int
    """
    Date the message was sent originally in Unix time
    """

    sender_user: User
    """
    User that sent the message originally
    """


class MessageOriginHiddenUser(TelegramObject):
    """
    The message was originally sent by an unknown user.
    """

    type: Literal["hidden_user"] = "hidden_user"
    """
    Type of the message origin, always "hidden_user"
    """

    date: int
    """
    Date the message was sent originally in Unix time
    """

    sender_user_name: str
    """
    Name of the user that sent the message originally
    """


class MessageOriginChat(TelegramObject):
    """
    The message was originally sent on behalf of a chat to a group chat.
    """

    type: Literal["chat"] = "chat"
    """
    Type of the message origin, always "chat"
    """

    date: int
    """
    Date the message was sent originally in Unix time
    """

    sender_chat: Chat
    """
    Chat that sent the message originally
    """

    author_signature: str | None = None
    """
    For messages originally sent by an anonymous chat administrator, original message
    author signature
    """


class MessageOriginChannel(TelegramObject):
    """
    The message was originally sent to a channel chat.
    """

    type: Literal["channel"] = "channel"
    """
    Type of the message origin, always "channel"
    """

    date: int
    """
    Date the message was sent originally in Unix time
    """

    chat: Chat
    """
    Channel chat to which the message was originally sent
    """

    message_id: int
    """
    Unique message identifier inside the chat
    """

    author_signature: str | None = None
    """
    Signature of the original post author
    """


class PhotoSize(TelegramObject):
    """
    This object represents one size of a photo or a file / sticker thumbnail.
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """

    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    """

    width: int
    """
    Photo width
    """

    height: int
    """
    Photo height
    """

    file_size: int | None = None
    """
    File size in bytes
    """


class Animation(TelegramObject):
    """
    This object represents an animation file (GIF or H.264/MPEG-4 AVC video without
    sound).
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """

    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    """

    width: int
    """
    Video width as defined by the sender
    """

    height: int
    """
    Video height as defined by the sender
    """

    duration: int
    """
    Duration of the video in seconds as defined by the sender
    """

    thumbnail: PhotoSize | None = None
    """
    Animation thumbnail as defined by the sender
    """

    file_name: str | None = None
    """
    Original animation filename as defined by the sender
    """

    mime_type: str | None = None
    """
    MIME type of the file as defined by the sender
    """

    file_size: int | None = None
    """
    File size in bytes. It can be bigger than 2^31 and some programming languages may
    have difficulty/silent defects in interpreting it. But it has at most 52 significant
    bits, so a signed 64-bit integer or double-precision float type are safe for storing
    this value.
    """


class Audio(TelegramObject):
    """
    This object represents an audio file to be treated as music by the Telegram clients.
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """

    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    """

    duration: int
    """
    Duration of the audio in seconds as defined by the sender
    """

    performer: str | None = None
    """
    Performer of the audio as defined by the sender or by audio tags
    """

    title: str | None = None
    """
    Title of the audio as defined by the sender or by audio tags
    """

    file_name: str | None = None
    """
    Original filename as defined by the sender
    """

    mime_type: str | None = None
    """
    MIME type of the file as defined by the sender
    """

    file_size: int | None = None
    """
    File size in bytes. It can be bigger than 2^31 and some programming languages may
    have difficulty/silent defects in interpreting it. But it has at most 52 significant
    bits, so a signed 64-bit integer or double-precision float type are safe for storing
    this value.
    """

    thumbnail: PhotoSize | None = None
    """
    Thumbnail of the album cover to which the music file belongs
    """


class Document(TelegramObject):
    """
    This object represents a general file (as opposed to photos, voice messages and
    audio files).
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """

    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    """

    thumbnail: PhotoSize | None = None
    """
    Document thumbnail as defined by the sender
    """

    file_name: str | None = None
    """
    Original filename as defined by the sender
    """

    mime_type: str | None = None
    """
    MIME type of the file as defined by the sender
    """

    file_size: int | None = None
    """
    File size in bytes. It can be bigger than 2^31 and some programming languages may
    have difficulty/silent defects in interpreting it. But it has at most 52 significant
    bits, so a signed 64-bit integer or double-precision float type are safe for storing
    this value.
    """


class LivePhoto(TelegramObject):
    """
    This object represents a live photo.
    """

    photo: list[PhotoSize] | None = None
    """
    Available sizes of the corresponding static photo
    """

    file_id: str
    """
    Identifier for the video file which can be used to download or reuse the file
    """

    file_unique_id: str
    """
    Unique identifier for the video file which is supposed to be the same over time and
    for different bots. Can't be used to download or reuse the file.
    """

    width: int
    """
    Video width as defined by the sender
    """

    height: int
    """
    Video height as defined by the sender
    """

    duration: int
    """
    Duration of the video in seconds as defined by the sender
    """

    mime_type: str | None = None
    """
    MIME type of the file as defined by the sender
    """

    file_size: int | None = None
    """
    File size in bytes. It can be bigger than 2^31 and some programming languages may
    have difficulty/silent defects in interpreting it. But it has at most 52 significant
    bits, so a signed 64-bit integer or double-precision float type are safe for storing
    this value.
    """


class Story(TelegramObject):
    """
    This object represents a story.
    """

    chat: Chat
    """
    Chat that posted the story
    """

    id: int
    """
    Unique identifier for the story in the chat
    """


class VideoQuality(TelegramObject):
    """
    This object represents a video file of a specific quality.
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """

    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    """

    width: int
    """
    Video width
    """

    height: int
    """
    Video height
    """

    codec: str
    """
    Codec that was used to encode the video, for example, "h264", "h265", or "av01"
    """

    file_size: int | None = None
    """
    File size in bytes. It can be bigger than 2^31 and some programming languages may
    have difficulty/silent defects in interpreting it. But it has at most 52 significant
    bits, so a signed 64-bit integer or double-precision float type are safe for storing
    this value.
    """


class Video(TelegramObject):
    """
    This object represents a video file.
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """

    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    """

    width: int
    """
    Video width as defined by the sender
    """

    height: int
    """
    Video height as defined by the sender
    """

    duration: int
    """
    Duration of the video in seconds as defined by the sender
    """

    thumbnail: PhotoSize | None = None
    """
    Video thumbnail
    """

    cover: list[PhotoSize] | None = None
    """
    Available sizes of the cover of the video in the message
    """

    start_timestamp: int | None = None
    """
    Timestamp in seconds from which the video will play in the message
    """

    qualities: list[VideoQuality] | None = None
    """
    List of available qualities of the video
    """

    file_name: str | None = None
    """
    Original filename as defined by the sender
    """

    mime_type: str | None = None
    """
    MIME type of the file as defined by the sender
    """

    file_size: int | None = None
    """
    File size in bytes. It can be bigger than 2^31 and some programming languages may
    have difficulty/silent defects in interpreting it. But it has at most 52 significant
    bits, so a signed 64-bit integer or double-precision float type are safe for storing
    this value.
    """


class VideoNote(TelegramObject):
    """
    This object represents a video message.
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """

    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    """

    length: int
    """
    Video width and height (diameter of the video message) as defined by the sender
    """

    duration: int
    """
    Duration of the video in seconds as defined by the sender
    """

    thumbnail: PhotoSize | None = None
    """
    Video thumbnail
    """

    file_size: int | None = None
    """
    File size in bytes
    """


class Voice(TelegramObject):
    """
    This object represents a voice note.
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """

    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    """

    duration: int
    """
    Duration of the audio in seconds as defined by the sender
    """

    mime_type: str | None = None
    """
    MIME type of the file as defined by the sender
    """

    file_size: int | None = None
    """
    File size in bytes. It can be bigger than 2^31 and some programming languages may
    have difficulty/silent defects in interpreting it. But it has at most 52 significant
    bits, so a signed 64-bit integer or double-precision float type are safe for storing
    this value.
    """


class PaidMediaInfo(TelegramObject):
    """
    Describes the paid media added to a message.
    """

    star_count: int
    """
    The number of Telegram Stars that must be paid to buy access to the media
    """

    paid_media: list[PaidMedia]
    """
    Information about the paid media
    """


type PaidMedia = Annotated[
    PaidMediaLivePhoto | PaidMediaPhoto | PaidMediaPreview | PaidMediaVideo,
    Field(discriminator="type"),
]


class PaidMediaLivePhoto(TelegramObject):
    """
    The paid media is a live photo.
    """

    type: Literal["live_photo"] = "live_photo"
    """
    Type of the paid media, always "live_photo"
    """

    live_photo: LivePhoto
    """
    The photo
    """


class PaidMediaPhoto(TelegramObject):
    """
    The paid media is a photo.
    """

    type: Literal["photo"] = "photo"
    """
    Type of the paid media, always "photo"
    """

    photo: list[PhotoSize]
    """
    The photo
    """


class PaidMediaPreview(TelegramObject):
    """
    The paid media isn't available before the payment.
    """

    type: Literal["preview"] = "preview"
    """
    Type of the paid media, always "preview"
    """

    width: int | None = None
    """
    Media width as defined by the sender
    """

    height: int | None = None
    """
    Media height as defined by the sender
    """

    duration: int | None = None
    """
    Duration of the media in seconds as defined by the sender
    """


class PaidMediaVideo(TelegramObject):
    """
    The paid media is a video.
    """

    type: Literal["video"] = "video"
    """
    Type of the paid media, always "video"
    """

    video: Video
    """
    The video
    """


class Contact(TelegramObject):
    """
    This object represents a phone contact.
    """

    phone_number: str
    """
    Contact's phone number
    """

    first_name: str
    """
    Contact's first name
    """

    last_name: str | None = None
    """
    Contact's last name
    """

    user_id: int | None = None
    """
    Contact's user identifier in Telegram. This number may have more than 32 significant
    bits and some programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a 64-bit integer or
    double-precision float type are safe for storing this identifier.
    """

    vcard: str | None = None
    """
    Additional data about the contact in the form of a vCard
    """


class Dice(TelegramObject):
    """
    This object represents an animated emoji that displays a random value.
    """

    emoji: str
    """
    Emoji on which the dice throw animation is based
    """

    value: int
    """
    Value of the dice, 1-6 for "🎲", "🎯" and "🎳" base emoji, 1-5 for "🏀" and "⚽" base
    emoji, 1-64 for "🎰" base emoji
    """


class Link(TelegramObject):
    """
    Represents an HTTP link.
    """

    url: str
    """
    URL of the link
    """


class PollMedia(TelegramObject):
    """
    At most one of the optional fields can be present in any given object.
    """

    animation: Animation | None = None
    """
    Media is an animation, information about the animation
    """

    audio: Audio | None = None
    """
    Media is an audio file, information about the file; currently, can't be received in
    a poll option
    """

    document: Document | None = None
    """
    Media is a general file, information about the file; currently, can't be received in
    a poll option
    """

    link: Link | None = None
    """
    The HTTP link attached to the poll option
    """

    live_photo: LivePhoto | None = None
    """
    Media is a live photo, information about the live photo
    """

    location: Location | None = None
    """
    Media is a shared location, information about the location
    """

    photo: list[PhotoSize] | None = None
    """
    Media is a photo, available sizes of the photo
    """

    sticker: Sticker | None = None
    """
    Media is a sticker, information about the sticker; currently, for poll options only
    """

    venue: Venue | None = None
    """
    Media is a venue, information about the venue
    """

    video: Video | None = None
    """
    Media is a video, information about the video
    """


type InputPollMedia = Annotated[
    InputMediaAnimation
    | InputMediaAudio
    | InputMediaDocument
    | InputMediaLivePhoto
    | InputMediaLocation
    | InputMediaPhoto
    | InputMediaVenue
    | InputMediaVideo,
    Field(discriminator="type"),
]


type InputPollOptionMedia = Annotated[
    InputMediaAnimation
    | InputMediaLink
    | InputMediaLivePhoto
    | InputMediaLocation
    | InputMediaPhoto
    | InputMediaSticker
    | InputMediaVenue
    | InputMediaVideo,
    Field(discriminator="type"),
]


class PollOption(TelegramObject):
    """
    This object contains information about one answer option in a poll.
    """

    persistent_id: str
    """
    Unique identifier of the option, persistent on option addition and deletion
    """

    text: str
    """
    Option text, 1-100 characters
    """

    text_entities: list[MessageEntity] | None = None
    """
    Special entities that appear in the option text. Currently, only custom emoji
    entities are allowed in poll option texts
    """

    media: PollMedia | None = None
    """
    Media added to the poll option
    """

    voter_count: int
    """
    Number of users who voted for this option; may be 0 if unknown
    """

    added_by_user: User | None = None
    """
    User who added the option; omitted if the option wasn't added by a user after poll
    creation
    """

    added_by_chat: Chat | None = None
    """
    Chat that added the option; omitted if the option wasn't added by a chat after poll
    creation
    """

    addition_date: int | None = None
    """
    Point in time (Unix timestamp) when the option was added; omitted if the option
    existed in the original poll
    """


class InputPollOption(TelegramObject):
    """
    This object contains information about one answer option in a poll to be sent.
    """

    text: str
    """
    Option text, 1-100 characters
    """

    text_parse_mode: str | None = None
    """
    Mode for parsing entities in the text. See formatting options for more details.
    Currently, only custom emoji entities are allowed.
    """

    text_entities: list[MessageEntity] | None = None
    """
    A JSON-serialized list of special entities that appear in the poll option text. It
    can be specified instead of text_parse_mode.
    """

    media: InputPollOptionMedia | None = None
    """
    Media added to the poll option
    """


class PollAnswer(TelegramObject):
    """
    This object represents an answer of a user in a non-anonymous poll.
    """

    poll_id: str
    """
    Unique poll identifier
    """

    voter_chat: Chat | None = None
    """
    The chat that changed the answer to the poll, if the voter is anonymous
    """

    user: User | None = None
    """
    The user that changed the answer to the poll, if the voter isn't anonymous
    """

    option_ids: list[int]
    """
    0-based identifiers of chosen answer options. May be empty if the vote was
    retracted.
    """

    option_persistent_ids: list[str]
    """
    Persistent identifiers of the chosen answer options. May be empty if the vote was
    retracted.
    """


class Poll(TelegramObject):
    """
    This object contains information about a poll.
    """

    id: str
    """
    Unique poll identifier
    """

    question: str
    """
    Poll question, 1-300 characters
    """

    question_entities: list[MessageEntity] | None = None
    """
    Special entities that appear in the question. Currently, only custom emoji entities
    are allowed in poll questions
    """

    options: list[PollOption]
    """
    List of poll options
    """

    total_voter_count: int
    """
    Total number of users that voted in the poll
    """

    is_closed: bool
    """
    True, if the poll is closed
    """

    is_anonymous: bool
    """
    True, if the poll is anonymous
    """

    type: str
    """
    Poll type, currently can be "regular" or "quiz"
    """

    allows_multiple_answers: bool
    """
    True, if the poll allows multiple answers
    """

    allows_revoting: bool
    """
    True, if the poll allows to change the chosen answer options
    """

    members_only: bool
    """
    True if voting is limited to users who have been members of the chat where the poll
    was originally sent for more than 24 hours
    """

    country_codes: list[str] | None = None
    """
    A list of two-letter ISO 3166-1 alpha-2 country codes indicating the countries from
    which users can vote in the poll. The country code "FT" is used for users with
    anonymous numbers. If omitted, then users from any country can participate in the
    poll.
    """

    correct_option_ids: list[int] | None = None
    """
    Array of 0-based identifiers of the correct answer options. Available only for polls
    in quiz mode which are closed or were sent (not forwarded) by the bot or to the
    private chat with the bot.
    """

    explanation: str | None = None
    """
    Text that is shown when a user chooses an incorrect answer or taps on the lamp icon
    in a quiz-style poll, 0-200 characters
    """

    explanation_entities: list[MessageEntity] | None = None
    """
    Special entities like usernames, URLs, bot commands, etc. that appear in the
    explanation
    """

    explanation_media: PollMedia | None = None
    """
    Media added to the quiz explanation
    """

    open_period: int | None = None
    """
    Amount of time in seconds the poll will be active after creation
    """

    close_date: int | None = None
    """
    Point in time (Unix timestamp) when the poll will be automatically closed
    """

    description: str | None = None
    """
    Description of the poll; for polls inside the Message object only
    """

    description_entities: list[MessageEntity] | None = None
    """
    Special entities like usernames, URLs, bot commands, etc. that appear in the
    description
    """

    media: PollMedia | None = None
    """
    Media added to the poll description; for polls inside the Message object only
    """


class ChecklistTask(TelegramObject):
    """
    Describes a task in a checklist.
    """

    id: int
    """
    Unique identifier of the task
    """

    text: str
    """
    Text of the task
    """

    text_entities: list[MessageEntity] | None = None
    """
    Special entities that appear in the task text
    """

    completed_by_user: User | None = None
    """
    User that completed the task; omitted if the task wasn't completed by a user
    """

    completed_by_chat: Chat | None = None
    """
    Chat that completed the task; omitted if the task wasn't completed by a chat
    """

    completion_date: int | None = None
    """
    Point in time (Unix timestamp) when the task was completed; 0 if the task wasn't
    completed
    """


class Checklist(TelegramObject):
    """
    Describes a checklist.
    """

    title: str
    """
    Title of the checklist
    """

    title_entities: list[MessageEntity] | None = None
    """
    Special entities that appear in the checklist title
    """

    tasks: list[ChecklistTask]
    """
    List of tasks in the checklist
    """

    others_can_add_tasks: bool | None = None
    """
    True, if users other than the creator of the list can add tasks to the list
    """

    others_can_mark_tasks_as_done: bool | None = None
    """
    True, if users other than the creator of the list can mark tasks as done or not done
    """


class InputChecklistTask(TelegramObject):
    """
    Describes a task to add to a checklist.
    """

    id: int
    """
    Unique identifier of the task; must be positive and unique among all task
    identifiers currently present in the checklist
    """

    text: str
    """
    Text of the task; 1-100 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the text. See formatting options for more details.
    """

    text_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the text, which can be specified instead of
    parse_mode. Currently, only bold, italic, underline, strikethrough, spoiler,
    custom_emoji, and date_time entities are allowed.
    """


class InputChecklist(TelegramObject):
    """
    Describes a checklist to create.
    """

    title: str
    """
    Title of the checklist; 1-255 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the title. See formatting options for more details.
    """

    title_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the title, which can be specified instead of
    parse_mode. Currently, only bold, italic, underline, strikethrough, spoiler,
    custom_emoji, and date_time entities are allowed.
    """

    tasks: list[InputChecklistTask]
    """
    List of 1-30 tasks in the checklist
    """

    others_can_add_tasks: bool | None = None
    """
    Pass True if other users can add tasks to the checklist
    """

    others_can_mark_tasks_as_done: bool | None = None
    """
    Pass True if other users can mark tasks as done or not done in the checklist
    """


class Location(TelegramObject):
    """
    This object represents a point on the map.
    """

    latitude: float
    """
    Latitude as defined by the sender
    """

    longitude: float
    """
    Longitude as defined by the sender
    """

    horizontal_accuracy: float | None = None
    """
    The radius of uncertainty for the location, measured in meters; 0-1500
    """

    live_period: int | None = None
    """
    Time relative to the message sending date, during which the location can be updated;
    in seconds. For active live locations only.
    """

    heading: int | None = None
    """
    The direction in which user is moving, in degrees; 1-360. For active live locations
    only.
    """

    proximity_alert_radius: int | None = None
    """
    The maximum distance for proximity alerts about approaching another chat member, in
    meters. For sent live locations only.
    """


class Venue(TelegramObject):
    """
    This object represents a venue.
    """

    location: Location
    """
    Venue location. Can't be a live location.
    """

    title: str
    """
    Name of the venue
    """

    address: str
    """
    Address of the venue
    """

    foursquare_id: str | None = None
    """
    Foursquare identifier of the venue
    """

    foursquare_type: str | None = None
    """
    Foursquare type of the venue. (For example, "arts_entertainment/default",
    "arts_entertainment/aquarium" or "food/icecream".)
    """

    google_place_id: str | None = None
    """
    Google Places identifier of the venue
    """

    google_place_type: str | None = None
    """
    Google Places type of the venue. (See supported types.)
    """


class WebAppData(TelegramObject):
    """
    Describes data sent from a Web App to the bot.
    """

    data: str
    """
    The data. Be aware that a bad client can send arbitrary data in this field.
    """

    button_text: str
    """
    Text of the web_app keyboard button from which the Web App was opened. Be aware that
    a bad client can send arbitrary data in this field.
    """


class ProximityAlertTriggered(TelegramObject):
    """
    This object represents the content of a service message, sent whenever a user in the
    chat triggers a proximity alert set by another user.
    """

    traveler: User
    """
    User that triggered the alert
    """

    watcher: User
    """
    User that set the alert
    """

    distance: int
    """
    The distance between the users
    """


class MessageAutoDeleteTimerChanged(TelegramObject):
    """
    This object represents a service message about a change in auto-delete timer
    settings.
    """

    message_auto_delete_time: int
    """
    New auto-delete time for messages in the chat; in seconds
    """


class ManagedBotCreated(TelegramObject):
    """
    This object contains information about the bot that was created to be managed by the
    current bot.
    """

    bot: User
    """
    Information about the bot. The bot's token can be fetched using the method
    getManagedBotToken.
    """


class ManagedBotUpdated(TelegramObject):
    """
    This object contains information about the creation, token update, or owner update
    of a bot that is managed by the current bot.
    """

    user: User
    """
    User that created the bot
    """

    bot: User
    """
    Information about the bot. Token of the bot can be fetched using the method
    getManagedBotToken.
    """


class BotSubscriptionUpdated(TelegramObject):
    """
    This object contains information about changes to a user payment subscription toward
    the current bot.
    """

    user: User
    """
    User who subscribed for payments toward the bot
    """

    invoice_payload: str
    """
    Bot-specified invoice payload
    """

    state: str
    """
    The new state of the subscription. Currently, it can be one of "canceled" if the
    user canceled the subscription, "active" if the user re-enabled a previously
    canceled subscription, or "failed" if payment for the subscription failed.
    """


class MessageGenerationStopped(TelegramObject):
    """
    This object describes an update about a user stopping message generation.
    """

    chat: Chat
    """
    Chat in which the message is generated
    """

    message_thread_id: int | None = None
    """
    Unique identifier of the message thread in which the message is generated
    """

    draft_id: int
    """
    Unique identifier of the message draft which was stopped
    """


class PollOptionAdded(TelegramObject):
    """
    Describes a service message about an option added to a poll.
    """

    poll_message: MaybeInaccessibleMessage | None = None
    """
    Message containing the poll to which the option was added, if known. Note that the
    Message object in this field will not contain the reply_to_message field even if it
    itself is a reply.
    """

    option_persistent_id: str
    """
    Unique identifier of the added option
    """

    option_text: str
    """
    Option text
    """

    option_text_entities: list[MessageEntity] | None = None
    """
    Special entities that appear in the option_text
    """


class PollOptionDeleted(TelegramObject):
    """
    Describes a service message about an option deleted from a poll.
    """

    poll_message: MaybeInaccessibleMessage | None = None
    """
    Message containing the poll from which the option was deleted, if known. Note that
    the Message object in this field will not contain the reply_to_message field even if
    it itself is a reply.
    """

    option_persistent_id: str
    """
    Unique identifier of the deleted option
    """

    option_text: str
    """
    Option text
    """

    option_text_entities: list[MessageEntity] | None = None
    """
    Special entities that appear in the option_text
    """


class ChatBoostAdded(TelegramObject):
    """
    This object represents a service message about a user boosting a chat.
    """

    boost_count: int
    """
    Number of boosts added by the user
    """


type BackgroundFill = Annotated[
    BackgroundFillSolid | BackgroundFillGradient | BackgroundFillFreeformGradient,
    Field(discriminator="type"),
]


class BackgroundFillSolid(TelegramObject):
    """
    The background is filled using the selected color.
    """

    type: Literal["solid"] = "solid"
    """
    Type of the background fill, always "solid"
    """

    color: int
    """
    The color of the background fill in the RGB24 format
    """


class BackgroundFillGradient(TelegramObject):
    """
    The background is a gradient fill.
    """

    type: Literal["gradient"] = "gradient"
    """
    Type of the background fill, always "gradient"
    """

    top_color: int
    """
    Top color of the gradient in the RGB24 format
    """

    bottom_color: int
    """
    Bottom color of the gradient in the RGB24 format
    """

    rotation_angle: int
    """
    Clockwise rotation angle of the background fill in degrees; 0-359
    """


class BackgroundFillFreeformGradient(TelegramObject):
    """
    The background is a freeform gradient that rotates after every message in the chat.
    """

    type: Literal["freeform_gradient"] = "freeform_gradient"
    """
    Type of the background fill, always "freeform_gradient"
    """

    colors: list[int]
    """
    A list of the 3 or 4 base colors that are used to generate the freeform gradient in
    the RGB24 format
    """


type BackgroundType = Annotated[
    BackgroundTypeFill
    | BackgroundTypeWallpaper
    | BackgroundTypePattern
    | BackgroundTypeChatTheme,
    Field(discriminator="type"),
]


class BackgroundTypeFill(TelegramObject):
    """
    The background is automatically filled based on the selected colors.
    """

    type: Literal["fill"] = "fill"
    """
    Type of the background, always "fill"
    """

    fill: BackgroundFill
    """
    The background fill
    """

    dark_theme_dimming: int
    """
    Dimming of the background in dark themes, as a percentage; 0-100
    """


class BackgroundTypeWallpaper(TelegramObject):
    """
    The background is a wallpaper in the JPEG format.
    """

    type: Literal["wallpaper"] = "wallpaper"
    """
    Type of the background, always "wallpaper"
    """

    document: Document
    """
    Document with the wallpaper
    """

    dark_theme_dimming: int
    """
    Dimming of the background in dark themes, as a percentage; 0-100
    """

    is_blurred: bool | None = None
    """
    True, if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred
    with radius 12
    """

    is_moving: bool | None = None
    """
    True, if the background moves slightly when the device is tilted
    """


class BackgroundTypePattern(TelegramObject):
    """
    The background is a .PNG or .TGV (gzipped subset of SVG with MIME type
    "application/x-tgwallpattern") pattern to be combined with the background fill
    chosen by the user.
    """

    type: Literal["pattern"] = "pattern"
    """
    Type of the background, always "pattern"
    """

    document: Document
    """
    Document with the pattern
    """

    fill: BackgroundFill
    """
    The background fill that is combined with the pattern
    """

    intensity: int
    """
    Intensity of the pattern when it is shown above the filled background; 0-100
    """

    is_inverted: bool | None = None
    """
    True, if the background fill must be applied only to the pattern itself. All other
    pixels are black in this case. For dark themes only.
    """

    is_moving: bool | None = None
    """
    True, if the background moves slightly when the device is tilted
    """


class BackgroundTypeChatTheme(TelegramObject):
    """
    The background is taken directly from a built-in chat theme.
    """

    type: Literal["chat_theme"] = "chat_theme"
    """
    Type of the background, always "chat_theme"
    """

    theme_name: str
    """
    Name of the chat theme, which is usually an emoji
    """


class ChatBackground(TelegramObject):
    """
    This object represents a chat background.
    """

    type: BackgroundType
    """
    Type of the background
    """


class ChecklistTasksDone(TelegramObject):
    """
    Describes a service message about checklist tasks marked as done or not done.
    """

    checklist_message: Message | None = None
    """
    Message containing the checklist whose tasks were marked as done or not done. Note
    that the Message object in this field will not contain the reply_to_message field
    even if it itself is a reply.
    """

    marked_as_done_task_ids: list[int] | None = None
    """
    Identifiers of the tasks that were marked as done
    """

    marked_as_not_done_task_ids: list[int] | None = None
    """
    Identifiers of the tasks that were marked as not done
    """


class ChecklistTasksAdded(TelegramObject):
    """
    Describes a service message about tasks added to a checklist.
    """

    checklist_message: Message | None = None
    """
    Message containing the checklist to which the tasks were added. Note that the
    Message object in this field will not contain the reply_to_message field even if it
    itself is a reply.
    """

    tasks: list[ChecklistTask]
    """
    List of tasks added to the checklist
    """


class CommunityChatAdded(TelegramObject):
    """
    Describes a service message about a chat or a bot being added to a community.
    """

    community: Community
    """
    The new community to which the chat or the bot belongs
    """


class CommunityChatJoined(TelegramObject):
    """
    Describes a service message about a chat being joined by a user from a community.
    """

    community: Community
    """
    The community from which the chat was joined
    """


class CommunityChatRemoved(TelegramObject):
    """
    Describes a service message about a chat or a bot being removed from a community.
    Currently holds no information.
    """


class ForumTopicCreated(TelegramObject):
    """
    This object represents a service message about a new forum topic created in the
    chat.
    """

    name: str
    """
    Name of the topic
    """

    icon_color: int
    """
    Color of the topic icon in RGB format
    """

    icon_custom_emoji_id: str | None = None
    """
    Unique identifier of the custom emoji shown as the topic icon
    """

    is_name_implicit: bool | None = None
    """
    True, if the name of the topic wasn't specified explicitly by its creator and likely
    needs to be changed by the bot
    """


class ForumTopicClosed(TelegramObject):
    """
    This object represents a service message about a forum topic closed in the chat.
    Currently holds no information.
    """


class ForumTopicEdited(TelegramObject):
    """
    This object represents a service message about an edited forum topic.
    """

    name: str | None = None
    """
    New name of the topic, if it was edited
    """

    icon_custom_emoji_id: str | None = None
    """
    New identifier of the custom emoji shown as the topic icon, if it was edited; an
    empty string if the icon was removed
    """


class ForumTopicReopened(TelegramObject):
    """
    This object represents a service message about a forum topic reopened in the chat.
    Currently holds no information.
    """


class GeneralForumTopicHidden(TelegramObject):
    """
    This object represents a service message about General forum topic hidden in the
    chat. Currently holds no information.
    """


class GeneralForumTopicUnhidden(TelegramObject):
    """
    This object represents a service message about General forum topic unhidden in the
    chat. Currently holds no information.
    """


class SharedUser(TelegramObject):
    """
    This object contains information about a user that was shared with the bot using a
    KeyboardButtonRequestUsers button.
    """

    user_id: int
    """
    Identifier of the shared user. This number may have more than 32 significant bits
    and some programming languages may have difficulty/silent defects in interpreting
    it. But it has at most 52 significant bits, so 64-bit integers or double-precision
    float types are safe for storing these identifiers. The bot may not have access to
    the user and could be unable to use this identifier, unless the user is already
    known to the bot by some other means.
    """

    first_name: str | None = None
    """
    First name of the user, if the name was requested by the bot
    """

    last_name: str | None = None
    """
    Last name of the user, if the name was requested by the bot
    """

    username: str | None = None
    """
    Username of the user, if the username was requested by the bot
    """

    photo: list[PhotoSize] | None = None
    """
    Available sizes of the chat photo, if the photo was requested by the bot
    """


class UsersShared(TelegramObject):
    """
    This object contains information about the users whose identifiers were shared with
    the bot using a KeyboardButtonRequestUsers button.
    """

    request_id: int
    """
    Identifier of the request
    """

    users: list[SharedUser]
    """
    Information about users shared with the bot
    """


class ChatShared(TelegramObject):
    """
    This object contains information about a chat that was shared with the bot using a
    KeyboardButtonRequestChat button.
    """

    request_id: int
    """
    Identifier of the request
    """

    chat_id: int
    """
    Identifier of the shared chat. This number may have more than 32 significant bits
    and some programming languages may have difficulty/silent defects in interpreting
    it. But it has at most 52 significant bits, so a 64-bit integer or double-precision
    float type are safe for storing this identifier. The bot may not have access to the
    chat and could be unable to use this identifier, unless the chat is already known to
    the bot by some other means.
    """

    title: str | None = None
    """
    Title of the chat, if the title was requested by the bot
    """

    username: str | None = None
    """
    Username of the chat, if the username was requested by the bot and available
    """

    photo: list[PhotoSize] | None = None
    """
    Available sizes of the chat photo, if the photo was requested by the bot
    """


class WriteAccessAllowed(TelegramObject):
    """
    This object represents a service message about a user allowing a bot to write
    messages after adding it to the attachment menu, launching a Web App from a link, or
    accepting an explicit request from a Web App sent by the method requestWriteAccess.
    """

    from_request: bool | None = None
    """
    True, if the access was granted after the user accepted an explicit request from a
    Web App sent by the method requestWriteAccess
    """

    web_app_name: str | None = None
    """
    Name of the Web App, if the access was granted when the Web App was launched from a
    link
    """

    from_attachment_menu: bool | None = None
    """
    True, if the access was granted when the bot was added to the attachment or side
    menu
    """


class VideoChatScheduled(TelegramObject):
    """
    This object represents a service message about a video chat scheduled in the chat.
    """

    start_date: int
    """
    Point in time (Unix timestamp) when the video chat is supposed to be started by a
    chat administrator
    """


class VideoChatStarted(TelegramObject):
    """
    This object represents a service message about a video chat started in the chat.
    Currently holds no information.
    """


class VideoChatEnded(TelegramObject):
    """
    This object represents a service message about a video chat ended in the chat.
    """

    duration: int
    """
    Video chat duration in seconds
    """


class VideoChatParticipantsInvited(TelegramObject):
    """
    This object represents a service message about new members invited to a video chat.
    """

    users: list[User]
    """
    New members that were invited to the video chat
    """


class PaidMessagePriceChanged(TelegramObject):
    """
    Describes a service message about a change in the price of paid messages within a
    chat.
    """

    paid_message_star_count: int
    """
    The new number of Telegram Stars that must be paid by non-administrator users of the
    supergroup chat for each sent message
    """


class DirectMessagePriceChanged(TelegramObject):
    """
    Describes a service message about a change in the price of direct messages sent to a
    channel chat.
    """

    are_direct_messages_enabled: bool
    """
    True, if direct messages are enabled for the channel chat; False otherwise
    """

    direct_message_star_count: int | None = None
    """
    The new number of Telegram Stars that must be paid by users for each direct message
    sent to the channel. Does not apply to users who have been exempted by
    administrators. Defaults to 0.
    """


class SuggestedPostApproved(TelegramObject):
    """
    Describes a service message about the approval of a suggested post.
    """

    suggested_post_message: Message | None = None
    """
    Message containing the suggested post. Note that the Message object in this field
    will not contain the reply_to_message field even if it itself is a reply.
    """

    price: SuggestedPostPrice | None = None
    """
    Amount paid for the post
    """

    send_date: int
    """
    Date when the post will be published
    """


class SuggestedPostApprovalFailed(TelegramObject):
    """
    Describes a service message about the failed approval of a suggested post.
    Currently, only caused by insufficient user funds at the time of approval.
    """

    suggested_post_message: Message | None = None
    """
    Message containing the suggested post whose approval has failed. Note that the
    Message object in this field will not contain the reply_to_message field even if it
    itself is a reply.
    """

    price: SuggestedPostPrice
    """
    Expected price of the post
    """


class SuggestedPostDeclined(TelegramObject):
    """
    Describes a service message about the rejection of a suggested post.
    """

    suggested_post_message: Message | None = None
    """
    Message containing the suggested post. Note that the Message object in this field
    will not contain the reply_to_message field even if it itself is a reply.
    """

    comment: str | None = None
    """
    Comment with which the post was declined
    """


class SuggestedPostPaid(TelegramObject):
    """
    Describes a service message about a successful payment for a suggested post.
    """

    suggested_post_message: Message | None = None
    """
    Message containing the suggested post. Note that the Message object in this field
    will not contain the reply_to_message field even if it itself is a reply.
    """

    currency: str
    """
    Currency in which the payment was made. Currently, one of "XTR" for Telegram Stars
    or "TON" for TON grams.
    """

    amount: int | None = None
    """
    The amount of the currency that was received by the channel in nanograms; for
    payments in TON grams only
    """

    star_amount: StarAmount | None = None
    """
    The amount of Telegram Stars that was received by the channel; for payments in
    Telegram Stars only
    """


class SuggestedPostRefunded(TelegramObject):
    """
    Describes a service message about a payment refund for a suggested post.
    """

    suggested_post_message: Message | None = None
    """
    Message containing the suggested post. Note that the Message object in this field
    will not contain the reply_to_message field even if it itself is a reply.
    """

    reason: str
    """
    Reason for the refund. Currently, one of "post_deleted" if the post was deleted
    within 24 hours of being posted or removed from scheduled messages without being
    posted, or "payment_refunded" if the payer refunded their payment.
    """


class GiveawayCreated(TelegramObject):
    """
    This object represents a service message about the creation of a scheduled giveaway.
    """

    prize_star_count: int | None = None
    """
    The number of Telegram Stars to be split between giveaway winners; for Telegram Star
    giveaways only
    """


class Giveaway(TelegramObject):
    """
    This object represents a message about a scheduled giveaway.
    """

    chats: list[Chat]
    """
    The list of chats which the user must join to participate in the giveaway
    """

    winners_selection_date: int
    """
    Point in time (Unix timestamp) when winners of the giveaway will be selected
    """

    winner_count: int
    """
    The number of users which are supposed to be selected as winners of the giveaway
    """

    only_new_members: bool | None = None
    """
    True, if only users who join the chats after the giveaway started should be eligible
    to win
    """

    has_public_winners: bool | None = None
    """
    True, if the list of giveaway winners will be visible to everyone
    """

    prize_description: str | None = None
    """
    Description of additional giveaway prize
    """

    country_codes: list[str] | None = None
    """
    A list of two-letter ISO 3166-1 alpha-2 country codes indicating the countries from
    which eligible users for the giveaway must come. If empty, then all users can
    participate in the giveaway. Users with a phone number that was bought on Fragment
    can always participate in giveaways.
    """

    prize_star_count: int | None = None
    """
    The number of Telegram Stars to be split between giveaway winners; for Telegram Star
    giveaways only
    """

    premium_subscription_month_count: int | None = None
    """
    The number of months the Telegram Premium subscription won from the giveaway will be
    active for; for Telegram Premium giveaways only
    """


class GiveawayWinners(TelegramObject):
    """
    This object represents a message about the completion of a giveaway with public
    winners.
    """

    chat: Chat
    """
    The chat that created the giveaway
    """

    giveaway_message_id: int
    """
    Identifier of the message with the giveaway in the chat
    """

    winners_selection_date: int
    """
    Point in time (Unix timestamp) when winners of the giveaway were selected
    """

    winner_count: int
    """
    Total number of winners in the giveaway
    """

    winners: list[User]
    """
    List of up to 100 winners of the giveaway
    """

    additional_chat_count: int | None = None
    """
    The number of other chats the user had to join in order to be eligible for the
    giveaway
    """

    prize_star_count: int | None = None
    """
    The number of Telegram Stars that were split between giveaway winners; for Telegram
    Star giveaways only
    """

    premium_subscription_month_count: int | None = None
    """
    The number of months the Telegram Premium subscription won from the giveaway will be
    active for; for Telegram Premium giveaways only
    """

    unclaimed_prize_count: int | None = None
    """
    Number of undistributed prizes
    """

    only_new_members: bool | None = None
    """
    True, if only users who had joined the chats after the giveaway started were
    eligible to win
    """

    was_refunded: bool | None = None
    """
    True, if the giveaway was canceled because the payment for it was refunded
    """

    prize_description: str | None = None
    """
    Description of additional giveaway prize
    """


class GiveawayCompleted(TelegramObject):
    """
    This object represents a service message about the completion of a giveaway without
    public winners.
    """

    winner_count: int
    """
    Number of winners in the giveaway
    """

    unclaimed_prize_count: int | None = None
    """
    Number of undistributed prizes
    """

    giveaway_message: Message | None = None
    """
    Message with the giveaway that was completed, if it wasn't deleted
    """

    is_star_giveaway: bool | None = None
    """
    True, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the
    giveaway is a Telegram Premium giveaway.
    """


class LinkPreviewOptions(TelegramObject):
    """
    Describes the options used for link preview generation.
    """

    is_disabled: bool | None = None
    """
    True, if the link preview is disabled
    """

    url: str | None = None
    """
    URL to use for the link preview. If empty, then the first URL found in the message
    text will be used.
    """

    prefer_small_media: bool | None = None
    """
    True, if the media in the link preview is supposed to be shrunk; ignored if the URL
    isn't explicitly specified or media size change isn't supported for the preview
    """

    prefer_large_media: bool | None = None
    """
    True, if the media in the link preview is supposed to be enlarged; ignored if the
    URL isn't explicitly specified or media size change isn't supported for the preview
    """

    show_above_text: bool | None = None
    """
    True, if the link preview must be shown above the message text; otherwise, the link
    preview will be shown below the message text
    """


class SuggestedPostPrice(TelegramObject):
    """
    Describes the price of a suggested post.
    """

    currency: str
    """
    Currency in which the post will be paid. Currently, must be one of "XTR" for
    Telegram Stars or "TON" for TON grams.
    """

    amount: int
    """
    The amount of the currency that will be paid for the post in the smallest units of
    the currency, i.e. Telegram Stars or nanograms. Currently, price in Telegram Stars
    must be between 5 and 100000, and price in nanograms must be between 10000000 and
    10000000000000.
    """


class SuggestedPostInfo(TelegramObject):
    """
    Contains information about a suggested post.
    """

    state: str
    """
    State of the suggested post. Currently, it can be one of "pending", "approved",
    "declined".
    """

    price: SuggestedPostPrice | None = None
    """
    Proposed price of the post. If the field is omitted, then the post is unpaid.
    """

    send_date: int | None = None
    """
    Proposed send date of the post. If the field is omitted, then the post can be
    published at any time within 30 days at the sole discretion of the user or
    administrator who approves it.
    """


class SuggestedPostParameters(TelegramObject):
    """
    Contains parameters of a post that is being suggested by the bot.
    """

    price: SuggestedPostPrice | None = None
    """
    Proposed price for the post. If the field is omitted, then the post is unpaid.
    """

    send_date: int | None = None
    """
    Proposed send date of the post. If specified, then the date must be between 300
    second and 2678400 seconds (30 days) in the future. If the field is omitted, then
    the post can be published at any time within 30 days at the sole discretion of the
    user who approves it.
    """


class DirectMessagesTopic(TelegramObject):
    """
    Describes a topic of a direct messages chat.
    """

    topic_id: int
    """
    Unique identifier of the topic. This number may have more than 32 significant bits
    and some programming languages may have difficulty/silent defects in interpreting
    it. But it has at most 52 significant bits, so a 64-bit integer or double-precision
    float type are safe for storing this identifier.
    """

    user: User | None = None
    """
    Information about the user that created the topic. Currently, it is always present.
    """


class UserProfilePhotos(TelegramObject):
    """
    This object represent a user's profile pictures.
    """

    total_count: int
    """
    Total number of profile pictures the target user has
    """

    photos: list[list[PhotoSize]]
    """
    Requested profile pictures (in up to 4 sizes each)
    """


class UserProfileAudios(TelegramObject):
    """
    This object represents the audios displayed on a user's profile.
    """

    total_count: int
    """
    Total number of profile audios for the target user
    """

    audios: list[Audio]
    """
    Requested profile audios
    """


class File(TelegramObject):
    """
    This object represents a file ready to be downloaded. The file can be downloaded via
    the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that
    the link will be valid for at least 1 hour. When the link expires, a new one can be
    requested by calling getFile.
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """

    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    """

    file_size: int | None = None
    """
    File size in bytes. It can be bigger than 2^31 and some programming languages may
    have difficulty/silent defects in interpreting it. But it has at most 52 significant
    bits, so a signed 64-bit integer or double-precision float type are safe for storing
    this value.
    """

    file_path: str | None = None
    """
    File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.
    """


class WebAppInfo(TelegramObject):
    """
    Describes a Web App.
    """

    url: str
    """
    An HTTPS URL of a Web App to be opened with additional data as specified in
    Initializing Web Apps
    """


class ReplyKeyboardMarkup(TelegramObject):
    """
    This object represents a custom keyboard with reply options (see Introduction to
    bots for details and examples). Not supported in channels and for messages sent on
    behalf of a business account.
    """

    keyboard: list[list[KeyboardButton]]
    """
    Array of button rows, each represented by an Array of KeyboardButton objects
    """

    is_persistent: bool | None = None
    """
    Requests clients to always show the keyboard when the regular keyboard is hidden.
    Defaults to False, in which case the custom keyboard can be hidden and opened with a
    keyboard icon.
    """

    resize_keyboard: bool | None = None
    """
    Requests clients to resize the keyboard vertically for optimal fit (e.g., make the
    keyboard smaller if there are just two rows of buttons). Defaults to False, in which
    case the custom keyboard is always of the same height as the app's standard
    keyboard.
    """

    one_time_keyboard: bool | None = None
    """
    Requests clients to hide the keyboard as soon as it's been used. The keyboard will
    still be available, but clients will automatically display the usual letter-keyboard
    in the chat - the user can press a special button in the input field to see the
    custom keyboard again. Defaults to False.
    """

    input_field_placeholder: str | None = None
    """
    The placeholder to be shown in the input field when the keyboard is active; 1-64
    characters
    """

    selective: bool | None = None
    """
    Use this parameter if you want to show the keyboard to specific users only. Targets:
    1) users that are @mentioned in the text of the Message object; 2) if the bot's
    message is a reply to a message in the same chat and forum topic, sender of the
    original message. Example: A user requests to change the bot's language, bot replies
    to the request with a keyboard to select the new language. Other users in the group
    don't see the keyboard.
    """

    force_reply: bool | None = None
    """
    Pass True if the reply interface must be shown to the user, as if they had manually
    selected the bot's message and tapped 'Reply'
    """


class KeyboardButton(TelegramObject):
    """
    This object represents one button of the reply keyboard. At most one of the fields
    other than text, icon_custom_emoji_id, and style must be used to specify the type of
    the button. For simple text buttons, String can be used instead of this object to
    specify the button text.
    """

    text: str
    """
    Text of the button. If none of the fields other than text, icon_custom_emoji_id, and
    style are used, it will be sent as a message when the button is pressed.
    """

    icon_custom_emoji_id: str | None = None
    """
    Unique identifier of the custom emoji shown before the text of the button. Can only
    be used by bots that purchased additional usernames on Fragment or in the messages
    directly sent by the bot to private, group and supergroup chats if the owner of the
    bot has a Telegram Premium subscription.
    """

    style: str | None = None
    """
    Style of the button. Must be one of "danger" (red), "success" (green) or "primary"
    (blue). If omitted, then an app-specific style is used.
    """

    request_users: KeyboardButtonRequestUsers | None = None
    """
    If specified, pressing the button will open a list of suitable users. Identifiers of
    selected users will be sent to the bot in a "users_shared" service message.
    Available in private chats only.
    """

    request_chat: KeyboardButtonRequestChat | None = None
    """
    If specified, pressing the button will open a list of suitable chats. Tapping on a
    chat will send its identifier to the bot in a "chat_shared" service message.
    Available in private chats only.
    """

    request_managed_bot: KeyboardButtonRequestManagedBot | None = None
    """
    If specified, pressing the button will ask the user to create and share a bot that
    will be managed by the current bot. Available for bots that enabled management of
    other bots in the @BotFather Mini App. Available in private chats only.
    """

    request_contact: bool | None = None
    """
    If True, the user's phone number will be sent as a contact when the button is
    pressed. Available in private chats only.
    """

    request_location: bool | None = None
    """
    If True, the user's current location will be sent when the button is pressed.
    Available in private chats only.
    """

    request_poll: KeyboardButtonPollType | None = None
    """
    If specified, the user will be asked to create a poll and send it to the bot when
    the button is pressed. Available in private chats only.
    """

    web_app: WebAppInfo | None = None
    """
    If specified, the described Web App will be launched when the button is pressed. The
    Web App will be able to send a "web_app_data" service message. Available in private
    chats only.
    """


class KeyboardButtonRequestUsers(TelegramObject):
    """
    This object defines the criteria used to request suitable users. Information about
    the selected users will be shared with the bot when the corresponding button is
    pressed. More about requesting users: https://core.telegram.org/bots/features#chat-
    and-user-selection
    """

    request_id: int
    """
    Signed 32-bit identifier of the request that will be received back in the
    UsersShared object. Must be unique within the message.
    """

    user_is_bot: bool | None = None
    """
    Pass True to request bots, pass False to request regular users. If not specified, no
    additional restrictions are applied.
    """

    user_is_premium: bool | None = None
    """
    Pass True to request premium users, pass False to request non-premium users. If not
    specified, no additional restrictions are applied.
    """

    max_quantity: int | None = None
    """
    The maximum number of users to be selected; 1-10. Defaults to 1.
    """

    request_name: bool | None = None
    """
    Pass True to request the users' first and last names
    """

    request_username: bool | None = None
    """
    Pass True to request the users' usernames
    """

    request_photo: bool | None = None
    """
    Pass True to request the users' photos
    """


class KeyboardButtonRequestChat(TelegramObject):
    """
    This object defines the criteria used to request a suitable chat. Information about
    the selected chat will be shared with the bot when the corresponding button is
    pressed. The bot will be granted requested rights in the chat if appropriate. More
    about requesting chats: https://core.telegram.org/bots/features#chat-and-user-
    selection.
    """

    request_id: int
    """
    Signed 32-bit identifier of the request, which will be received back in the
    ChatShared object. Must be unique within the message.
    """

    chat_is_channel: bool
    """
    Pass True to request a channel chat, pass False to request a group or a supergroup
    chat
    """

    chat_is_forum: bool | None = None
    """
    Pass True to request a forum supergroup, pass False to request a non-forum chat. If
    not specified, no additional restrictions are applied.
    """

    chat_has_username: bool | None = None
    """
    Pass True to request a supergroup or a channel with a username, pass False to
    request a chat without a username. If not specified, no additional restrictions are
    applied.
    """

    chat_is_created: bool | None = None
    """
    Pass True to request a chat owned by the user. Otherwise, no additional restrictions
    are applied.
    """

    user_administrator_rights: ChatAdministratorRights | None = None
    """
    A JSON-serialized object listing the required administrator rights of the user in
    the chat. The rights must be a superset of bot_administrator_rights. If not
    specified, no additional restrictions are applied.
    """

    bot_administrator_rights: ChatAdministratorRights | None = None
    """
    A JSON-serialized object listing the required administrator rights of the bot in the
    chat. The rights must be a subset of user_administrator_rights. If not specified, no
    additional restrictions are applied.
    """

    bot_is_member: bool | None = None
    """
    Pass True to request a chat with the bot as a member. Otherwise, no additional
    restrictions are applied.
    """

    request_title: bool | None = None
    """
    Pass True to request the chat's title
    """

    request_username: bool | None = None
    """
    Pass True to request the chat's username
    """

    request_photo: bool | None = None
    """
    Pass True to request the chat's photo
    """


class KeyboardButtonRequestManagedBot(TelegramObject):
    """
    This object defines the parameters for the creation of a managed bot. Information
    about the created bot will be shared with the bot using the update managed_bot and a
    Message with the field managed_bot_created.
    """

    request_id: int
    """
    Signed 32-bit identifier of the request. Must be unique within the message.
    """

    suggested_name: str | None = None
    """
    Suggested name for the bot
    """

    suggested_username: str | None = None
    """
    Suggested username for the bot
    """


class KeyboardButtonPollType(TelegramObject):
    """
    This object represents type of a poll, which is allowed to be created and sent when
    the corresponding button is pressed.
    """

    type: str | None = None
    """
    If quiz is passed, the user will be allowed to create only polls in the quiz mode.
    If regular is passed, only regular polls will be allowed. Otherwise, the user will
    be allowed to create a poll of any type.
    """


class ReplyKeyboardRemove(TelegramObject):
    """
    Upon receiving a message with this object, Telegram clients will remove the current
    custom keyboard and display the default letter-keyboard. By default, custom
    keyboards are displayed until a new keyboard is sent by a bot. An exception is made
    for one-time keyboards that are hidden immediately after the user presses a button
    (see ReplyKeyboardMarkup). Not supported in channels and for messages sent on behalf
    of a business account.
    """

    remove_keyboard: bool
    """
    Requests clients to remove the custom keyboard (user will not be able to summon this
    keyboard; if you want to hide the keyboard from sight but keep it accessible, use
    one_time_keyboard in ReplyKeyboardMarkup)
    """

    selective: bool | None = None
    """
    Use this parameter if you want to remove the keyboard for specific users only.
    Targets: 1) users that are @mentioned in the text of the Message object; 2) if the
    bot's message is a reply to a message in the same chat and forum topic, sender of
    the original message. Example: A user votes in a poll, bot returns confirmation
    message in reply to the vote and removes the keyboard for that user, while still
    showing the keyboard with poll options to users who haven't voted yet.
    """


class InlineKeyboardMarkup(TelegramObject):
    """
    This object represents an inline keyboard that appears right next to the message it
    belongs to.
    """

    inline_keyboard: list[list[InlineKeyboardButton]]
    """
    Array of button rows, each represented by an Array of InlineKeyboardButton objects
    """

    force_reply: bool | None = None
    """
    Pass True if the reply interface must be shown to the user, as if they had manually
    selected the bot's message and tapped 'Reply'. The value of the field can't be
    changed when the inline keyboard is edited.
    """


class InlineKeyboardButton(TelegramObject):
    """
    This object represents one button of an inline keyboard. Exactly one of the fields
    other than text, icon_custom_emoji_id, and style must be used to specify the type of
    the button.
    """

    text: str
    """
    Label text on the button
    """

    icon_custom_emoji_id: str | None = None
    """
    Unique identifier of the custom emoji shown before the text of the button. Can only
    be used by bots that purchased additional usernames on Fragment or in the messages
    directly sent by the bot to private, group and supergroup chats if the owner of the
    bot has a Telegram Premium subscription.
    """

    style: str | None = None
    """
    Style of the button. Must be one of "danger" (red), "success" (green) or "primary"
    (blue). If omitted, then an app-specific style is used.
    """

    url: str | None = None
    """
    HTTP or tg:// URL to be opened when the button is pressed. Links
    tg://user?id=<user_id> can be used to mention a user by their identifier without
    using a username, if this is allowed by their privacy settings.
    """

    callback_data: str | None = None
    """
    Data to be sent in a callback query to the bot when the button is pressed, 1-64
    bytes
    """

    web_app: WebAppInfo | None = None
    """
    Description of the Web App that will be launched when the user presses the button.
    The Web App will be able to send an arbitrary message on behalf of the user using
    the method answerWebAppQuery. Available only in private chats between a user and the
    bot. Not supported for messages sent on behalf of a business account.
    """

    login_url: LoginUrl | None = None
    """
    An HTTPS URL used to automatically authorize the user. Can be used as a replacement
    for the Telegram Login Widget. Not supported for ephemeral messages.
    """

    switch_inline_query: str | None = None
    """
    If set, pressing the button will prompt the user to select one of their chats, open
    that chat and insert the bot's username and the specified inline query in the input
    field. May be empty, in which case just the bot's username will be inserted. Not
    supported for messages sent in channel direct messages chats and on behalf of a
    business account.
    """

    switch_inline_query_current_chat: str | None = None
    """
    If set, pressing the button will insert the bot's username and the specified inline
    query in the current chat's input field. May be empty, in which case only the bot's
    username will be inserted. This offers a quick way for the user to open your bot in
    inline mode in the same chat - good for selecting something from multiple options.
    Not supported in channels and for messages sent in channel direct messages chats and
    on behalf of a business account.
    """

    switch_inline_query_chosen_chat: SwitchInlineQueryChosenChat | None = None
    """
    If set, pressing the button will prompt the user to select one of their chats of the
    specified type, open that chat and insert the bot's username and the specified
    inline query in the input field. Not supported for messages sent in channel direct
    messages chats and on behalf of a business account.
    """

    copy_text: CopyTextButton | None = None
    """
    Description of the button that copies the specified text to the clipboard
    """

    callback_game: CallbackGame | None = None
    """
    Description of the game that will be launched when the user presses the button.
    NOTE: This type of button must always be the first button in the first row.
    """

    pay: bool | None = None
    """
    Specify True, to send a Pay button. Substrings "⭐" and "XTR" in the buttons's text
    will be replaced with a Telegram Star icon. NOTE: This type of button must always be
    the first button in the first row and can only be used in invoice messages.
    """

    disabled: DisabledButton | None = None
    """
    If set, then the button is disabled and does nothing
    """


class LoginUrl(TelegramObject):
    """
    This object represents a parameter of the inline keyboard button used to
    automatically authorize a user. It serves as a great replacement for the Telegram
    Login Widget when the user is coming from Telegram. All the user needs to do is
    tap/click a button and confirm that they want to log in:
    """

    url: str
    """
    An HTTPS URL to be opened with user authorization data added to the query string
    when the button is pressed. If the user refuses to provide authorization data, the
    original URL without information about the user will be opened. The data added is
    the same as described in Receiving authorization data. NOTE: You must always check
    the hash of the received data to verify the authentication and the integrity of the
    data as described in Checking authorization.
    """

    forward_text: str | None = None
    """
    New text of the button in forwarded messages
    """

    bot_username: str | None = None
    """
    Username of a bot, which will be used for user authorization; not supported in
    RichMessageButton. See Setting up a bot for more details. If not specified, the
    current bot's username will be assumed. The url's domain must be the same as the
    domain linked with the bot. See Linking your domain to the bot for more details.
    """

    request_write_access: bool | None = None
    """
    Pass True to request the permission for your bot to send messages to the user
    """


class SwitchInlineQueryChosenChat(TelegramObject):
    """
    This object represents an inline button that switches the current user to inline
    mode in a chosen chat, with an optional default inline query.
    """

    query: str | None = None
    """
    The default inline query to be inserted in the input field. If left empty, only the
    bot's username will be inserted.
    """

    allow_user_chats: bool | None = None
    """
    True, if private chats with users can be chosen
    """

    allow_bot_chats: bool | None = None
    """
    True, if private chats with bots can be chosen
    """

    allow_group_chats: bool | None = None
    """
    True, if group and supergroup chats can be chosen
    """

    allow_channel_chats: bool | None = None
    """
    True, if channel chats can be chosen
    """


class CopyTextButton(TelegramObject):
    """
    This object represents an inline keyboard button that copies specified text to the
    clipboard.
    """

    text: str
    """
    The text to be copied to the clipboard; 1-256 characters
    """


class DisabledButton(TelegramObject):
    """
    This object represents a disabled button which does nothing. Currently holds no
    information.
    """


class CallbackQuery(TelegramObject):
    """
    This object represents an incoming callback query from a callback button in an
    inline keyboard. If the button that originated the query was attached to a message
    sent by the bot, the field message will be present. If the button was attached to a
    message sent via the bot (in inline mode), the field inline_message_id will be
    present. Exactly one of the fields data or game_short_name will be present.
    """

    id: str
    """
    Unique identifier for this query
    """

    from_: User = Field(alias="from")
    """
    Sender
    """

    message: MaybeInaccessibleMessage | None = None
    """
    Message sent by the bot with the callback button that originated the query
    """

    inline_message_id: str | None = None
    """
    Identifier of the message sent via the bot in inline mode, that originated the query
    """

    chat_instance: str
    """
    Global identifier, uniquely corresponding to the chat to which the message with the
    callback button was sent. Useful for high scores in games.
    """

    data: str | None = None
    """
    Data associated with the callback button. Be aware that the message originated the
    query can contain no callback buttons with this data.
    """

    game_short_name: str | None = None
    """
    Short name of a Game to be returned, serves as the unique identifier for the game
    """


class ForceReply(TelegramObject):
    """
    Upon receiving a message with this object, Telegram clients will display a reply
    interface to the user (act as if the user has selected the bot's message and tapped
    'Reply'). This can be extremely useful if you want to create user-friendly step-by-
    step interfaces without having to sacrifice privacy mode. Not supported in channels
    and for messages sent on behalf of a user account.
    """

    force_reply: bool
    """
    Shows reply interface to the user, as if they had manually selected the bot's
    message and tapped 'Reply'
    """

    input_field_placeholder: str | None = None
    """
    The placeholder to be shown in the input field when the reply is active; 1-64
    characters
    """

    selective: bool | None = None
    """
    Use this parameter if you want to force reply from specific users only. Targets: 1)
    users that are @mentioned in the text of the Message object; 2) if the bot's message
    is a reply to a message in the same chat and forum topic, sender of the original
    message.
    """


class Community(TelegramObject):
    """
    Represents a community (a group of chats).
    """

    id: int
    """
    Unique identifier for this community. This number may have more than 32 significant
    bits and some programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer
    or double-precision float type are safe for storing this identifier.
    """

    name: str
    """
    Name of the community
    """


class ChatPhoto(TelegramObject):
    """
    This object represents a chat photo.
    """

    small_file_id: str
    """
    File identifier of small (160x160) chat photo. This file_id can be used only for
    photo download and only for as long as the photo is not changed.
    """

    small_file_unique_id: str
    """
    Unique file identifier of small (160x160) chat photo, which is supposed to be the
    same over time and for different bots. Can't be used to download or reuse the file.
    """

    big_file_id: str
    """
    File identifier of big (640x640) chat photo. This file_id can be used only for photo
    download and only for as long as the photo is not changed.
    """

    big_file_unique_id: str
    """
    Unique file identifier of big (640x640) chat photo, which is supposed to be the same
    over time and for different bots. Can't be used to download or reuse the file.
    """


class ChatInviteLink(TelegramObject):
    """
    Represents an invite link for a chat.
    """

    invite_link: str
    """
    The invite link. If the link was created by another chat administrator, then the
    second part of the link will be replaced with "...".
    """

    creator: User
    """
    Creator of the link
    """

    creates_join_request: bool
    """
    True, if users joining the chat via the link need to be approved by chat
    administrators
    """

    is_primary: bool
    """
    True, if the link is primary
    """

    is_revoked: bool
    """
    True, if the link is revoked
    """

    name: str | None = None
    """
    Invite link name
    """

    expire_date: int | None = None
    """
    Point in time (Unix timestamp) when the link will expire or has been expired
    """

    member_limit: int | None = None
    """
    The maximum number of users that can be members of the chat simultaneously after
    joining the chat via this invite link; 1-99999
    """

    pending_join_request_count: int | None = None
    """
    Number of pending join requests created using this link
    """

    subscription_period: int | None = None
    """
    The number of seconds the subscription will be active for before the next payment
    """

    subscription_price: int | None = None
    """
    The amount of Telegram Stars a user must pay initially and after each subsequent
    subscription period to be a member of the chat using the link
    """


class ChatAdministratorRights(TelegramObject):
    """
    Represents the rights of an administrator in a chat.
    """

    is_anonymous: bool
    """
    True, if the user's presence in the chat is hidden
    """

    can_manage_chat: bool
    """
    True, if the administrator can access the chat event log, get boost list, see hidden
    supergroup and channel members, report spam messages, ignore slow mode, and send
    messages to the chat without paying Telegram Stars. Implied by any other
    administrator privilege.
    """

    can_delete_messages: bool
    """
    True, if the administrator can delete messages of other users
    """

    can_manage_video_chats: bool
    """
    True, if the administrator can manage video chats
    """

    can_restrict_members: bool
    """
    True, if the administrator can restrict, ban or unban chat members, or access
    supergroup statistics
    """

    can_promote_members: bool
    """
    True, if the administrator can add new administrators with a subset of their own
    privileges or demote administrators that they have promoted, directly or indirectly
    (promoted by administrators that were appointed by the user)
    """

    can_change_info: bool
    """
    True, if the user is allowed to change the chat title, photo and other settings
    """

    can_invite_users: bool
    """
    True, if the user is allowed to invite new users to the chat
    """

    can_post_stories: bool
    """
    True, if the administrator can post stories to the chat
    """

    can_edit_stories: bool
    """
    True, if the administrator can edit stories posted by other users, post stories to
    the chat page, pin chat stories, and access the chat's story archive
    """

    can_delete_stories: bool
    """
    True, if the administrator can delete stories posted by other users
    """

    can_post_messages: bool | None = None
    """
    True, if the administrator can post messages in the channel, approve suggested
    posts, or access channel statistics; for channels only
    """

    can_edit_messages: bool | None = None
    """
    True, if the administrator can edit messages of other users and can pin messages;
    for channels only
    """

    can_pin_messages: bool | None = None
    """
    True, if the user is allowed to pin messages; for groups and supergroups only
    """

    can_manage_topics: bool | None = None
    """
    True, if the user is allowed to create, rename, close, and reopen forum topics; for
    supergroups only
    """

    can_manage_direct_messages: bool | None = None
    """
    True, if the administrator can manage direct messages of the channel and decline
    suggested posts; for channels only
    """

    can_manage_tags: bool | None = None
    """
    True, if the administrator can edit the tags of regular members; for groups and
    supergroups only
    """

    can_send_welcome_messages: bool
    """
    True, if the administrator can manage chat welcome messages or directly send them in
    the case of bots
    """


class ChatMemberUpdated(TelegramObject):
    """
    This object represents changes in the status of a chat member.
    """

    chat: Chat
    """
    Chat the user belongs to
    """

    from_: User = Field(alias="from")
    """
    Performer of the action, which resulted in the change
    """

    date: int
    """
    Date the change was done in Unix time
    """

    old_chat_member: ChatMember
    """
    Previous information about the chat member
    """

    new_chat_member: ChatMember
    """
    New information about the chat member
    """

    invite_link: ChatInviteLink | None = None
    """
    Chat invite link, which was used by the user to join the chat; for joining by invite
    link events only
    """

    via_join_request: bool | None = None
    """
    True, if the user joined the chat after sending a direct join request without using
    an invite link and being approved by an administrator
    """

    via_chat_folder_invite_link: bool | None = None
    """
    True, if the user joined the chat via a chat folder invite link
    """


type ChatMember = Annotated[
    ChatMemberOwner
    | ChatMemberAdministrator
    | ChatMemberMember
    | ChatMemberRestricted
    | ChatMemberLeft
    | ChatMemberBanned,
    Field(discriminator="status"),
]


class ChatMemberOwner(TelegramObject):
    """
    Represents a chat member that owns the chat and has all administrator privileges.
    """

    status: Literal["creator"] = "creator"
    """
    The member's status in the chat, always "creator"
    """

    user: User
    """
    Information about the user
    """

    is_anonymous: bool
    """
    True, if the user's presence in the chat is hidden
    """

    custom_title: str | None = None
    """
    Custom title for this user
    """


class ChatMemberAdministrator(TelegramObject):
    """
    Represents a chat member that has some additional privileges.
    """

    status: Literal["administrator"] = "administrator"
    """
    The member's status in the chat, always "administrator"
    """

    user: User
    """
    Information about the user
    """

    can_be_edited: bool
    """
    True, if the bot is allowed to edit administrator privileges of that user
    """

    is_anonymous: bool
    """
    True, if the user's presence in the chat is hidden
    """

    can_manage_chat: bool
    """
    True, if the administrator can access the chat event log, get boost list, see hidden
    supergroup and channel members, report spam messages, ignore slow mode, and send
    messages to the chat without paying Telegram Stars. Implied by any other
    administrator privilege.
    """

    can_delete_messages: bool
    """
    True, if the administrator can delete messages of other users
    """

    can_manage_video_chats: bool
    """
    True, if the administrator can manage video chats
    """

    can_restrict_members: bool
    """
    True, if the administrator can restrict, ban or unban chat members, or access
    supergroup statistics
    """

    can_promote_members: bool
    """
    True, if the administrator can add new administrators with a subset of their own
    privileges or demote administrators that they have promoted, directly or indirectly
    (promoted by administrators that were appointed by the user)
    """

    can_change_info: bool
    """
    True, if the user is allowed to change the chat title, photo and other settings
    """

    can_invite_users: bool
    """
    True, if the user is allowed to invite new users to the chat
    """

    can_post_stories: bool
    """
    True, if the administrator can post stories to the chat
    """

    can_edit_stories: bool
    """
    True, if the administrator can edit stories posted by other users, post stories to
    the chat page, pin chat stories, and access the chat's story archive
    """

    can_delete_stories: bool
    """
    True, if the administrator can delete stories posted by other users
    """

    can_post_messages: bool | None = None
    """
    True, if the administrator can post messages in the channel, approve suggested
    posts, or access channel statistics; for channels only
    """

    can_edit_messages: bool | None = None
    """
    True, if the administrator can edit messages of other users and can pin messages;
    for channels only
    """

    can_pin_messages: bool | None = None
    """
    True, if the user is allowed to pin messages; for groups and supergroups only
    """

    can_manage_topics: bool | None = None
    """
    True, if the user is allowed to create, rename, close, and reopen forum topics; for
    supergroups only
    """

    can_manage_direct_messages: bool | None = None
    """
    True, if the administrator can manage direct messages of the channel and decline
    suggested posts; for channels only
    """

    can_manage_tags: bool | None = None
    """
    True, if the administrator can edit the tags of regular members; for groups and
    supergroups only
    """

    can_send_welcome_messages: bool
    """
    True, if the administrator can manage chat welcome messages or directly send them in
    the case of bots
    """

    custom_title: str | None = None
    """
    Custom title for this user
    """


class ChatMemberMember(TelegramObject):
    """
    Represents a chat member that has no additional privileges or restrictions.
    """

    status: Literal["member"] = "member"
    """
    The member's status in the chat, always "member"
    """

    tag: str | None = None
    """
    Tag of the member
    """

    user: User
    """
    Information about the user
    """

    until_date: int | None = None
    """
    Date when the user's subscription will expire; Unix time
    """


class ChatMemberRestricted(TelegramObject):
    """
    Represents a chat member that is under certain restrictions in the chat. Supergroups
    only.
    """

    status: Literal["restricted"] = "restricted"
    """
    The member's status in the chat, always "restricted"
    """

    tag: str | None = None
    """
    Tag of the member
    """

    user: User
    """
    Information about the user
    """

    is_member: bool
    """
    True, if the user is a member of the chat at the moment of the request
    """

    can_send_messages: bool
    """
    True, if the user is allowed to send text messages, rich messages, contacts,
    giveaways, giveaway winners, invoices, locations and venues
    """

    can_send_audios: bool
    """
    True, if the user is allowed to send audios
    """

    can_send_documents: bool
    """
    True, if the user is allowed to send documents
    """

    can_send_photos: bool
    """
    True, if the user is allowed to send photos
    """

    can_send_videos: bool
    """
    True, if the user is allowed to send videos
    """

    can_send_video_notes: bool
    """
    True, if the user is allowed to send video notes
    """

    can_send_voice_notes: bool
    """
    True, if the user is allowed to send voice notes
    """

    can_send_polls: bool
    """
    True, if the user is allowed to send polls and checklists
    """

    can_send_other_messages: bool
    """
    True, if the user is allowed to send animations, games, stickers and use inline bots
    """

    can_add_web_page_previews: bool
    """
    True, if the user is allowed to add web page previews to their messages
    """

    can_react_to_messages: bool
    """
    True, if the user is allowed to react to messages
    """

    can_edit_tag: bool
    """
    True, if the user is allowed to edit their own tag
    """

    can_change_info: bool
    """
    True, if the user is allowed to change the chat title, photo and other settings
    """

    can_invite_users: bool
    """
    True, if the user is allowed to invite new users to the chat
    """

    can_pin_messages: bool
    """
    True, if the user is allowed to pin messages
    """

    can_manage_topics: bool
    """
    True, if the user is allowed to create forum topics
    """

    until_date: int
    """
    Date when restrictions will be lifted for this user; Unix time. If 0, then the user
    is restricted forever.
    """


class ChatMemberLeft(TelegramObject):
    """
    Represents a chat member that isn't currently a member of the chat, but may join it
    themselves.
    """

    status: Literal["left"] = "left"
    """
    The member's status in the chat, always "left"
    """

    user: User
    """
    Information about the user
    """


class ChatMemberBanned(TelegramObject):
    """
    Represents a chat member that was banned in the chat and can't return to the chat or
    view chat messages.
    """

    status: Literal["kicked"] = "kicked"
    """
    The member's status in the chat, always "kicked"
    """

    user: User
    """
    Information about the user
    """

    until_date: int
    """
    Date when restrictions will be lifted for this user; Unix time. If 0, then the user
    is banned forever.
    """


class ChatJoinRequest(TelegramObject):
    """
    Represents a join request sent to a chat.
    """

    chat: Chat
    """
    Chat to which the request was sent
    """

    from_: User = Field(alias="from")
    """
    User that sent the join request
    """

    user_chat_id: int
    """
    Identifier of a private chat with the user who sent the join request. This number
    may have more than 32 significant bits and some programming languages may have
    difficulty/silent defects in interpreting it. But it has at most 52 significant
    bits, so a 64-bit integer or double-precision float type are safe for storing this
    identifier. The bot can use this identifier for 5 minutes to send messages until the
    join request is processed, assuming no other administrator contacted the user.
    """

    date: int
    """
    Date the request was sent in Unix time
    """

    bio: str | None = None
    """
    Bio of the user
    """

    invite_link: ChatInviteLink | None = None
    """
    Chat invite link that was used by the user to send the join request
    """

    query_id: str | None = None
    """
    Identifier of the join request query; for bots assigned to process join requests
    only. If present, then the bot must call sendChatJoinRequestWebApp or directly call
    answerChatJoinRequestQuery within 10 seconds.
    """


class ChatPermissions(TelegramObject):
    """
    Describes actions that a non-administrator user is allowed to take in a chat.
    """

    can_send_messages: bool | None = None
    """
    True, if the user is allowed to send text messages, rich messages, contacts,
    giveaways, giveaway winners, invoices, locations and venues
    """

    can_send_audios: bool | None = None
    """
    True, if the user is allowed to send audios
    """

    can_send_documents: bool | None = None
    """
    True, if the user is allowed to send documents
    """

    can_send_photos: bool | None = None
    """
    True, if the user is allowed to send photos
    """

    can_send_videos: bool | None = None
    """
    True, if the user is allowed to send videos
    """

    can_send_video_notes: bool | None = None
    """
    True, if the user is allowed to send video notes
    """

    can_send_voice_notes: bool | None = None
    """
    True, if the user is allowed to send voice notes
    """

    can_send_polls: bool | None = None
    """
    True, if the user is allowed to send polls and checklists
    """

    can_send_other_messages: bool | None = None
    """
    True, if the user is allowed to send animations, games, stickers and use inline bots
    """

    can_add_web_page_previews: bool | None = None
    """
    True, if the user is allowed to add web page previews to their messages
    """

    can_react_to_messages: bool | None = None
    """
    True, if the user is allowed to react to messages. If omitted, defaults to the value
    of can_send_messages.
    """

    can_edit_tag: bool | None = None
    """
    True, if the user is allowed to edit their own tag. If omitted, defaults to the
    value of can_pin_messages.
    """

    can_change_info: bool | None = None
    """
    True, if the user is allowed to change the chat title, photo and other settings.
    Ignored in public supergroups.
    """

    can_invite_users: bool | None = None
    """
    True, if the user is allowed to invite new users to the chat
    """

    can_pin_messages: bool | None = None
    """
    True, if the user is allowed to pin messages. Ignored in public supergroups.
    """

    can_manage_topics: bool | None = None
    """
    True, if the user is allowed to create forum topics. If omitted, defaults to the
    value of can_pin_messages.
    """


class Birthdate(TelegramObject):
    """
    Describes the birthdate of a user.
    """

    day: int
    """
    Day of the user's birth; 1-31
    """

    month: int
    """
    Month of the user's birth; 1-12
    """

    year: int | None = None
    """
    Year of the user's birth
    """


class BusinessIntro(TelegramObject):
    """
    Contains information about the start page settings of a Telegram Business account.
    """

    title: str | None = None
    """
    Title text of the business intro
    """

    message: str | None = None
    """
    Message text of the business intro
    """

    sticker: Sticker | None = None
    """
    Sticker of the business intro
    """


class BusinessLocation(TelegramObject):
    """
    Contains information about the location of a Telegram Business account.
    """

    address: str
    """
    Address of the business
    """

    location: Location | None = None
    """
    Location of the business
    """


class BusinessOpeningHoursInterval(TelegramObject):
    """
    Describes an interval of time during which a business is open.
    """

    opening_minute: int
    """
    The minute's sequence number in a week, starting on Monday, marking the start of the
    time interval during which the business is open; 0 - 7 * 24 * 60
    """

    closing_minute: int
    """
    The minute's sequence number in a week, starting on Monday, marking the end of the
    time interval during which the business is open; 0 - 8 * 24 * 60
    """


class BusinessOpeningHours(TelegramObject):
    """
    Describes the opening hours of a business.
    """

    time_zone_name: str
    """
    Unique name of the time zone for which the opening hours are defined
    """

    opening_hours: list[BusinessOpeningHoursInterval]
    """
    List of time intervals describing business opening hours
    """


class UserRating(TelegramObject):
    """
    This object describes the rating of a user based on their Telegram Star spendings.
    """

    level: int
    """
    Current level of the user, indicating their reliability when purchasing digital
    goods and services. A higher level suggests a more trustworthy customer; a negative
    level is likely reason for concern.
    """

    rating: int
    """
    Numerical value of the user's rating; the higher the rating, the better
    """

    current_level_rating: int
    """
    The rating value required to get the current level
    """

    next_level_rating: int | None = None
    """
    The rating value required to get to the next level; omitted if the maximum level was
    reached
    """


class StoryAreaPosition(TelegramObject):
    """
    Describes the position of a clickable area within a story.
    """

    x_percentage: float
    """
    The abscissa of the area's center, as a percentage of the media width
    """

    y_percentage: float
    """
    The ordinate of the area's center, as a percentage of the media height
    """

    width_percentage: float
    """
    The width of the area's rectangle, as a percentage of the media width
    """

    height_percentage: float
    """
    The height of the area's rectangle, as a percentage of the media height
    """

    rotation_angle: float
    """
    The clockwise rotation angle of the rectangle, in degrees; 0-360
    """

    corner_radius_percentage: float
    """
    The radius of the rectangle corner rounding, as a percentage of the media width
    """


class LocationAddress(TelegramObject):
    """
    Describes the physical address of a location.
    """

    country_code: str
    """
    The two-letter ISO 3166-1 alpha-2 country code of the country where the location is
    located
    """

    state: str | None = None
    """
    State of the location
    """

    city: str | None = None
    """
    City of the location
    """

    street: str | None = None
    """
    Street address of the location
    """


type StoryAreaType = Annotated[
    StoryAreaTypeLocation
    | StoryAreaTypeSuggestedReaction
    | StoryAreaTypeLink
    | StoryAreaTypeWeather
    | StoryAreaTypeUniqueGift,
    Field(discriminator="type"),
]


class StoryAreaTypeLocation(TelegramObject):
    """
    Describes a story area pointing to a location. Currently, a story can have up to 10
    location areas.
    """

    type: Literal["location"] = "location"
    """
    Type of the area, always "location"
    """

    latitude: float
    """
    Location latitude in degrees
    """

    longitude: float
    """
    Location longitude in degrees
    """

    address: LocationAddress | None = None
    """
    Address of the location
    """


class StoryAreaTypeSuggestedReaction(TelegramObject):
    """
    Describes a story area pointing to a suggested reaction. Currently, a story can have
    up to 5 suggested reaction areas.
    """

    type: Literal["suggested_reaction"] = "suggested_reaction"
    """
    Type of the area, always "suggested_reaction"
    """

    reaction_type: ReactionType
    """
    Type of the reaction
    """

    is_dark: bool | None = None
    """
    Pass True if the reaction area has a dark background
    """

    is_flipped: bool | None = None
    """
    Pass True if reaction area corner is flipped
    """


class StoryAreaTypeLink(TelegramObject):
    """
    Describes a story area pointing to an HTTP or tg:// link. Currently, a story can
    have up to 3 link areas.
    """

    type: Literal["link"] = "link"
    """
    Type of the area, always "link"
    """

    url: str
    """
    HTTP or tg:// URL to be opened when the area is clicked
    """


class StoryAreaTypeWeather(TelegramObject):
    """
    Describes a story area containing weather information. Currently, a story can have
    up to 3 weather areas.
    """

    type: Literal["weather"] = "weather"
    """
    Type of the area, always "weather"
    """

    temperature: float
    """
    Temperature, in degree Celsius
    """

    emoji: str
    """
    Emoji representing the weather
    """

    background_color: int
    """
    A color of the area background in the ARGB format
    """


class StoryAreaTypeUniqueGift(TelegramObject):
    """
    Describes a story area pointing to a unique gift. Currently, a story can have at
    most 1 unique gift area.
    """

    type: Literal["unique_gift"] = "unique_gift"
    """
    Type of the area, always "unique_gift"
    """

    name: str
    """
    Unique name of the gift
    """


class StoryArea(TelegramObject):
    """
    Describes a clickable area on a story media.
    """

    position: StoryAreaPosition
    """
    Position of the area
    """

    type: StoryAreaType
    """
    Type of the area
    """


class ChatLocation(TelegramObject):
    """
    Represents a location to which a chat is connected.
    """

    location: Location
    """
    The location to which the supergroup is connected. Can't be a live location.
    """

    address: str
    """
    Location address; 1-64 characters, as defined by the chat owner
    """


type ReactionType = Annotated[
    ReactionTypeEmoji | ReactionTypeCustomEmoji | ReactionTypePaid,
    Field(discriminator="type"),
]


class ReactionTypeEmoji(TelegramObject):
    """
    The reaction is based on an emoji.
    """

    type: Literal["emoji"] = "emoji"
    """
    Type of the reaction, always "emoji"
    """

    emoji: str
    """
    Reaction emoji. Currently, it can be one of "❤", "👍", "👎", "🔥", "🥰", "👏", "😁", "🤔",
    "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳",
    "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈",
    "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄",
    "☃", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀",
    "😡".
    """


class ReactionTypeCustomEmoji(TelegramObject):
    """
    The reaction is based on a custom emoji.
    """

    type: Literal["custom_emoji"] = "custom_emoji"
    """
    Type of the reaction, always "custom_emoji"
    """

    custom_emoji_id: str
    """
    Custom emoji identifier
    """


class ReactionTypePaid(TelegramObject):
    """
    The reaction is paid.
    """

    type: Literal["paid"] = "paid"
    """
    Type of the reaction, always "paid"
    """


class ReactionCount(TelegramObject):
    """
    Represents a reaction added to a message along with the number of times it was
    added.
    """

    type: ReactionType
    """
    Type of the reaction
    """

    total_count: int
    """
    Number of times the reaction was added
    """


class MessageReactionUpdated(TelegramObject):
    """
    This object represents a change of a reaction on a message performed by a user.
    """

    chat: Chat
    """
    The chat containing the message the user reacted to
    """

    message_id: int
    """
    Unique identifier of the message inside the chat
    """

    user: User | None = None
    """
    The user that changed the reaction, if the user isn't anonymous
    """

    actor_chat: Chat | None = None
    """
    The chat on behalf of which the reaction was changed, if the user is anonymous
    """

    date: int
    """
    Date of the change in Unix time
    """

    old_reaction: list[ReactionType]
    """
    Previous list of reaction types that were set by the user
    """

    new_reaction: list[ReactionType]
    """
    New list of reaction types that have been set by the user
    """


class MessageReactionCountUpdated(TelegramObject):
    """
    This object represents reaction changes on a message with anonymous reactions.
    """

    chat: Chat
    """
    The chat containing the message
    """

    message_id: int
    """
    Unique message identifier inside the chat
    """

    date: int
    """
    Date of the change in Unix time
    """

    reactions: list[ReactionCount]
    """
    List of reactions that are present on the message
    """


class ForumTopic(TelegramObject):
    """
    This object represents a forum topic.
    """

    message_thread_id: int
    """
    Unique identifier of the forum topic
    """

    name: str
    """
    Name of the topic
    """

    icon_color: int
    """
    Color of the topic icon in RGB format
    """

    icon_custom_emoji_id: str | None = None
    """
    Unique identifier of the custom emoji shown as the topic icon
    """

    is_name_implicit: bool | None = None
    """
    True, if the name of the topic wasn't specified explicitly by its creator and likely
    needs to be changed by the bot
    """


class GiftBackground(TelegramObject):
    """
    This object describes the background of a gift.
    """

    center_color: int
    """
    Center color of the background in RGB format
    """

    edge_color: int
    """
    Edge color of the background in RGB format
    """

    text_color: int
    """
    Text color of the background in RGB format
    """


class Gift(TelegramObject):
    """
    This object represents a gift that can be sent by the bot.
    """

    id: str
    """
    Unique identifier of the gift
    """

    sticker: Sticker
    """
    The sticker that represents the gift
    """

    star_count: int
    """
    The number of Telegram Stars that must be paid to send the sticker
    """

    upgrade_star_count: int | None = None
    """
    The number of Telegram Stars that must be paid to upgrade the gift to a unique one
    """

    is_premium: bool | None = None
    """
    True, if the gift can only be purchased by Telegram Premium subscribers
    """

    has_colors: bool | None = None
    """
    True, if the gift can be used (after being upgraded) to customize a user's
    appearance
    """

    total_count: int | None = None
    """
    The total number of gifts of this type that can be sent by all users; for limited
    gifts only
    """

    remaining_count: int | None = None
    """
    The number of remaining gifts of this type that can be sent by all users; for
    limited gifts only
    """

    personal_total_count: int | None = None
    """
    The total number of gifts of this type that can be sent by the bot; for limited
    gifts only
    """

    personal_remaining_count: int | None = None
    """
    The number of remaining gifts of this type that can be sent by the bot; for limited
    gifts only
    """

    background: GiftBackground | None = None
    """
    Background of the gift
    """

    unique_gift_variant_count: int | None = None
    """
    The total number of different unique gifts that can be obtained by upgrading the
    gift
    """

    publisher_chat: Chat | None = None
    """
    Information about the chat that published the gift
    """


class Gifts(TelegramObject):
    """
    This object represent a list of gifts.
    """

    gifts: list[Gift]
    """
    The list of gifts
    """


class UniqueGiftModel(TelegramObject):
    """
    This object describes the model of a unique gift.
    """

    name: str
    """
    Name of the model
    """

    sticker: Sticker
    """
    The sticker that represents the unique gift
    """

    rarity_per_mille: int
    """
    The number of unique gifts that receive this model for every 1000 gift upgrades.
    Always 0 for crafted gifts.
    """

    rarity: str | None = None
    """
    Rarity of the model if it is a crafted model. Currently, can be "uncommon", "rare",
    "epic", or "legendary".
    """


class UniqueGiftSymbol(TelegramObject):
    """
    This object describes the symbol shown on the pattern of a unique gift.
    """

    name: str
    """
    Name of the symbol
    """

    sticker: Sticker
    """
    The sticker that represents the unique gift
    """

    rarity_per_mille: int
    """
    The number of unique gifts that receive this model for every 1000 gifts upgraded
    """


class UniqueGiftBackdropColors(TelegramObject):
    """
    This object describes the colors of the backdrop of a unique gift.
    """

    center_color: int
    """
    The color in the center of the backdrop in RGB format
    """

    edge_color: int
    """
    The color on the edges of the backdrop in RGB format
    """

    symbol_color: int
    """
    The color to be applied to the symbol in RGB format
    """

    text_color: int
    """
    The color for the text on the backdrop in RGB format
    """


class UniqueGiftBackdrop(TelegramObject):
    """
    This object describes the backdrop of a unique gift.
    """

    name: str
    """
    Name of the backdrop
    """

    colors: UniqueGiftBackdropColors
    """
    Colors of the backdrop
    """

    rarity_per_mille: int
    """
    The number of unique gifts that receive this backdrop for every 1000 gifts upgraded
    """


class UniqueGiftColors(TelegramObject):
    """
    This object contains information about the color scheme for a user's name, message
    replies and link previews based on a unique gift.
    """

    model_custom_emoji_id: str
    """
    Custom emoji identifier of the unique gift's model
    """

    symbol_custom_emoji_id: str
    """
    Custom emoji identifier of the unique gift's symbol
    """

    light_theme_main_color: int
    """
    Main color used in light themes; RGB format
    """

    light_theme_other_colors: list[int]
    """
    List of 1-3 additional colors used in light themes; RGB format
    """

    dark_theme_main_color: int
    """
    Main color used in dark themes; RGB format
    """

    dark_theme_other_colors: list[int]
    """
    List of 1-3 additional colors used in dark themes; RGB format
    """


class UniqueGift(TelegramObject):
    """
    This object describes a unique gift that was upgraded from a regular gift.
    """

    gift_id: str
    """
    Identifier of the regular gift from which the gift was upgraded
    """

    base_name: str
    """
    Human-readable name of the regular gift from which this unique gift was upgraded
    """

    name: str
    """
    Unique name of the gift. This name can be used in https://t.me/nft/... links and
    story areas.
    """

    number: int
    """
    Unique number of the upgraded gift among gifts upgraded from the same regular gift
    """

    model: UniqueGiftModel
    """
    Model of the gift
    """

    symbol: UniqueGiftSymbol
    """
    Symbol of the gift
    """

    backdrop: UniqueGiftBackdrop
    """
    Backdrop of the gift
    """

    is_premium: bool | None = None
    """
    True, if the original regular gift was exclusively purchaseable by Telegram Premium
    subscribers
    """

    is_burned: bool | None = None
    """
    True, if the gift was used to craft another gift and isn't available anymore
    """

    is_from_blockchain: bool | None = None
    """
    True, if the gift is assigned from the TON blockchain and can't be resold or
    transferred in Telegram
    """

    colors: UniqueGiftColors | None = None
    """
    The color scheme that can be used by the gift's owner for the chat's name, replies
    to messages and link previews; for business account gifts and gifts that are
    currently on sale only
    """

    publisher_chat: Chat | None = None
    """
    Information about the chat that published the gift
    """


class GiftInfo(TelegramObject):
    """
    Describes a service message about a regular gift that was sent or received.
    """

    gift: Gift
    """
    Information about the gift
    """

    owned_gift_id: str | None = None
    """
    Unique identifier of the received gift for the bot; only present for gifts received
    on behalf of business accounts
    """

    convert_star_count: int | None = None
    """
    Number of Telegram Stars that can be claimed by the receiver by converting the gift;
    omitted if conversion to Telegram Stars is impossible
    """

    prepaid_upgrade_star_count: int | None = None
    """
    Number of Telegram Stars that were prepaid for the ability to upgrade the gift
    """

    is_upgrade_separate: bool | None = None
    """
    True, if the gift's upgrade was purchased after the gift was sent
    """

    can_be_upgraded: bool | None = None
    """
    True, if the gift can be upgraded to a unique gift
    """

    text: str | None = None
    """
    Text of the message that was added to the gift
    """

    entities: list[MessageEntity] | None = None
    """
    Special entities that appear in the text
    """

    is_private: bool | None = None
    """
    True, if the sender and gift text are shown only to the gift receiver; otherwise,
    everyone will be able to see them
    """

    unique_gift_number: int | None = None
    """
    Unique number reserved for this gift when upgraded. See the number field in
    UniqueGift.
    """


class UniqueGiftInfo(TelegramObject):
    """
    Describes a service message about a unique gift that was sent or received.
    """

    gift: UniqueGift
    """
    Information about the gift
    """

    origin: str
    """
    Origin of the gift. Currently, either "upgrade" for gifts upgraded from regular
    gifts, "transfer" for gifts transferred from other users or channels, "resale" for
    gifts bought from other users, "gifted_upgrade" for upgrades purchased after the
    gift was sent, or "offer" for gifts bought or sold through gift purchase offers.
    """

    text: str | None = None
    """
    Text of the message that was added to the gift
    """

    entities: list[MessageEntity] | None = None
    """
    Special entities that appear in the text
    """

    is_private: bool | None = None
    """
    True, if the sender and gift text are shown only to the gift receiver; otherwise,
    everyone will be able to see them
    """

    last_resale_currency: str | None = None
    """
    For gifts bought from other users, the currency in which the payment for the gift
    was done. Currently, one of "XTR" for Telegram Stars or "TON" for TON grams.
    """

    last_resale_amount: int | None = None
    """
    For gifts bought from other users, the price paid for the gift in either Telegram
    Stars or nanograms
    """

    owned_gift_id: str | None = None
    """
    Unique identifier of the received gift for the bot; only present for gifts received
    on behalf of business accounts
    """

    transfer_star_count: int | None = None
    """
    Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot
    cannot transfer the gift
    """

    next_transfer_date: int | None = None
    """
    Point in time (Unix timestamp) when the gift can be transferred. If it is in the
    past, then the gift can be transferred now.
    """


type OwnedGift = Annotated[
    OwnedGiftRegular | OwnedGiftUnique, Field(discriminator="type")
]


class OwnedGiftRegular(TelegramObject):
    """
    Describes a regular gift owned by a user or a chat.
    """

    type: Literal["regular"] = "regular"
    """
    Type of the gift, always "regular"
    """

    gift: Gift
    """
    Information about the regular gift
    """

    owned_gift_id: str | None = None
    """
    Unique identifier of the gift for the bot; for gifts received on behalf of business
    accounts only
    """

    sender_user: User | None = None
    """
    Sender of the gift if it is a known user
    """

    send_date: int
    """
    Date the gift was sent in Unix time
    """

    text: str | None = None
    """
    Text of the message that was added to the gift
    """

    entities: list[MessageEntity] | None = None
    """
    Special entities that appear in the text
    """

    is_private: bool | None = None
    """
    True, if the sender and gift text are shown only to the gift receiver; otherwise,
    everyone will be able to see them
    """

    is_saved: bool | None = None
    """
    True, if the gift is displayed on the account's profile page; for gifts received on
    behalf of business accounts only
    """

    can_be_upgraded: bool | None = None
    """
    True, if the gift can be upgraded to a unique gift; for gifts received on behalf of
    business accounts only
    """

    was_refunded: bool | None = None
    """
    True, if the gift was refunded and isn't available anymore
    """

    convert_star_count: int | None = None
    """
    Number of Telegram Stars that can be claimed by the receiver instead of the gift;
    omitted if the gift cannot be converted to Telegram Stars; for gifts received on
    behalf of business accounts only
    """

    prepaid_upgrade_star_count: int | None = None
    """
    Number of Telegram Stars that were paid for the ability to upgrade the gift
    """

    is_upgrade_separate: bool | None = None
    """
    True, if the gift's upgrade was purchased after the gift was sent; for gifts
    received on behalf of business accounts only
    """

    unique_gift_number: int | None = None
    """
    Unique number reserved for this gift when upgraded. See the number field in
    UniqueGift.
    """


class OwnedGiftUnique(TelegramObject):
    """
    Describes a unique gift received and owned by a user or a chat.
    """

    type: Literal["unique"] = "unique"
    """
    Type of the gift, always "unique"
    """

    gift: UniqueGift
    """
    Information about the unique gift
    """

    owned_gift_id: str | None = None
    """
    Unique identifier of the received gift for the bot; for gifts received on behalf of
    business accounts only
    """

    sender_user: User | None = None
    """
    Sender of the gift if it is a known user
    """

    send_date: int
    """
    Date the gift was sent in Unix time
    """

    is_saved: bool | None = None
    """
    True, if the gift is displayed on the account's profile page; for gifts received on
    behalf of business accounts only
    """

    can_be_transferred: bool | None = None
    """
    True, if the gift can be transferred to another owner; for gifts received on behalf
    of business accounts only
    """

    transfer_star_count: int | None = None
    """
    Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot
    cannot transfer the gift
    """

    next_transfer_date: int | None = None
    """
    Point in time (Unix timestamp) when the gift can be transferred. If it is in the
    past, then the gift can be transferred now.
    """


class OwnedGifts(TelegramObject):
    """
    Contains the list of gifts received and owned by a user or a chat.
    """

    total_count: int
    """
    The total number of gifts owned by the user or the chat
    """

    gifts: list[OwnedGift]
    """
    The list of gifts
    """

    next_offset: str | None = None
    """
    Offset for the next request. If empty, then there are no more results.
    """


class BotAccessSettings(TelegramObject):
    """
    This object describes the access settings of a bot.
    """

    is_access_restricted: bool
    """
    True, if only selected users can access the bot. The bot's owner can always access
    it.
    """

    added_users: list[User] | None = None
    """
    The list of other users who have access to the bot if the access is restricted
    """


class AcceptedGiftTypes(TelegramObject):
    """
    This object describes the types of gifts that can be gifted to a user or a chat.
    """

    unlimited_gifts: bool
    """
    True, if unlimited regular gifts are accepted
    """

    limited_gifts: bool
    """
    True, if limited regular gifts are accepted
    """

    unique_gifts: bool
    """
    True, if unique gifts or gifts that can be upgraded to unique for free are accepted
    """

    premium_subscription: bool
    """
    True, if a Telegram Premium subscription is accepted
    """

    gifts_from_channels: bool
    """
    True, if transfers of unique gifts from channels are accepted
    """


class StarAmount(TelegramObject):
    """
    Describes an amount of Telegram Stars.
    """

    amount: int
    """
    Integer amount of Telegram Stars, rounded to 0; can be negative
    """

    nanostar_amount: int | None = None
    """
    The number of 1/1000000000 shares of Telegram Stars; from -999999999 to 999999999;
    can be negative if and only if amount is non-positive
    """


class BotCommand(TelegramObject):
    """
    This object represents a bot command.
    """

    command: str
    """
    Text of the command; 1-32 characters. Can contain only lowercase English letters,
    digits and underscores.
    """

    description: str
    """
    Description of the command; 1-256 characters
    """

    is_ephemeral: bool | None = None
    """
    True, if the command sends an ephemeral message, which can be seen only by the
    sender of the message and the bot
    """


type BotCommandScope = Annotated[
    BotCommandScopeDefault
    | BotCommandScopeAllPrivateChats
    | BotCommandScopeAllGroupChats
    | BotCommandScopeAllChatAdministrators
    | BotCommandScopeChat
    | BotCommandScopeChatAdministrators
    | BotCommandScopeChatMember,
    Field(discriminator="type"),
]


class BotCommandScopeDefault(TelegramObject):
    """
    Represents the default scope of bot commands. Default commands are used if no
    commands with a narrower scope are specified for the user.
    """

    type: Literal["default"] = "default"
    """
    Scope type, must be default
    """


class BotCommandScopeAllPrivateChats(TelegramObject):
    """
    Represents the scope of bot commands, covering all private chats.
    """

    type: Literal["all_private_chats"] = "all_private_chats"
    """
    Scope type, must be all_private_chats
    """


class BotCommandScopeAllGroupChats(TelegramObject):
    """
    Represents the scope of bot commands, covering all group and supergroup chats.
    """

    type: Literal["all_group_chats"] = "all_group_chats"
    """
    Scope type, must be all_group_chats
    """


class BotCommandScopeAllChatAdministrators(TelegramObject):
    """
    Represents the scope of bot commands, covering all group and supergroup chat
    administrators.
    """

    type: Literal["all_chat_administrators"] = "all_chat_administrators"
    """
    Scope type, must be all_chat_administrators
    """


class BotCommandScopeChat(TelegramObject):
    """
    Represents the scope of bot commands, covering a specific chat.
    """

    type: Literal["chat"] = "chat"
    """
    Scope type, must be chat
    """

    chat_id: int | str
    """
    Unique identifier for the target chat or username of the target supergroup in the
    format @username. Channel direct messages chats and channel chats aren't supported.
    """


class BotCommandScopeChatAdministrators(TelegramObject):
    """
    Represents the scope of bot commands, covering all administrators of a specific
    group or supergroup chat.
    """

    type: Literal["chat_administrators"] = "chat_administrators"
    """
    Scope type, must be chat_administrators
    """

    chat_id: int | str
    """
    Unique identifier for the target chat or username of the target supergroup in the
    format @username. Channel direct messages chats and channel chats aren't supported.
    """


class BotCommandScopeChatMember(TelegramObject):
    """
    Represents the scope of bot commands, covering a specific member of a group or
    supergroup chat.
    """

    type: Literal["chat_member"] = "chat_member"
    """
    Scope type, must be chat_member
    """

    chat_id: int | str
    """
    Unique identifier for the target chat or username of the target supergroup in the
    format @username. Channel direct messages chats and channel chats aren't supported.
    """

    user_id: int
    """
    Unique identifier of the target user
    """


class BotName(TelegramObject):
    """
    This object represents the bot's name.
    """

    name: str
    """
    The bot's name
    """


class BotDescription(TelegramObject):
    """
    This object represents the bot's description.
    """

    description: str
    """
    The bot's description
    """


class BotShortDescription(TelegramObject):
    """
    This object represents the bot's short description.
    """

    short_description: str
    """
    The bot's short description
    """


type MenuButton = Annotated[
    MenuButtonCommands | MenuButtonWebApp | MenuButtonDefault,
    Field(discriminator="type"),
]


class MenuButtonCommands(TelegramObject):
    """
    Represents a menu button, which opens the bot's list of commands.
    """

    type: Literal["commands"] = "commands"
    """
    Type of the button, must be commands
    """


class MenuButtonWebApp(TelegramObject):
    """
    Represents a menu button, which launches a Web App.
    """

    type: Literal["web_app"] = "web_app"
    """
    Type of the button, must be web_app
    """

    text: str
    """
    Text on the button
    """

    web_app: WebAppInfo
    """
    Description of the Web App that will be launched when the user presses the button.
    The Web App will be able to send an arbitrary message on behalf of the user using
    the method answerWebAppQuery. Alternatively, a t.me link to a Web App of the bot can
    be specified in the object instead of the Web App's URL, in which case the Web App
    will be opened as if the user pressed the link.
    """


class MenuButtonDefault(TelegramObject):
    """
    Describes that no specific value for the menu button was set.
    """

    type: Literal["default"] = "default"
    """
    Type of the button, must be default
    """


type ChatBoostSource = Annotated[
    ChatBoostSourcePremium | ChatBoostSourceGiftCode | ChatBoostSourceGiveaway,
    Field(discriminator="source"),
]


class ChatBoostSourcePremium(TelegramObject):
    """
    The boost was obtained by subscribing to Telegram Premium or by gifting a Telegram
    Premium subscription to another user.
    """

    source: Literal["premium"] = "premium"
    """
    Source of the boost, always "premium"
    """

    user: User
    """
    User that boosted the chat
    """


class ChatBoostSourceGiftCode(TelegramObject):
    """
    The boost was obtained by the creation of Telegram Premium gift codes to boost a
    chat. Each such code boosts the chat 4 times for the duration of the corresponding
    Telegram Premium subscription.
    """

    source: Literal["gift_code"] = "gift_code"
    """
    Source of the boost, always "gift_code"
    """

    user: User
    """
    User for which the gift code was created
    """


class ChatBoostSourceGiveaway(TelegramObject):
    """
    The boost was obtained by the creation of a Telegram Premium or a Telegram Star
    giveaway. This boosts the chat 4 times for the duration of the corresponding
    Telegram Premium subscription for Telegram Premium giveaways and prize_star_count /
    500 times for one year for Telegram Star giveaways.
    """

    source: Literal["giveaway"] = "giveaway"
    """
    Source of the boost, always "giveaway"
    """

    giveaway_message_id: int
    """
    Identifier of a message in the chat with the giveaway; the message could have been
    deleted already. May be 0 if the message isn't sent yet.
    """

    user: User | None = None
    """
    User that won the prize in the giveaway if any; for Telegram Premium giveaways only
    """

    prize_star_count: int | None = None
    """
    The number of Telegram Stars to be split between giveaway winners; for Telegram Star
    giveaways only
    """

    is_unclaimed: bool | None = None
    """
    True, if the giveaway was completed, but there was no user to win the prize
    """


class ChatBoost(TelegramObject):
    """
    This object contains information about a chat boost.
    """

    boost_id: str
    """
    Unique identifier of the boost
    """

    add_date: int
    """
    Point in time (Unix timestamp) when the chat was boosted
    """

    expiration_date: int
    """
    Point in time (Unix timestamp) when the boost will automatically expire, unless the
    booster's Telegram Premium subscription is prolonged
    """

    source: ChatBoostSource
    """
    Source of the added boost
    """


class ChatBoostUpdated(TelegramObject):
    """
    This object represents a boost added to a chat or changed.
    """

    chat: Chat
    """
    Chat which was boosted
    """

    boost: ChatBoost
    """
    Information about the chat boost
    """


class ChatBoostRemoved(TelegramObject):
    """
    This object represents a boost removed from a chat.
    """

    chat: Chat
    """
    Chat which was boosted
    """

    boost_id: str
    """
    Unique identifier of the boost
    """

    remove_date: int
    """
    Point in time (Unix timestamp) when the boost was removed
    """

    source: ChatBoostSource
    """
    Source of the removed boost
    """


class ChatOwnerLeft(TelegramObject):
    """
    Describes a service message about the chat owner leaving the chat.
    """

    new_owner: User | None = None
    """
    The user who will become the new owner of the chat if the previous owner does not
    return to the chat
    """


class ChatOwnerChanged(TelegramObject):
    """
    Describes a service message about an ownership change in the chat.
    """

    new_owner: User
    """
    The new owner of the chat
    """


class UserChatBoosts(TelegramObject):
    """
    This object represents a list of boosts added to a chat by a user.
    """

    boosts: list[ChatBoost]
    """
    The list of boosts added to the chat by the user
    """


class BusinessBotRights(TelegramObject):
    """
    Represents the rights of a business bot.
    """

    can_reply: bool | None = None
    """
    True, if the bot can send and edit messages in the private chats that had incoming
    messages in the last 24 hours
    """

    can_read_messages: bool | None = None
    """
    True, if the bot can mark incoming private messages as read
    """

    can_delete_sent_messages: bool | None = None
    """
    True, if the bot can delete messages sent by the bot
    """

    can_delete_all_messages: bool | None = None
    """
    True, if the bot can delete all private messages in managed chats
    """

    can_edit_name: bool | None = None
    """
    True, if the bot can edit the first and last name of the business account
    """

    can_edit_bio: bool | None = None
    """
    True, if the bot can edit the bio of the business account
    """

    can_edit_profile_photo: bool | None = None
    """
    True, if the bot can edit the profile photo of the business account
    """

    can_edit_username: bool | None = None
    """
    True, if the bot can edit the username of the business account
    """

    can_change_gift_settings: bool | None = None
    """
    True, if the bot can change the privacy settings pertaining to gifts for the
    business account
    """

    can_view_gifts_and_stars: bool | None = None
    """
    True, if the bot can view gifts and the amount of Telegram Stars owned by the
    business account
    """

    can_convert_gifts_to_stars: bool | None = None
    """
    True, if the bot can convert regular gifts owned by the business account to Telegram
    Stars
    """

    can_transfer_and_upgrade_gifts: bool | None = None
    """
    True, if the bot can transfer and upgrade gifts owned by the business account
    """

    can_transfer_stars: bool | None = None
    """
    True, if the bot can transfer Telegram Stars received by the business account to its
    own account, or use them to upgrade and transfer gifts
    """

    can_manage_stories: bool | None = None
    """
    True, if the bot can post, edit and delete stories on behalf of the business account
    """


class BusinessConnection(TelegramObject):
    """
    Describes the connection of the bot with a business account.
    """

    id: str
    """
    Unique identifier of the business connection
    """

    user: User
    """
    Business account user that created the business connection
    """

    user_chat_id: int
    """
    Identifier of a private chat with the user who created the business connection. This
    number may have more than 32 significant bits and some programming languages may
    have difficulty/silent defects in interpreting it. But it has at most 52 significant
    bits, so a 64-bit integer or double-precision float type are safe for storing this
    identifier.
    """

    date: int
    """
    Date the connection was established in Unix time
    """

    rights: BusinessBotRights | None = None
    """
    Rights of the business bot
    """

    is_enabled: bool
    """
    True, if the connection is active
    """


class BusinessMessagesDeleted(TelegramObject):
    """
    This object is received when messages are deleted from a connected business account.
    """

    business_connection_id: str
    """
    Unique identifier of the business connection
    """

    chat: Chat
    """
    Information about a chat in the business account. The bot may not have access to the
    chat or the corresponding user.
    """

    message_ids: list[int]
    """
    The list of identifiers of deleted messages in the chat of the business account
    """


class SentWebAppMessage(TelegramObject):
    """
    Describes an inline message sent by a Web App on behalf of a user.
    """

    inline_message_id: str | None = None
    """
    Identifier of the sent inline message. Available only if there is an inline keyboard
    attached to the message.
    """


class SentGuestMessage(TelegramObject):
    """
    Describes an inline message sent by a guest bot.
    """

    inline_message_id: str
    """
    Identifier of the sent inline message
    """


class PreparedInlineMessage(TelegramObject):
    """
    Describes an inline message to be sent by a user of a Mini App.
    """

    id: str
    """
    Unique identifier of the prepared message
    """

    expiration_date: int
    """
    Expiration date of the prepared message, in Unix time. Expired prepared messages can
    no longer be used.
    """


class PreparedKeyboardButton(TelegramObject):
    """
    Describes a keyboard button to be used by a user of a Mini App.
    """

    id: str
    """
    Unique identifier of the keyboard button
    """


class ResponseParameters(TelegramObject):
    """
    Describes why a request was unsuccessful.
    """

    migrate_to_chat_id: int | None = None
    """
    The group has been migrated to a supergroup with the specified identifier. This
    number may have more than 32 significant bits and some programming languages may
    have difficulty/silent defects in interpreting it. But it has at most 52 significant
    bits, so a signed 64-bit integer or double-precision float type are safe for storing
    this identifier.
    """

    retry_after: int | None = None
    """
    In case of exceeding flood control, the number of seconds left to wait before the
    request can be repeated
    """


type InputMedia = Annotated[
    InputMediaAnimation
    | InputMediaAudio
    | InputMediaDocument
    | InputMediaLivePhoto
    | InputMediaPhoto
    | InputMediaVideo,
    Field(discriminator="type"),
]


class InputMediaAnimation(TelegramObject):
    """
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be
    sent.
    """

    type: Literal["animation"] = "animation"
    """
    Type of the media, must be animation
    """

    media: InputFile | str
    """
    File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass "attach://<file_attach_name>" to upload a new one using multipart/form-data
    under <file_attach_name> name. More information on Sending Files:
    https://core.telegram.org/bots/api#sending-files
    """

    thumbnail: InputFile | str | None = None
    """
    Thumbnail of the file sent; can be ignored if thumbnail generation for the file is
    supported server-side. The thumbnail should be in JPEG format and less than 200 kB
    in size. A thumbnail's width and height should not exceed 320. Ignored if the file
    is not uploaded using multipart/form-data. Thumbnails can't be reused and can be
    only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the
    thumbnail was uploaded using multipart/form-data under <file_attach_name>. More
    information on Sending Files: https://core.telegram.org/bots/api#sending-files
    """

    caption: str | None = None
    """
    Caption of the animation to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the animation caption. See formatting options for more
    details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    show_caption_above_media: bool | None = None
    """
    Pass True if the caption must be shown above the message media
    """

    width: int | None = None
    """
    Animation width
    """

    height: int | None = None
    """
    Animation height
    """

    duration: int | None = None
    """
    Animation duration in seconds
    """

    has_spoiler: bool | None = None
    """
    Pass True if the animation needs to be covered with a spoiler animation
    """


class InputMediaAudio(TelegramObject):
    """
    Represents an audio file to be treated as music to be sent.
    """

    type: Literal["audio"] = "audio"
    """
    Type of the media, must be audio
    """

    media: InputFile | str
    """
    File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass "attach://<file_attach_name>" to upload a new one using multipart/form-data
    under <file_attach_name> name. More information on Sending Files:
    https://core.telegram.org/bots/api#sending-files
    """

    thumbnail: InputFile | str | None = None
    """
    Thumbnail of the file sent; can be ignored if thumbnail generation for the file is
    supported server-side. The thumbnail should be in JPEG format and less than 200 kB
    in size. A thumbnail's width and height should not exceed 320. Ignored if the file
    is not uploaded using multipart/form-data. Thumbnails can't be reused and can be
    only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the
    thumbnail was uploaded using multipart/form-data under <file_attach_name>. More
    information on Sending Files: https://core.telegram.org/bots/api#sending-files
    """

    caption: str | None = None
    """
    Caption of the audio to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the audio caption. See formatting options for more
    details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    duration: int | None = None
    """
    Duration of the audio in seconds
    """

    performer: str | None = None
    """
    Performer of the audio
    """

    title: str | None = None
    """
    Title of the audio
    """


class InputMediaDocument(TelegramObject):
    """
    Represents a general file to be sent.
    """

    type: Literal["document"] = "document"
    """
    Type of the media, must be document
    """

    media: InputFile | str
    """
    File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass "attach://<file_attach_name>" to upload a new one using multipart/form-data
    under <file_attach_name> name. More information on Sending Files:
    https://core.telegram.org/bots/api#sending-files
    """

    thumbnail: InputFile | str | None = None
    """
    Thumbnail of the file sent; can be ignored if thumbnail generation for the file is
    supported server-side. The thumbnail should be in JPEG format and less than 200 kB
    in size. A thumbnail's width and height should not exceed 320. Ignored if the file
    is not uploaded using multipart/form-data. Thumbnails can't be reused and can be
    only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the
    thumbnail was uploaded using multipart/form-data under <file_attach_name>. More
    information on Sending Files: https://core.telegram.org/bots/api#sending-files
    """

    caption: str | None = None
    """
    Caption of the document to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the document caption. See formatting options for more
    details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    disable_content_type_detection: bool | None = None
    """
    Disables automatic server-side content type detection for files uploaded using
    multipart/form-data. Always True, if the document is sent as part of an album.
    """


class InputMediaLink(TelegramObject):
    """
    Represents an HTTP link to be sent.
    """

    type: Literal["link"] = "link"
    """
    Type of the media, must be link
    """

    url: str
    """
    HTTP URL of the link
    """


class InputMediaLivePhoto(TelegramObject):
    """
    Represents a live photo to be sent.
    """

    type: Literal["live_photo"] = "live_photo"
    """
    Type of the media, must be live_photo
    """

    media: InputFile | str
    """
    Video of the live photo to send. Pass a file_id to send a file that exists on the
    Telegram servers (recommended) or pass "attach://<file_attach_name>" to upload a new
    one using multipart/form-data under <file_attach_name> name. More information on
    Sending Files: https://core.telegram.org/bots/api#sending-files. Sending live photos
    by a URL is currently unsupported.
    """

    photo: InputFile | str
    """
    The static photo to send. Pass a file_id to send a file that exists on the Telegram
    servers (recommended) or pass "attach://<file_attach_name>" to upload a new one
    using multipart/form-data under <file_attach_name> name. More information on Sending
    Files: https://core.telegram.org/bots/api#sending-files. Sending live photos by a
    URL is currently unsupported.
    """

    caption: str | None = None
    """
    Caption of the live photo to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the live photo caption. See formatting options for more
    details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    show_caption_above_media: bool | None = None
    """
    Pass True if the caption must be shown above the message media
    """

    has_spoiler: bool | None = None
    """
    Pass True if the live photo needs to be covered with a spoiler animation
    """


class InputMediaLocation(TelegramObject):
    """
    Represents a location to be sent.
    """

    type: Literal["location"] = "location"
    """
    Type of the media, must be location
    """

    latitude: float
    """
    Latitude of the location
    """

    longitude: float
    """
    Longitude of the location
    """

    horizontal_accuracy: float | None = None
    """
    The radius of uncertainty for the location, measured in meters; 0-1500
    """


class InputMediaPhoto(TelegramObject):
    """
    Represents a photo to be sent.
    """

    type: Literal["photo"] = "photo"
    """
    Type of the media, must be photo
    """

    media: InputFile | str
    """
    File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass "attach://<file_attach_name>" to upload a new one using multipart/form-data
    under <file_attach_name> name. More information on Sending Files:
    https://core.telegram.org/bots/api#sending-files
    """

    caption: str | None = None
    """
    Caption of the photo to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the photo caption. See formatting options for more
    details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    show_caption_above_media: bool | None = None
    """
    Pass True if the caption must be shown above the message media
    """

    has_spoiler: bool | None = None
    """
    Pass True if the photo needs to be covered with a spoiler animation
    """


class InputMediaSticker(TelegramObject):
    """
    Represents a sticker file to be sent.
    """

    type: Literal["sticker"] = "sticker"
    """
    Type of the media, must be sticker
    """

    media: InputFile | str
    """
    File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a .WEBP sticker from the
    Internet, or pass "attach://<file_attach_name>" to upload a new .WEBP, .TGS, or
    .WEBM sticker using multipart/form-data under <file_attach_name> name. More
    information on Sending Files: https://core.telegram.org/bots/api#sending-files
    """

    emoji: str | None = None
    """
    Emoji associated with the sticker; only for just uploaded stickers
    """


class InputMediaVenue(TelegramObject):
    """
    Represents a venue to be sent.
    """

    type: Literal["venue"] = "venue"
    """
    Type of the media, must be venue
    """

    latitude: float
    """
    Latitude of the location
    """

    longitude: float
    """
    Longitude of the location
    """

    title: str
    """
    Name of the venue
    """

    address: str
    """
    Address of the venue
    """

    foursquare_id: str | None = None
    """
    Foursquare identifier of the venue
    """

    foursquare_type: str | None = None
    """
    Foursquare type of the venue, if known. (For example, "arts_entertainment/default",
    "arts_entertainment/aquarium" or "food/icecream".)
    """

    google_place_id: str | None = None
    """
    Google Places identifier of the venue
    """

    google_place_type: str | None = None
    """
    Google Places type of the venue. (See supported types.)
    """


class InputMediaVideo(TelegramObject):
    """
    Represents a video to be sent.
    """

    type: Literal["video"] = "video"
    """
    Type of the media, must be video
    """

    media: InputFile | str
    """
    File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass "attach://<file_attach_name>" to upload a new one using multipart/form-data
    under <file_attach_name> name. More information on Sending Files:
    https://core.telegram.org/bots/api#sending-files
    """

    thumbnail: InputFile | str | None = None
    """
    Thumbnail of the file sent; can be ignored if thumbnail generation for the file is
    supported server-side. The thumbnail should be in JPEG format and less than 200 kB
    in size. A thumbnail's width and height should not exceed 320. Ignored if the file
    is not uploaded using multipart/form-data. Thumbnails can't be reused and can be
    only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the
    thumbnail was uploaded using multipart/form-data under <file_attach_name>. More
    information on Sending Files: https://core.telegram.org/bots/api#sending-files
    """

    cover: InputFile | str | None = None
    """
    Cover for the video in the message. Pass a file_id to send a file that exists on the
    Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the
    Internet, or pass "attach://<file_attach_name>" to upload a new one using
    multipart/form-data under <file_attach_name> name. More information on Sending
    Files: https://core.telegram.org/bots/api#sending-files
    """

    start_timestamp: int | None = None
    """
    Start timestamp for the video in the message
    """

    caption: str | None = None
    """
    Caption of the video to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the video caption. See formatting options for more
    details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    show_caption_above_media: bool | None = None
    """
    Pass True if the caption must be shown above the message media
    """

    width: int | None = None
    """
    Video width
    """

    height: int | None = None
    """
    Video height
    """

    duration: int | None = None
    """
    Video duration in seconds
    """

    supports_streaming: bool | None = None
    """
    Pass True if the uploaded video is suitable for streaming
    """

    has_spoiler: bool | None = None
    """
    Pass True if the video needs to be covered with a spoiler animation
    """


class InputMediaVoiceNote(TelegramObject):
    """
    Represents a voice message file to be sent.
    """

    type: Literal["voice_note"] = "voice_note"
    """
    Type of the media, must be voice_note
    """

    media: InputFile | str
    """
    File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass "attach://<file_attach_name>" to upload a new one using multipart/form-data
    under <file_attach_name> name. More information on Sending Files:
    https://core.telegram.org/bots/api#sending-files
    """

    caption: str | None = None
    """
    Caption of the voice message to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the voice message caption. See formatting options for
    more details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    duration: int | None = None
    """
    Duration of the voice message in seconds
    """


type InputPaidMedia = Annotated[
    InputPaidMediaLivePhoto | InputPaidMediaPhoto | InputPaidMediaVideo,
    Field(discriminator="type"),
]


class InputPaidMediaLivePhoto(TelegramObject):
    """
    The paid media to send is a live photo.
    """

    type: Literal["live_photo"] = "live_photo"
    """
    Type of the media, must be live_photo
    """

    media: InputFile | str
    """
    Video of the live photo to send. Pass a file_id to send a file that exists on the
    Telegram servers (recommended) or pass "attach://<file_attach_name>" to upload a new
    one using multipart/form-data under <file_attach_name> name. More information on
    Sending Files: https://core.telegram.org/bots/api#sending-files. Sending live photos
    by a URL is currently unsupported.
    """

    photo: InputFile | str
    """
    The static photo to send. Pass a file_id to send a file that exists on the Telegram
    servers (recommended) or pass "attach://<file_attach_name>" to upload a new one
    using multipart/form-data under <file_attach_name> name. More information on Sending
    Files: https://core.telegram.org/bots/api#sending-files. Sending live photos by a
    URL is currently unsupported.
    """


class InputPaidMediaPhoto(TelegramObject):
    """
    The paid media to send is a photo.
    """

    type: Literal["photo"] = "photo"
    """
    Type of the media, must be photo
    """

    media: InputFile | str
    """
    File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass "attach://<file_attach_name>" to upload a new one using multipart/form-data
    under <file_attach_name> name. More information on Sending Files:
    https://core.telegram.org/bots/api#sending-files
    """


class InputPaidMediaVideo(TelegramObject):
    """
    The paid media to send is a video.
    """

    type: Literal["video"] = "video"
    """
    Type of the media, must be video
    """

    media: InputFile | str
    """
    File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass "attach://<file_attach_name>" to upload a new one using multipart/form-data
    under <file_attach_name> name. More information on Sending Files:
    https://core.telegram.org/bots/api#sending-files
    """

    thumbnail: InputFile | str | None = None
    """
    Thumbnail of the file sent; can be ignored if thumbnail generation for the file is
    supported server-side. The thumbnail should be in JPEG format and less than 200 kB
    in size. A thumbnail's width and height should not exceed 320. Ignored if the file
    is not uploaded using multipart/form-data. Thumbnails can't be reused and can be
    only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the
    thumbnail was uploaded using multipart/form-data under <file_attach_name>. More
    information on Sending Files: https://core.telegram.org/bots/api#sending-files
    """

    cover: InputFile | str | None = None
    """
    Cover for the video in the message. Pass a file_id to send a file that exists on the
    Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the
    Internet, or pass "attach://<file_attach_name>" to upload a new one using
    multipart/form-data under <file_attach_name> name. More information on Sending
    Files: https://core.telegram.org/bots/api#sending-files
    """

    start_timestamp: int | None = None
    """
    Start timestamp for the video in the message
    """

    width: int | None = None
    """
    Video width
    """

    height: int | None = None
    """
    Video height
    """

    duration: int | None = None
    """
    Video duration in seconds
    """

    supports_streaming: bool | None = None
    """
    Pass True if the uploaded video is suitable for streaming
    """


type InputProfilePhoto = Annotated[
    InputProfilePhotoStatic | InputProfilePhotoAnimated, Field(discriminator="type")
]


class InputProfilePhotoStatic(TelegramObject):
    """
    A static profile photo in the .JPG format.
    """

    type: Literal["static"] = "static"
    """
    Type of the profile photo, must be static
    """

    photo: InputFile | str
    """
    The static profile photo. Profile photos can't be reused and can only be uploaded as
    a new file, so you can pass "attach://<file_attach_name>" if the photo was uploaded
    using multipart/form-data under <file_attach_name>. More information on Sending
    Files: https://core.telegram.org/bots/api#sending-files
    """


class InputProfilePhotoAnimated(TelegramObject):
    """
    An animated profile photo in the MPEG4 format.
    """

    type: Literal["animated"] = "animated"
    """
    Type of the profile photo, must be animated
    """

    animation: InputFile | str
    """
    The animated profile photo. Profile photos can't be reused and can only be uploaded
    as a new file, so you can pass "attach://<file_attach_name>" if the photo was
    uploaded using multipart/form-data under <file_attach_name>. More information on
    Sending Files: https://core.telegram.org/bots/api#sending-files
    """

    main_frame_timestamp: float | None = None
    """
    Timestamp in seconds of the frame that will be used as the static profile photo.
    Defaults to 0.0.
    """


type InputStoryContent = Annotated[
    InputStoryContentPhoto | InputStoryContentVideo, Field(discriminator="type")
]


class InputStoryContentPhoto(TelegramObject):
    """
    Describes a photo to post as a story.
    """

    type: Literal["photo"] = "photo"
    """
    Type of the content, must be photo
    """

    photo: InputFile | str
    """
    The photo to post as a story. The photo must be of the size 1080x1920 and must not
    exceed 10 MB. The photo can't be reused and can only be uploaded as a new file, so
    you can pass "attach://<file_attach_name>" if the photo was uploaded using
    multipart/form-data under <file_attach_name>. More information on Sending Files:
    https://core.telegram.org/bots/api#sending-files
    """


class InputStoryContentVideo(TelegramObject):
    """
    Describes a video to post as a story.
    """

    type: Literal["video"] = "video"
    """
    Type of the content, must be video
    """

    video: InputFile | str
    """
    The video to post as a story. The video must be of the size 720x1280, streamable,
    encoded with H.265 codec, with key frames added each second in the MPEG4 format, and
    must not exceed 30 MB. The video can't be reused and can only be uploaded as a new
    file, so you can pass "attach://<file_attach_name>" if the video was uploaded using
    multipart/form-data under <file_attach_name>. More information on Sending Files:
    https://core.telegram.org/bots/api#sending-files
    """

    duration: float | None = None
    """
    Precise duration of the video in seconds; 0-60
    """

    cover_frame_timestamp: float | None = None
    """
    Timestamp in seconds of the frame that will be used as the static cover for the
    story. Defaults to 0.0.
    """

    is_animation: bool | None = None
    """
    Pass True if the video has no sound
    """


class Sticker(TelegramObject):
    """
    This object represents a sticker.
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """

    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    """

    type: str
    """
    Type of the sticker, currently one of "regular", "mask", "custom_emoji". The type of
    the sticker is independent from its format, which is determined by the fields
    is_animated and is_video.
    """

    width: int
    """
    Sticker width
    """

    height: int
    """
    Sticker height
    """

    is_animated: bool
    """
    True, if the sticker is animated
    """

    is_video: bool
    """
    True, if the sticker is a video sticker
    """

    thumbnail: PhotoSize | None = None
    """
    Sticker thumbnail in the .WEBP or .JPG format
    """

    emoji: str | None = None
    """
    Emoji associated with the sticker
    """

    set_name: str | None = None
    """
    Name of the sticker set to which the sticker belongs
    """

    premium_animation: File | None = None
    """
    For premium regular stickers, premium animation for the sticker
    """

    mask_position: MaskPosition | None = None
    """
    For mask stickers, the position where the mask should be placed
    """

    custom_emoji_id: str | None = None
    """
    For custom emoji stickers, unique identifier of the custom emoji
    """

    needs_repainting: bool | None = None
    """
    True, if the sticker must be repainted to a text color in messages, the color of the
    Telegram Premium badge in emoji status, white color on chat photos, or another
    appropriate color in other places
    """

    file_size: int | None = None
    """
    File size in bytes
    """


class StickerSet(TelegramObject):
    """
    This object represents a sticker set.
    """

    name: str
    """
    Sticker set name
    """

    title: str
    """
    Sticker set title
    """

    sticker_type: str
    """
    Type of stickers in the set, currently one of "regular", "mask", "custom_emoji"
    """

    stickers: list[Sticker]
    """
    List of all set stickers
    """

    thumbnail: PhotoSize | None = None
    """
    Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format
    """


class MaskPosition(TelegramObject):
    """
    This object describes the position on faces where a mask should be placed by
    default.
    """

    point: str
    """
    The part of the face relative to which the mask should be placed. One of "forehead",
    "eyes", "mouth", or "chin".
    """

    x_shift: float
    """
    Shift by X-axis measured in widths of the mask scaled to the face size, from left to
    right. For example, choosing -1.0 will place mask just to the left of the default
    mask position.
    """

    y_shift: float
    """
    Shift by Y-axis measured in heights of the mask scaled to the face size, from top to
    bottom. For example, 1.0 will place the mask just below the default mask position.
    """

    scale: float
    """
    Mask scaling coefficient. For example, 2.0 means double size.
    """


class InputSticker(TelegramObject):
    """
    This object describes a sticker to be added to a sticker set.
    """

    sticker: InputFile | str
    """
    The added sticker. Pass a file_id as a String to send a file that already exists on
    the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from
    the Internet, or pass "attach://<file_attach_name>" to upload a new file using
    multipart/form-data under <file_attach_name> name. Animated and video stickers can't
    be uploaded via HTTP URL. More information on Sending Files:
    https://core.telegram.org/bots/api#sending-files
    """

    format: str
    """
    Format of the added sticker, must be one of "static" for a .WEBP or .PNG image,
    "animated" for a .TGS animation, "video" for a .WEBM video
    """

    emoji_list: list[str]
    """
    List of 1-20 emoji associated with the sticker
    """

    mask_position: MaskPosition | None = None
    """
    Position where the mask should be placed on faces. For "mask" stickers only.
    """

    keywords: list[str] | None = None
    """
    List of 0-20 search keywords for the sticker with total length of up to 64
    characters. For "regular" and "custom_emoji" stickers only.
    """


class RichMessage(TelegramObject):
    """
    Rich formatted message.
    """

    blocks: list[RichBlock]
    """
    Content of the message
    """

    is_rtl: bool | None = None
    """
    True, if the rich message must be shown right-to-left
    """


class InputRichMessage(TelegramObject):
    """
    Describes a rich message to be sent. Exactly one of the fields html, markdown, or
    blocks must be used.
    """

    blocks: list[InputRichBlock] | None = None
    """
    Content of the rich message to send described as a list of blocks
    """

    html: str | None = None
    """
    Content of the rich message to send described using HTML formatting. See rich
    message formatting options for more details. Use media field to specify the media
    used in the message.
    """

    markdown: str | None = None
    """
    Content of the rich message to send described using Markdown formatting. See rich
    message formatting options for more details. Use media field to specify the media
    used in the message.
    """

    media: list[InputRichMessageMedia] | None = None
    """
    List of media that are specified in the markdown or html fields using
    tg://photo?id=, tg://video?id=, tg://document?id=, and tg://audio?id= links
    """

    is_rtl: bool | None = None
    """
    Pass True if the rich message must be shown right-to-left
    """

    skip_entity_detection: bool | None = None
    """
    Pass True to skip automatic detection of entities (e.g., URLs, email addresses,
    username mentions, hashtags, cashtags, bot commands, or phone numbers) in the text
    """


class InputRichMessageMedia(TelegramObject):
    """
    Describes a media element embedded in an outgoing rich message.
    """

    id: str
    """
    Unique identifier of the media used in a tg://photo?id=, tg://video?id=,
    tg://document?id=, or tg://audio?id= link. 1-64 characters, only A-Z, a-z, 0-9, _
    and - are allowed.
    """

    media: (
        InputMediaAnimation
        | InputMediaAudio
        | InputMediaDocument
        | InputMediaPhoto
        | InputMediaVideo
        | InputMediaVoiceNote
    )
    """
    The media to be sent. Everything except the media itself and its properties is
    ignored.
    """


class RichMessageButton(TelegramObject):
    """
    This object represents a button in a RichMessage. Exactly one of the fields other
    than text and style must be used to specify the type of the button.
    """

    text: RichText
    """
    Text of the button. May contain only plain text, RichTextCustomEmoji and
    RichTextDateTime entities.
    """

    style: str | None = None
    """
    Style of the button. Must be one of "danger", "success", "primary", or "link" (the
    button is shown as a regular link without borders). Apps may use theme-specific
    colors for the button background and text based on the style. The style "link" is
    allowed only for callback buttons.
    """

    url: str | None = None
    """
    HTTP or tg:// URL to be opened when the button is pressed. Links
    tg://user?id=<user_id> can be used to mention a user by their identifier without
    using a username, if this is allowed by their privacy settings.
    """

    callback_data: str | None = None
    """
    Data to be sent in a callback query to the bot when the button is pressed, 1-64
    bytes
    """

    web_app: WebAppInfo | None = None
    """
    Description of the Web App that will be launched when the user presses the button.
    The Web App will be able to send an arbitrary message on behalf of the user using
    the method answerWebAppQuery. Available only in private chats between a user and the
    bot. Not supported for messages sent on behalf of a business account.
    """

    login_url: LoginUrl | None = None
    """
    An HTTPS URL used to automatically authorize the user. Can be used as a replacement
    for the Telegram Login Widget. Not supported for ephemeral messages.
    """

    switch_inline_query: str | None = None
    """
    If set, pressing the button will prompt the user to select one of their chats, open
    that chat and insert the bot's username and the specified inline query in the input
    field. May be empty, in which case just the bot's username will be inserted. Not
    supported for messages sent in channel direct messages chats and on behalf of a
    business account.
    """

    switch_inline_query_current_chat: str | None = None
    """
    If set, pressing the button will insert the bot's username and the specified inline
    query in the current chat's input field. May be empty, in which case only the bot's
    username will be inserted. Not supported in channels and for messages sent in
    channel direct messages chats and on behalf of a business account.
    """

    switch_inline_query_chosen_chat: SwitchInlineQueryChosenChat | None = None
    """
    If set, pressing the button will prompt the user to select one of their chats of the
    specified type, open that chat and insert the bot's username and the specified
    inline query in the input field. Not supported for messages sent in channel direct
    messages chats and on behalf of a business account.
    """

    copy_text: CopyTextButton | None = None
    """
    A button that copies the specified text to the clipboard
    """

    disabled: DisabledButton | None = None
    """
    If set, then the button is disabled and does nothing
    """


type RichText = (
    str
    | list[RichText]
    | RichTextBold
    | RichTextItalic
    | RichTextUnderline
    | RichTextStrikethrough
    | RichTextSpoiler
    | RichTextDateTime
    | RichTextTextMention
    | RichTextSubscript
    | RichTextSuperscript
    | RichTextMarked
    | RichTextCode
    | RichTextCustomEmoji
    | RichTextMathematicalExpression
    | RichTextUrl
    | RichTextEmailAddress
    | RichTextPhoneNumber
    | RichTextBankCardNumber
    | RichTextMention
    | RichTextHashtag
    | RichTextCashtag
    | RichTextBotCommand
    | RichTextButton
    | RichTextAnchor
    | RichTextAnchorLink
    | RichTextReference
    | RichTextReferenceLink
)


class RichTextBold(TelegramObject):
    """
    A bold text.
    """

    type: Literal["bold"] = "bold"
    """
    Type of the rich text, always "bold"
    """

    text: RichText
    """
    The text
    """


class RichTextItalic(TelegramObject):
    """
    An italicized text.
    """

    type: Literal["italic"] = "italic"
    """
    Type of the rich text, always "italic"
    """

    text: RichText
    """
    The text
    """


class RichTextUnderline(TelegramObject):
    """
    An underlined text.
    """

    type: Literal["underline"] = "underline"
    """
    Type of the rich text, always "underline"
    """

    text: RichText
    """
    The text
    """


class RichTextStrikethrough(TelegramObject):
    """
    A strikethrough text.
    """

    type: Literal["strikethrough"] = "strikethrough"
    """
    Type of the rich text, always "strikethrough"
    """

    text: RichText
    """
    The text
    """


class RichTextSpoiler(TelegramObject):
    """
    A text covered by a spoiler.
    """

    type: Literal["spoiler"] = "spoiler"
    """
    Type of the rich text, always "spoiler"
    """

    text: RichText
    """
    The text
    """


class RichTextDateTime(TelegramObject):
    """
    Formatted date and time.
    """

    type: Literal["date_time"] = "date_time"
    """
    Type of the rich text, always "date_time"
    """

    text: RichText
    """
    The text
    """

    unix_time: int
    """
    The Unix time associated with the entity
    """

    date_time_format: str
    """
    The string that defines the formatting of the date and time. See date-time entity
    formatting for more details.
    """


class RichTextTextMention(TelegramObject):
    """
    A mention of a Telegram user by their identifier.
    """

    type: Literal["text_mention"] = "text_mention"
    """
    Type of the rich text, always "text_mention"
    """

    text: RichText
    """
    The text
    """

    user: User
    """
    The mentioned user
    """


class RichTextSubscript(TelegramObject):
    """
    A subscript text.
    """

    type: Literal["subscript"] = "subscript"
    """
    Type of the rich text, always "subscript"
    """

    text: RichText
    """
    The text
    """


class RichTextSuperscript(TelegramObject):
    """
    A superscript text.
    """

    type: Literal["superscript"] = "superscript"
    """
    Type of the rich text, always "superscript"
    """

    text: RichText
    """
    The text
    """


class RichTextMarked(TelegramObject):
    """
    A marked text.
    """

    type: Literal["marked"] = "marked"
    """
    Type of the rich text, always "marked"
    """

    text: RichText
    """
    The text
    """


class RichTextCode(TelegramObject):
    """
    A monowidth text.
    """

    type: Literal["code"] = "code"
    """
    Type of the rich text, always "code"
    """

    text: RichText
    """
    The text
    """


class RichTextCustomEmoji(TelegramObject):
    """
    A custom emoji.
    """

    type: Literal["custom_emoji"] = "custom_emoji"
    """
    Type of the rich text, always "custom_emoji"
    """

    custom_emoji_id: str
    """
    Unique identifier of the custom emoji. Use getCustomEmojiStickers to get full
    information about the sticker.
    """

    alternative_text: str
    """
    Alternative emoji for the custom emoji
    """


class RichTextMathematicalExpression(TelegramObject):
    """
    A mathematical expression.
    """

    type: Literal["mathematical_expression"] = "mathematical_expression"
    """
    Type of the rich text, always "mathematical_expression"
    """

    expression: str
    """
    The expression in LaTeX format
    """


class RichTextUrl(TelegramObject):
    """
    A text with a link.
    """

    type: Literal["url"] = "url"
    """
    Type of the rich text, always "url"
    """

    text: RichText
    """
    The text
    """

    url: str
    """
    URL of the link
    """


class RichTextEmailAddress(TelegramObject):
    """
    A text with an email address.
    """

    type: Literal["email_address"] = "email_address"
    """
    Type of the rich text, always "email_address"
    """

    text: RichText
    """
    The text
    """

    email_address: str
    """
    The email address
    """


class RichTextPhoneNumber(TelegramObject):
    """
    A text with a phone number.
    """

    type: Literal["phone_number"] = "phone_number"
    """
    Type of the rich text, always "phone_number"
    """

    text: RichText
    """
    The text
    """

    phone_number: str
    """
    The phone number
    """


class RichTextBankCardNumber(TelegramObject):
    """
    A text with a bank card number.
    """

    type: Literal["bank_card_number"] = "bank_card_number"
    """
    Type of the rich text, always "bank_card_number"
    """

    text: RichText
    """
    The text
    """

    bank_card_number: str
    """
    The bank card number
    """


class RichTextMention(TelegramObject):
    """
    A mention by a username.
    """

    type: Literal["mention"] = "mention"
    """
    Type of the rich text, always "mention"
    """

    text: RichText
    """
    The text
    """

    username: str
    """
    The username
    """


class RichTextHashtag(TelegramObject):
    """
    A hashtag.
    """

    type: Literal["hashtag"] = "hashtag"
    """
    Type of the rich text, always "hashtag"
    """

    text: RichText
    """
    The text
    """

    hashtag: str
    """
    The hashtag
    """


class RichTextCashtag(TelegramObject):
    """
    A cashtag.
    """

    type: Literal["cashtag"] = "cashtag"
    """
    Type of the rich text, always "cashtag"
    """

    text: RichText
    """
    The text
    """

    cashtag: str
    """
    The cashtag
    """


class RichTextBotCommand(TelegramObject):
    """
    A bot command.
    """

    type: Literal["bot_command"] = "bot_command"
    """
    Type of the rich text, always "bot_command"
    """

    text: RichText
    """
    The text
    """

    bot_command: str
    """
    The bot command
    """


class RichTextButton(TelegramObject):
    """
    A button.
    """

    type: Literal["button"] = "button"
    """
    Type of the rich text, always "button"
    """

    button: RichMessageButton
    """
    The button
    """


class RichTextAnchor(TelegramObject):
    """
    An anchor.
    """

    type: Literal["anchor"] = "anchor"
    """
    Type of the rich text, always "anchor"
    """

    name: str
    """
    The name of the anchor
    """


class RichTextAnchorLink(TelegramObject):
    """
    A link to an anchor.
    """

    type: Literal["anchor_link"] = "anchor_link"
    """
    Type of the rich text, always "anchor_link"
    """

    text: RichText
    """
    The link text
    """

    anchor_name: str
    """
    The name of the anchor. If the name is empty, then the link brings back to the top
    of the message.
    """


class RichTextReference(TelegramObject):
    """
    A reference.
    """

    type: Literal["reference"] = "reference"
    """
    Type of the rich text, always "reference"
    """

    text: RichText
    """
    Text of the reference
    """

    name: str
    """
    The name of the reference
    """


class RichTextReferenceLink(TelegramObject):
    """
    A link to a reference.
    """

    type: Literal["reference_link"] = "reference_link"
    """
    Type of the rich text, always "reference_link"
    """

    text: RichText
    """
    The link text
    """

    reference_name: str
    """
    The name of the reference
    """


class RichBlockCaption(TelegramObject):
    """
    Caption of a rich formatted block.
    """

    text: RichText
    """
    Block caption
    """

    credit: RichText | None = None
    """
    Block credit which corresponds to the HTML tag <cite>
    """


class RichBlockTableCell(TelegramObject):
    """
    Cell in a table.
    """

    text: RichText | None = None
    """
    Text in the cell. If omitted, then the cell is invisible.
    """

    is_header: bool | None = None
    """
    True, if the cell is a header cell
    """

    colspan: int | None = None
    """
    The number of columns the cell spans if it is bigger than 1
    """

    rowspan: int | None = None
    """
    The number of rows the cell spans if it is bigger than 1
    """

    align: str
    """
    Horizontal cell content alignment. Currently, must be one of "left", "center", or
    "right".
    """

    valign: str
    """
    Vertical cell content alignment. Currently, must be one of "top", "middle", or
    "bottom".
    """


class RichBlockListItem(TelegramObject):
    """
    An item of a list.
    """

    label: str
    """
    Label of the item
    """

    blocks: list[RichBlock]
    """
    The content of the item
    """

    has_checkbox: bool | None = None
    """
    True, if the item has a checkbox
    """

    is_checked: bool | None = None
    """
    True, if the item has a checked checkbox
    """

    value: int | None = None
    """
    For ordered lists, the numeric value of the item label
    """

    type: str | None = None
    """
    For ordered lists, the type of the item label; must be one of "a" for lowercase
    letters, "A" for uppercase letters, "i" for lowercase Roman numerals, "I" for
    uppercase Roman numerals, or "1" for decimal numbers
    """


type RichBlock = Annotated[
    RichBlockParagraph
    | RichBlockSectionHeading
    | RichBlockPreformatted
    | RichBlockFooter
    | RichBlockDivider
    | RichBlockMathematicalExpression
    | RichBlockAnchor
    | RichBlockList
    | RichBlockBlockQuotation
    | RichBlockExpandableBlockQuotation
    | RichBlockPullQuotation
    | RichBlockCollage
    | RichBlockSlideshow
    | RichBlockTable
    | RichBlockDetails
    | RichBlockMap
    | RichBlockButtons
    | RichBlockAnimation
    | RichBlockAudio
    | RichBlockDocument
    | RichBlockPhoto
    | RichBlockVideo
    | RichBlockVoiceNote
    | RichBlockThinking,
    Field(discriminator="type"),
]


class RichBlockParagraph(TelegramObject):
    """
    A text paragraph, corresponding to the HTML tag <p>.
    """

    type: Literal["paragraph"] = "paragraph"
    """
    Type of the block, always "paragraph"
    """

    text: RichText
    """
    Text of the block
    """


class RichBlockSectionHeading(TelegramObject):
    """
    A section heading, corresponding to the HTML tags <h1>, <h2>, <h3>, <h4>, <h5>, or
    <h6>.
    """

    type: Literal["heading"] = "heading"
    """
    Type of the block, always "heading"
    """

    text: RichText
    """
    Text of the block
    """

    size: int
    """
    Relative size of the text font; 1-6, 1 is the largest, 6 is the smallest
    """


class RichBlockPreformatted(TelegramObject):
    """
    A preformatted text block, corresponding to the nested HTML tags <pre> and <code>.
    """

    type: Literal["pre"] = "pre"
    """
    Type of the block, always "pre"
    """

    text: RichText
    """
    Text of the block
    """

    language: str | None = None
    """
    The programming language of the text
    """


class RichBlockFooter(TelegramObject):
    """
    A footer, corresponding to the HTML tag <footer>.
    """

    type: Literal["footer"] = "footer"
    """
    Type of the block, always "footer"
    """

    text: RichText
    """
    Text of the block
    """


class RichBlockDivider(TelegramObject):
    """
    A divider, corresponding to the HTML tag <hr/>.
    """

    type: Literal["divider"] = "divider"
    """
    Type of the block, always "divider"
    """


class RichBlockMathematicalExpression(TelegramObject):
    """
    A block with a mathematical expression in LaTeX format, corresponding to the custom
    HTML tag <tg-math-block>.
    """

    type: Literal["mathematical_expression"] = "mathematical_expression"
    """
    Type of the block, always "mathematical_expression"
    """

    expression: str
    """
    The mathematical expression in LaTeX format
    """


class RichBlockAnchor(TelegramObject):
    """
    A block with an anchor, corresponding to the HTML tag <a> with the attribute name.
    """

    type: Literal["anchor"] = "anchor"
    """
    Type of the block, always "anchor"
    """

    name: str
    """
    The name of the anchor
    """


class RichBlockList(TelegramObject):
    """
    A list of blocks, corresponding to the HTML tag <ul> or <ol> with multiple nested
    tags <li>.
    """

    type: Literal["list"] = "list"
    """
    Type of the block, always "list"
    """

    items: list[RichBlockListItem]
    """
    Items of the list
    """


class RichBlockBlockQuotation(TelegramObject):
    """
    A block quotation, corresponding to the HTML tag <blockquote>.
    """

    type: Literal["blockquote"] = "blockquote"
    """
    Type of the block, always "blockquote"
    """

    blocks: list[RichBlock]
    """
    Content of the block
    """

    credit: RichText | None = None
    """
    Credit of the block
    """


class RichBlockExpandableBlockQuotation(TelegramObject):
    """
    A block quotation, corresponding to the HTML tag <blockquote> with custom attribute
    "expandable".
    """

    type: Literal["expandable_blockquote"] = "expandable_blockquote"
    """
    Type of the block, always "expandable_blockquote"
    """

    text: RichText
    """
    Content of the block
    """

    credit: RichText | None = None
    """
    Credit of the block
    """


class RichBlockPullQuotation(TelegramObject):
    """
    A quotation with centered text, loosely corresponding to the HTML tag <aside>.
    """

    type: Literal["pullquote"] = "pullquote"
    """
    Type of the block, always "pullquote"
    """

    text: RichText
    """
    Text of the block
    """

    credit: RichText | None = None
    """
    Credit of the block
    """


class RichBlockCollage(TelegramObject):
    """
    A collage, corresponding to the custom HTML tag <tg-collage>.
    """

    type: Literal["collage"] = "collage"
    """
    Type of the block, always "collage"
    """

    blocks: list[RichBlock]
    """
    Elements of the collage
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class RichBlockSlideshow(TelegramObject):
    """
    A slideshow, corresponding to the custom HTML tag <tg-slideshow>.
    """

    type: Literal["slideshow"] = "slideshow"
    """
    Type of the block, always "slideshow"
    """

    blocks: list[RichBlock]
    """
    Elements of the slideshow
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class RichBlockTable(TelegramObject):
    """
    A table, corresponding to the HTML tag <table>.
    """

    type: Literal["table"] = "table"
    """
    Type of the block, always "table"
    """

    cells: list[list[RichBlockTableCell]]
    """
    Cells of the table
    """

    is_bordered: bool | None = None
    """
    True, if the table has borders
    """

    is_striped: bool | None = None
    """
    True, if the table is striped
    """

    is_compact: bool | None = None
    """
    True, if table cells have smaller indents
    """

    caption: RichText | None = None
    """
    Caption of the table
    """


class RichBlockDetails(TelegramObject):
    """
    An expandable block for details disclosure, corresponding to the HTML tag <details>.
    """

    type: Literal["details"] = "details"
    """
    Type of the block, always "details"
    """

    summary: RichText
    """
    Always shown summary of the block
    """

    blocks: list[RichBlock]
    """
    Content of the block
    """

    is_open: bool | None = None
    """
    True, if the content of the block is visible by default
    """


class RichBlockMap(TelegramObject):
    """
    A block with a map, corresponding to the custom HTML tag <tg-map>.
    """

    type: Literal["map"] = "map"
    """
    Type of the block, always "map"
    """

    location: Location
    """
    Location of the center of the map
    """

    zoom: int
    """
    Map zoom level
    """

    width: int
    """
    Expected width of the map
    """

    height: int
    """
    Expected height of the map
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class RichBlockButtons(TelegramObject):
    """
    A block containing a list of buttons that are shown in one row, corresponding to the
    custom HTML tag <tg-button-row>.
    """

    type: Literal["buttons"] = "buttons"
    """
    Type of the block, always "buttons"
    """

    buttons: list[RichMessageButton]
    """
    The buttons
    """

    align: str | None = None
    """
    Horizontal alignment of the buttons. Currently, must be one of "left", "center", or
    "right".
    """


class RichBlockAnimation(TelegramObject):
    """
    A block with an animation, corresponding to the HTML tag <video>.
    """

    type: Literal["animation"] = "animation"
    """
    Type of the block, always "animation"
    """

    animation: Animation
    """
    The animation
    """

    has_spoiler: bool | None = None
    """
    True, if the media preview is covered by a spoiler animation
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class RichBlockAudio(TelegramObject):
    """
    A block with a music file, corresponding to the HTML tag <audio>.
    """

    type: Literal["audio"] = "audio"
    """
    Type of the block, always "audio"
    """

    audio: Audio
    """
    The audio
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class RichBlockDocument(TelegramObject):
    """
    A block with a general file, corresponding to the custom HTML tag <tg-document>.
    """

    type: Literal["document"] = "document"
    """
    Type of the block, always "document"
    """

    document: Document
    """
    The document
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class RichBlockPhoto(TelegramObject):
    """
    A block with a photo, corresponding to the HTML tag <img>.
    """

    type: Literal["photo"] = "photo"
    """
    Type of the block, always "photo"
    """

    photo: list[PhotoSize]
    """
    Available sizes of the photo
    """

    has_spoiler: bool | None = None
    """
    True, if the media preview is covered by a spoiler animation
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class RichBlockVideo(TelegramObject):
    """
    A block with a video, corresponding to the HTML tag <video>.
    """

    type: Literal["video"] = "video"
    """
    Type of the block, always "video"
    """

    video: Video
    """
    The video
    """

    has_spoiler: bool | None = None
    """
    True, if the media preview is covered by a spoiler animation
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class RichBlockVoiceNote(TelegramObject):
    """
    A block with a voice note, corresponding to the HTML tag <audio>.
    """

    type: Literal["voice_note"] = "voice_note"
    """
    Type of the block, always "voice_note"
    """

    voice_note: Voice
    """
    The voice note
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class RichBlockThinking(TelegramObject):
    """
    A block with a "Thinking..." placeholder, corresponding to the custom HTML tag <tg-
    thinking>. The block may be used only in sendRichMessageDraft, therefore it can't be
    received in messages. See https://t.me/addemoji/AIActions for examples of custom
    emoji that are recommended for usage in the block.
    """

    type: Literal["thinking"] = "thinking"
    """
    Type of the block, always "thinking"
    """

    text: RichText
    """
    Text of the block. See https://t.me/addemoji/AIActions for examples of custom emoji
    that are recommended for usage in the block.
    """


class InputRichBlockListItem(TelegramObject):
    """
    An item of a list to be sent.
    """

    blocks: list[InputRichBlock]
    """
    The content of the item
    """

    has_checkbox: bool | None = None
    """
    Pass True if the item has a checkbox
    """

    is_checked: bool | None = None
    """
    Pass True if the item has a checked checkbox
    """

    value: int | None = None
    """
    For ordered lists, the numeric value of the item label
    """

    type: str | None = None
    """
    For ordered lists, the type of the item label; must be one of "a" for lowercase
    letters, "A" for uppercase letters, "i" for lowercase Roman numerals, "I" for
    uppercase Roman numerals, or "1" for decimal numbers
    """


type InputRichBlock = Annotated[
    InputRichBlockParagraph
    | InputRichBlockSectionHeading
    | InputRichBlockPreformatted
    | InputRichBlockFooter
    | InputRichBlockDivider
    | InputRichBlockMathematicalExpression
    | InputRichBlockAnchor
    | InputRichBlockList
    | InputRichBlockBlockQuotation
    | InputRichBlockExpandableBlockQuotation
    | InputRichBlockPullQuotation
    | InputRichBlockCollage
    | InputRichBlockSlideshow
    | InputRichBlockTable
    | InputRichBlockDetails
    | InputRichBlockMap
    | InputRichBlockButtons
    | InputRichBlockAnimation
    | InputRichBlockAudio
    | InputRichBlockDocument
    | InputRichBlockPhoto
    | InputRichBlockVideo
    | InputRichBlockVoiceNote
    | InputRichBlockThinking,
    Field(discriminator="type"),
]


class InputRichBlockParagraph(TelegramObject):
    """
    A text paragraph, corresponding to the HTML tag <p>.
    """

    type: Literal["paragraph"] = "paragraph"
    """
    Type of the block, always "paragraph"
    """

    text: RichText
    """
    Text of the block
    """


class InputRichBlockSectionHeading(TelegramObject):
    """
    A section heading, corresponding to the HTML tags <h1>, <h2>, <h3>, <h4>, <h5>, or
    <h6>.
    """

    type: Literal["heading"] = "heading"
    """
    Type of the block, always "heading"
    """

    text: RichText
    """
    Text of the block
    """

    size: int
    """
    Relative size of the text font; 1-6, 1 is the largest, 6 is the smallest
    """


class InputRichBlockPreformatted(TelegramObject):
    """
    A preformatted text block, corresponding to the nested HTML tags <pre> and <code>.
    """

    type: Literal["pre"] = "pre"
    """
    Type of the block, always "pre"
    """

    text: RichText
    """
    Text of the block
    """

    language: str | None = None
    """
    The programming language of the text
    """


class InputRichBlockFooter(TelegramObject):
    """
    A footer, corresponding to the HTML tag <footer>.
    """

    type: Literal["footer"] = "footer"
    """
    Type of the block, always "footer"
    """

    text: RichText
    """
    Text of the block
    """


class InputRichBlockDivider(TelegramObject):
    """
    A divider, corresponding to the HTML tag <hr/>.
    """

    type: Literal["divider"] = "divider"
    """
    Type of the block, always "divider"
    """


class InputRichBlockMathematicalExpression(TelegramObject):
    """
    A block with a mathematical expression in LaTeX format, corresponding to the custom
    HTML tag <tg-math-block>.
    """

    type: Literal["mathematical_expression"] = "mathematical_expression"
    """
    Type of the block, always "mathematical_expression"
    """

    expression: str
    """
    The mathematical expression in LaTeX format
    """


class InputRichBlockAnchor(TelegramObject):
    """
    A block with an anchor, corresponding to the HTML tag <a> with the attribute name.
    """

    type: Literal["anchor"] = "anchor"
    """
    Type of the block, always "anchor"
    """

    name: str
    """
    The name of the anchor
    """


class InputRichBlockList(TelegramObject):
    """
    A list of blocks, corresponding to the HTML tag <ul> or <ol> with multiple nested
    tags <li>.
    """

    type: Literal["list"] = "list"
    """
    Type of the block, always "list"
    """

    items: list[InputRichBlockListItem]
    """
    Items of the list
    """


class InputRichBlockBlockQuotation(TelegramObject):
    """
    A block quotation, corresponding to the HTML tag <blockquote>.
    """

    type: Literal["blockquote"] = "blockquote"
    """
    Type of the block, always "blockquote"
    """

    blocks: list[InputRichBlock]
    """
    Content of the block
    """

    credit: RichText | None = None
    """
    Credit of the block
    """


class InputRichBlockExpandableBlockQuotation(TelegramObject):
    """
    A block quotation, corresponding to the HTML tag <blockquote> with custom attribute
    "expandable".
    """

    type: Literal["expandable_blockquote"] = "expandable_blockquote"
    """
    Type of the block, always "expandable_blockquote"
    """

    text: RichText
    """
    Content of the block
    """

    credit: RichText | None = None
    """
    Credit of the block
    """


class InputRichBlockPullQuotation(TelegramObject):
    """
    A quotation with centered text, loosely corresponding to the HTML tag <aside>.
    """

    type: Literal["pullquote"] = "pullquote"
    """
    Type of the block, always "pullquote"
    """

    text: RichText
    """
    Text of the block
    """

    credit: RichText | None = None
    """
    Credit of the block
    """


class InputRichBlockCollage(TelegramObject):
    """
    A collage, corresponding to the custom HTML tag <tg-collage>.
    """

    type: Literal["collage"] = "collage"
    """
    Type of the block, always "collage"
    """

    blocks: list[InputRichBlock]
    """
    Elements of the collage
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class InputRichBlockSlideshow(TelegramObject):
    """
    A slideshow, corresponding to the custom HTML tag <tg-slideshow>.
    """

    type: Literal["slideshow"] = "slideshow"
    """
    Type of the block, always "slideshow"
    """

    blocks: list[InputRichBlock]
    """
    Elements of the slideshow
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class InputRichBlockTable(TelegramObject):
    """
    A table, corresponding to the HTML tag <table>.
    """

    type: Literal["table"] = "table"
    """
    Type of the block, always "table"
    """

    cells: list[list[RichBlockTableCell]]
    """
    Cells of the table
    """

    is_bordered: bool | None = None
    """
    Pass True if the table has borders
    """

    is_striped: bool | None = None
    """
    Pass True if the table is striped
    """

    is_compact: bool | None = None
    """
    Pass True if table cells must have smaller indents
    """

    caption: RichText | None = None
    """
    Caption of the table
    """


class InputRichBlockDetails(TelegramObject):
    """
    An expandable block for details disclosure, corresponding to the HTML tag <details>.
    """

    type: Literal["details"] = "details"
    """
    Type of the block, always "details"
    """

    summary: RichText
    """
    Always shown summary of the block
    """

    blocks: list[InputRichBlock]
    """
    Content of the block
    """

    is_open: bool | None = None
    """
    Pass True if the content of the block is visible by default
    """


class InputRichBlockMap(TelegramObject):
    """
    A block with a map, corresponding to the custom HTML tag <tg-map>. The map's width
    and height must not exceed 10000 in total. The width and height ratio must be at
    most 20.
    """

    type: Literal["map"] = "map"
    """
    Type of the block, always "map"
    """

    location: Location
    """
    Location of the center of the map
    """

    zoom: int | None = None
    """
    Map zoom level; 0-24
    """

    width: int | None = None
    """
    Map width; 0-10000
    """

    height: int | None = None
    """
    Map height; 0-10000
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class InputRichBlockButtons(TelegramObject):
    """
    A block containing a list of buttons that are shown in one row, corresponding to the
    custom HTML tag <tg-button-row>.
    """

    type: Literal["buttons"] = "buttons"
    """
    Type of the block, always "buttons"
    """

    buttons: list[RichMessageButton]
    """
    List of 1-8 buttons to send
    """

    align: str | None = None
    """
    Horizontal alignment of the buttons. Currently, must be one of "left", "center", or
    "right".
    """


class InputRichBlockAnimation(TelegramObject):
    """
    A block with an animation, corresponding to the HTML tag <video>.
    """

    type: Literal["animation"] = "animation"
    """
    Type of the block, always "animation"
    """

    animation: InputMediaAnimation
    """
    The animation. Caption is ignored.
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class InputRichBlockAudio(TelegramObject):
    """
    A block with a music file, corresponding to the HTML tag <audio>.
    """

    type: Literal["audio"] = "audio"
    """
    Type of the block, always "audio"
    """

    audio: InputMediaAudio
    """
    The audio. Caption is ignored.
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class InputRichBlockDocument(TelegramObject):
    """
    A block with a general file, corresponding to the custom HTML tag <tg-document>.
    """

    type: Literal["document"] = "document"
    """
    Type of the block, always "document"
    """

    document: InputMediaDocument
    """
    The document. Caption is ignored.
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class InputRichBlockPhoto(TelegramObject):
    """
    A block with a photo, corresponding to the HTML tag <img>.
    """

    type: Literal["photo"] = "photo"
    """
    Type of the block, always "photo"
    """

    photo: InputMediaPhoto
    """
    The photo. Caption is ignored.
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class InputRichBlockVideo(TelegramObject):
    """
    A block with a video, corresponding to the HTML tag <video>.
    """

    type: Literal["video"] = "video"
    """
    Type of the block, always "video"
    """

    video: InputMediaVideo
    """
    The video. Caption is ignored.
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class InputRichBlockVoiceNote(TelegramObject):
    """
    A block with a voice note, corresponding to the HTML tag <audio>.
    """

    type: Literal["voice_note"] = "voice_note"
    """
    Type of the block, always "voice_note"
    """

    voice_note: InputMediaVoiceNote
    """
    The voice note. Caption is ignored.
    """

    caption: RichBlockCaption | None = None
    """
    Caption of the block
    """


class InputRichBlockThinking(TelegramObject):
    """
    A block with a "Thinking..." placeholder, corresponding to the custom HTML tag <tg-
    thinking>. The block may be used only in sendRichMessageDraft, therefore it can't be
    received in messages. See https://t.me/addemoji/AIActions for examples of custom
    emoji that are recommended for usage in the block.
    """

    type: Literal["thinking"] = "thinking"
    """
    Type of the block, always "thinking"
    """

    text: RichText
    """
    Text of the block. See https://t.me/addemoji/AIActions for examples of custom emoji
    that are recommended for usage in the block.
    """


class InlineQuery(TelegramObject):
    """
    This object represents an incoming inline query. When the user sends an empty query,
    your bot could return some default or trending results.
    """

    id: str
    """
    Unique identifier for this query
    """

    from_: User = Field(alias="from")
    """
    Sender
    """

    query: str
    """
    Text of the query (up to 256 characters)
    """

    offset: str
    """
    Offset of the results to be returned, can be controlled by the bot
    """

    chat_type: str | None = None
    """
    Type of the chat from which the inline query was sent. Can be either "sender" for a
    private chat with the inline query sender, "private", "group", "supergroup", or
    "channel". The chat type should be always known for requests sent from official
    clients and most third-party clients, unless the request was sent from a secret
    chat.
    """

    location: Location | None = None
    """
    Sender location, only for bots that request user location
    """


class InlineQueryResultsButton(TelegramObject):
    """
    This object represents a button to be shown above inline query results. You must use
    exactly one of the optional fields.
    """

    text: str
    """
    Label text on the button
    """

    web_app: WebAppInfo | None = None
    """
    Description of the Web App that will be launched when the user presses the button.
    The Web App will be able to switch back to the inline mode using the method
    switchInlineQuery inside the Web App.
    """

    start_parameter: str | None = None
    """
    Deep-linking parameter for the /start message sent to the bot when a user presses
    the button. 1-64 characters, only A-Z, a-z, 0-9, _ and - are allowed. Example: An
    inline bot that sends YouTube videos can ask the user to connect the bot to their
    YouTube account to adapt search results accordingly. To do this, it displays a
    'Connect your YouTube account' button above the results, or even before showing any.
    The user presses the button, switches to a private chat with the bot and, in doing
    so, passes a start parameter that instructs the bot to return an OAuth link. Once
    done, the bot can offer a switch_inline button so that the user can easily return to
    the chat where they wanted to use the bot's inline capabilities.
    """


type InlineQueryResult = Annotated[
    InlineQueryResultCachedAudio
    | InlineQueryResultCachedDocument
    | InlineQueryResultCachedGif
    | InlineQueryResultCachedMpeg4Gif
    | InlineQueryResultCachedPhoto
    | InlineQueryResultCachedSticker
    | InlineQueryResultCachedVideo
    | InlineQueryResultCachedVoice
    | InlineQueryResultArticle
    | InlineQueryResultAudio
    | InlineQueryResultContact
    | InlineQueryResultGame
    | InlineQueryResultDocument
    | InlineQueryResultGif
    | InlineQueryResultLocation
    | InlineQueryResultMpeg4Gif
    | InlineQueryResultPhoto
    | InlineQueryResultVenue
    | InlineQueryResultVideo
    | InlineQueryResultVoice,
    Field(discriminator="type"),
]


class InlineQueryResultArticle(TelegramObject):
    """
    Represents a link to an article or web page.
    """

    type: Literal["article"] = "article"
    """
    Type of the result, must be article
    """

    id: str
    """
    Unique identifier for this result, 1-64 Bytes
    """

    title: str
    """
    Title of the result
    """

    input_message_content: InputMessageContent
    """
    Content of the message to be sent
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    url: str | None = None
    """
    URL of the result
    """

    description: str | None = None
    """
    Short description of the result
    """

    thumbnail_url: str | None = None
    """
    Url of the thumbnail for the result
    """

    thumbnail_width: int | None = None
    """
    Thumbnail width
    """

    thumbnail_height: int | None = None
    """
    Thumbnail height
    """


class InlineQueryResultPhoto(TelegramObject):
    """
    Represents a link to a photo. By default, this photo will be sent by the user with
    optional caption. Alternatively, you can use input_message_content to send a message
    with the specified content instead of the photo.
    """

    type: Literal["photo"] = "photo"
    """
    Type of the result, must be photo
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    photo_url: str
    """
    A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed
    5MB.
    """

    thumbnail_url: str
    """
    URL of the thumbnail for the photo
    """

    photo_width: int | None = None
    """
    Width of the photo
    """

    photo_height: int | None = None
    """
    Height of the photo
    """

    title: str | None = None
    """
    Title for the result
    """

    description: str | None = None
    """
    Short description of the result
    """

    caption: str | None = None
    """
    Caption of the photo to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the photo caption. See formatting options for more
    details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    show_caption_above_media: bool | None = None
    """
    Pass True if the caption must be shown above the message media
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the photo
    """


class InlineQueryResultGif(TelegramObject):
    """
    Represents a link to an animated GIF file. By default, this animated GIF file will
    be sent by the user with optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    animation.
    """

    type: Literal["gif"] = "gif"
    """
    Type of the result, must be gif
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    gif_url: str
    """
    A valid URL for the GIF file
    """

    gif_width: int | None = None
    """
    Width of the GIF
    """

    gif_height: int | None = None
    """
    Height of the GIF
    """

    gif_duration: int | None = None
    """
    Duration of the GIF in seconds
    """

    thumbnail_url: str
    """
    URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    """

    thumbnail_mime_type: str | None = None
    """
    MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or
    "video/mp4". Defaults to "image/jpeg".
    """

    title: str | None = None
    """
    Title for the result
    """

    caption: str | None = None
    """
    Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the caption. See formatting options for more details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    show_caption_above_media: bool | None = None
    """
    Pass True if the caption must be shown above the message media
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the GIF animation
    """


class InlineQueryResultMpeg4Gif(TelegramObject):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By
    default, this animated MPEG-4 file will be sent by the user with optional caption.
    Alternatively, you can use input_message_content to send a message with the
    specified content instead of the animation.
    """

    type: Literal["mpeg4_gif"] = "mpeg4_gif"
    """
    Type of the result, must be mpeg4_gif
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    mpeg4_url: str
    """
    A valid URL for the MPEG4 file
    """

    mpeg4_width: int | None = None
    """
    Video width
    """

    mpeg4_height: int | None = None
    """
    Video height
    """

    mpeg4_duration: int | None = None
    """
    Video duration in seconds
    """

    thumbnail_url: str
    """
    URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    """

    thumbnail_mime_type: str | None = None
    """
    MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or
    "video/mp4". Defaults to "image/jpeg".
    """

    title: str | None = None
    """
    Title for the result
    """

    caption: str | None = None
    """
    Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the caption. See formatting options for more details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    show_caption_above_media: bool | None = None
    """
    Pass True if the caption must be shown above the message media
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the video animation
    """


class InlineQueryResultVideo(TelegramObject):
    """
    Represents a link to a page containing an embedded video player or a video file. By
    default, this video file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message with the
    specified content instead of the video.
    """

    type: Literal["video"] = "video"
    """
    Type of the result, must be video
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    video_url: str
    """
    A valid URL for the embedded video player or video file
    """

    mime_type: str
    """
    MIME type of the content of the video URL, "text/html" or "video/mp4"
    """

    thumbnail_url: str
    """
    URL of the thumbnail (JPEG only) for the video
    """

    title: str
    """
    Title for the result
    """

    caption: str | None = None
    """
    Caption of the video to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the video caption. See formatting options for more
    details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    show_caption_above_media: bool | None = None
    """
    Pass True if the caption must be shown above the message media
    """

    video_width: int | None = None
    """
    Video width
    """

    video_height: int | None = None
    """
    Video height
    """

    video_duration: int | None = None
    """
    Video duration in seconds
    """

    description: str | None = None
    """
    Short description of the result
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the video. This field is required if
    InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube
    video).
    """


class InlineQueryResultAudio(TelegramObject):
    """
    Represents a link to an MP3 audio file. By default, this audio file will be sent by
    the user. Alternatively, you can use input_message_content to send a message with
    the specified content instead of the audio.
    """

    type: Literal["audio"] = "audio"
    """
    Type of the result, must be audio
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    audio_url: str
    """
    A valid URL for the audio file
    """

    title: str
    """
    Title
    """

    caption: str | None = None
    """
    Caption, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the audio caption. See formatting options for more
    details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    performer: str | None = None
    """
    Performer
    """

    audio_duration: int | None = None
    """
    Audio duration in seconds
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the audio
    """


class InlineQueryResultVoice(TelegramObject):
    """
    Represents a link to a voice recording in an .OGG container encoded with OPUS. By
    default, this voice recording will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    the voice message.
    """

    type: Literal["voice"] = "voice"
    """
    Type of the result, must be voice
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    voice_url: str
    """
    A valid URL for the voice recording
    """

    title: str
    """
    Recording title
    """

    caption: str | None = None
    """
    Caption, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the voice message caption. See formatting options for
    more details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    voice_duration: int | None = None
    """
    Recording duration in seconds
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the voice recording
    """


class InlineQueryResultDocument(TelegramObject):
    """
    Represents a link to a file. By default, this file will be sent by the user with an
    optional caption. Alternatively, you can use input_message_content to send a message
    with the specified content instead of the file. Currently, only .PDF and .ZIP files
    can be sent using this method.
    """

    type: Literal["document"] = "document"
    """
    Type of the result, must be document
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    title: str
    """
    Title for the result
    """

    caption: str | None = None
    """
    Caption of the document to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the document caption. See formatting options for more
    details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    document_url: str
    """
    A valid URL for the file
    """

    mime_type: str
    """
    MIME type of the content of the file, either "application/pdf" or "application/zip"
    """

    description: str | None = None
    """
    Short description of the result
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the file
    """

    thumbnail_url: str | None = None
    """
    URL of the thumbnail (JPEG only) for the file
    """

    thumbnail_width: int | None = None
    """
    Thumbnail width
    """

    thumbnail_height: int | None = None
    """
    Thumbnail height
    """


class InlineQueryResultLocation(TelegramObject):
    """
    Represents a location on a map. By default, the location will be sent by the user.
    Alternatively, you can use input_message_content to send a message with the
    specified content instead of the location.
    """

    type: Literal["location"] = "location"
    """
    Type of the result, must be location
    """

    id: str
    """
    Unique identifier for this result, 1-64 Bytes
    """

    latitude: float
    """
    Location latitude in degrees
    """

    longitude: float
    """
    Location longitude in degrees
    """

    title: str
    """
    Location title
    """

    horizontal_accuracy: float | None = None
    """
    The radius of uncertainty for the location, measured in meters; 0-1500
    """

    live_period: int | None = None
    """
    Period in seconds during which the location can be updated, must be between 60 and
    86400, or 0x7FFFFFFF for live locations that can be edited indefinitely
    """

    heading: int | None = None
    """
    For live locations, a direction in which the user is moving, in degrees. Must be
    between 1 and 360 if specified.
    """

    proximity_alert_radius: int | None = None
    """
    For live locations, a maximum distance for proximity alerts about approaching
    another chat member, in meters. Must be between 1 and 100000 if specified.
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the location
    """

    thumbnail_url: str | None = None
    """
    Url of the thumbnail for the result
    """

    thumbnail_width: int | None = None
    """
    Thumbnail width
    """

    thumbnail_height: int | None = None
    """
    Thumbnail height
    """


class InlineQueryResultVenue(TelegramObject):
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively,
    you can use input_message_content to send a message with the specified content
    instead of the venue.
    """

    type: Literal["venue"] = "venue"
    """
    Type of the result, must be venue
    """

    id: str
    """
    Unique identifier for this result, 1-64 Bytes
    """

    latitude: float
    """
    Latitude of the venue location in degrees
    """

    longitude: float
    """
    Longitude of the venue location in degrees
    """

    title: str
    """
    Title of the venue
    """

    address: str
    """
    Address of the venue
    """

    foursquare_id: str | None = None
    """
    Foursquare identifier of the venue if known
    """

    foursquare_type: str | None = None
    """
    Foursquare type of the venue, if known. (For example, "arts_entertainment/default",
    "arts_entertainment/aquarium" or "food/icecream".)
    """

    google_place_id: str | None = None
    """
    Google Places identifier of the venue
    """

    google_place_type: str | None = None
    """
    Google Places type of the venue. (See supported types.)
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the venue
    """

    thumbnail_url: str | None = None
    """
    Url of the thumbnail for the result
    """

    thumbnail_width: int | None = None
    """
    Thumbnail width
    """

    thumbnail_height: int | None = None
    """
    Thumbnail height
    """


class InlineQueryResultContact(TelegramObject):
    """
    Represents a contact with a phone number. By default, this contact will be sent by
    the user. Alternatively, you can use input_message_content to send a message with
    the specified content instead of the contact.
    """

    type: Literal["contact"] = "contact"
    """
    Type of the result, must be contact
    """

    id: str
    """
    Unique identifier for this result, 1-64 Bytes
    """

    phone_number: str
    """
    Contact's phone number
    """

    first_name: str
    """
    Contact's first name
    """

    last_name: str | None = None
    """
    Contact's last name
    """

    vcard: str | None = None
    """
    Additional data about the contact in the form of a vCard, 0-2048 bytes
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the contact
    """

    thumbnail_url: str | None = None
    """
    Url of the thumbnail for the result
    """

    thumbnail_width: int | None = None
    """
    Thumbnail width
    """

    thumbnail_height: int | None = None
    """
    Thumbnail height
    """


class InlineQueryResultGame(TelegramObject):
    """
    Represents a Game.
    """

    type: Literal["game"] = "game"
    """
    Type of the result, must be game
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    game_short_name: str
    """
    Short name of the game
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """


class InlineQueryResultCachedPhoto(TelegramObject):
    """
    Represents a link to a photo stored on the Telegram servers. By default, this photo
    will be sent by the user with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    photo.
    """

    type: Literal["photo"] = "photo"
    """
    Type of the result, must be photo
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    photo_file_id: str
    """
    A valid file identifier of the photo
    """

    title: str | None = None
    """
    Title for the result
    """

    description: str | None = None
    """
    Short description of the result
    """

    caption: str | None = None
    """
    Caption of the photo to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the photo caption. See formatting options for more
    details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    show_caption_above_media: bool | None = None
    """
    Pass True if the caption must be shown above the message media
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the photo
    """


class InlineQueryResultCachedGif(TelegramObject):
    """
    Represents a link to an animated GIF file stored on the Telegram servers. By
    default, this animated GIF file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message with specified
    content instead of the animation.
    """

    type: Literal["gif"] = "gif"
    """
    Type of the result, must be gif
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    gif_file_id: str
    """
    A valid file identifier for the GIF file
    """

    title: str | None = None
    """
    Title for the result
    """

    caption: str | None = None
    """
    Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the caption. See formatting options for more details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    show_caption_above_media: bool | None = None
    """
    Pass True if the caption must be shown above the message media
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the GIF animation
    """


class InlineQueryResultCachedMpeg4Gif(TelegramObject):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored
    on the Telegram servers. By default, this animated MPEG-4 file will be sent by the
    user with an optional caption. Alternatively, you can use input_message_content to
    send a message with the specified content instead of the animation.
    """

    type: Literal["mpeg4_gif"] = "mpeg4_gif"
    """
    Type of the result, must be mpeg4_gif
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    mpeg4_file_id: str
    """
    A valid file identifier for the MPEG4 file
    """

    title: str | None = None
    """
    Title for the result
    """

    caption: str | None = None
    """
    Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the caption. See formatting options for more details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    show_caption_above_media: bool | None = None
    """
    Pass True if the caption must be shown above the message media
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the video animation
    """


class InlineQueryResultCachedSticker(TelegramObject):
    """
    Represents a link to a sticker stored on the Telegram servers. By default, this
    sticker will be sent by the user. Alternatively, you can use input_message_content
    to send a message with the specified content instead of the sticker.
    """

    type: Literal["sticker"] = "sticker"
    """
    Type of the result, must be sticker
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    sticker_file_id: str
    """
    A valid file identifier of the sticker
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the sticker
    """


class InlineQueryResultCachedDocument(TelegramObject):
    """
    Represents a link to a file stored on the Telegram servers. By default, this file
    will be sent by the user with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    file.
    """

    type: Literal["document"] = "document"
    """
    Type of the result, must be document
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    title: str
    """
    Title for the result
    """

    document_file_id: str
    """
    A valid file identifier for the file
    """

    description: str | None = None
    """
    Short description of the result
    """

    caption: str | None = None
    """
    Caption of the document to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the document caption. See formatting options for more
    details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the file
    """


class InlineQueryResultCachedVideo(TelegramObject):
    """
    Represents a link to a video file stored on the Telegram servers. By default, this
    video file will be sent by the user with an optional caption. Alternatively, you can
    use input_message_content to send a message with the specified content instead of
    the video.
    """

    type: Literal["video"] = "video"
    """
    Type of the result, must be video
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    video_file_id: str
    """
    A valid file identifier for the video file
    """

    title: str
    """
    Title for the result
    """

    description: str | None = None
    """
    Short description of the result
    """

    caption: str | None = None
    """
    Caption of the video to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the video caption. See formatting options for more
    details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    show_caption_above_media: bool | None = None
    """
    Pass True if the caption must be shown above the message media
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the video
    """


class InlineQueryResultCachedVoice(TelegramObject):
    """
    Represents a link to a voice message stored on the Telegram servers. By default,
    this voice message will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    voice message.
    """

    type: Literal["voice"] = "voice"
    """
    Type of the result, must be voice
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    voice_file_id: str
    """
    A valid file identifier for the voice message
    """

    title: str
    """
    Voice message title
    """

    caption: str | None = None
    """
    Caption, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the voice message caption. See formatting options for
    more details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the voice message
    """


class InlineQueryResultCachedAudio(TelegramObject):
    """
    Represents a link to an MP3 audio file stored on the Telegram servers. By default,
    this audio file will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    audio.
    """

    type: Literal["audio"] = "audio"
    """
    Type of the result, must be audio
    """

    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """

    audio_file_id: str
    """
    A valid file identifier for the audio file
    """

    caption: str | None = None
    """
    Caption, 0-1024 characters after entities parsing
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the audio caption. See formatting options for more
    details.
    """

    caption_entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in the caption, which can be specified instead
    of parse_mode
    """

    reply_markup: InlineKeyboardMarkup | None = None
    """
    Inline keyboard attached to the message
    """

    input_message_content: InputMessageContent | None = None
    """
    Content of the message to be sent instead of the audio
    """


type InputMessageContent = (
    InputTextMessageContent
    | InputRichMessageContent
    | InputLocationMessageContent
    | InputVenueMessageContent
    | InputContactMessageContent
    | InputInvoiceMessageContent
)


class InputTextMessageContent(TelegramObject):
    """
    Represents the content of a text message to be sent as the result of an inline
    query.
    """

    message_text: str
    """
    Text of the message to be sent, 1-4096 characters
    """

    parse_mode: str | None = None
    """
    Mode for parsing entities in the message text. See formatting options for more
    details.
    """

    entities: list[MessageEntity] | None = None
    """
    List of special entities that appear in message text, which can be specified instead
    of parse_mode
    """

    link_preview_options: LinkPreviewOptions | None = None
    """
    Link preview generation options for the message
    """


class InputRichMessageContent(TelegramObject):
    """
    Represents the content of a rich message to be sent as the result of an inline
    query.
    """

    rich_message: InputRichMessage
    """
    The message to be sent. Only previously uploaded files may be used in the message.
    """


class InputLocationMessageContent(TelegramObject):
    """
    Represents the content of a location message to be sent as the result of an inline
    query.
    """

    latitude: float
    """
    Latitude of the location in degrees
    """

    longitude: float
    """
    Longitude of the location in degrees
    """

    horizontal_accuracy: float | None = None
    """
    The radius of uncertainty for the location, measured in meters; 0-1500
    """

    live_period: int | None = None
    """
    Period in seconds during which the location can be updated, must be between 60 and
    86400, or 0x7FFFFFFF for live locations that can be edited indefinitely
    """

    heading: int | None = None
    """
    For live locations, a direction in which the user is moving, in degrees. Must be
    between 1 and 360 if specified.
    """

    proximity_alert_radius: int | None = None
    """
    For live locations, a maximum distance for proximity alerts about approaching
    another chat member, in meters. Must be between 1 and 100000 if specified.
    """


class InputVenueMessageContent(TelegramObject):
    """
    Represents the content of a venue message to be sent as the result of an inline
    query.
    """

    latitude: float
    """
    Latitude of the venue in degrees
    """

    longitude: float
    """
    Longitude of the venue in degrees
    """

    title: str
    """
    Name of the venue
    """

    address: str
    """
    Address of the venue
    """

    foursquare_id: str | None = None
    """
    Foursquare identifier of the venue, if known
    """

    foursquare_type: str | None = None
    """
    Foursquare type of the venue, if known. (For example, "arts_entertainment/default",
    "arts_entertainment/aquarium" or "food/icecream".)
    """

    google_place_id: str | None = None
    """
    Google Places identifier of the venue
    """

    google_place_type: str | None = None
    """
    Google Places type of the venue. (See supported types.)
    """


class InputContactMessageContent(TelegramObject):
    """
    Represents the content of a contact message to be sent as the result of an inline
    query.
    """

    phone_number: str
    """
    Contact's phone number
    """

    first_name: str
    """
    Contact's first name
    """

    last_name: str | None = None
    """
    Contact's last name
    """

    vcard: str | None = None
    """
    Additional data about the contact in the form of a vCard, 0-2048 bytes
    """


class InputInvoiceMessageContent(TelegramObject):
    """
    Represents the content of an invoice message to be sent as the result of an inline
    query.
    """

    title: str
    """
    Product name, 1-32 characters
    """

    description: str
    """
    Product description, 1-255 characters
    """

    payload: str
    """
    Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user,
    use it for your internal processes.
    """

    provider_token: str | None = None
    """
    Payment provider token, obtained via @BotFather. Pass an empty string for payments
    in Telegram Stars.
    """

    currency: str
    """
    Three-letter ISO 4217 currency code, see more on currencies. Pass "XTR" for payments
    in Telegram Stars.
    """

    prices: list[LabeledPrice]
    """
    Price breakdown, a JSON-serialized list of components (e.g. product price, tax,
    discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item
    for payments in Telegram Stars.
    """

    max_tip_amount: int | None = None
    """
    The maximum accepted amount for tips in the smallest units of the currency (integer,
    not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount =
    145. See the exp parameter in currencies.json, it shows the number of digits past
    the decimal point for each currency (2 for the majority of currencies). Defaults to
    0. Not supported for payments in Telegram Stars.
    """

    suggested_tip_amounts: list[int] | None = None
    """
    A JSON-serialized Array of suggested amounts of tip in the smallest units of the
    currency (integer, not float/double). At most 4 suggested tip amounts can be
    specified. The suggested tip amounts must be positive, passed in a strictly
    increased order and must not exceed max_tip_amount.
    """

    provider_data: str | None = None
    """
    A JSON-serialized object for data about the invoice, which will be shared with the
    payment provider. A detailed description of the required fields should be provided
    by the payment provider.
    """

    photo_url: str | None = None
    """
    URL of the product photo for the invoice. Can be a photo of the goods or a marketing
    image for a service.
    """

    photo_size: int | None = None
    """
    Photo size in bytes
    """

    photo_width: int | None = None
    """
    Photo width
    """

    photo_height: int | None = None
    """
    Photo height
    """

    need_name: bool | None = None
    """
    Pass True if you require the user's full name to complete the order. Ignored for
    payments in Telegram Stars.
    """

    need_phone_number: bool | None = None
    """
    Pass True if you require the user's phone number to complete the order. Ignored for
    payments in Telegram Stars.
    """

    need_email: bool | None = None
    """
    Pass True if you require the user's email address to complete the order. Ignored for
    payments in Telegram Stars.
    """

    need_shipping_address: bool | None = None
    """
    Pass True if you require the user's shipping address to complete the order. Ignored
    for payments in Telegram Stars.
    """

    send_phone_number_to_provider: bool | None = None
    """
    Pass True if the user's phone number should be sent to the provider. Ignored for
    payments in Telegram Stars.
    """

    send_email_to_provider: bool | None = None
    """
    Pass True if the user's email address should be sent to the provider. Ignored for
    payments in Telegram Stars.
    """

    is_flexible: bool | None = None
    """
    Pass True if the final price depends on the shipping method. Ignored for payments in
    Telegram Stars.
    """


class ChosenInlineResult(TelegramObject):
    """
    Represents a result of an inline query that was chosen by the user and sent to their
    chat partner.
    Note: It is necessary to enable inline feedback via @BotFather in order to receive
    these objects in updates.
    """

    result_id: str
    """
    The unique identifier for the result that was chosen
    """

    from_: User = Field(alias="from")
    """
    The user that chose the result
    """

    location: Location | None = None
    """
    Sender location, only for bots that require user location
    """

    inline_message_id: str | None = None
    """
    Identifier of the sent inline message. Available only if there is an inline keyboard
    attached to the message. Will be also received in callback queries and can be used
    to edit the message.
    """

    query: str
    """
    The query that was used to obtain the result
    """


class LabeledPrice(TelegramObject):
    """
    This object represents a portion of the price for goods or services.
    """

    label: str
    """
    Portion label
    """

    amount: int
    """
    Price of the product in the smallest units of the currency (integer, not
    float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp
    parameter in currencies.json, it shows the number of digits past the decimal point
    for each currency (2 for the majority of currencies).
    """


class Invoice(TelegramObject):
    """
    This object contains basic information about an invoice.
    """

    title: str
    """
    Product name
    """

    description: str
    """
    Product description
    """

    start_parameter: str
    """
    Unique bot deep-linking parameter that can be used to generate this invoice
    """

    currency: str
    """
    Three-letter ISO 4217 currency code, or "XTR" for payments in Telegram Stars
    """

    total_amount: int
    """
    Total price in the smallest units of the currency (integer, not float/double). For
    example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in
    currencies.json, it shows the number of digits past the decimal point for each
    currency (2 for the majority of currencies).
    """


class ShippingAddress(TelegramObject):
    """
    This object represents a shipping address.
    """

    country_code: str
    """
    Two-letter ISO 3166-1 alpha-2 country code
    """

    state: str
    """
    State, if applicable
    """

    city: str
    """
    City
    """

    street_line1: str
    """
    First line for the address
    """

    street_line2: str
    """
    Second line for the address
    """

    post_code: str
    """
    Address post code
    """


class OrderInfo(TelegramObject):
    """
    This object represents information about an order.
    """

    name: str | None = None
    """
    User name
    """

    phone_number: str | None = None
    """
    User's phone number
    """

    email: str | None = None
    """
    User email
    """

    shipping_address: ShippingAddress | None = None
    """
    User shipping address
    """


class ShippingOption(TelegramObject):
    """
    This object represents one shipping option.
    """

    id: str
    """
    Shipping option identifier
    """

    title: str
    """
    Option title
    """

    prices: list[LabeledPrice]
    """
    List of price portions
    """


class SuccessfulPayment(TelegramObject):
    """
    This object contains basic information about a successful payment. Note that if the
    buyer initiates a chargeback with the relevant payment provider following this
    transaction, the funds may be debited from your balance. This is outside of
    Telegram's control.
    """

    currency: str
    """
    Three-letter ISO 4217 currency code, or "XTR" for payments in Telegram Stars
    """

    total_amount: int
    """
    Total price in the smallest units of the currency (integer, not float/double). For
    example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in
    currencies.json, it shows the number of digits past the decimal point for each
    currency (2 for the majority of currencies).
    """

    invoice_payload: str
    """
    Bot-specified invoice payload
    """

    subscription_expiration_date: int | None = None
    """
    Expiration date of the subscription, in Unix time; for recurring payments only
    """

    is_recurring: bool | None = None
    """
    True, if the payment is a recurring payment for a subscription
    """

    is_first_recurring: bool | None = None
    """
    True, if the payment is the first payment for a subscription
    """

    shipping_option_id: str | None = None
    """
    Identifier of the shipping option chosen by the user
    """

    order_info: OrderInfo | None = None
    """
    Order information provided by the user
    """

    telegram_payment_charge_id: str
    """
    Telegram payment identifier
    """

    provider_payment_charge_id: str
    """
    Provider payment identifier
    """


class RefundedPayment(TelegramObject):
    """
    This object contains basic information about a refunded payment.
    """

    currency: str
    """
    Three-letter ISO 4217 currency code, or "XTR" for payments in Telegram Stars.
    Currently, always "XTR".
    """

    total_amount: int
    """
    Total refunded price in the smallest units of the currency (integer, not
    float/double). For example, for a price of US$ 1.45, total_amount = 145. See the exp
    parameter in currencies.json, it shows the number of digits past the decimal point
    for each currency (2 for the majority of currencies).
    """

    invoice_payload: str
    """
    Bot-specified invoice payload
    """

    telegram_payment_charge_id: str
    """
    Telegram payment identifier
    """

    provider_payment_charge_id: str | None = None
    """
    Provider payment identifier
    """


class ShippingQuery(TelegramObject):
    """
    This object contains information about an incoming shipping query.
    """

    id: str
    """
    Unique query identifier
    """

    from_: User = Field(alias="from")
    """
    User who sent the query
    """

    invoice_payload: str
    """
    Bot-specified invoice payload
    """

    shipping_address: ShippingAddress
    """
    User specified shipping address
    """


class PreCheckoutQuery(TelegramObject):
    """
    This object contains information about an incoming pre-checkout query.
    """

    id: str
    """
    Unique query identifier
    """

    from_: User = Field(alias="from")
    """
    User who sent the query
    """

    currency: str
    """
    Three-letter ISO 4217 currency code, or "XTR" for payments in Telegram Stars
    """

    total_amount: int
    """
    Total price in the smallest units of the currency (integer, not float/double). For
    example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in
    currencies.json, it shows the number of digits past the decimal point for each
    currency (2 for the majority of currencies).
    """

    invoice_payload: str
    """
    Bot-specified invoice payload
    """

    shipping_option_id: str | None = None
    """
    Identifier of the shipping option chosen by the user
    """

    order_info: OrderInfo | None = None
    """
    Order information provided by the user
    """


class PaidMediaPurchased(TelegramObject):
    """
    This object contains information about a paid media purchase.
    """

    from_: User = Field(alias="from")
    """
    User who purchased the media
    """

    paid_media_payload: str
    """
    Bot-specified paid media payload
    """


type RevenueWithdrawalState = Annotated[
    RevenueWithdrawalStatePending
    | RevenueWithdrawalStateSucceeded
    | RevenueWithdrawalStateFailed,
    Field(discriminator="type"),
]


class RevenueWithdrawalStatePending(TelegramObject):
    """
    The withdrawal is in progress.
    """

    type: Literal["pending"] = "pending"
    """
    Type of the state, always "pending"
    """


class RevenueWithdrawalStateSucceeded(TelegramObject):
    """
    The withdrawal succeeded.
    """

    type: Literal["succeeded"] = "succeeded"
    """
    Type of the state, always "succeeded"
    """

    date: int
    """
    Date the withdrawal was completed in Unix time
    """

    url: str
    """
    An HTTPS URL that can be used to see transaction details
    """


class RevenueWithdrawalStateFailed(TelegramObject):
    """
    The withdrawal failed and the transaction was refunded.
    """

    type: Literal["failed"] = "failed"
    """
    Type of the state, always "failed"
    """


class AffiliateInfo(TelegramObject):
    """
    Contains information about the affiliate that received a commission via this
    transaction.
    """

    affiliate_user: User | None = None
    """
    The bot or the user that received an affiliate commission if it was received by a
    bot or a user
    """

    affiliate_chat: Chat | None = None
    """
    The chat that received an affiliate commission if it was received by a chat
    """

    commission_per_mille: int
    """
    The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars
    received by the bot from referred users
    """

    amount: int
    """
    Integer amount of Telegram Stars received by the affiliate from the transaction,
    rounded to 0; can be negative for refunds
    """

    nanostar_amount: int | None = None
    """
    The number of 1/1000000000 shares of Telegram Stars received by the affiliate; from
    -999999999 to 999999999; can be negative for refunds
    """


type TransactionPartner = Annotated[
    TransactionPartnerUser
    | TransactionPartnerChat
    | TransactionPartnerAffiliateProgram
    | TransactionPartnerFragment
    | TransactionPartnerTelegramAds
    | TransactionPartnerTelegramApi
    | TransactionPartnerOther,
    Field(discriminator="type"),
]


class TransactionPartnerUser(TelegramObject):
    """
    Describes a transaction with a user.
    """

    type: Literal["user"] = "user"
    """
    Type of the transaction partner, always "user"
    """

    transaction_type: str
    """
    Type of the transaction, currently one of "invoice_payment" for payments via
    invoices, "paid_media_payment" for payments for paid media, "gift_purchase" for
    gifts sent by the bot, "premium_purchase" for Telegram Premium subscriptions gifted
    by the bot, "business_account_transfer" for direct transfers from managed business
    accounts
    """

    user: User
    """
    Information about the user
    """

    affiliate: AffiliateInfo | None = None
    """
    Information about the affiliate that received a commission via this transaction. Can
    be available only for "invoice_payment" and "paid_media_payment" transactions.
    """

    invoice_payload: str | None = None
    """
    Bot-specified invoice payload. Can be available only for "invoice_payment"
    transactions.
    """

    subscription_period: int | None = None
    """
    The duration of the paid subscription. Can be available only for "invoice_payment"
    transactions.
    """

    paid_media: list[PaidMedia] | None = None
    """
    Information about the paid media bought by the user; for "paid_media_payment"
    transactions only
    """

    paid_media_payload: str | None = None
    """
    Bot-specified paid media payload. Can be available only for "paid_media_payment"
    transactions.
    """

    gift: Gift | None = None
    """
    The gift sent to the user by the bot; for "gift_purchase" transactions only
    """

    premium_subscription_duration: int | None = None
    """
    Number of months the gifted Telegram Premium subscription will be active for; for
    "premium_purchase" transactions only
    """


class TransactionPartnerChat(TelegramObject):
    """
    Describes a transaction with a chat.
    """

    type: Literal["chat"] = "chat"
    """
    Type of the transaction partner, always "chat"
    """

    chat: Chat
    """
    Information about the chat
    """

    gift: Gift | None = None
    """
    The gift sent to the chat by the bot
    """


class TransactionPartnerAffiliateProgram(TelegramObject):
    """
    Describes the affiliate program that issued the affiliate commission received via
    this transaction.
    """

    type: Literal["affiliate_program"] = "affiliate_program"
    """
    Type of the transaction partner, always "affiliate_program"
    """

    sponsor_user: User | None = None
    """
    Information about the bot that sponsored the affiliate program
    """

    commission_per_mille: int
    """
    The number of Telegram Stars received by the bot for each 1000 Telegram Stars
    received by the affiliate program sponsor from referred users
    """


class TransactionPartnerFragment(TelegramObject):
    """
    Describes a withdrawal transaction with Fragment.
    """

    type: Literal["fragment"] = "fragment"
    """
    Type of the transaction partner, always "fragment"
    """

    withdrawal_state: RevenueWithdrawalState | None = None
    """
    State of the transaction if the transaction is outgoing
    """


class TransactionPartnerTelegramAds(TelegramObject):
    """
    Describes a withdrawal transaction to the Telegram Ads platform.
    """

    type: Literal["telegram_ads"] = "telegram_ads"
    """
    Type of the transaction partner, always "telegram_ads"
    """


class TransactionPartnerTelegramApi(TelegramObject):
    """
    Describes a transaction with payment for paid broadcasting.
    """

    type: Literal["telegram_api"] = "telegram_api"
    """
    Type of the transaction partner, always "telegram_api"
    """

    request_count: int
    """
    The number of successful requests that exceeded regular limits and were therefore
    billed
    """


class TransactionPartnerOther(TelegramObject):
    """
    Describes a transaction with an unknown source or recipient.
    """

    type: Literal["other"] = "other"
    """
    Type of the transaction partner, always "other"
    """


class StarTransaction(TelegramObject):
    """
    Describes a Telegram Star transaction. Note that if the buyer initiates a chargeback
    with the payment provider from whom they acquired Stars (e.g., Apple, Google)
    following this transaction, the refunded Stars will be deducted from the bot's
    balance. This is outside of Telegram's control.
    """

    id: str
    """
    Unique identifier of the transaction. Coincides with the identifier of the original
    transaction for refund transactions. Coincides with
    SuccessfulPayment.telegram_payment_charge_id for successful incoming payments from
    users.
    """

    amount: int
    """
    Integer amount of Telegram Stars transferred by the transaction
    """

    nanostar_amount: int | None = None
    """
    The number of 1/1000000000 shares of Telegram Stars transferred by the transaction;
    from 0 to 999999999
    """

    date: int
    """
    Date the transaction was created in Unix time
    """

    source: TransactionPartner | None = None
    """
    Source of an incoming transaction (e.g., a user purchasing goods or services,
    Fragment refunding a failed withdrawal). Only for incoming transactions.
    """

    receiver: TransactionPartner | None = None
    """
    Receiver of an outgoing transaction (e.g., a user for a purchase refund, Fragment
    for a withdrawal). Only for outgoing transactions.
    """


class StarTransactions(TelegramObject):
    """
    Contains a list of Telegram Star transactions.
    """

    transactions: list[StarTransaction]
    """
    The list of transactions
    """


class PassportData(TelegramObject):
    """
    Describes Telegram Passport data shared with the bot by the user.
    """

    data: list[EncryptedPassportElement]
    """
    Array with information about documents and other Telegram Passport elements that was
    shared with the bot
    """

    credentials: EncryptedCredentials
    """
    Encrypted credentials required to decrypt the data
    """


class PassportFile(TelegramObject):
    """
    This object represents a file uploaded to Telegram Passport. Currently all Telegram
    Passport files are in JPEG format when decrypted and don't exceed 10MB.
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """

    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    """

    file_size: int
    """
    File size in bytes
    """

    file_date: int
    """
    Unix time when the file was uploaded
    """


class EncryptedPassportElement(TelegramObject):
    """
    Describes documents or other Telegram Passport elements shared with the bot by the
    user.
    """

    type: str
    """
    Element type. One of "personal_details", "passport", "driver_license",
    "identity_card", "internal_passport", "address", "utility_bill", "bank_statement",
    "rental_agreement", "passport_registration", "temporary_registration",
    "phone_number", "email".
    """

    data: str | None = None
    """
    Base64-encoded encrypted Telegram Passport element data provided by the user;
    available only for "personal_details", "passport", "driver_license",
    "identity_card", "internal_passport" and "address" types. Can be decrypted and
    verified using the accompanying EncryptedCredentials.
    """

    phone_number: str | None = None
    """
    User's verified phone number; available only for "phone_number" type
    """

    email: str | None = None
    """
    User's verified email address; available only for "email" type
    """

    files: list[PassportFile] | None = None
    """
    Array of encrypted files with documents provided by the user; available only for
    "utility_bill", "bank_statement", "rental_agreement", "passport_registration" and
    "temporary_registration" types. Files can be decrypted and verified using the
    accompanying EncryptedCredentials.
    """

    front_side: PassportFile | None = None
    """
    Encrypted file with the front side of the document, provided by the user; available
    only for "passport", "driver_license", "identity_card" and "internal_passport". The
    file can be decrypted and verified using the accompanying EncryptedCredentials.
    """

    reverse_side: PassportFile | None = None
    """
    Encrypted file with the reverse side of the document, provided by the user;
    available only for "driver_license" and "identity_card". The file can be decrypted
    and verified using the accompanying EncryptedCredentials.
    """

    selfie: PassportFile | None = None
    """
    Encrypted file with the selfie of the user holding a document, provided by the user;
    available if requested for "passport", "driver_license", "identity_card" and
    "internal_passport". The file can be decrypted and verified using the accompanying
    EncryptedCredentials.
    """

    translation: list[PassportFile] | None = None
    """
    Array of encrypted files with translated versions of documents provided by the user;
    available if requested for "passport", "driver_license", "identity_card",
    "internal_passport", "utility_bill", "bank_statement", "rental_agreement",
    "passport_registration" and "temporary_registration" types. Files can be decrypted
    and verified using the accompanying EncryptedCredentials.
    """

    hash: str
    """
    Base64-encoded element hash for using in PassportElementErrorUnspecified
    """


class EncryptedCredentials(TelegramObject):
    """
    Describes data required for decrypting and authenticating EncryptedPassportElement.
    See the Telegram Passport Documentation for a complete description of the data
    decryption and authentication processes.
    """

    data: str
    """
    Base64-encoded encrypted JSON-serialized data with unique user's payload, data
    hashes and secrets required for EncryptedPassportElement decryption and
    authentication
    """

    hash: str
    """
    Base64-encoded data hash for data authentication
    """

    secret: str
    """
    Base64-encoded secret, encrypted with the bot's public RSA key, required for data
    decryption
    """


type PassportElementError = Annotated[
    PassportElementErrorDataField
    | PassportElementErrorFrontSide
    | PassportElementErrorReverseSide
    | PassportElementErrorSelfie
    | PassportElementErrorFile
    | PassportElementErrorFiles
    | PassportElementErrorTranslationFile
    | PassportElementErrorTranslationFiles
    | PassportElementErrorUnspecified,
    Field(discriminator="source"),
]


class PassportElementErrorDataField(TelegramObject):
    """
    Represents an issue in one of the data fields that was provided by the user. The
    error is considered resolved when the field's value changes.
    """

    source: Literal["data"] = "data"
    """
    Error source, must be data
    """

    type: str
    """
    The section of the user's Telegram Passport which has the error, one of
    "personal_details", "passport", "driver_license", "identity_card",
    "internal_passport", "address"
    """

    field_name: str
    """
    Name of the data field which has the error
    """

    data_hash: str
    """
    Base64-encoded data hash
    """

    message: str
    """
    Error message
    """


class PassportElementErrorFrontSide(TelegramObject):
    """
    Represents an issue with the front side of a document. The error is considered
    resolved when the file with the front side of the document changes.
    """

    source: Literal["front_side"] = "front_side"
    """
    Error source, must be front_side
    """

    type: str
    """
    The section of the user's Telegram Passport which has the issue, one of "passport",
    "driver_license", "identity_card", "internal_passport"
    """

    file_hash: str
    """
    Base64-encoded hash of the file with the front side of the document
    """

    message: str
    """
    Error message
    """


class PassportElementErrorReverseSide(TelegramObject):
    """
    Represents an issue with the reverse side of a document. The error is considered
    resolved when the file with reverse side of the document changes.
    """

    source: Literal["reverse_side"] = "reverse_side"
    """
    Error source, must be reverse_side
    """

    type: str
    """
    The section of the user's Telegram Passport which has the issue, one of
    "driver_license", "identity_card"
    """

    file_hash: str
    """
    Base64-encoded hash of the file with the reverse side of the document
    """

    message: str
    """
    Error message
    """


class PassportElementErrorSelfie(TelegramObject):
    """
    Represents an issue with the selfie with a document. The error is considered
    resolved when the file with the selfie changes.
    """

    source: Literal["selfie"] = "selfie"
    """
    Error source, must be selfie
    """

    type: str
    """
    The section of the user's Telegram Passport which has the issue, one of "passport",
    "driver_license", "identity_card", "internal_passport"
    """

    file_hash: str
    """
    Base64-encoded hash of the file with the selfie
    """

    message: str
    """
    Error message
    """


class PassportElementErrorFile(TelegramObject):
    """
    Represents an issue with a document scan. The error is considered resolved when the
    file with the document scan changes.
    """

    source: Literal["file"] = "file"
    """
    Error source, must be file
    """

    type: str
    """
    The section of the user's Telegram Passport which has the issue, one of
    "utility_bill", "bank_statement", "rental_agreement", "passport_registration",
    "temporary_registration"
    """

    file_hash: str
    """
    Base64-encoded file hash
    """

    message: str
    """
    Error message
    """


class PassportElementErrorFiles(TelegramObject):
    """
    Represents an issue with a list of scans. The error is considered resolved when the
    list of files containing the scans changes.
    """

    source: Literal["files"] = "files"
    """
    Error source, must be files
    """

    type: str
    """
    The section of the user's Telegram Passport which has the issue, one of
    "utility_bill", "bank_statement", "rental_agreement", "passport_registration",
    "temporary_registration"
    """

    file_hashes: list[str]
    """
    List of base64-encoded file hashes
    """

    message: str
    """
    Error message
    """


class PassportElementErrorTranslationFile(TelegramObject):
    """
    Represents an issue with one of the files that constitute the translation of a
    document. The error is considered resolved when the file changes.
    """

    source: Literal["translation_file"] = "translation_file"
    """
    Error source, must be translation_file
    """

    type: str
    """
    Type of element of the user's Telegram Passport which has the issue, one of
    "passport", "driver_license", "identity_card", "internal_passport", "utility_bill",
    "bank_statement", "rental_agreement", "passport_registration",
    "temporary_registration"
    """

    file_hash: str
    """
    Base64-encoded file hash
    """

    message: str
    """
    Error message
    """


class PassportElementErrorTranslationFiles(TelegramObject):
    """
    Represents an issue with the translated version of a document. The error is
    considered resolved when a file with the document translation change.
    """

    source: Literal["translation_files"] = "translation_files"
    """
    Error source, must be translation_files
    """

    type: str
    """
    Type of element of the user's Telegram Passport which has the issue, one of
    "passport", "driver_license", "identity_card", "internal_passport", "utility_bill",
    "bank_statement", "rental_agreement", "passport_registration",
    "temporary_registration"
    """

    file_hashes: list[str]
    """
    List of base64-encoded file hashes
    """

    message: str
    """
    Error message
    """


class PassportElementErrorUnspecified(TelegramObject):
    """
    Represents an issue in an unspecified place. The error is considered resolved when
    new data is added.
    """

    source: Literal["unspecified"] = "unspecified"
    """
    Error source, must be unspecified
    """

    type: str
    """
    Type of element of the user's Telegram Passport which has the issue
    """

    element_hash: str
    """
    Base64-encoded element hash
    """

    message: str
    """
    Error message
    """


class Game(TelegramObject):
    """
    This object represents a game. Use BotFather to create and edit games, their short
    names will act as unique identifiers.
    """

    title: str
    """
    Title of the game
    """

    description: str
    """
    Description of the game
    """

    photo: list[PhotoSize]
    """
    Photo that will be displayed in the game message in chats
    """

    text: str | None = None
    """
    Brief description of the game or high scores included in the game message. Can be
    automatically edited to include current high scores for the game when the bot calls
    setGameScore, or manually edited using editMessageText. 0-4096 characters.
    """

    text_entities: list[MessageEntity] | None = None
    """
    Special entities that appear in text, such as usernames, URLs, bot commands, etc.
    """

    animation: Animation | None = None
    """
    Animation that will be displayed in the game message in chats. Upload via BotFather.
    """


class CallbackGame(TelegramObject):
    """
    A placeholder, currently holds no information. Use BotFather to set up your game.
    """


class GameHighScore(TelegramObject):
    """
    This object represents one row of the high scores table for a game.
    """

    position: int
    """
    Position in high score table for the game
    """

    user: User
    """
    User
    """

    score: int
    """
    Score
    """
