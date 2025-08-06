from dataclasses import dataclass


@dataclass(frozen=True)
class ANSI:
    # Foreground colors
    BLACK: str = "\033[30m"
    RED: str = "\033[31m"
    GREEN: str = "\033[32m"
    YELLOW: str = "\033[33m"
    BLUE: str = "\033[34m"
    PURPLE: str = "\033[35m"
    CYAN: str = "\033[36m"
    WHITE: str = "\033[37m"
    GRAY: str = "\033[90m"
    LIME: str = "\033[38;5;82m"
    ORANGE: str = "\033[38;5;208m"

    LIGHT_BLACK: str = "\033[90m"
    LIGHT_RED: str = "\033[91m"
    LIGHT_GREEN: str = "\033[92m"
    LIGHT_YELLOW: str = "\033[93m"
    LIGHT_BLUE: str = "\033[94m"
    LIGHT_PURPLE: str = "\033[95m"
    LIGHT_CYAN: str = "\033[96m"
    LIGHT_WHITE: str = "\033[97m"

    STR: str = "\033[38;2;206;145;120m"

    # Background colors
    BG_BLACK: str = "\033[40m"
    BG_RED: str = "\033[41m"
    BG_GREEN: str = "\033[42m"
    BG_YELLOW: str = "\033[43m"
    BG_BLUE: str = "\033[44m"
    BG_PURPLE: str = "\033[45m"
    BG_CYAN: str = "\033[46m"
    BG_WHITE: str = "\033[47m"
    BG_ORANGE: str = "\033[48;5;208m"

    BG_LIGHT_BLACK: str = "\033[100m"
    BG_LIGHT_RED: str = "\033[101m"
    BG_LIGHT_GREEN: str = "\033[102m"
    BG_LIGHT_YELLOW: str = "\033[103m"
    BG_LIGHT_BLUE: str = "\033[104m"
    BG_LIGHT_PURPLE: str = "\033[105m"
    BG_LIGHT_CYAN: str = "\033[106m"
    BG_LIGHT_WHITE: str = "\033[107m"
    BG_LIME: str = "\033[48;5;82m"
    BG_STR: str = "\033[48;2;206;145;120m"

    # Text effects
    RESET: str = "\033[0m"
    BOLD: str = "\033[1m"
    DIM: str = "\033[2m"
    ITALIC: str = "\033[3m"
    UNDERLINE: str = "\033[4m"
    BLINK: str = "\033[5m"
    REVERSED: str = "\033[7m"
    HIDDEN: str = "\033[8m"
    STRIKETHROUGH: str = "\033[9m"

    # Effect resets
    BOLD_OFF: str = "\033[22m"
    ITALIC_OFF: str = "\033[23m"
    UNDERLINE_OFF: str = "\033[24m"
    BLINK_OFF: str = "\033[25m"
    REVERSED_OFF: str = "\033[27m"
    HIDDEN_OFF: str = "\033[28m"
    STRIKETHROUGH_OFF: str = "\033[29m"


ansi = ANSI()
