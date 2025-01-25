from pygments.lexer import RegexLexer, words, bygroups
from pygments.token import *

import sys
def printf(fmt, *args):
    sys.stderr.write(fmt % args)

ID = r'([A-Za-z_][A-Za-z0-9_]*)'

S = r'((")((\\")|[^"])*("))'

N_D = r'[0-9_]+'
N_E = r'[Ee][-+]?' + N_D
N_H = r'0[Xx][A-Fa-f0-9_]+'
N_B = r'0[Bb][0-1_]+'

W_OTHERS = words((
    'fail', 'halt', 'print'), suffix=r'\b')

W_KEYWORDS = words((
    'break', 'catch', 'continue', 'else', 'for', 'if', 'inline',
    'orelse', 'return', 'switch', 'try', 'while'), suffix=r'\b')

W_RESERVED = words((
    'and', 'asm', 'comptime', 'const', 'enum', 'error', 'export', 'extern', 'fn', 'or', 'packed',
    'pub', 'struct', 'test', 'union', 'unreachable', 'usingnamespace', 'var', 'volatile'), suffix=r'\b')

W_TYPES = words((
    'anyopaque', 'anytype', 'bool', 'comptime_float', 'comptime_int', 'isize', 'noreturn', 'type', 'usize', 'void'), suffix=r'\b')

class ZigEmLexer(RegexLexer):

    def semantic_callback(lexer, match):
        name = match.group(1)
        suf = match.group(len(match.groups()))
        tok = Name if suf == None else Name.Function if suf == '#f' else Keyword if suf == '#k' else Keyword.Type if suf == '#t' else Keyword.Type if suf == '@u' else Generic.Error
        yield match.start(), tok, name

    def zigem_strip_callback(lexer, match):
        name = match.group(1)
        tok = Name.Builtin
        yield match.start(), tok, name

    name = 'ZIGEM'
    aliases = ['ZIGEM', 'ZigEm', 'zigem']
    filenames = ['*.em.zig']
    tokens = {
        'root': [
            (r'//.*?$', Comment.Single),
            (r'\\\\.*?$', String.Interpol),
            (r'^\s+\|->.*?$', String.Interpol),
            (r'^\|->>>(.|\n)*?\n\|-<<<', String.Interpol),
            (r'em__C\b', Name.Builtin),
            (r'em\.(fail|halt|print)\b', Name.Other),
            (r'em\.[@]"%%[^"]+"', Name.Other),
            (rf'(em{ID}\.{ID})([#][a-z])', zigem_strip_callback),
            (rf'em{ID}?((\.{ID})|(\.[@]{S}))?\b', Name.Builtin),
            (rf'^pub[ ]const[ ]EM__{ID}\b', Name.Tag),
            ## (W_OTHERS, Name.Other),
            (W_KEYWORDS, Keyword),
            (W_RESERVED, Keyword.Reserved),
            (W_TYPES, Keyword.Type),
            (rf'[@]{ID}\b', Name.Function),
            (r'[iu]\d+', Keyword.Type),
            (rf'{ID}([#][a-z])?', semantic_callback),
            (rf'([@]{S})([#][a-z])?', semantic_callback),
            (r"(')((\\.+)|[^'])*(')", String.Char),
            (rf'{N_H}|{N_B}|{N_D}[.]{N_D}{N_E}?|{N_D}[LlUu]?', Other),
            (rf'{S}', String),
            (r'.', Other),
        ],
    }




