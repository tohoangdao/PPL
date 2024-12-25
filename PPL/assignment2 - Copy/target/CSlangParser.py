# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u01b8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\7\2b\n\2\f\2\16\2e\13\2\3\2\3\2\3\3")
        buf.write("\3\3\5\3k\n\3\3\3\3\3\3\3\7\3p\n\3\f\3\16\3s\13\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\5\3\5\5\5}\n\5\3\6\3\6\5\6\u0081")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\5\b\u0091\n\b\3\b\3\b\3\t\3\t\3\t\7\t\u0098\n\t")
        buf.write("\f\t\16\t\u009b\13\t\3\n\3\n\3\n\7\n\u00a0\n\n\f\n\16")
        buf.write("\n\u00a3\13\n\3\13\3\13\5\13\u00a7\n\13\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00ad\n\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\7\r\u00b7")
        buf.write("\n\r\f\r\16\r\u00ba\13\r\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00c4\n\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\5\20\u00ce\n\20\3\21\3\21\5\21\u00d2\n\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00de\n\23\3\24\3\24\3\24\3\24\3\24\5\24\u00e5\n\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\7\25\u00ed\n\25\f\25\16\25")
        buf.write("\u00f0\13\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u00f8")
        buf.write("\n\26\f\26\16\26\u00fb\13\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\7\27\u0103\n\27\f\27\16\27\u0106\13\27\3\30\3\30")
        buf.write("\3\30\5\30\u010b\n\30\3\31\3\31\3\31\5\31\u0110\n\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\5\32\u0118\n\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0125")
        buf.write("\n\33\3\33\7\33\u0128\n\33\f\33\16\33\u012b\13\33\3\34")
        buf.write("\3\34\3\34\5\34\u0130\n\34\3\34\3\34\3\34\3\34\5\34\u0136")
        buf.write("\n\34\3\34\3\34\3\34\5\34\u013b\n\34\3\34\3\34\5\34\u013f")
        buf.write("\n\34\3\35\3\35\3\35\3\35\5\35\u0145\n\35\3\35\3\35\5")
        buf.write("\35\u0149\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u0156\n\36\3\37\3\37\3\37\7\37\u015b")
        buf.write("\n\37\f\37\16\37\u015e\13\37\3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \5 \u0169\n \3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\5#\u0174")
        buf.write("\n#\3#\3#\3#\3#\5#\u017a\n#\3$\3$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\5")
        buf.write("*\u0195\n*\3*\3*\3+\3+\7+\u019b\n+\f+\16+\u019e\13+\3")
        buf.write("+\3+\3,\3,\3,\3,\3-\3-\3-\7-\u01a9\n-\f-\16-\u01ac\13")
        buf.write("-\3.\3.\3.\3.\5.\u01b2\n.\3/\3/\3\60\3\60\3\60\2\6(*,")
        buf.write("\64\61\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668:<>@BDFHJLNPRTVXZ\\^\2\t\3\2\n\r\4\2  \"")
        buf.write("&\3\2\36\37\3\2\30\31\4\2\32\34**\3\2\678\3\2\b\t\2\u01c3")
        buf.write("\2c\3\2\2\2\4h\3\2\2\2\6v\3\2\2\2\b|\3\2\2\2\n\u0080\3")
        buf.write("\2\2\2\f\u0082\3\2\2\2\16\u008a\3\2\2\2\20\u0094\3\2\2")
        buf.write("\2\22\u009c\3\2\2\2\24\u00a6\3\2\2\2\26\u00a8\3\2\2\2")
        buf.write("\30\u00b3\3\2\2\2\32\u00bb\3\2\2\2\34\u00bf\3\2\2\2\36")
        buf.write("\u00cd\3\2\2\2 \u00d1\3\2\2\2\"\u00d3\3\2\2\2$\u00dd\3")
        buf.write("\2\2\2&\u00e4\3\2\2\2(\u00e6\3\2\2\2*\u00f1\3\2\2\2,\u00fc")
        buf.write("\3\2\2\2.\u010a\3\2\2\2\60\u010f\3\2\2\2\62\u0117\3\2")
        buf.write("\2\2\64\u0119\3\2\2\2\66\u013e\3\2\2\28\u0148\3\2\2\2")
        buf.write(":\u0155\3\2\2\2<\u0157\3\2\2\2>\u0168\3\2\2\2@\u016a\3")
        buf.write("\2\2\2B\u016c\3\2\2\2D\u0171\3\2\2\2F\u017b\3\2\2\2H\u017d")
        buf.write("\3\2\2\2J\u0185\3\2\2\2L\u0189\3\2\2\2N\u018c\3\2\2\2")
        buf.write("P\u018f\3\2\2\2R\u0192\3\2\2\2T\u0198\3\2\2\2V\u01a1\3")
        buf.write("\2\2\2X\u01a5\3\2\2\2Z\u01b1\3\2\2\2\\\u01b3\3\2\2\2^")
        buf.write("\u01b5\3\2\2\2`b\5\4\3\2a`\3\2\2\2be\3\2\2\2ca\3\2\2\2")
        buf.write("cd\3\2\2\2df\3\2\2\2ec\3\2\2\2fg\7\2\2\3g\3\3\2\2\2hj")
        buf.write("\7\20\2\2ik\5\6\4\2ji\3\2\2\2jk\3\2\2\2kl\3\2\2\2lm\7")
        buf.write("8\2\2mq\7\63\2\2np\5\b\5\2on\3\2\2\2ps\3\2\2\2qo\3\2\2")
        buf.write("\2qr\3\2\2\2rt\3\2\2\2sq\3\2\2\2tu\7\64\2\2u\5\3\2\2\2")
        buf.write("vw\78\2\2wx\7#\2\2xy\7\31\2\2y\7\3\2\2\2z}\5\n\6\2{}\5")
        buf.write("\24\13\2|z\3\2\2\2|{\3\2\2\2}\t\3\2\2\2~\u0081\5\f\7\2")
        buf.write("\177\u0081\5\16\b\2\u0080~\3\2\2\2\u0080\177\3\2\2\2\u0081")
        buf.write("\13\3\2\2\2\u0082\u0083\7\26\2\2\u0083\u0084\5\20\t\2")
        buf.write("\u0084\u0085\7.\2\2\u0085\u0086\5\36\20\2\u0086\u0087")
        buf.write("\7!\2\2\u0087\u0088\5\22\n\2\u0088\u0089\7-\2\2\u0089")
        buf.write("\r\3\2\2\2\u008a\u008b\7\22\2\2\u008b\u008c\5\20\t\2\u008c")
        buf.write("\u008d\7.\2\2\u008d\u0090\5\36\20\2\u008e\u008f\7!\2\2")
        buf.write("\u008f\u0091\5\22\n\2\u0090\u008e\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\7-\2\2\u0093")
        buf.write("\17\3\2\2\2\u0094\u0099\5\\/\2\u0095\u0096\7,\2\2\u0096")
        buf.write("\u0098\5\\/\2\u0097\u0095\3\2\2\2\u0098\u009b\3\2\2\2")
        buf.write("\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\21\3\2")
        buf.write("\2\2\u009b\u0099\3\2\2\2\u009c\u00a1\5$\23\2\u009d\u009e")
        buf.write("\7,\2\2\u009e\u00a0\5$\23\2\u009f\u009d\3\2\2\2\u00a0")
        buf.write("\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\23\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a7\5\26")
        buf.write("\f\2\u00a5\u00a7\5\34\17\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5")
        buf.write("\3\2\2\2\u00a7\25\3\2\2\2\u00a8\u00a9\7\27\2\2\u00a9\u00aa")
        buf.write("\5\\/\2\u00aa\u00ac\7/\2\2\u00ab\u00ad\5\30\r\2\u00ac")
        buf.write("\u00ab\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\3\2\2\2")
        buf.write("\u00ae\u00af\7\60\2\2\u00af\u00b0\7.\2\2\u00b0\u00b1\5")
        buf.write(" \21\2\u00b1\u00b2\5T+\2\u00b2\27\3\2\2\2\u00b3\u00b8")
        buf.write("\5\32\16\2\u00b4\u00b5\7,\2\2\u00b5\u00b7\5\32\16\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2")
        buf.write("\u00b8\u00b9\3\2\2\2\u00b9\31\3\2\2\2\u00ba\u00b8\3\2")
        buf.write("\2\2\u00bb\u00bc\5\20\t\2\u00bc\u00bd\7.\2\2\u00bd\u00be")
        buf.write("\5\36\20\2\u00be\33\3\2\2\2\u00bf\u00c0\7\27\2\2\u00c0")
        buf.write("\u00c1\7\21\2\2\u00c1\u00c3\7/\2\2\u00c2\u00c4\5\30\r")
        buf.write("\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5")
        buf.write("\3\2\2\2\u00c5\u00c6\7\60\2\2\u00c6\u00c7\5T+\2\u00c7")
        buf.write("\35\3\2\2\2\u00c8\u00ce\7\n\2\2\u00c9\u00ce\7\13\2\2\u00ca")
        buf.write("\u00ce\7\r\2\2\u00cb\u00ce\7\f\2\2\u00cc\u00ce\5\"\22")
        buf.write("\2\u00cd\u00c8\3\2\2\2\u00cd\u00c9\3\2\2\2\u00cd\u00ca")
        buf.write("\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce")
        buf.write("\37\3\2\2\2\u00cf\u00d2\5\36\20\2\u00d0\u00d2\7\25\2\2")
        buf.write("\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2!\3\2\2")
        buf.write("\2\u00d3\u00d4\7\61\2\2\u00d4\u00d5\79\2\2\u00d5\u00d6")
        buf.write("\7\62\2\2\u00d6\u00d7\t\2\2\2\u00d7#\3\2\2\2\u00d8\u00d9")
        buf.write("\5&\24\2\u00d9\u00da\7(\2\2\u00da\u00db\5&\24\2\u00db")
        buf.write("\u00de\3\2\2\2\u00dc\u00de\5&\24\2\u00dd\u00d8\3\2\2\2")
        buf.write("\u00dd\u00dc\3\2\2\2\u00de%\3\2\2\2\u00df\u00e0\5(\25")
        buf.write("\2\u00e0\u00e1\t\3\2\2\u00e1\u00e2\5(\25\2\u00e2\u00e5")
        buf.write("\3\2\2\2\u00e3\u00e5\5(\25\2\u00e4\u00df\3\2\2\2\u00e4")
        buf.write("\u00e3\3\2\2\2\u00e5\'\3\2\2\2\u00e6\u00e7\b\25\1\2\u00e7")
        buf.write("\u00e8\5*\26\2\u00e8\u00ee\3\2\2\2\u00e9\u00ea\f\4\2\2")
        buf.write("\u00ea\u00eb\t\4\2\2\u00eb\u00ed\5*\26\2\u00ec\u00e9\3")
        buf.write("\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef")
        buf.write("\3\2\2\2\u00ef)\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f2")
        buf.write("\b\26\1\2\u00f2\u00f3\5,\27\2\u00f3\u00f9\3\2\2\2\u00f4")
        buf.write("\u00f5\f\4\2\2\u00f5\u00f6\t\5\2\2\u00f6\u00f8\5,\27\2")
        buf.write("\u00f7\u00f4\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3")
        buf.write("\2\2\2\u00f9\u00fa\3\2\2\2\u00fa+\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fc\u00fd\b\27\1\2\u00fd\u00fe\5.\30\2\u00fe")
        buf.write("\u0104\3\2\2\2\u00ff\u0100\f\4\2\2\u0100\u0101\t\6\2\2")
        buf.write("\u0101\u0103\5.\30\2\u0102\u00ff\3\2\2\2\u0103\u0106\3")
        buf.write("\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105-")
        buf.write("\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108\7\35\2\2\u0108")
        buf.write("\u010b\5.\30\2\u0109\u010b\5\60\31\2\u010a\u0107\3\2\2")
        buf.write("\2\u010a\u0109\3\2\2\2\u010b/\3\2\2\2\u010c\u010d\7\31")
        buf.write("\2\2\u010d\u0110\5\60\31\2\u010e\u0110\5\62\32\2\u010f")
        buf.write("\u010c\3\2\2\2\u010f\u010e\3\2\2\2\u0110\61\3\2\2\2\u0111")
        buf.write("\u0112\5\64\33\2\u0112\u0113\7\61\2\2\u0113\u0114\5$\23")
        buf.write("\2\u0114\u0115\7\62\2\2\u0115\u0118\3\2\2\2\u0116\u0118")
        buf.write("\5\64\33\2\u0117\u0111\3\2\2\2\u0117\u0116\3\2\2\2\u0118")
        buf.write("\63\3\2\2\2\u0119\u011a\b\33\1\2\u011a\u011b\5\66\34\2")
        buf.write("\u011b\u0129\3\2\2\2\u011c\u011d\f\5\2\2\u011d\u011e\7")
        buf.write("+\2\2\u011e\u0128\78\2\2\u011f\u0120\f\4\2\2\u0120\u0121")
        buf.write("\7+\2\2\u0121\u0122\78\2\2\u0122\u0124\7/\2\2\u0123\u0125")
        buf.write("\5<\37\2\u0124\u0123\3\2\2\2\u0124\u0125\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126\u0128\7\60\2\2\u0127\u011c\3\2\2")
        buf.write("\2\u0127\u011f\3\2\2\2\u0128\u012b\3\2\2\2\u0129\u0127")
        buf.write("\3\2\2\2\u0129\u012a\3\2\2\2\u012a\65\3\2\2\2\u012b\u0129")
        buf.write("\3\2\2\2\u012c\u012d\58\35\2\u012d\u012e\7+\2\2\u012e")
        buf.write("\u0130\3\2\2\2\u012f\u012c\3\2\2\2\u012f\u0130\3\2\2\2")
        buf.write("\u0130\u0131\3\2\2\2\u0131\u013f\7\67\2\2\u0132\u0133")
        buf.write("\58\35\2\u0133\u0134\7+\2\2\u0134\u0136\3\2\2\2\u0135")
        buf.write("\u0132\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0137\3\2\2\2")
        buf.write("\u0137\u0138\7\67\2\2\u0138\u013a\7/\2\2\u0139\u013b\5")
        buf.write("<\37\2\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c")
        buf.write("\3\2\2\2\u013c\u013f\7\60\2\2\u013d\u013f\58\35\2\u013e")
        buf.write("\u012f\3\2\2\2\u013e\u0135\3\2\2\2\u013e\u013d\3\2\2\2")
        buf.write("\u013f\67\3\2\2\2\u0140\u0141\7\24\2\2\u0141\u0142\78")
        buf.write("\2\2\u0142\u0144\7/\2\2\u0143\u0145\5<\37\2\u0144\u0143")
        buf.write("\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\3\2\2\2\u0146")
        buf.write("\u0149\7\60\2\2\u0147\u0149\5:\36\2\u0148\u0140\3\2\2")
        buf.write("\2\u0148\u0147\3\2\2\2\u01499\3\2\2\2\u014a\u014b\7/\2")
        buf.write("\2\u014b\u014c\5$\23\2\u014c\u014d\7\60\2\2\u014d\u0156")
        buf.write("\3\2\2\2\u014e\u0156\5\\/\2\u014f\u0156\79\2\2\u0150\u0156")
        buf.write("\7:\2\2\u0151\u0156\5^\60\2\u0152\u0156\7;\2\2\u0153\u0156")
        buf.write("\5V,\2\u0154\u0156\7\23\2\2\u0155\u014a\3\2\2\2\u0155")
        buf.write("\u014e\3\2\2\2\u0155\u014f\3\2\2\2\u0155\u0150\3\2\2\2")
        buf.write("\u0155\u0151\3\2\2\2\u0155\u0152\3\2\2\2\u0155\u0153\3")
        buf.write("\2\2\2\u0155\u0154\3\2\2\2\u0156;\3\2\2\2\u0157\u015c")
        buf.write("\5$\23\2\u0158\u0159\7,\2\2\u0159\u015b\5$\23\2\u015a")
        buf.write("\u0158\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2\2\2")
        buf.write("\u015c\u015d\3\2\2\2\u015d=\3\2\2\2\u015e\u015c\3\2\2")
        buf.write("\2\u015f\u0169\5@!\2\u0160\u0169\5B\"\2\u0161\u0169\5")
        buf.write("D#\2\u0162\u0169\5H%\2\u0163\u0169\5L\'\2\u0164\u0169")
        buf.write("\5N(\2\u0165\u0169\5P)\2\u0166\u0169\5R*\2\u0167\u0169")
        buf.write("\5T+\2\u0168\u015f\3\2\2\2\u0168\u0160\3\2\2\2\u0168\u0161")
        buf.write("\3\2\2\2\u0168\u0162\3\2\2\2\u0168\u0163\3\2\2\2\u0168")
        buf.write("\u0164\3\2\2\2\u0168\u0165\3\2\2\2\u0168\u0166\3\2\2\2")
        buf.write("\u0168\u0167\3\2\2\2\u0169?\3\2\2\2\u016a\u016b\5\n\6")
        buf.write("\2\u016bA\3\2\2\2\u016c\u016d\5$\23\2\u016d\u016e\7\'")
        buf.write("\2\2\u016e\u016f\5$\23\2\u016f\u0170\7-\2\2\u0170C\3\2")
        buf.write("\2\2\u0171\u0173\7\5\2\2\u0172\u0174\5F$\2\u0173\u0172")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\3\2\2\2\u0175")
        buf.write("\u0176\5$\23\2\u0176\u0179\5T+\2\u0177\u0178\7\6\2\2\u0178")
        buf.write("\u017a\5T+\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a")
        buf.write("E\3\2\2\2\u017b\u017c\5T+\2\u017cG\3\2\2\2\u017d\u017e")
        buf.write("\7\7\2\2\u017e\u017f\5J&\2\u017f\u0180\7-\2\2\u0180\u0181")
        buf.write("\5$\23\2\u0181\u0182\7-\2\2\u0182\u0183\5J&\2\u0183\u0184")
        buf.write("\5T+\2\u0184I\3\2\2\2\u0185\u0186\5$\23\2\u0186\u0187")
        buf.write("\7\'\2\2\u0187\u0188\5$\23\2\u0188K\3\2\2\2\u0189\u018a")
        buf.write("\7\3\2\2\u018a\u018b\7-\2\2\u018bM\3\2\2\2\u018c\u018d")
        buf.write("\7\4\2\2\u018d\u018e\7-\2\2\u018eO\3\2\2\2\u018f\u0190")
        buf.write("\5\66\34\2\u0190\u0191\7-\2\2\u0191Q\3\2\2\2\u0192\u0194")
        buf.write("\7\16\2\2\u0193\u0195\5$\23\2\u0194\u0193\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\7-\2\2")
        buf.write("\u0197S\3\2\2\2\u0198\u019c\7\63\2\2\u0199\u019b\5> \2")
        buf.write("\u019a\u0199\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a\3")
        buf.write("\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f\3\2\2\2\u019e\u019c")
        buf.write("\3\2\2\2\u019f\u01a0\7\64\2\2\u01a0U\3\2\2\2\u01a1\u01a2")
        buf.write("\7\61\2\2\u01a2\u01a3\5X-\2\u01a3\u01a4\7\62\2\2\u01a4")
        buf.write("W\3\2\2\2\u01a5\u01aa\5Z.\2\u01a6\u01a7\7,\2\2\u01a7\u01a9")
        buf.write("\5Z.\2\u01a8\u01a6\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01aa\u01ab\3\2\2\2\u01abY\3\2\2\2\u01ac\u01aa")
        buf.write("\3\2\2\2\u01ad\u01b2\79\2\2\u01ae\u01b2\7:\2\2\u01af\u01b2")
        buf.write("\5^\60\2\u01b0\u01b2\7;\2\2\u01b1\u01ad\3\2\2\2\u01b1")
        buf.write("\u01ae\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b0\3\2\2\2")
        buf.write("\u01b2[\3\2\2\2\u01b3\u01b4\t\7\2\2\u01b4]\3\2\2\2\u01b5")
        buf.write("\u01b6\t\b\2\2\u01b6_\3\2\2\2*cjq|\u0080\u0090\u0099\u00a1")
        buf.write("\u00a6\u00ac\u00b8\u00c3\u00cd\u00d1\u00dd\u00e4\u00ee")
        buf.write("\u00f9\u0104\u010a\u010f\u0117\u0124\u0127\u0129\u012f")
        buf.write("\u0135\u013a\u013e\u0144\u0148\u0155\u015c\u0168\u0173")
        buf.write("\u0179\u0194\u019c\u01aa\u01b1")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'break'", "'continue'", "'if'", "'else'", 
                     "'for'", "'true'", "'false'", "'int'", "'float'", "'bool'", 
                     "'string'", "'return'", "'null'", "'class'", "'constructor'", 
                     "'var'", "'self'", "'new'", "'void'", "'const'", "'func'", 
                     "'+'", "'-'", "'*'", "'/'", "'\\'", "'!'", "'&&'", 
                     "'||'", "'=='", "'='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "':='", "'^'", "<INVALID>", "'%'", "'.'", "','", 
                     "';'", "':'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", 
                      "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", 
                      "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", 
                      "NEW", "VOID", "CONST", "FUNC", "PLUS", "MINUS", "MUL", 
                      "DIV", "BSLASH", "NOT", "AND", "OR", "EQUAL", "EQ", 
                      "DIF", "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", 
                      "ASSIGN", "CONCAT", "NEWOP", "MOD", "DOT", "COMMA", 
                      "SEMICO", "COLON", "OPENCC", "CLOSECC", "OPENSQ", 
                      "CLOSESQ", "OPENBR", "CLOSEBR", "LINE_CMT", "BLOCK_CMT", 
                      "At", "ID", "INTLIT", "FLOATLIT", "STRINGLIT", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_dec = 1
    RULE_super_part = 2
    RULE_member = 3
    RULE_attribute = 4
    RULE_const_dec = 5
    RULE_var_dec = 6
    RULE_id_list = 7
    RULE_expressions_list = 8
    RULE_method = 9
    RULE_method_dec = 10
    RULE_parameter_list = 11
    RULE_parameter = 12
    RULE_method_con = 13
    RULE_at_type = 14
    RULE_func_type = 15
    RULE_array_type = 16
    RULE_expressions = 17
    RULE_expr = 18
    RULE_expr1 = 19
    RULE_expr2 = 20
    RULE_expr3 = 21
    RULE_expr4 = 22
    RULE_expr5 = 23
    RULE_expr6 = 24
    RULE_expr7 = 25
    RULE_expr8 = 26
    RULE_expr9 = 27
    RULE_expr10 = 28
    RULE_expr_list = 29
    RULE_statement = 30
    RULE_vardec_statement = 31
    RULE_assign_statement = 32
    RULE_if_statement = 33
    RULE_pre_statement = 34
    RULE_for_statement = 35
    RULE_for_condition = 36
    RULE_break_statement = 37
    RULE_continue_statement = 38
    RULE_method_statement = 39
    RULE_return_statement = 40
    RULE_block_statement = 41
    RULE_arraylit = 42
    RULE_litlist = 43
    RULE_literal = 44
    RULE_iden = 45
    RULE_boollit = 46

    ruleNames =  [ "program", "class_dec", "super_part", "member", "attribute", 
                   "const_dec", "var_dec", "id_list", "expressions_list", 
                   "method", "method_dec", "parameter_list", "parameter", 
                   "method_con", "at_type", "func_type", "array_type", "expressions", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "expr9", "expr10", "expr_list", 
                   "statement", "vardec_statement", "assign_statement", 
                   "if_statement", "pre_statement", "for_statement", "for_condition", 
                   "break_statement", "continue_statement", "method_statement", 
                   "return_statement", "block_statement", "arraylit", "litlist", 
                   "literal", "iden", "boollit" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSE=4
    FOR=5
    TRUE=6
    FALSE=7
    INT=8
    FLOAT=9
    BOOL=10
    STRING=11
    RETURN=12
    NULL=13
    CLASS=14
    CONSTRUCTOR=15
    VAR=16
    SELF=17
    NEW=18
    VOID=19
    CONST=20
    FUNC=21
    PLUS=22
    MINUS=23
    MUL=24
    DIV=25
    BSLASH=26
    NOT=27
    AND=28
    OR=29
    EQUAL=30
    EQ=31
    DIF=32
    LESS=33
    LESS_EQUAL=34
    GREATER=35
    GREATER_EQUAL=36
    ASSIGN=37
    CONCAT=38
    NEWOP=39
    MOD=40
    DOT=41
    COMMA=42
    SEMICO=43
    COLON=44
    OPENCC=45
    CLOSECC=46
    OPENSQ=47
    CLOSESQ=48
    OPENBR=49
    CLOSEBR=50
    LINE_CMT=51
    BLOCK_CMT=52
    At=53
    ID=54
    INTLIT=55
    FLOATLIT=56
    STRINGLIT=57
    WS=58
    ERROR_CHAR=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def class_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Class_decContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Class_decContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CLASS:
                self.state = 94
                self.class_dec()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def OPENBR(self):
            return self.getToken(CSlangParser.OPENBR, 0)

        def CLOSEBR(self):
            return self.getToken(CSlangParser.CLOSEBR, 0)

        def super_part(self):
            return self.getTypedRuleContext(CSlangParser.Super_partContext,0)


        def member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.MemberContext)
            else:
                return self.getTypedRuleContext(CSlangParser.MemberContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_dec" ):
                return visitor.visitClass_dec(self)
            else:
                return visitor.visitChildren(self)




    def class_dec(self):

        localctx = CSlangParser.Class_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(CSlangParser.CLASS)
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 103
                self.super_part()


            self.state = 106
            self.match(CSlangParser.ID)
            self.state = 107
            self.match(CSlangParser.OPENBR)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.VAR) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 108
                self.member()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(CSlangParser.CLOSEBR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Super_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LESS(self):
            return self.getToken(CSlangParser.LESS, 0)

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_super_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuper_part" ):
                return visitor.visitSuper_part(self)
            else:
                return visitor.visitChildren(self)




    def super_part(self):

        localctx = CSlangParser.Super_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_super_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(CSlangParser.ID)
            self.state = 117
            self.match(CSlangParser.LESS)
            self.state = 118
            self.match(CSlangParser.MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(CSlangParser.AttributeContext,0)


        def method(self):
            return self.getTypedRuleContext(CSlangParser.MethodContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = CSlangParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_member)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.attribute()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.method()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_dec(self):
            return self.getTypedRuleContext(CSlangParser.Const_decContext,0)


        def var_dec(self):
            return self.getTypedRuleContext(CSlangParser.Var_decContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = CSlangParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute)
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.const_dec()
                pass
            elif token in [CSlangParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.var_dec()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def id_list(self):
            return self.getTypedRuleContext(CSlangParser.Id_listContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def at_type(self):
            return self.getTypedRuleContext(CSlangParser.At_typeContext,0)


        def EQ(self):
            return self.getToken(CSlangParser.EQ, 0)

        def expressions_list(self):
            return self.getTypedRuleContext(CSlangParser.Expressions_listContext,0)


        def SEMICO(self):
            return self.getToken(CSlangParser.SEMICO, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_const_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_dec" ):
                return visitor.visitConst_dec(self)
            else:
                return visitor.visitChildren(self)




    def const_dec(self):

        localctx = CSlangParser.Const_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_const_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(CSlangParser.CONST)
            self.state = 129
            self.id_list()
            self.state = 130
            self.match(CSlangParser.COLON)
            self.state = 131
            self.at_type()
            self.state = 132
            self.match(CSlangParser.EQ)
            self.state = 133
            self.expressions_list()
            self.state = 134
            self.match(CSlangParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def id_list(self):
            return self.getTypedRuleContext(CSlangParser.Id_listContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def at_type(self):
            return self.getTypedRuleContext(CSlangParser.At_typeContext,0)


        def SEMICO(self):
            return self.getToken(CSlangParser.SEMICO, 0)

        def EQ(self):
            return self.getToken(CSlangParser.EQ, 0)

        def expressions_list(self):
            return self.getTypedRuleContext(CSlangParser.Expressions_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_var_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dec" ):
                return visitor.visitVar_dec(self)
            else:
                return visitor.visitChildren(self)




    def var_dec(self):

        localctx = CSlangParser.Var_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(CSlangParser.VAR)
            self.state = 137
            self.id_list()
            self.state = 138
            self.match(CSlangParser.COLON)
            self.state = 139
            self.at_type()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.EQ:
                self.state = 140
                self.match(CSlangParser.EQ)
                self.state = 141
                self.expressions_list()


            self.state = 144
            self.match(CSlangParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iden(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.IdenContext)
            else:
                return self.getTypedRuleContext(CSlangParser.IdenContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = CSlangParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.iden()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 147
                self.match(CSlangParser.COMMA)
                self.state = 148
                self.iden()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expressions_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpressionsContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpressionsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_expressions_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressions_list" ):
                return visitor.visitExpressions_list(self)
            else:
                return visitor.visitChildren(self)




    def expressions_list(self):

        localctx = CSlangParser.Expressions_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expressions_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.expressions()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 155
                self.match(CSlangParser.COMMA)
                self.state = 156
                self.expressions()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_dec(self):
            return self.getTypedRuleContext(CSlangParser.Method_decContext,0)


        def method_con(self):
            return self.getTypedRuleContext(CSlangParser.Method_conContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = CSlangParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_method)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.method_dec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.method_con()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def OPENCC(self):
            return self.getToken(CSlangParser.OPENCC, 0)

        def CLOSECC(self):
            return self.getToken(CSlangParser.CLOSECC, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def func_type(self):
            return self.getTypedRuleContext(CSlangParser.Func_typeContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(CSlangParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_dec" ):
                return visitor.visitMethod_dec(self)
            else:
                return visitor.visitChildren(self)




    def method_dec(self):

        localctx = CSlangParser.Method_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(CSlangParser.FUNC)
            self.state = 167
            self.iden()
            self.state = 168
            self.match(CSlangParser.OPENCC)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.At or _la==CSlangParser.ID:
                self.state = 169
                self.parameter_list()


            self.state = 172
            self.match(CSlangParser.CLOSECC)
            self.state = 173
            self.match(CSlangParser.COLON)
            self.state = 174
            self.func_type()
            self.state = 175
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ParameterContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = CSlangParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.parameter()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 178
                self.match(CSlangParser.COMMA)
                self.state = 179
                self.parameter()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(CSlangParser.Id_listContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def at_type(self):
            return self.getTypedRuleContext(CSlangParser.At_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = CSlangParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.id_list()
            self.state = 186
            self.match(CSlangParser.COLON)
            self.state = 187
            self.at_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_conContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def OPENCC(self):
            return self.getToken(CSlangParser.OPENCC, 0)

        def CLOSECC(self):
            return self.getToken(CSlangParser.CLOSECC, 0)

        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(CSlangParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method_con

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_con" ):
                return visitor.visitMethod_con(self)
            else:
                return visitor.visitChildren(self)




    def method_con(self):

        localctx = CSlangParser.Method_conContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_method_con)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(CSlangParser.FUNC)
            self.state = 190
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 191
            self.match(CSlangParser.OPENCC)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.At or _la==CSlangParser.ID:
                self.state = 192
                self.parameter_list()


            self.state = 195
            self.match(CSlangParser.CLOSECC)
            self.state = 196
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class At_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def array_type(self):
            return self.getTypedRuleContext(CSlangParser.Array_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_at_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAt_type" ):
                return visitor.visitAt_type(self)
            else:
                return visitor.visitChildren(self)




    def at_type(self):

        localctx = CSlangParser.At_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_at_type)
        try:
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(CSlangParser.INT)
                pass
            elif token in [CSlangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.match(CSlangParser.FLOAT)
                pass
            elif token in [CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 200
                self.match(CSlangParser.STRING)
                pass
            elif token in [CSlangParser.BOOL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 201
                self.match(CSlangParser.BOOL)
                pass
            elif token in [CSlangParser.OPENSQ]:
                self.enterOuterAlt(localctx, 5)
                self.state = 202
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def at_type(self):
            return self.getTypedRuleContext(CSlangParser.At_typeContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_func_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_type" ):
                return visitor.visitFunc_type(self)
            else:
                return visitor.visitChildren(self)




    def func_type(self):

        localctx = CSlangParser.Func_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_type)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.OPENSQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.at_type()
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(CSlangParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENSQ(self):
            return self.getToken(CSlangParser.OPENSQ, 0)

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def CLOSESQ(self):
            return self.getToken(CSlangParser.CLOSESQ, 0)

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = CSlangParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(CSlangParser.OPENSQ)
            self.state = 210
            self.match(CSlangParser.INTLIT)
            self.state = 211
            self.match(CSlangParser.CLOSESQ)
            self.state = 212
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def CONCAT(self):
            return self.getToken(CSlangParser.CONCAT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expressions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressions" ):
                return visitor.visitExpressions(self)
            else:
                return visitor.visitChildren(self)




    def expressions(self):

        localctx = CSlangParser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expressions)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.expr()
                self.state = 215
                self.match(CSlangParser.CONCAT)
                self.state = 216
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr1Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr1Context,i)


        def EQUAL(self):
            return self.getToken(CSlangParser.EQUAL, 0)

        def DIF(self):
            return self.getToken(CSlangParser.DIF, 0)

        def LESS(self):
            return self.getToken(CSlangParser.LESS, 0)

        def LESS_EQUAL(self):
            return self.getToken(CSlangParser.LESS_EQUAL, 0)

        def GREATER(self):
            return self.getToken(CSlangParser.GREATER, 0)

        def GREATER_EQUAL(self):
            return self.getToken(CSlangParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CSlangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.expr1(0)
                self.state = 222
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL) | (1 << CSlangParser.DIF) | (1 << CSlangParser.LESS) | (1 << CSlangParser.LESS_EQUAL) | (1 << CSlangParser.GREATER) | (1 << CSlangParser.GREATER_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self.expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.expr1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(CSlangParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(CSlangParser.Expr1Context,0)


        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 231
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 232
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 233
                    self.expr2(0) 
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(CSlangParser.Expr2Context,0)


        def PLUS(self):
            return self.getToken(CSlangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 242
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 243
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.PLUS or _la==CSlangParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 244
                    self.expr3(0) 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def MUL(self):
            return self.getToken(CSlangParser.MUL, 0)

        def DIV(self):
            return self.getToken(CSlangParser.DIV, 0)

        def MOD(self):
            return self.getToken(CSlangParser.MOD, 0)

        def BSLASH(self):
            return self.getToken(CSlangParser.BSLASH, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 253
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 254
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MUL) | (1 << CSlangParser.DIV) | (1 << CSlangParser.BSLASH) | (1 << CSlangParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 255
                    self.expr4() 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(CSlangParser.NOT, 0)

        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)




    def expr4(self):

        localctx = CSlangParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr4)
        try:
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.match(CSlangParser.NOT)
                self.state = 262
                self.expr4()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.OPENCC, CSlangParser.OPENSQ, CSlangParser.At, CSlangParser.ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.expr5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = CSlangParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr5)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(CSlangParser.MINUS)
                self.state = 267
                self.expr5()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.OPENCC, CSlangParser.OPENSQ, CSlangParser.At, CSlangParser.ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def OPENSQ(self):
            return self.getToken(CSlangParser.OPENSQ, 0)

        def expressions(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionsContext,0)


        def CLOSESQ(self):
            return self.getToken(CSlangParser.CLOSESQ, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = CSlangParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr6)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.expr7(0)
                self.state = 272
                self.match(CSlangParser.OPENSQ)
                self.state = 273
                self.expressions()
                self.state = 274
                self.match(CSlangParser.CLOSESQ)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.expr7(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def OPENCC(self):
            return self.getToken(CSlangParser.OPENCC, 0)

        def CLOSECC(self):
            return self.getToken(CSlangParser.CLOSECC, 0)

        def expr_list(self):
            return self.getTypedRuleContext(CSlangParser.Expr_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr7, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 293
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Expr7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                        self.state = 282
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 283
                        self.match(CSlangParser.DOT)
                        self.state = 284
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Expr7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                        self.state = 285
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 286
                        self.match(CSlangParser.DOT)
                        self.state = 287
                        self.match(CSlangParser.ID)
                        self.state = 288
                        self.match(CSlangParser.OPENCC)
                        self.state = 290
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.NOT) | (1 << CSlangParser.OPENCC) | (1 << CSlangParser.OPENSQ) | (1 << CSlangParser.At) | (1 << CSlangParser.ID) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT))) != 0):
                            self.state = 289
                            self.expr_list()


                        self.state = 292
                        self.match(CSlangParser.CLOSECC)
                        pass

             
                self.state = 297
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def At(self):
            return self.getToken(CSlangParser.At, 0)

        def expr9(self):
            return self.getTypedRuleContext(CSlangParser.Expr9Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def OPENCC(self):
            return self.getToken(CSlangParser.OPENCC, 0)

        def CLOSECC(self):
            return self.getToken(CSlangParser.CLOSECC, 0)

        def expr_list(self):
            return self.getTypedRuleContext(CSlangParser.Expr_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = CSlangParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr8)
        self._la = 0 # Token type
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 298
                    self.expr9()
                    self.state = 299
                    self.match(CSlangParser.DOT)


                self.state = 303
                self.match(CSlangParser.At)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 304
                    self.expr9()
                    self.state = 305
                    self.match(CSlangParser.DOT)


                self.state = 309
                self.match(CSlangParser.At)
                self.state = 310
                self.match(CSlangParser.OPENCC)
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.NOT) | (1 << CSlangParser.OPENCC) | (1 << CSlangParser.OPENSQ) | (1 << CSlangParser.At) | (1 << CSlangParser.ID) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT))) != 0):
                    self.state = 311
                    self.expr_list()


                self.state = 314
                self.match(CSlangParser.CLOSECC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 315
                self.expr9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def OPENCC(self):
            return self.getToken(CSlangParser.OPENCC, 0)

        def CLOSECC(self):
            return self.getToken(CSlangParser.CLOSECC, 0)

        def expr_list(self):
            return self.getTypedRuleContext(CSlangParser.Expr_listContext,0)


        def expr10(self):
            return self.getTypedRuleContext(CSlangParser.Expr10Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = CSlangParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr9)
        self._la = 0 # Token type
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(CSlangParser.NEW)
                self.state = 319
                self.match(CSlangParser.ID)
                self.state = 320
                self.match(CSlangParser.OPENCC)
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.NOT) | (1 << CSlangParser.OPENCC) | (1 << CSlangParser.OPENSQ) | (1 << CSlangParser.At) | (1 << CSlangParser.ID) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT))) != 0):
                    self.state = 321
                    self.expr_list()


                self.state = 324
                self.match(CSlangParser.CLOSECC)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.OPENCC, CSlangParser.OPENSQ, CSlangParser.At, CSlangParser.ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.expr10()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENCC(self):
            return self.getToken(CSlangParser.OPENCC, 0)

        def expressions(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionsContext,0)


        def CLOSECC(self):
            return self.getToken(CSlangParser.CLOSECC, 0)

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def boollit(self):
            return self.getTypedRuleContext(CSlangParser.BoollitContext,0)


        def STRINGLIT(self):
            return self.getToken(CSlangParser.STRINGLIT, 0)

        def arraylit(self):
            return self.getTypedRuleContext(CSlangParser.ArraylitContext,0)


        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = CSlangParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr10)
        try:
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.OPENCC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.match(CSlangParser.OPENCC)
                self.state = 329
                self.expressions()
                self.state = 330
                self.match(CSlangParser.CLOSECC)
                pass
            elif token in [CSlangParser.At, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.iden()
                pass
            elif token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 333
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 334
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 335
                self.boollit()
                pass
            elif token in [CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 336
                self.match(CSlangParser.STRINGLIT)
                pass
            elif token in [CSlangParser.OPENSQ]:
                self.enterOuterAlt(localctx, 7)
                self.state = 337
                self.arraylit()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 8)
                self.state = 338
                self.match(CSlangParser.SELF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpressionsContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpressionsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = CSlangParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.expressions()
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 342
                self.match(CSlangParser.COMMA)
                self.state = 343
                self.expressions()
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardec_statement(self):
            return self.getTypedRuleContext(CSlangParser.Vardec_statementContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(CSlangParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(CSlangParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(CSlangParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(CSlangParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(CSlangParser.Continue_statementContext,0)


        def method_statement(self):
            return self.getTypedRuleContext(CSlangParser.Method_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(CSlangParser.Return_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CSlangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_statement)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.vardec_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 351
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 352
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 353
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 354
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 355
                self.method_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 356
                self.return_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 357
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardec_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(CSlangParser.AttributeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_vardec_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardec_statement" ):
                return visitor.visitVardec_statement(self)
            else:
                return visitor.visitChildren(self)




    def vardec_statement(self):

        localctx = CSlangParser.Vardec_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_vardec_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.attribute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpressionsContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpressionsContext,i)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def SEMICO(self):
            return self.getToken(CSlangParser.SEMICO, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = CSlangParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.expressions()
            self.state = 363
            self.match(CSlangParser.ASSIGN)
            self.state = 364
            self.expressions()
            self.state = 365
            self.match(CSlangParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def expressions(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionsContext,0)


        def block_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Block_statementContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Block_statementContext,i)


        def pre_statement(self):
            return self.getTypedRuleContext(CSlangParser.Pre_statementContext,0)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = CSlangParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(CSlangParser.IF)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.OPENBR:
                self.state = 368
                self.pre_statement()


            self.state = 371
            self.expressions()
            self.state = 372
            self.block_statement()
            self.state = 375
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 373
                self.match(CSlangParser.ELSE)
                self.state = 374
                self.block_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pre_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_pre_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPre_statement" ):
                return visitor.visitPre_statement(self)
            else:
                return visitor.visitChildren(self)




    def pre_statement(self):

        localctx = CSlangParser.Pre_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_pre_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def for_condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.For_conditionContext)
            else:
                return self.getTypedRuleContext(CSlangParser.For_conditionContext,i)


        def SEMICO(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SEMICO)
            else:
                return self.getToken(CSlangParser.SEMICO, i)

        def expressions(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionsContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = CSlangParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(CSlangParser.FOR)
            self.state = 380
            self.for_condition()
            self.state = 381
            self.match(CSlangParser.SEMICO)
            self.state = 382
            self.expressions()
            self.state = 383
            self.match(CSlangParser.SEMICO)
            self.state = 384
            self.for_condition()
            self.state = 385
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpressionsContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpressionsContext,i)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_for_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_condition" ):
                return visitor.visitFor_condition(self)
            else:
                return visitor.visitChildren(self)




    def for_condition(self):

        localctx = CSlangParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.expressions()
            self.state = 388
            self.match(CSlangParser.ASSIGN)
            self.state = 389
            self.expressions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def SEMICO(self):
            return self.getToken(CSlangParser.SEMICO, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = CSlangParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(CSlangParser.BREAK)
            self.state = 392
            self.match(CSlangParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def SEMICO(self):
            return self.getToken(CSlangParser.SEMICO, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = CSlangParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(CSlangParser.CONTINUE)
            self.state = 395
            self.match(CSlangParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def SEMICO(self):
            return self.getToken(CSlangParser.SEMICO, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_statement" ):
                return visitor.visitMethod_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_statement(self):

        localctx = CSlangParser.Method_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_method_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.expr8()
            self.state = 398
            self.match(CSlangParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def SEMICO(self):
            return self.getToken(CSlangParser.SEMICO, 0)

        def expressions(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = CSlangParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(CSlangParser.RETURN)
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.NOT) | (1 << CSlangParser.OPENCC) | (1 << CSlangParser.OPENSQ) | (1 << CSlangParser.At) | (1 << CSlangParser.ID) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT))) != 0):
                self.state = 401
                self.expressions()


            self.state = 404
            self.match(CSlangParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENBR(self):
            return self.getToken(CSlangParser.OPENBR, 0)

        def CLOSEBR(self):
            return self.getToken(CSlangParser.CLOSEBR, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StatementContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StatementContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = CSlangParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(CSlangParser.OPENBR)
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.NOT) | (1 << CSlangParser.OPENCC) | (1 << CSlangParser.OPENSQ) | (1 << CSlangParser.OPENBR) | (1 << CSlangParser.At) | (1 << CSlangParser.ID) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT))) != 0):
                self.state = 407
                self.statement()
                self.state = 412
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 413
            self.match(CSlangParser.CLOSEBR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENSQ(self):
            return self.getToken(CSlangParser.OPENSQ, 0)

        def litlist(self):
            return self.getTypedRuleContext(CSlangParser.LitlistContext,0)


        def CLOSESQ(self):
            return self.getToken(CSlangParser.CLOSESQ, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = CSlangParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(CSlangParser.OPENSQ)
            self.state = 416
            self.litlist()
            self.state = 417
            self.match(CSlangParser.CLOSESQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.LiteralContext)
            else:
                return self.getTypedRuleContext(CSlangParser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_litlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitlist" ):
                return visitor.visitLitlist(self)
            else:
                return visitor.visitChildren(self)




    def litlist(self):

        localctx = CSlangParser.LitlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_litlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.literal()
            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 420
                self.match(CSlangParser.COMMA)
                self.state = 421
                self.literal()
                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def boollit(self):
            return self.getTypedRuleContext(CSlangParser.BoollitContext,0)


        def STRINGLIT(self):
            return self.getToken(CSlangParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_literal)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 429
                self.boollit()
                pass
            elif token in [CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 430
                self.match(CSlangParser.STRINGLIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def At(self):
            return self.getToken(CSlangParser.At, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_iden

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIden" ):
                return visitor.visitIden(self)
            else:
                return visitor.visitChildren(self)




    def iden(self):

        localctx = CSlangParser.IdenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_iden)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            _la = self._input.LA(1)
            if not(_la==CSlangParser.At or _la==CSlangParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoollitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CSlangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSlangParser.FALSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_boollit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoollit" ):
                return visitor.visitBoollit(self)
            else:
                return visitor.visitChildren(self)




    def boollit(self):

        localctx = CSlangParser.BoollitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            _la = self._input.LA(1)
            if not(_la==CSlangParser.TRUE or _la==CSlangParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.expr1_sempred
        self._predicates[20] = self.expr2_sempred
        self._predicates[21] = self.expr3_sempred
        self._predicates[25] = self.expr7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




