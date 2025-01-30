from pygments.lexer import RegexLexer, words, bygroups
from pygments.token import *

import sys
def printf(fmt, *args):
    sys.stderr.write(fmt % args)

ID = r'([A-Za-z_][A-Za-z0-9_$]*)'

S = r'((")((\\")|[^"])*("))'

N_D = r'[0-9_]+'
N_E = r'[Ee][-+]?' + N_D
N_H = r'0[Xx][A-Fa-f0-9_]+'
N_B = r'0[Bb][0-1_]+'

W_OTHERS = words((
    'fail', 'halt', 'print'), suffix=r'\b')

W_KEYWORDS = words((
    'as', 'break', 'continue', 'else', 'export', 'for', 'from', 'if', 'import', 'return', 'switch', 'while'), suffix=r'\b')

W_RESERVED = words((
    'class', 'const', 'declare', 'extends', 'function', 'interface', 'let', 'namespace', 'type', 'var'), suffix=r'\b')

W_TYPES = words((
    'arg_t, bool_t', 'i8', 'i16', 'i32', 'text_t', 'u8', 'u16', 'u32' 'void'), suffix=r'\b')

class EmsLexer(RegexLexer):

    def semantic_callback(lexer, match):
        name = match.group(1)
        suf = match.group(len(match.groups()))
        tok = Name if suf == None else Name.Function if suf == '#f' else Keyword if suf == '#k' else Keyword.Type if suf == '#t' else Keyword.Type if suf == '#u' else Generic.Error
        yield match.start(), tok, name

    def zigem_strip_callback(lexer, match):
        name = match.group(1)
        tok = Name.Builtin
        yield match.start(), tok, name

    name = 'EMS'
    aliases = ['EMS', 'ems']
    filenames = ['*.em.ts']
    tokens = {
        'root': [
            (r'//.*?$', Comment.Single),
            (r'\\\\.*?$', String.Interpol),
            (r'^\s+\|->.*?$', String.Interpol),
            (r'^\|->>>(.|\n)*?\n\|-<<<', String.Interpol),
            (r'em__C\b', Name.Builtin),
            (r'em\.(fail|halt|print)\b', Name.Other),
            (r'em\.[@]"%%[^"]+"', Name.Other),
            (r'em\$(meta|template)\b', Name.Class),
            (rf'^pub[ ]const[ ]EM__{ID}\b', Name.Tag),
            ## (W_OTHERS, Name.Other),
            (W_KEYWORDS, Keyword),
            (W_RESERVED, Keyword.Reserved),
            (W_TYPES, Keyword.Type),
            (rf'(em)?[$]{ID}\b', Name.Builtin),
            (r'[iu]\d+', Keyword.Type),
            (rf'{ID}([#][a-z])?', semantic_callback),
            (rf'([@]{S})([#][a-z])?', semantic_callback),
            (r"(')((\\.+)|[^'])*(')", String),
            (rf'{N_H}|{N_B}|{N_D}[.]{N_D}{N_E}?|{N_D}[LlUu]?', Other),
            (rf'{S}', String),
            (r'.', Other),
        ],
    }




