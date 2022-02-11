"""
This type stub file was generated by pyright.
"""

from .interaction import *

__all__ = (
    "InteractionDataOption",
    "ApplicationCommandInteractionData",
    "SlashInteractionData",
    "ContextMenuInteractionData",
    "SlashInteraction",
    "ContextMenuInteraction",
    "Interaction",
)

class Resolved:
    def __init__(self, *, data, guild, state) -> None: ...
    def __repr__(self): ...
    def get(self, any_id): ...

class ApplicationCommandInteractionData:
    def __init__(self, *, data, guild, state) -> None: ...

class InteractionDataOption:
    """
    Represents user's input for a specific option

    Attributes
    ----------
    name : str
        The name of the option
    value : Any
        The value of the option
    options : dict
        | Represents options of a sub-slash-command.
        | {``name``: :class:`InteractionDataOption`, ...}
    """

    def __init__(self, *, data, resolved: Resolved) -> None: ...
    def __repr__(self): ...
    @property
    def sub_command(self): ...
    def get_option(self, name: str):  # -> InteractionDataOption | None:
        """
        Get the raw :class:`InteractionDataOption` matching the specified name

        Parameters
        ----------
        name : str
            The name of the option you want to get

        Returns
        -------
        option : InteractionDataOption | ``None``
        """
        ...
    def get(self, name: str, default=...):  # -> int | InteractionDataOption:
        """
        Get the value of an option with the specified name

        Parameters
        ----------
        name : str
            the name of the option you want to get
        default : any
            what to return in case nothing was found

        Returns
        -------
        option_value : any
            The option type isn't ``SUB_COMMAND_GROUP`` or ``SUB_COMMAND``
        option: InteractionDataOption | ``default``
            Otherwise
        """
        ...
    def option_at(self, index: int):  # -> InteractionDataOption | None:
        """Similar to :class:`InteractionData.option_at`"""
        ...

class SlashInteractionData(ApplicationCommandInteractionData):
    """
    Attributes
    ----------
    id : :class:`int`
        The id of the interaction
    name : :class:`str`
        The name of activated slash-command
    options : :class:`dict`
        | Represents options of the slash-command.
        | {``name``: :class:`InteractionDataOption`, ...}
    resolved : :class:`Resolved`
        The collection of related objects, such as users, members, roles, channels and messages
    """

    def __init__(self, *, data, guild, state) -> None: ...
    def __repr__(self): ...
    def __getitem__(self, key): ...
    @property
    def sub_command(self): ...
    @property
    def sub_command_group(self): ...
    def get_option(self, name: str):  # -> InteractionDataOption | None:
        """
        Get the raw :class:`InteractionDataOption` matching the specified name

        Parameters
        ----------
        name : str
            The name of the option you want to get

        Returns
        -------
        option : :class:`InteractionDataOption` | ``None``
        """
        ...
    def get(self, name: str, default=...):  # -> int | InteractionDataOption:
        """
        Get the value of an option with the specified name

        Parameters
        ----------
        name : str
            the name of the option you want to get
        default : any
            what to return in case nothing was found

        Returns
        -------
        option_value : any
            The option type isn't ``SUB_COMMAND_GROUP`` or ``SUB_COMMAND``
        option: :class:`InteractionDataOption` | ``default``
            Otherwise
        """
        ...
    def option_at(self, index: int):  # -> InteractionDataOption | None:
        """
        Get an option by it's index

        Parameters
        ----------
        index : int
            the index of the option you want to get

        Returns
        -------
        option : :class:`InteractionDataOption` | ``None``
            the option located at the specified index
        """
        ...

class ContextMenuInteractionData(ApplicationCommandInteractionData):
    def __init__(self, data, guild, state) -> None: ...
    def __repr__(self): ...
    @property
    def member(self): ...
    @property
    def user(self): ...
    @property
    def message(self): ...

class SlashInteraction(BaseInteraction):
    """
    Every interaction with slash-commands is represented by instances of this class

    Attributes
    ----------
    author : :class:`discord.Member` | :class:`discord.User`
        The member/user that used the slash-command.
    guild : discord.Guild
        The guild where interaction was created
    channel : :class:`discord.TextChannel`
        The channel where interaction was created
    data : :class:`InteractionData`
        The arguments that were passed
    created_at : :class:`datetime.datetime`
        Then interaction was created
    expired : :class:`bool`:
        Whether the interaction token is still valid
    """

    def __init__(self, client, payload) -> None: ...
    def __repr__(self): ...
    def __getitem__(self, key): ...
    def get(self, name: str, default=...):  # -> int | InteractionDataOption:
        """Equivalent to :class:`InteractionData.get`"""
        ...
    def get_option(self, name: str):  # -> InteractionDataOption | None:
        """Equivalent to :class:`InteractionData.get_option`"""
        ...
    def option_at(self, index: int):  # -> InteractionDataOption | None:
        """Equivalent to :class:`InteractionData.option_at`"""
        ...

class ContextMenuInteraction(BaseInteraction):
    def __init__(self, client, payload) -> None: ...
    def __repr__(self): ...
    @property
    def target(self): ...
    @property
    def user(self): ...
    @property
    def member(self): ...
    @property
    def message(self): ...

Interaction = SlashInteraction