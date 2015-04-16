import re

HEADING_REGEX = r"^[^\n]+\n={2,}"
HEADING_PATTERN = re.compile(HEADING_REGEX)

SUB_HEADING_REGEX = r"^[^\n]+\n-{2,}"
SUB_HEADING_PATTERN = re.compile(SUB_HEADING_REGEX)

SUB_SUB_HEADING_REGEX = r"^(?:(\#+) .+ \1)"
SUB_SUB_HEADING_PATTERN = re.compile(SUB_SUB_HEADING_REGEX)

ORDERED_LIST_REGEX = r"^(?:\d\..+(?:\n|$))+"
ORDERED_LIST_PATTERN = re.compile(ORDERED_LIST_REGEX)

UNORDERED_LIST_REGEX = r"^(?:(?:\*|\-) .+(?:\n|$))+"
UNORDERED_LIST_PATTERN = re.compile(UNORDERED_LIST_REGEX)

BOLD_TEXT_REGEX = r"\*\*(.+?)\*\*"
START_BOLD_TEXT_REGEX = r"^" + BOLD_TEXT_REGEX
START_BOLD_TEXT_PATTERN = re.compile(START_BOLD_TEXT_REGEX)

ITALIC_TEXT_REGEX = r"\*([^\*]+?)\*"
START_ITALIC_TEXT_REGEX = r"^" + ITALIC_TEXT_REGEX
START_ITALIC_TEXT_PATTERN = re.compile(START_ITALIC_TEXT_REGEX)

STRIKETHROUGH_TEXT_REGEX = r"\-\-(.+?)\-\-"
START_STRIKETHROUGH_TEXT_REGEX = r"^" + STRIKETHROUGH_TEXT_REGEX
START_STRIKETHROUGH_TEXT_PATTERN = re.compile(START_STRIKETHROUGH_TEXT_REGEX)

UNDERLINE_TEXT_REGEX = r"\_(.+?)\_"
START_UNDERLINE_TEXT_REGEX = r"^" + UNDERLINE_TEXT_REGEX
START_UNDERLINE_TEXT_PATTERN = re.compile(START_UNDERLINE_TEXT_REGEX)

QUOTE_TEXT_REGEX = r"\`\`(.+?)\'\'"
START_QUOTE_TEXT_REGEX = r"^" + QUOTE_TEXT_REGEX
START_QUOTE_TEXT_PATTERN = re.compile(START_QUOTE_TEXT_REGEX)

LINK_TEXT_REGEX = r"\[(.+?)\]\((.+?)\)"
START_LINK_TEXT_REGEX = r"^" + LINK_TEXT_REGEX
START_LINK_TEXT_PATTERN = re.compile(START_LINK_TEXT_REGEX)

START_PLAIN_TEXT_REGEX = r"(.+?)(" + \
                                    BOLD_TEXT_REGEX + "|" +\
                                    ITALIC_TEXT_REGEX + "|" +\
                                    STRIKETHROUGH_TEXT_REGEX + "|" +\
                                    UNDERLINE_TEXT_REGEX + "|" +\
                                    QUOTE_TEXT_REGEX + "|" +\
                                    LINK_TEXT_REGEX + "|" +\
                               "$)"

START_PLAIN_TEXT_PATTERN = re.compile(START_PLAIN_TEXT_REGEX)
