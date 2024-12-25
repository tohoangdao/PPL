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
        buf.write("\u019e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\7\2")
        buf.write("\\\n\2\f\2\16\2_\13\2\3\2\3\2\3\3\3\3\5\3e\n\3\3\3\3\3")
        buf.write("\3\3\7\3j\n\3\f\3\16\3m\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\5\5w\n\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\177\n\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\7\7\u0086\n\7\f\7\16\7\u0089\13\7\3")
        buf.write("\b\3\b\3\b\7\b\u008e\n\b\f\b\16\b\u0091\13\b\3\t\3\t\5")
        buf.write("\t\u0095\n\t\3\n\3\n\3\n\3\n\5\n\u009b\n\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\7\13\u00a5\n\13\f\13\16\13\u00a8")
        buf.write("\13\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00b2\n\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\5\16\u00bc\n\16\3")
        buf.write("\17\3\17\5\17\u00c0\n\17\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u00cc\n\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\5\22\u00d3\n\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\7\23\u00db\n\23\f\23\16\23\u00de\13\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\7\24\u00e6\n\24\f\24\16\24\u00e9\13\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00f1\n\25\f\25\16")
        buf.write("\25\u00f4\13\25\3\26\3\26\3\26\5\26\u00f9\n\26\3\27\3")
        buf.write("\27\3\27\5\27\u00fe\n\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u0106\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\5\31\u0113\n\31\3\31\7\31\u0116\n\31")
        buf.write("\f\31\16\31\u0119\13\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\5\32\u0123\n\32\3\32\3\32\5\32\u0127\n\32\3")
        buf.write("\33\3\33\3\33\3\33\5\33\u012d\n\33\3\33\3\33\5\33\u0131")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\5\34\u013e\n\34\3\35\3\35\3\35\7\35\u0143\n\35\f")
        buf.write("\35\16\35\u0146\13\35\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\5\36\u0151\n\36\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3!\3!\5!\u015c\n!\3!\3!\3!\3!\5!\u0162\n!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3")
        buf.write("&\3&\3&\3\'\3\'\5\'\u017b\n\'\3\'\3\'\3(\3(\7(\u0181\n")
        buf.write("(\f(\16(\u0184\13(\3(\3(\3)\3)\3)\3)\3*\3*\3*\7*\u018f")
        buf.write("\n*\f*\16*\u0192\13*\3+\3+\3+\3+\5+\u0198\n+\3,\3,\3-")
        buf.write("\3-\3-\2\6$&(\60.\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX\2\n\4\2\22\22")
        buf.write("\26\26\3\2\n\r\4\2  \"&\3\2\36\37\3\2\30\31\4\2\32\34")
        buf.write("**\3\2\678\3\2\b\t\2\u01a9\2]\3\2\2\2\4b\3\2\2\2\6p\3")
        buf.write("\2\2\2\bv\3\2\2\2\nx\3\2\2\2\f\u0082\3\2\2\2\16\u008a")
        buf.write("\3\2\2\2\20\u0094\3\2\2\2\22\u0096\3\2\2\2\24\u00a1\3")
        buf.write("\2\2\2\26\u00a9\3\2\2\2\30\u00ad\3\2\2\2\32\u00bb\3\2")
        buf.write("\2\2\34\u00bf\3\2\2\2\36\u00c1\3\2\2\2 \u00cb\3\2\2\2")
        buf.write("\"\u00d2\3\2\2\2$\u00d4\3\2\2\2&\u00df\3\2\2\2(\u00ea")
        buf.write("\3\2\2\2*\u00f8\3\2\2\2,\u00fd\3\2\2\2.\u0105\3\2\2\2")
        buf.write("\60\u0107\3\2\2\2\62\u0126\3\2\2\2\64\u0130\3\2\2\2\66")
        buf.write("\u013d\3\2\2\28\u013f\3\2\2\2:\u0150\3\2\2\2<\u0152\3")
        buf.write("\2\2\2>\u0154\3\2\2\2@\u0159\3\2\2\2B\u0163\3\2\2\2D\u016b")
        buf.write("\3\2\2\2F\u016f\3\2\2\2H\u0172\3\2\2\2J\u0175\3\2\2\2")
        buf.write("L\u0178\3\2\2\2N\u017e\3\2\2\2P\u0187\3\2\2\2R\u018b\3")
        buf.write("\2\2\2T\u0197\3\2\2\2V\u0199\3\2\2\2X\u019b\3\2\2\2Z\\")
        buf.write("\5\4\3\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^`\3")
        buf.write("\2\2\2_]\3\2\2\2`a\7\2\2\3a\3\3\2\2\2bd\7\20\2\2ce\5\6")
        buf.write("\4\2dc\3\2\2\2de\3\2\2\2ef\3\2\2\2fg\78\2\2gk\7\63\2\2")
        buf.write("hj\5\b\5\2ih\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2ln\3")
        buf.write("\2\2\2mk\3\2\2\2no\7\64\2\2o\5\3\2\2\2pq\78\2\2qr\7#\2")
        buf.write("\2rs\7\31\2\2s\7\3\2\2\2tw\5\n\6\2uw\5\20\t\2vt\3\2\2")
        buf.write("\2vu\3\2\2\2w\t\3\2\2\2xy\t\2\2\2yz\5\f\7\2z{\7.\2\2{")
        buf.write("~\5\32\16\2|}\7!\2\2}\177\5\16\b\2~|\3\2\2\2~\177\3\2")
        buf.write("\2\2\177\u0080\3\2\2\2\u0080\u0081\7-\2\2\u0081\13\3\2")
        buf.write("\2\2\u0082\u0087\5V,\2\u0083\u0084\7,\2\2\u0084\u0086")
        buf.write("\5V,\2\u0085\u0083\3\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085")
        buf.write("\3\2\2\2\u0087\u0088\3\2\2\2\u0088\r\3\2\2\2\u0089\u0087")
        buf.write("\3\2\2\2\u008a\u008f\5 \21\2\u008b\u008c\7,\2\2\u008c")
        buf.write("\u008e\5 \21\2\u008d\u008b\3\2\2\2\u008e\u0091\3\2\2\2")
        buf.write("\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\17\3\2")
        buf.write("\2\2\u0091\u008f\3\2\2\2\u0092\u0095\5\22\n\2\u0093\u0095")
        buf.write("\5\30\r\2\u0094\u0092\3\2\2\2\u0094\u0093\3\2\2\2\u0095")
        buf.write("\21\3\2\2\2\u0096\u0097\7\27\2\2\u0097\u0098\5V,\2\u0098")
        buf.write("\u009a\7/\2\2\u0099\u009b\5\24\13\2\u009a\u0099\3\2\2")
        buf.write("\2\u009a\u009b\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d")
        buf.write("\7\60\2\2\u009d\u009e\7.\2\2\u009e\u009f\5\34\17\2\u009f")
        buf.write("\u00a0\5N(\2\u00a0\23\3\2\2\2\u00a1\u00a6\5\26\f\2\u00a2")
        buf.write("\u00a3\7,\2\2\u00a3\u00a5\5\26\f\2\u00a4\u00a2\3\2\2\2")
        buf.write("\u00a5\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3")
        buf.write("\2\2\2\u00a7\25\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00aa")
        buf.write("\5V,\2\u00aa\u00ab\7.\2\2\u00ab\u00ac\5\32\16\2\u00ac")
        buf.write("\27\3\2\2\2\u00ad\u00ae\7\27\2\2\u00ae\u00af\7\21\2\2")
        buf.write("\u00af\u00b1\7/\2\2\u00b0\u00b2\5\24\13\2\u00b1\u00b0")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\u00b4\7\60\2\2\u00b4\u00b5\5N(\2\u00b5\31\3\2\2\2\u00b6")
        buf.write("\u00bc\7\n\2\2\u00b7\u00bc\7\13\2\2\u00b8\u00bc\7\r\2")
        buf.write("\2\u00b9\u00bc\7\f\2\2\u00ba\u00bc\5\36\20\2\u00bb\u00b6")
        buf.write("\3\2\2\2\u00bb\u00b7\3\2\2\2\u00bb\u00b8\3\2\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\33\3\2\2\2\u00bd")
        buf.write("\u00c0\5\32\16\2\u00be\u00c0\7\25\2\2\u00bf\u00bd\3\2")
        buf.write("\2\2\u00bf\u00be\3\2\2\2\u00c0\35\3\2\2\2\u00c1\u00c2")
        buf.write("\7\61\2\2\u00c2\u00c3\79\2\2\u00c3\u00c4\7\62\2\2\u00c4")
        buf.write("\u00c5\t\3\2\2\u00c5\37\3\2\2\2\u00c6\u00c7\5\"\22\2\u00c7")
        buf.write("\u00c8\7(\2\2\u00c8\u00c9\5\"\22\2\u00c9\u00cc\3\2\2\2")
        buf.write("\u00ca\u00cc\5\"\22\2\u00cb\u00c6\3\2\2\2\u00cb\u00ca")
        buf.write("\3\2\2\2\u00cc!\3\2\2\2\u00cd\u00ce\5$\23\2\u00ce\u00cf")
        buf.write("\t\4\2\2\u00cf\u00d0\5$\23\2\u00d0\u00d3\3\2\2\2\u00d1")
        buf.write("\u00d3\5$\23\2\u00d2\u00cd\3\2\2\2\u00d2\u00d1\3\2\2\2")
        buf.write("\u00d3#\3\2\2\2\u00d4\u00d5\b\23\1\2\u00d5\u00d6\5&\24")
        buf.write("\2\u00d6\u00dc\3\2\2\2\u00d7\u00d8\f\4\2\2\u00d8\u00d9")
        buf.write("\t\5\2\2\u00d9\u00db\5&\24\2\u00da\u00d7\3\2\2\2\u00db")
        buf.write("\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2")
        buf.write("\u00dd%\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e0\b\24\1")
        buf.write("\2\u00e0\u00e1\5(\25\2\u00e1\u00e7\3\2\2\2\u00e2\u00e3")
        buf.write("\f\4\2\2\u00e3\u00e4\t\6\2\2\u00e4\u00e6\5(\25\2\u00e5")
        buf.write("\u00e2\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2")
        buf.write("\u00e7\u00e8\3\2\2\2\u00e8\'\3\2\2\2\u00e9\u00e7\3\2\2")
        buf.write("\2\u00ea\u00eb\b\25\1\2\u00eb\u00ec\5*\26\2\u00ec\u00f2")
        buf.write("\3\2\2\2\u00ed\u00ee\f\4\2\2\u00ee\u00ef\t\7\2\2\u00ef")
        buf.write("\u00f1\5*\26\2\u00f0\u00ed\3\2\2\2\u00f1\u00f4\3\2\2\2")
        buf.write("\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3)\3\2\2")
        buf.write("\2\u00f4\u00f2\3\2\2\2\u00f5\u00f6\7\35\2\2\u00f6\u00f9")
        buf.write("\5*\26\2\u00f7\u00f9\5,\27\2\u00f8\u00f5\3\2\2\2\u00f8")
        buf.write("\u00f7\3\2\2\2\u00f9+\3\2\2\2\u00fa\u00fb\7\31\2\2\u00fb")
        buf.write("\u00fe\5,\27\2\u00fc\u00fe\5.\30\2\u00fd\u00fa\3\2\2\2")
        buf.write("\u00fd\u00fc\3\2\2\2\u00fe-\3\2\2\2\u00ff\u0100\5\60\31")
        buf.write("\2\u0100\u0101\7\61\2\2\u0101\u0102\5 \21\2\u0102\u0103")
        buf.write("\7\62\2\2\u0103\u0106\3\2\2\2\u0104\u0106\5\60\31\2\u0105")
        buf.write("\u00ff\3\2\2\2\u0105\u0104\3\2\2\2\u0106/\3\2\2\2\u0107")
        buf.write("\u0108\b\31\1\2\u0108\u0109\5\62\32\2\u0109\u0117\3\2")
        buf.write("\2\2\u010a\u010b\f\5\2\2\u010b\u010c\7+\2\2\u010c\u0116")
        buf.write("\78\2\2\u010d\u010e\f\4\2\2\u010e\u010f\7+\2\2\u010f\u0110")
        buf.write("\78\2\2\u0110\u0112\7/\2\2\u0111\u0113\58\35\2\u0112\u0111")
        buf.write("\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0114\3\2\2\2\u0114")
        buf.write("\u0116\7\60\2\2\u0115\u010a\3\2\2\2\u0115\u010d\3\2\2")
        buf.write("\2\u0116\u0119\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118")
        buf.write("\3\2\2\2\u0118\61\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b")
        buf.write("\78\2\2\u011b\u011c\7+\2\2\u011c\u0127\7\67\2\2\u011d")
        buf.write("\u011e\78\2\2\u011e\u011f\7+\2\2\u011f\u0120\7\67\2\2")
        buf.write("\u0120\u0122\7/\2\2\u0121\u0123\58\35\2\u0122\u0121\3")
        buf.write("\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0127")
        buf.write("\7\60\2\2\u0125\u0127\5\64\33\2\u0126\u011a\3\2\2\2\u0126")
        buf.write("\u011d\3\2\2\2\u0126\u0125\3\2\2\2\u0127\63\3\2\2\2\u0128")
        buf.write("\u0129\7\24\2\2\u0129\u012a\78\2\2\u012a\u012c\7/\2\2")
        buf.write("\u012b\u012d\58\35\2\u012c\u012b\3\2\2\2\u012c\u012d\3")
        buf.write("\2\2\2\u012d\u012e\3\2\2\2\u012e\u0131\7\60\2\2\u012f")
        buf.write("\u0131\5\66\34\2\u0130\u0128\3\2\2\2\u0130\u012f\3\2\2")
        buf.write("\2\u0131\65\3\2\2\2\u0132\u0133\7/\2\2\u0133\u0134\5 ")
        buf.write("\21\2\u0134\u0135\7\60\2\2\u0135\u013e\3\2\2\2\u0136\u013e")
        buf.write("\5V,\2\u0137\u013e\79\2\2\u0138\u013e\7:\2\2\u0139\u013e")
        buf.write("\5X-\2\u013a\u013e\7;\2\2\u013b\u013e\5P)\2\u013c\u013e")
        buf.write("\7\23\2\2\u013d\u0132\3\2\2\2\u013d\u0136\3\2\2\2\u013d")
        buf.write("\u0137\3\2\2\2\u013d\u0138\3\2\2\2\u013d\u0139\3\2\2\2")
        buf.write("\u013d\u013a\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013c\3")
        buf.write("\2\2\2\u013e\67\3\2\2\2\u013f\u0144\5 \21\2\u0140\u0141")
        buf.write("\7,\2\2\u0141\u0143\5 \21\2\u0142\u0140\3\2\2\2\u0143")
        buf.write("\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u01459\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0151\5<\37")
        buf.write("\2\u0148\u0151\5> \2\u0149\u0151\5@!\2\u014a\u0151\5B")
        buf.write("\"\2\u014b\u0151\5F$\2\u014c\u0151\5H%\2\u014d\u0151\5")
        buf.write("J&\2\u014e\u0151\5L\'\2\u014f\u0151\5N(\2\u0150\u0147")
        buf.write("\3\2\2\2\u0150\u0148\3\2\2\2\u0150\u0149\3\2\2\2\u0150")
        buf.write("\u014a\3\2\2\2\u0150\u014b\3\2\2\2\u0150\u014c\3\2\2\2")
        buf.write("\u0150\u014d\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u014f\3")
        buf.write("\2\2\2\u0151;\3\2\2\2\u0152\u0153\5\n\6\2\u0153=\3\2\2")
        buf.write("\2\u0154\u0155\5 \21\2\u0155\u0156\7\'\2\2\u0156\u0157")
        buf.write("\5 \21\2\u0157\u0158\7-\2\2\u0158?\3\2\2\2\u0159\u015b")
        buf.write("\7\5\2\2\u015a\u015c\5N(\2\u015b\u015a\3\2\2\2\u015b\u015c")
        buf.write("\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\5 \21\2\u015e")
        buf.write("\u0161\5N(\2\u015f\u0160\7\6\2\2\u0160\u0162\5N(\2\u0161")
        buf.write("\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162A\3\2\2\2\u0163")
        buf.write("\u0164\7\7\2\2\u0164\u0165\5D#\2\u0165\u0166\7-\2\2\u0166")
        buf.write("\u0167\5 \21\2\u0167\u0168\7-\2\2\u0168\u0169\5D#\2\u0169")
        buf.write("\u016a\5N(\2\u016aC\3\2\2\2\u016b\u016c\78\2\2\u016c\u016d")
        buf.write("\7\'\2\2\u016d\u016e\5 \21\2\u016eE\3\2\2\2\u016f\u0170")
        buf.write("\7\3\2\2\u0170\u0171\7-\2\2\u0171G\3\2\2\2\u0172\u0173")
        buf.write("\7\4\2\2\u0173\u0174\7-\2\2\u0174I\3\2\2\2\u0175\u0176")
        buf.write("\5\62\32\2\u0176\u0177\7-\2\2\u0177K\3\2\2\2\u0178\u017a")
        buf.write("\7\16\2\2\u0179\u017b\5 \21\2\u017a\u0179\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017d\7-\2\2")
        buf.write("\u017dM\3\2\2\2\u017e\u0182\7\63\2\2\u017f\u0181\5:\36")
        buf.write("\2\u0180\u017f\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180")
        buf.write("\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0185\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0185\u0186\7\64\2\2\u0186O\3\2\2\2\u0187")
        buf.write("\u0188\7\61\2\2\u0188\u0189\5R*\2\u0189\u018a\7\62\2\2")
        buf.write("\u018aQ\3\2\2\2\u018b\u0190\5T+\2\u018c\u018d\7,\2\2\u018d")
        buf.write("\u018f\5T+\2\u018e\u018c\3\2\2\2\u018f\u0192\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191S\3\2\2\2\u0192")
        buf.write("\u0190\3\2\2\2\u0193\u0198\79\2\2\u0194\u0198\7:\2\2\u0195")
        buf.write("\u0198\5X-\2\u0196\u0198\7;\2\2\u0197\u0193\3\2\2\2\u0197")
        buf.write("\u0194\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0196\3\2\2\2")
        buf.write("\u0198U\3\2\2\2\u0199\u019a\t\b\2\2\u019aW\3\2\2\2\u019b")
        buf.write("\u019c\t\t\2\2\u019cY\3\2\2\2\']dkv~\u0087\u008f\u0094")
        buf.write("\u009a\u00a6\u00b1\u00bb\u00bf\u00cb\u00d2\u00dc\u00e7")
        buf.write("\u00f2\u00f8\u00fd\u0105\u0112\u0115\u0117\u0122\u0126")
        buf.write("\u012c\u0130\u013d\u0144\u0150\u015b\u0161\u017a\u0182")
        buf.write("\u0190\u0197")
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
    RULE_id_list = 5
    RULE_expressions_list = 6
    RULE_method = 7
    RULE_method_dec = 8
    RULE_parameter_list = 9
    RULE_parameter = 10
    RULE_method_con = 11
    RULE_at_type = 12
    RULE_func_type = 13
    RULE_array_type = 14
    RULE_expressions = 15
    RULE_expr = 16
    RULE_expr1 = 17
    RULE_expr2 = 18
    RULE_expr3 = 19
    RULE_expr4 = 20
    RULE_expr5 = 21
    RULE_expr6 = 22
    RULE_expr7 = 23
    RULE_expr8 = 24
    RULE_expr9 = 25
    RULE_expr10 = 26
    RULE_expr_list = 27
    RULE_statement = 28
    RULE_vardec_statement = 29
    RULE_assign_statement = 30
    RULE_if_statement = 31
    RULE_for_statement = 32
    RULE_for_condition = 33
    RULE_break_statement = 34
    RULE_continue_statement = 35
    RULE_method_statement = 36
    RULE_return_statement = 37
    RULE_block_statement = 38
    RULE_arraylit = 39
    RULE_litlist = 40
    RULE_literal = 41
    RULE_iden = 42
    RULE_boollit = 43

    ruleNames =  [ "program", "class_dec", "super_part", "member", "attribute", 
                   "id_list", "expressions_list", "method", "method_dec", 
                   "parameter_list", "parameter", "method_con", "at_type", 
                   "func_type", "array_type", "expressions", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "expr8", "expr9", "expr10", "expr_list", "statement", 
                   "vardec_statement", "assign_statement", "if_statement", 
                   "for_statement", "for_condition", "break_statement", 
                   "continue_statement", "method_statement", "return_statement", 
                   "block_statement", "arraylit", "litlist", "literal", 
                   "iden", "boollit" ]

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
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CLASS:
                self.state = 88
                self.class_dec()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
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
            self.state = 96
            self.match(CSlangParser.CLASS)
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 97
                self.super_part()


            self.state = 100
            self.match(CSlangParser.ID)
            self.state = 101
            self.match(CSlangParser.OPENBR)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.VAR) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 102
                self.member()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
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
            self.state = 110
            self.match(CSlangParser.ID)
            self.state = 111
            self.match(CSlangParser.LESS)
            self.state = 112
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
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.attribute()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
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

        def id_list(self):
            return self.getTypedRuleContext(CSlangParser.Id_listContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def at_type(self):
            return self.getTypedRuleContext(CSlangParser.At_typeContext,0)


        def SEMICO(self):
            return self.getToken(CSlangParser.SEMICO, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def EQ(self):
            return self.getToken(CSlangParser.EQ, 0)

        def expressions_list(self):
            return self.getTypedRuleContext(CSlangParser.Expressions_listContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 119
            self.id_list()
            self.state = 120
            self.match(CSlangParser.COLON)
            self.state = 121
            self.at_type()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.EQ:
                self.state = 122
                self.match(CSlangParser.EQ)
                self.state = 123
                self.expressions_list()


            self.state = 126
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
        self.enterRule(localctx, 10, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.iden()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 129
                self.match(CSlangParser.COMMA)
                self.state = 130
                self.iden()
                self.state = 135
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
        self.enterRule(localctx, 12, self.RULE_expressions_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.expressions()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 137
                self.match(CSlangParser.COMMA)
                self.state = 138
                self.expressions()
                self.state = 143
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
        self.enterRule(localctx, 14, self.RULE_method)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.method_dec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
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
        self.enterRule(localctx, 16, self.RULE_method_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(CSlangParser.FUNC)
            self.state = 149
            self.iden()
            self.state = 150
            self.match(CSlangParser.OPENCC)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.At or _la==CSlangParser.ID:
                self.state = 151
                self.parameter_list()


            self.state = 154
            self.match(CSlangParser.CLOSECC)
            self.state = 155
            self.match(CSlangParser.COLON)
            self.state = 156
            self.func_type()
            self.state = 157
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
        self.enterRule(localctx, 18, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.parameter()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 160
                self.match(CSlangParser.COMMA)
                self.state = 161
                self.parameter()
                self.state = 166
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

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


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
        self.enterRule(localctx, 20, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.iden()
            self.state = 168
            self.match(CSlangParser.COLON)
            self.state = 169
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
        self.enterRule(localctx, 22, self.RULE_method_con)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(CSlangParser.FUNC)
            self.state = 172
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 173
            self.match(CSlangParser.OPENCC)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.At or _la==CSlangParser.ID:
                self.state = 174
                self.parameter_list()


            self.state = 177
            self.match(CSlangParser.CLOSECC)
            self.state = 178
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
        self.enterRule(localctx, 24, self.RULE_at_type)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(CSlangParser.INT)
                pass
            elif token in [CSlangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(CSlangParser.FLOAT)
                pass
            elif token in [CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.match(CSlangParser.STRING)
                pass
            elif token in [CSlangParser.BOOL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
                self.match(CSlangParser.BOOL)
                pass
            elif token in [CSlangParser.OPENSQ]:
                self.enterOuterAlt(localctx, 5)
                self.state = 184
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
        self.enterRule(localctx, 26, self.RULE_func_type)
        try:
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.OPENSQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.at_type()
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
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
        self.enterRule(localctx, 28, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(CSlangParser.OPENSQ)
            self.state = 192
            self.match(CSlangParser.INTLIT)
            self.state = 193
            self.match(CSlangParser.CLOSESQ)
            self.state = 194
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
        self.enterRule(localctx, 30, self.RULE_expressions)
        try:
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.expr()
                self.state = 197
                self.match(CSlangParser.CONCAT)
                self.state = 198
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
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
        self.enterRule(localctx, 32, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.expr1(0)
                self.state = 204
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL) | (1 << CSlangParser.DIF) | (1 << CSlangParser.LESS) | (1 << CSlangParser.LESS_EQUAL) | (1 << CSlangParser.GREATER) | (1 << CSlangParser.GREATER_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 205
                self.expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 213
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 214
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 215
                    self.expr2(0) 
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 224
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 225
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.PLUS or _la==CSlangParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 226
                    self.expr3(0) 
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 240
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 235
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 236
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MUL) | (1 << CSlangParser.DIV) | (1 << CSlangParser.BSLASH) | (1 << CSlangParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 237
                    self.expr4() 
                self.state = 242
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self.enterRule(localctx, 40, self.RULE_expr4)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(CSlangParser.NOT)
                self.state = 244
                self.expr4()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.OPENCC, CSlangParser.OPENSQ, CSlangParser.At, CSlangParser.ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
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
        self.enterRule(localctx, 42, self.RULE_expr5)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(CSlangParser.MINUS)
                self.state = 249
                self.expr5()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.OPENCC, CSlangParser.OPENSQ, CSlangParser.At, CSlangParser.ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
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
        self.enterRule(localctx, 44, self.RULE_expr6)
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.expr7(0)
                self.state = 254
                self.match(CSlangParser.OPENSQ)
                self.state = 255
                self.expressions()
                self.state = 256
                self.match(CSlangParser.CLOSESQ)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr7, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 275
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Expr7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                        self.state = 264
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 265
                        self.match(CSlangParser.DOT)
                        self.state = 266
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Expr7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                        self.state = 267
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 268
                        self.match(CSlangParser.DOT)
                        self.state = 269
                        self.match(CSlangParser.ID)
                        self.state = 270
                        self.match(CSlangParser.OPENCC)
                        self.state = 272
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.NOT) | (1 << CSlangParser.OPENCC) | (1 << CSlangParser.OPENSQ) | (1 << CSlangParser.At) | (1 << CSlangParser.ID) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT))) != 0):
                            self.state = 271
                            self.expr_list()


                        self.state = 274
                        self.match(CSlangParser.CLOSECC)
                        pass

             
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def At(self):
            return self.getToken(CSlangParser.At, 0)

        def OPENCC(self):
            return self.getToken(CSlangParser.OPENCC, 0)

        def CLOSECC(self):
            return self.getToken(CSlangParser.CLOSECC, 0)

        def expr_list(self):
            return self.getTypedRuleContext(CSlangParser.Expr_listContext,0)


        def expr9(self):
            return self.getTypedRuleContext(CSlangParser.Expr9Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = CSlangParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr8)
        self._la = 0 # Token type
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(CSlangParser.ID)
                self.state = 281
                self.match(CSlangParser.DOT)
                self.state = 282
                self.match(CSlangParser.At)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.match(CSlangParser.ID)
                self.state = 284
                self.match(CSlangParser.DOT)
                self.state = 285
                self.match(CSlangParser.At)
                self.state = 286
                self.match(CSlangParser.OPENCC)
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.NOT) | (1 << CSlangParser.OPENCC) | (1 << CSlangParser.OPENSQ) | (1 << CSlangParser.At) | (1 << CSlangParser.ID) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT))) != 0):
                    self.state = 287
                    self.expr_list()


                self.state = 290
                self.match(CSlangParser.CLOSECC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 291
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
        self.enterRule(localctx, 50, self.RULE_expr9)
        self._la = 0 # Token type
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(CSlangParser.NEW)
                self.state = 295
                self.match(CSlangParser.ID)
                self.state = 296
                self.match(CSlangParser.OPENCC)
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.NOT) | (1 << CSlangParser.OPENCC) | (1 << CSlangParser.OPENSQ) | (1 << CSlangParser.At) | (1 << CSlangParser.ID) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT))) != 0):
                    self.state = 297
                    self.expr_list()


                self.state = 300
                self.match(CSlangParser.CLOSECC)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.OPENCC, CSlangParser.OPENSQ, CSlangParser.At, CSlangParser.ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
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
        self.enterRule(localctx, 52, self.RULE_expr10)
        try:
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.OPENCC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(CSlangParser.OPENCC)
                self.state = 305
                self.expressions()
                self.state = 306
                self.match(CSlangParser.CLOSECC)
                pass
            elif token in [CSlangParser.At, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.iden()
                pass
            elif token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 309
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 310
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 311
                self.boollit()
                pass
            elif token in [CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 312
                self.match(CSlangParser.STRINGLIT)
                pass
            elif token in [CSlangParser.OPENSQ]:
                self.enterOuterAlt(localctx, 7)
                self.state = 313
                self.arraylit()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 8)
                self.state = 314
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
        self.enterRule(localctx, 54, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.expressions()
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 318
                self.match(CSlangParser.COMMA)
                self.state = 319
                self.expressions()
                self.state = 324
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
        self.enterRule(localctx, 56, self.RULE_statement)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.vardec_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 328
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 329
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 330
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 331
                self.method_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 332
                self.return_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 333
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
        self.enterRule(localctx, 58, self.RULE_vardec_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
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
        self.enterRule(localctx, 60, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.expressions()
            self.state = 339
            self.match(CSlangParser.ASSIGN)
            self.state = 340
            self.expressions()
            self.state = 341
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
        self.enterRule(localctx, 62, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(CSlangParser.IF)
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.OPENBR:
                self.state = 344
                self.block_statement()


            self.state = 347
            self.expressions()
            self.state = 348
            self.block_statement()
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 349
                self.match(CSlangParser.ELSE)
                self.state = 350
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
        self.enterRule(localctx, 64, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(CSlangParser.FOR)
            self.state = 354
            self.for_condition()
            self.state = 355
            self.match(CSlangParser.SEMICO)
            self.state = 356
            self.expressions()
            self.state = 357
            self.match(CSlangParser.SEMICO)
            self.state = 358
            self.for_condition()
            self.state = 359
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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def expressions(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_for_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_condition" ):
                return visitor.visitFor_condition(self)
            else:
                return visitor.visitChildren(self)




    def for_condition(self):

        localctx = CSlangParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(CSlangParser.ID)
            self.state = 362
            self.match(CSlangParser.ASSIGN)
            self.state = 363
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
        self.enterRule(localctx, 68, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(CSlangParser.BREAK)
            self.state = 366
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
        self.enterRule(localctx, 70, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(CSlangParser.CONTINUE)
            self.state = 369
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
        self.enterRule(localctx, 72, self.RULE_method_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.expr8()
            self.state = 372
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
        self.enterRule(localctx, 74, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(CSlangParser.RETURN)
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.NOT) | (1 << CSlangParser.OPENCC) | (1 << CSlangParser.OPENSQ) | (1 << CSlangParser.At) | (1 << CSlangParser.ID) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT))) != 0):
                self.state = 375
                self.expressions()


            self.state = 378
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
        self.enterRule(localctx, 76, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(CSlangParser.OPENBR)
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.NOT) | (1 << CSlangParser.OPENCC) | (1 << CSlangParser.OPENSQ) | (1 << CSlangParser.OPENBR) | (1 << CSlangParser.At) | (1 << CSlangParser.ID) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT))) != 0):
                self.state = 381
                self.statement()
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 387
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
        self.enterRule(localctx, 78, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(CSlangParser.OPENSQ)
            self.state = 390
            self.litlist()
            self.state = 391
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
        self.enterRule(localctx, 80, self.RULE_litlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.literal()
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 394
                self.match(CSlangParser.COMMA)
                self.state = 395
                self.literal()
                self.state = 400
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
        self.enterRule(localctx, 82, self.RULE_literal)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 403
                self.boollit()
                pass
            elif token in [CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 404
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
        self.enterRule(localctx, 84, self.RULE_iden)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
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
        self.enterRule(localctx, 86, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
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
        self._predicates[17] = self.expr1_sempred
        self._predicates[18] = self.expr2_sempred
        self._predicates[19] = self.expr3_sempred
        self._predicates[23] = self.expr7_sempred
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
         




