# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\u017b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3`\n\3\3\4\3\4\5\4d\n\4\3\5\3\5\5\5h")
        buf.write("\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\5\6x\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b\u0082")
        buf.write("\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u008a\n\t\3\t\3\t\3\t")
        buf.write("\5\t\u008f\n\t\3\t\3\t\3\n\3\n\3\13\5\13\u0096\n\13\3")
        buf.write("\13\5\13\u0099\n\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\5\f\u00a4\n\f\3\r\3\r\3\r\5\r\u00a9\n\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00b1\n\16\3\17\3\17\3\17\5")
        buf.write("\17\u00b6\n\17\3\20\3\20\3\20\3\20\5\20\u00bc\n\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\5\24\u00cb\n\24\3\24\3\24\3\25\3\25\3\25\3\25\3")
        buf.write("\25\5\25\u00d4\n\25\3\26\3\26\3\26\3\26\3\26\5\26\u00db")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u00e3\n\27\f")
        buf.write("\27\16\27\u00e6\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7")
        buf.write("\30\u00ee\n\30\f\30\16\30\u00f1\13\30\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\7\31\u00f9\n\31\f\31\16\31\u00fc\13\31\3")
        buf.write("\32\3\32\3\32\5\32\u0101\n\32\3\33\3\33\3\33\5\33\u0106")
        buf.write("\n\33\3\34\3\34\5\34\u010a\n\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0117\n\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\5\37\u0128\n\37\3 \3 \5 \u012c\n \3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u013a\n\"\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3")
        buf.write("%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\5)\u015d")
        buf.write("\n)\3)\3)\3*\3*\3*\5*\u0164\n*\3*\3*\3*\3+\3+\3+\7+\u016c")
        buf.write("\n+\f+\16+\u016f\13+\3+\3+\3,\3,\3,\7,\u0176\n,\f,\16")
        buf.write(",\u0179\13,\3,\2\5,.\60-\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTV\2\b\3\2")
        buf.write("\13\f\3\2\r\20\7\2\35\35!!##%&((\4\2  \"\"\4\2\33\33\36")
        buf.write("\36\5\2\37\37$$\'\'\2\u0180\2X\3\2\2\2\4_\3\2\2\2\6c\3")
        buf.write("\2\2\2\bg\3\2\2\2\nw\3\2\2\2\fy\3\2\2\2\16\u0081\3\2\2")
        buf.write("\2\20\u0083\3\2\2\2\22\u0092\3\2\2\2\24\u0095\3\2\2\2")
        buf.write("\26\u00a3\3\2\2\2\30\u00a5\3\2\2\2\32\u00b0\3\2\2\2\34")
        buf.write("\u00b5\3\2\2\2\36\u00bb\3\2\2\2 \u00bd\3\2\2\2\"\u00c4")
        buf.write("\3\2\2\2$\u00c6\3\2\2\2&\u00c8\3\2\2\2(\u00d3\3\2\2\2")
        buf.write("*\u00da\3\2\2\2,\u00dc\3\2\2\2.\u00e7\3\2\2\2\60\u00f2")
        buf.write("\3\2\2\2\62\u0100\3\2\2\2\64\u0105\3\2\2\2\66\u0109\3")
        buf.write("\2\2\28\u0116\3\2\2\2:\u0118\3\2\2\2<\u0127\3\2\2\2>\u012b")
        buf.write("\3\2\2\2@\u012d\3\2\2\2B\u0132\3\2\2\2D\u013b\3\2\2\2")
        buf.write("F\u0147\3\2\2\2H\u014a\3\2\2\2J\u014f\3\2\2\2L\u0154\3")
        buf.write("\2\2\2N\u0157\3\2\2\2P\u015a\3\2\2\2R\u0160\3\2\2\2T\u0168")
        buf.write("\3\2\2\2V\u0172\3\2\2\2XY\5\4\3\2YZ\7\2\2\3Z\3\3\2\2\2")
        buf.write("[\\\5\6\4\2\\]\5\4\3\2]`\3\2\2\2^`\5\6\4\2_[\3\2\2\2_")
        buf.write("^\3\2\2\2`\5\3\2\2\2ad\5\20\t\2bd\5\b\5\2ca\3\2\2\2cb")
        buf.write("\3\2\2\2d\7\3\2\2\2eh\5\n\6\2fh\5\f\7\2ge\3\2\2\2gf\3")
        buf.write("\2\2\2hi\3\2\2\2ij\7-\2\2j\t\3\2\2\2kl\7\65\2\2lm\7,\2")
        buf.write("\2mn\5\n\6\2no\7,\2\2op\5(\25\2px\3\2\2\2qr\7\65\2\2r")
        buf.write("s\7+\2\2st\5\34\17\2tu\7\64\2\2uv\5(\25\2vx\3\2\2\2wk")
        buf.write("\3\2\2\2wq\3\2\2\2x\13\3\2\2\2yz\5\16\b\2z{\7+\2\2{|\5")
        buf.write("\34\17\2|\r\3\2\2\2}~\7\65\2\2~\177\7,\2\2\177\u0082\5")
        buf.write("\16\b\2\u0080\u0082\7\65\2\2\u0081}\3\2\2\2\u0081\u0080")
        buf.write("\3\2\2\2\u0082\17\3\2\2\2\u0083\u0084\7\65\2\2\u0084\u0085")
        buf.write("\7+\2\2\u0085\u0086\7\24\2\2\u0086\u0087\5\36\20\2\u0087")
        buf.write("\u0089\7.\2\2\u0088\u008a\5\26\f\2\u0089\u0088\3\2\2\2")
        buf.write("\u0089\u008a\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008e\7")
        buf.write("/\2\2\u008c\u008d\7\32\2\2\u008d\u008f\7\65\2\2\u008e")
        buf.write("\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\u0091\5\22\n\2\u0091\21\3\2\2\2\u0092\u0093\5T")
        buf.write("+\2\u0093\23\3\2\2\2\u0094\u0096\7\32\2\2\u0095\u0094")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\3\2\2\2\u0097")
        buf.write("\u0099\7\23\2\2\u0098\u0097\3\2\2\2\u0098\u0099\3\2\2")
        buf.write("\2\u0099\u009a\3\2\2\2\u009a\u009b\7\65\2\2\u009b\u009c")
        buf.write("\7+\2\2\u009c\u009d\5\34\17\2\u009d\25\3\2\2\2\u009e\u009f")
        buf.write("\5\24\13\2\u009f\u00a0\7,\2\2\u00a0\u00a1\5\26\f\2\u00a1")
        buf.write("\u00a4\3\2\2\2\u00a2\u00a4\5\24\13\2\u00a3\u009e\3\2\2")
        buf.write("\2\u00a3\u00a2\3\2\2\2\u00a4\27\3\2\2\2\u00a5\u00a6\7")
        buf.write("\65\2\2\u00a6\u00a8\7.\2\2\u00a7\u00a9\5V,\2\u00a8\u00a7")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa")
        buf.write("\u00ab\7/\2\2\u00ab\31\3\2\2\2\u00ac\u00ad\7\66\2\2\u00ad")
        buf.write("\u00ae\7,\2\2\u00ae\u00b1\5\32\16\2\u00af\u00b1\7\66\2")
        buf.write("\2\u00b0\u00ac\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1\33\3")
        buf.write("\2\2\2\u00b2\u00b6\5$\23\2\u00b3\u00b6\5 \21\2\u00b4\u00b6")
        buf.write("\7\6\2\2\u00b5\u00b2\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5")
        buf.write("\u00b4\3\2\2\2\u00b6\35\3\2\2\2\u00b7\u00bc\5$\23\2\u00b8")
        buf.write("\u00bc\5 \21\2\u00b9\u00bc\7\22\2\2\u00ba\u00bc\7\6\2")
        buf.write("\2\u00bb\u00b7\3\2\2\2\u00bb\u00b8\3\2\2\2\u00bb\u00b9")
        buf.write("\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\37\3\2\2\2\u00bd\u00be")
        buf.write("\7\26\2\2\u00be\u00bf\7\60\2\2\u00bf\u00c0\5\32\16\2\u00c0")
        buf.write("\u00c1\7\61\2\2\u00c1\u00c2\7\25\2\2\u00c2\u00c3\5$\23")
        buf.write("\2\u00c3!\3\2\2\2\u00c4\u00c5\t\2\2\2\u00c5#\3\2\2\2\u00c6")
        buf.write("\u00c7\t\3\2\2\u00c7%\3\2\2\2\u00c8\u00ca\7\62\2\2\u00c9")
        buf.write("\u00cb\5V,\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb")
        buf.write("\u00cc\3\2\2\2\u00cc\u00cd\7\63\2\2\u00cd\'\3\2\2\2\u00ce")
        buf.write("\u00cf\5*\26\2\u00cf\u00d0\7)\2\2\u00d0\u00d1\5*\26\2")
        buf.write("\u00d1\u00d4\3\2\2\2\u00d2\u00d4\5*\26\2\u00d3\u00ce\3")
        buf.write("\2\2\2\u00d3\u00d2\3\2\2\2\u00d4)\3\2\2\2\u00d5\u00d6")
        buf.write("\5,\27\2\u00d6\u00d7\t\4\2\2\u00d7\u00d8\5,\27\2\u00d8")
        buf.write("\u00db\3\2\2\2\u00d9\u00db\5,\27\2\u00da\u00d5\3\2\2\2")
        buf.write("\u00da\u00d9\3\2\2\2\u00db+\3\2\2\2\u00dc\u00dd\b\27\1")
        buf.write("\2\u00dd\u00de\5.\30\2\u00de\u00e4\3\2\2\2\u00df\u00e0")
        buf.write("\f\4\2\2\u00e0\u00e1\t\5\2\2\u00e1\u00e3\5.\30\2\u00e2")
        buf.write("\u00df\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2")
        buf.write("\u00e4\u00e5\3\2\2\2\u00e5-\3\2\2\2\u00e6\u00e4\3\2\2")
        buf.write("\2\u00e7\u00e8\b\30\1\2\u00e8\u00e9\5\60\31\2\u00e9\u00ef")
        buf.write("\3\2\2\2\u00ea\u00eb\f\4\2\2\u00eb\u00ec\t\6\2\2\u00ec")
        buf.write("\u00ee\5\60\31\2\u00ed\u00ea\3\2\2\2\u00ee\u00f1\3\2\2")
        buf.write("\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0/\3\2")
        buf.write("\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\b\31\1\2\u00f3\u00f4")
        buf.write("\5\62\32\2\u00f4\u00fa\3\2\2\2\u00f5\u00f6\f\4\2\2\u00f6")
        buf.write("\u00f7\t\7\2\2\u00f7\u00f9\5\62\32\2\u00f8\u00f5\3\2\2")
        buf.write("\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb")
        buf.write("\3\2\2\2\u00fb\61\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00fe")
        buf.write("\7\34\2\2\u00fe\u0101\5\62\32\2\u00ff\u0101\5\64\33\2")
        buf.write("\u0100\u00fd\3\2\2\2\u0100\u00ff\3\2\2\2\u0101\63\3\2")
        buf.write("\2\2\u0102\u0103\7\36\2\2\u0103\u0106\5\64\33\2\u0104")
        buf.write("\u0106\5\66\34\2\u0105\u0102\3\2\2\2\u0105\u0104\3\2\2")
        buf.write("\2\u0106\65\3\2\2\2\u0107\u010a\5:\36\2\u0108\u010a\5")
        buf.write("8\35\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2\u010a\67")
        buf.write("\3\2\2\2\u010b\u0117\7\65\2\2\u010c\u0117\7\66\2\2\u010d")
        buf.write("\u0117\7\67\2\2\u010e\u0117\5\"\22\2\u010f\u0117\78\2")
        buf.write("\2\u0110\u0117\5&\24\2\u0111\u0117\5\30\r\2\u0112\u0113")
        buf.write("\7.\2\2\u0113\u0114\5(\25\2\u0114\u0115\7/\2\2\u0115\u0117")
        buf.write("\3\2\2\2\u0116\u010b\3\2\2\2\u0116\u010c\3\2\2\2\u0116")
        buf.write("\u010d\3\2\2\2\u0116\u010e\3\2\2\2\u0116\u010f\3\2\2\2")
        buf.write("\u0116\u0110\3\2\2\2\u0116\u0111\3\2\2\2\u0116\u0112\3")
        buf.write("\2\2\2\u01179\3\2\2\2\u0118\u0119\7\65\2\2\u0119\u011a")
        buf.write("\7\60\2\2\u011a\u011b\5V,\2\u011b\u011c\7\61\2\2\u011c")
        buf.write(";\3\2\2\2\u011d\u0128\5@!\2\u011e\u0128\5B\"\2\u011f\u0128")
        buf.write("\5D#\2\u0120\u0128\5F$\2\u0121\u0128\5H%\2\u0122\u0128")
        buf.write("\5L\'\2\u0123\u0128\5N(\2\u0124\u0128\5P)\2\u0125\u0128")
        buf.write("\5R*\2\u0126\u0128\5T+\2\u0127\u011d\3\2\2\2\u0127\u011e")
        buf.write("\3\2\2\2\u0127\u011f\3\2\2\2\u0127\u0120\3\2\2\2\u0127")
        buf.write("\u0121\3\2\2\2\u0127\u0122\3\2\2\2\u0127\u0123\3\2\2\2")
        buf.write("\u0127\u0124\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0126\3")
        buf.write("\2\2\2\u0128=\3\2\2\2\u0129\u012c\7\65\2\2\u012a\u012c")
        buf.write("\5:\36\2\u012b\u0129\3\2\2\2\u012b\u012a\3\2\2\2\u012c")
        buf.write("?\3\2\2\2\u012d\u012e\5> \2\u012e\u012f\7\64\2\2\u012f")
        buf.write("\u0130\5(\25\2\u0130\u0131\7-\2\2\u0131A\3\2\2\2\u0132")
        buf.write("\u0133\7\27\2\2\u0133\u0134\7.\2\2\u0134\u0135\5(\25\2")
        buf.write("\u0135\u0136\7/\2\2\u0136\u0139\5<\37\2\u0137\u0138\7")
        buf.write("\30\2\2\u0138\u013a\5<\37\2\u0139\u0137\3\2\2\2\u0139")
        buf.write("\u013a\3\2\2\2\u013aC\3\2\2\2\u013b\u013c\7\n\2\2\u013c")
        buf.write("\u013d\7.\2\2\u013d\u013e\5> \2\u013e\u013f\7\64\2\2\u013f")
        buf.write("\u0140\5(\25\2\u0140\u0141\7,\2\2\u0141\u0142\5(\25\2")
        buf.write("\u0142\u0143\7,\2\2\u0143\u0144\5(\25\2\u0144\u0145\7")
        buf.write("/\2\2\u0145\u0146\5<\37\2\u0146E\3\2\2\2\u0147\u0148\5")
        buf.write("J&\2\u0148\u0149\5<\37\2\u0149G\3\2\2\2\u014a\u014b\7")
        buf.write("\b\2\2\u014b\u014c\5T+\2\u014c\u014d\5J&\2\u014d\u014e")
        buf.write("\7-\2\2\u014eI\3\2\2\2\u014f\u0150\7\31\2\2\u0150\u0151")
        buf.write("\7.\2\2\u0151\u0152\5(\25\2\u0152\u0153\7/\2\2\u0153K")
        buf.write("\3\2\2\2\u0154\u0155\7\7\2\2\u0155\u0156\7-\2\2\u0156")
        buf.write("M\3\2\2\2\u0157\u0158\7\t\2\2\u0158\u0159\7-\2\2\u0159")
        buf.write("O\3\2\2\2\u015a\u015c\7\21\2\2\u015b\u015d\5(\25\2\u015c")
        buf.write("\u015b\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\3\2\2\2")
        buf.write("\u015e\u015f\7-\2\2\u015fQ\3\2\2\2\u0160\u0161\7\65\2")
        buf.write("\2\u0161\u0163\7.\2\2\u0162\u0164\5V,\2\u0163\u0162\3")
        buf.write("\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166")
        buf.write("\7/\2\2\u0166\u0167\7-\2\2\u0167S\3\2\2\2\u0168\u016d")
        buf.write("\7\62\2\2\u0169\u016c\5<\37\2\u016a\u016c\5\b\5\2\u016b")
        buf.write("\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016c\u016f\3\2\2\2")
        buf.write("\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0170\3")
        buf.write("\2\2\2\u016f\u016d\3\2\2\2\u0170\u0171\7\63\2\2\u0171")
        buf.write("U\3\2\2\2\u0172\u0177\5(\25\2\u0173\u0174\7,\2\2\u0174")
        buf.write("\u0176\5(\25\2\u0175\u0173\3\2\2\2\u0176\u0179\3\2\2\2")
        buf.write("\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178W\3\2\2")
        buf.write("\2\u0179\u0177\3\2\2\2\"_cgw\u0081\u0089\u008e\u0095\u0098")
        buf.write("\u00a3\u00a8\u00b0\u00b5\u00bb\u00ca\u00d3\u00da\u00e4")
        buf.write("\u00ef\u00fa\u0100\u0105\u0109\u0116\u0127\u012b\u0139")
        buf.write("\u015c\u0163\u016b\u016d\u0177")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'break'", "'do'", "'continue'", "'for'", 
                     "'true'", "'false'", "'integer'", "'float'", "'boolean'", 
                     "'string'", "'return'", "'void'", "'out'", "'function'", 
                     "'of'", "'array'", "'if'", "'else'", "'while'", "'inherit'", 
                     "'+'", "'!'", "'!='", "'-'", "'*'", "'&&'", "'<'", 
                     "'||'", "'<='", "'/'", "'=='", "'>'", "'%'", "'>='", 
                     "'::'", "'.'", "':'", "','", "';'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "WS", "LINE_CMT", "BLOCK_CMT", "AUTO", 
                      "BREAK", "DO", "CONTINUE", "FOR", "TRUE", "FALSE", 
                      "INTEGER", "FLOAT", "BOOLEAN", "STRING", "RETURN", 
                      "VOID", "OUT", "FUNCTION", "OF", "ARRAY", "IF", "ELSE", 
                      "WHILE", "INHERIT", "PLUS", "NOT", "DIF", "MINUS", 
                      "MUL", "AND", "SMALLER", "OR", "SMALLER_EQAL", "DIV", 
                      "EQ", "GREATER", "MOD", "GREATER_EQAL", "STRCONCAT", 
                      "DOT", "COLON", "COMMA", "SEMICO", "OPENCC", "CLOSECC", 
                      "OPENSQ", "CLOSESQ", "OPENBR", "CLOSEBR", "ASSIGN", 
                      "ID", "INTLIT", "FLOATLIT", "STRINGLIT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decl = 2
    RULE_vardec = 3
    RULE_var_assign = 4
    RULE_var_declare = 5
    RULE_id_list = 6
    RULE_funcdec = 7
    RULE_funcbody = 8
    RULE_param = 9
    RULE_param_list = 10
    RULE_funccall = 11
    RULE_dimension = 12
    RULE_var_type = 13
    RULE_type_list = 14
    RULE_array_type = 15
    RULE_boolean = 16
    RULE_atomic = 17
    RULE_arraylit = 18
    RULE_expr = 19
    RULE_expr1 = 20
    RULE_expr2 = 21
    RULE_expr3 = 22
    RULE_expr4 = 23
    RULE_expr5 = 24
    RULE_expr6 = 25
    RULE_expr7 = 26
    RULE_expr8 = 27
    RULE_indexOp = 28
    RULE_statement = 29
    RULE_lhs = 30
    RULE_assign_statement = 31
    RULE_if_statement = 32
    RULE_for_statement = 33
    RULE_while_statement = 34
    RULE_dowhile_statement = 35
    RULE_while_con = 36
    RULE_break_statement = 37
    RULE_continue_statement = 38
    RULE_return_statement = 39
    RULE_call_statement = 40
    RULE_block_statement = 41
    RULE_expr_list = 42

    ruleNames =  [ "program", "decls", "decl", "vardec", "var_assign", "var_declare", 
                   "id_list", "funcdec", "funcbody", "param", "param_list", 
                   "funccall", "dimension", "var_type", "type_list", "array_type", 
                   "boolean", "atomic", "arraylit", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr8", 
                   "indexOp", "statement", "lhs", "assign_statement", "if_statement", 
                   "for_statement", "while_statement", "dowhile_statement", 
                   "while_con", "break_statement", "continue_statement", 
                   "return_statement", "call_statement", "block_statement", 
                   "expr_list" ]

    EOF = Token.EOF
    WS=1
    LINE_CMT=2
    BLOCK_CMT=3
    AUTO=4
    BREAK=5
    DO=6
    CONTINUE=7
    FOR=8
    TRUE=9
    FALSE=10
    INTEGER=11
    FLOAT=12
    BOOLEAN=13
    STRING=14
    RETURN=15
    VOID=16
    OUT=17
    FUNCTION=18
    OF=19
    ARRAY=20
    IF=21
    ELSE=22
    WHILE=23
    INHERIT=24
    PLUS=25
    NOT=26
    DIF=27
    MINUS=28
    MUL=29
    AND=30
    SMALLER=31
    OR=32
    SMALLER_EQAL=33
    DIV=34
    EQ=35
    GREATER=36
    MOD=37
    GREATER_EQAL=38
    STRCONCAT=39
    DOT=40
    COLON=41
    COMMA=42
    SEMICO=43
    OPENCC=44
    CLOSECC=45
    OPENSQ=46
    CLOSESQ=47
    OPENBR=48
    CLOSEBR=49
    ASSIGN=50
    ID=51
    INTLIT=52
    FLOATLIT=53
    STRINGLIT=54
    UNCLOSE_STRING=55
    ILLEGAL_ESCAPE=56
    ERROR_CHAR=57

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

        def decls(self):
            return self.getTypedRuleContext(MT22Parser.DeclsContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.decls()
            self.state = 87
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(MT22Parser.DeclsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = MT22Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.decl()
                self.state = 90
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdec(self):
            return self.getTypedRuleContext(MT22Parser.FuncdecContext,0)


        def vardec(self):
            return self.getTypedRuleContext(MT22Parser.VardecContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.funcdec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.vardec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICO(self):
            return self.getToken(MT22Parser.SEMICO, 0)

        def var_assign(self):
            return self.getTypedRuleContext(MT22Parser.Var_assignContext,0)


        def var_declare(self):
            return self.getTypedRuleContext(MT22Parser.Var_declareContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardec" ):
                return visitor.visitVardec(self)
            else:
                return visitor.visitChildren(self)




    def vardec(self):

        localctx = MT22Parser.VardecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 99
                self.var_assign()
                pass

            elif la_ == 2:
                self.state = 100
                self.var_declare()
                pass


            self.state = 103
            self.match(MT22Parser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def var_assign(self):
            return self.getTypedRuleContext(MT22Parser.Var_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def var_type(self):
            return self.getTypedRuleContext(MT22Parser.Var_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_var_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_assign" ):
                return visitor.visitVar_assign(self)
            else:
                return visitor.visitChildren(self)




    def var_assign(self):

        localctx = MT22Parser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_assign)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(MT22Parser.ID)
                self.state = 106
                self.match(MT22Parser.COMMA)
                self.state = 107
                self.var_assign()
                self.state = 108
                self.match(MT22Parser.COMMA)
                self.state = 109
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(MT22Parser.ID)
                self.state = 112
                self.match(MT22Parser.COLON)
                self.state = 113
                self.var_type()
                self.state = 114
                self.match(MT22Parser.ASSIGN)
                self.state = 115
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(MT22Parser.Id_listContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def var_type(self):
            return self.getTypedRuleContext(MT22Parser.Var_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = MT22Parser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.id_list()
            self.state = 120
            self.match(MT22Parser.COLON)
            self.state = 121
            self.var_type()
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

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def id_list(self):
            return self.getTypedRuleContext(MT22Parser.Id_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = MT22Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_id_list)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(MT22Parser.ID)
                self.state = 124
                self.match(MT22Parser.COMMA)
                self.state = 125
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def type_list(self):
            return self.getTypedRuleContext(MT22Parser.Type_listContext,0)


        def OPENCC(self):
            return self.getToken(MT22Parser.OPENCC, 0)

        def CLOSECC(self):
            return self.getToken(MT22Parser.CLOSECC, 0)

        def funcbody(self):
            return self.getTypedRuleContext(MT22Parser.FuncbodyContext,0)


        def param_list(self):
            return self.getTypedRuleContext(MT22Parser.Param_listContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funcdec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdec" ):
                return visitor.visitFuncdec(self)
            else:
                return visitor.visitChildren(self)




    def funcdec(self):

        localctx = MT22Parser.FuncdecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcdec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(MT22Parser.ID)
            self.state = 130
            self.match(MT22Parser.COLON)
            self.state = 131
            self.match(MT22Parser.FUNCTION)
            self.state = 132
            self.type_list()
            self.state = 133
            self.match(MT22Parser.OPENCC)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.OUT) | (1 << MT22Parser.INHERIT) | (1 << MT22Parser.ID))) != 0):
                self.state = 134
                self.param_list()


            self.state = 137
            self.match(MT22Parser.CLOSECC)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 138
                self.match(MT22Parser.INHERIT)
                self.state = 139
                self.match(MT22Parser.ID)


            self.state = 142
            self.funcbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_statement(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncbody" ):
                return visitor.visitFuncbody(self)
            else:
                return visitor.visitChildren(self)




    def funcbody(self):

        localctx = MT22Parser.FuncbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def var_type(self):
            return self.getTypedRuleContext(MT22Parser.Var_typeContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MT22Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 146
                self.match(MT22Parser.INHERIT)


            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 149
                self.match(MT22Parser.OUT)


            self.state = 152
            self.match(MT22Parser.ID)
            self.state = 153
            self.match(MT22Parser.COLON)
            self.state = 154
            self.var_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MT22Parser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def param_list(self):
            return self.getTypedRuleContext(MT22Parser.Param_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = MT22Parser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param_list)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.param()
                self.state = 157
                self.match(MT22Parser.COMMA)
                self.state = 158
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def OPENCC(self):
            return self.getToken(MT22Parser.OPENCC, 0)

        def CLOSECC(self):
            return self.getToken(MT22Parser.CLOSECC, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = MT22Parser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funccall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(MT22Parser.ID)
            self.state = 164
            self.match(MT22Parser.OPENCC)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.TRUE) | (1 << MT22Parser.FALSE) | (1 << MT22Parser.NOT) | (1 << MT22Parser.MINUS) | (1 << MT22Parser.OPENCC) | (1 << MT22Parser.OPENBR) | (1 << MT22Parser.ID) | (1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.STRINGLIT))) != 0):
                self.state = 165
                self.expr_list()


            self.state = 168
            self.match(MT22Parser.CLOSECC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def dimension(self):
            return self.getTypedRuleContext(MT22Parser.DimensionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = MT22Parser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dimension)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.match(MT22Parser.INTLIT)
                self.state = 171
                self.match(MT22Parser.COMMA)
                self.state = 172
                self.dimension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(MT22Parser.INTLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomic(self):
            return self.getTypedRuleContext(MT22Parser.AtomicContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_var_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_type" ):
                return visitor.visitVar_type(self)
            else:
                return visitor.visitChildren(self)




    def var_type(self):

        localctx = MT22Parser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_var_type)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTEGER, MT22Parser.FLOAT, MT22Parser.BOOLEAN, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.atomic()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.array_type()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
                self.match(MT22Parser.AUTO)
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


    class Type_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomic(self):
            return self.getTypedRuleContext(MT22Parser.AtomicContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_type_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_list" ):
                return visitor.visitType_list(self)
            else:
                return visitor.visitChildren(self)




    def type_list(self):

        localctx = MT22Parser.Type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_type_list)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTEGER, MT22Parser.FLOAT, MT22Parser.BOOLEAN, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.atomic()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.array_type()
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.match(MT22Parser.VOID)
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 184
                self.match(MT22Parser.AUTO)
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

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def OPENSQ(self):
            return self.getToken(MT22Parser.OPENSQ, 0)

        def dimension(self):
            return self.getTypedRuleContext(MT22Parser.DimensionContext,0)


        def CLOSESQ(self):
            return self.getToken(MT22Parser.CLOSESQ, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomic(self):
            return self.getTypedRuleContext(MT22Parser.AtomicContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MT22Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(MT22Parser.ARRAY)
            self.state = 188
            self.match(MT22Parser.OPENSQ)
            self.state = 189
            self.dimension()
            self.state = 190
            self.match(MT22Parser.CLOSESQ)
            self.state = 191
            self.match(MT22Parser.OF)
            self.state = 192
            self.atomic()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MT22Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MT22Parser.FALSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_boolean

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)




    def boolean(self):

        localctx = MT22Parser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            _la = self._input.LA(1)
            if not(_la==MT22Parser.TRUE or _la==MT22Parser.FALSE):
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


    class AtomicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic" ):
                return visitor.visitAtomic(self)
            else:
                return visitor.visitChildren(self)




    def atomic(self):

        localctx = MT22Parser.AtomicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_atomic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.STRING))) != 0)):
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


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENBR(self):
            return self.getToken(MT22Parser.OPENBR, 0)

        def CLOSEBR(self):
            return self.getToken(MT22Parser.CLOSEBR, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = MT22Parser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arraylit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(MT22Parser.OPENBR)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.TRUE) | (1 << MT22Parser.FALSE) | (1 << MT22Parser.NOT) | (1 << MT22Parser.MINUS) | (1 << MT22Parser.OPENCC) | (1 << MT22Parser.OPENBR) | (1 << MT22Parser.ID) | (1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.STRINGLIT))) != 0):
                self.state = 199
                self.expr_list()


            self.state = 202
            self.match(MT22Parser.CLOSEBR)
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
                return self.getTypedRuleContexts(MT22Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr1Context,i)


        def STRCONCAT(self):
            return self.getToken(MT22Parser.STRCONCAT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.expr1()
                self.state = 205
                self.match(MT22Parser.STRCONCAT)
                self.state = 206
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.expr1()
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

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr2Context,i)


        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def DIF(self):
            return self.getToken(MT22Parser.DIF, 0)

        def SMALLER(self):
            return self.getToken(MT22Parser.SMALLER, 0)

        def GREATER(self):
            return self.getToken(MT22Parser.GREATER, 0)

        def GREATER_EQAL(self):
            return self.getToken(MT22Parser.GREATER_EQAL, 0)

        def SMALLER_EQAL(self):
            return self.getToken(MT22Parser.SMALLER_EQAL, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.expr2(0)
                self.state = 212
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.DIF) | (1 << MT22Parser.SMALLER) | (1 << MT22Parser.SMALLER_EQAL) | (1 << MT22Parser.EQ) | (1 << MT22Parser.GREATER) | (1 << MT22Parser.GREATER_EQAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 213
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 221
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 222
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 223
                    self.expr3(0) 
                self.state = 228
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
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def PLUS(self):
            return self.getToken(MT22Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 232
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 233
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.PLUS or _la==MT22Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 234
                    self.expr4(0) 
                self.state = 239
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

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def MUL(self):
            return self.getToken(MT22Parser.MUL, 0)

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def MOD(self):
            return self.getToken(MT22Parser.MOD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 243
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 244
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUL) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 245
                    self.expr5() 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr5)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(MT22Parser.NOT)
                self.state = 252
                self.expr5()
                pass
            elif token in [MT22Parser.TRUE, MT22Parser.FALSE, MT22Parser.MINUS, MT22Parser.OPENCC, MT22Parser.OPENBR, MT22Parser.ID, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
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

        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def expr7(self):
            return self.getTypedRuleContext(MT22Parser.Expr7Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr6)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(MT22Parser.MINUS)
                self.state = 257
                self.expr6()
                pass
            elif token in [MT22Parser.TRUE, MT22Parser.FALSE, MT22Parser.OPENCC, MT22Parser.OPENBR, MT22Parser.ID, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.expr7()
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexOp(self):
            return self.getTypedRuleContext(MT22Parser.IndexOpContext,0)


        def expr8(self):
            return self.getTypedRuleContext(MT22Parser.Expr8Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MT22Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr7)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.indexOp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.expr8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def boolean(self):
            return self.getTypedRuleContext(MT22Parser.BooleanContext,0)


        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

        def arraylit(self):
            return self.getTypedRuleContext(MT22Parser.ArraylitContext,0)


        def funccall(self):
            return self.getTypedRuleContext(MT22Parser.FunccallContext,0)


        def OPENCC(self):
            return self.getToken(MT22Parser.OPENCC, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def CLOSECC(self):
            return self.getToken(MT22Parser.CLOSECC, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = MT22Parser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr8)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.match(MT22Parser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 268
                self.boolean()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 269
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 270
                self.arraylit()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 271
                self.funccall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 272
                self.match(MT22Parser.OPENCC)
                self.state = 273
                self.expr()
                self.state = 274
                self.match(MT22Parser.CLOSECC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def OPENSQ(self):
            return self.getToken(MT22Parser.OPENSQ, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def CLOSESQ(self):
            return self.getToken(MT22Parser.CLOSESQ, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_indexOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexOp" ):
                return visitor.visitIndexOp(self)
            else:
                return visitor.visitChildren(self)




    def indexOp(self):

        localctx = MT22Parser.IndexOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_indexOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(MT22Parser.ID)
            self.state = 279
            self.match(MT22Parser.OPENSQ)
            self.state = 280
            self.expr_list()
            self.state = 281
            self.match(MT22Parser.CLOSESQ)
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

        def assign_statement(self):
            return self.getTypedRuleContext(MT22Parser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MT22Parser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MT22Parser.For_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(MT22Parser.While_statementContext,0)


        def dowhile_statement(self):
            return self.getTypedRuleContext(MT22Parser.Dowhile_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MT22Parser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MT22Parser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MT22Parser.Return_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MT22Parser.Call_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_statement)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.assign_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 285
                self.for_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 286
                self.while_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 287
                self.dowhile_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 288
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 289
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 290
                self.return_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 291
                self.call_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 292
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def indexOp(self):
            return self.getTypedRuleContext(MT22Parser.IndexOpContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MT22Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_lhs)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.indexOp()
                pass


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

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def SEMICO(self):
            return self.getToken(MT22Parser.SEMICO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MT22Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.lhs()
            self.state = 300
            self.match(MT22Parser.ASSIGN)
            self.state = 301
            self.expr()
            self.state = 302
            self.match(MT22Parser.SEMICO)
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
            return self.getToken(MT22Parser.IF, 0)

        def OPENCC(self):
            return self.getToken(MT22Parser.OPENCC, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def CLOSECC(self):
            return self.getToken(MT22Parser.CLOSECC, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MT22Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(MT22Parser.IF)
            self.state = 305
            self.match(MT22Parser.OPENCC)
            self.state = 306
            self.expr()
            self.state = 307
            self.match(MT22Parser.CLOSECC)
            self.state = 308
            self.statement()
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 309
                self.match(MT22Parser.ELSE)
                self.state = 310
                self.statement()


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
            return self.getToken(MT22Parser.FOR, 0)

        def OPENCC(self):
            return self.getToken(MT22Parser.OPENCC, 0)

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def CLOSECC(self):
            return self.getToken(MT22Parser.CLOSECC, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MT22Parser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(MT22Parser.FOR)
            self.state = 314
            self.match(MT22Parser.OPENCC)
            self.state = 315
            self.lhs()
            self.state = 316
            self.match(MT22Parser.ASSIGN)
            self.state = 317
            self.expr()
            self.state = 318
            self.match(MT22Parser.COMMA)
            self.state = 319
            self.expr()
            self.state = 320
            self.match(MT22Parser.COMMA)
            self.state = 321
            self.expr()
            self.state = 322
            self.match(MT22Parser.CLOSECC)
            self.state = 323
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def while_con(self):
            return self.getTypedRuleContext(MT22Parser.While_conContext,0)


        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = MT22Parser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.while_con()
            self.state = 326
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dowhile_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def block_statement(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementContext,0)


        def while_con(self):
            return self.getTypedRuleContext(MT22Parser.While_conContext,0)


        def SEMICO(self):
            return self.getToken(MT22Parser.SEMICO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dowhile_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhile_statement" ):
                return visitor.visitDowhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def dowhile_statement(self):

        localctx = MT22Parser.Dowhile_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_dowhile_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(MT22Parser.DO)
            self.state = 329
            self.block_statement()
            self.state = 330
            self.while_con()
            self.state = 331
            self.match(MT22Parser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_conContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def OPENCC(self):
            return self.getToken(MT22Parser.OPENCC, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def CLOSECC(self):
            return self.getToken(MT22Parser.CLOSECC, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_while_con

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_con" ):
                return visitor.visitWhile_con(self)
            else:
                return visitor.visitChildren(self)




    def while_con(self):

        localctx = MT22Parser.While_conContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_while_con)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(MT22Parser.WHILE)
            self.state = 334
            self.match(MT22Parser.OPENCC)
            self.state = 335
            self.expr()
            self.state = 336
            self.match(MT22Parser.CLOSECC)
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
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMICO(self):
            return self.getToken(MT22Parser.SEMICO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MT22Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(MT22Parser.BREAK)
            self.state = 339
            self.match(MT22Parser.SEMICO)
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
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEMICO(self):
            return self.getToken(MT22Parser.SEMICO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MT22Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(MT22Parser.CONTINUE)
            self.state = 342
            self.match(MT22Parser.SEMICO)
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
            return self.getToken(MT22Parser.RETURN, 0)

        def SEMICO(self):
            return self.getToken(MT22Parser.SEMICO, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MT22Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(MT22Parser.RETURN)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.TRUE) | (1 << MT22Parser.FALSE) | (1 << MT22Parser.NOT) | (1 << MT22Parser.MINUS) | (1 << MT22Parser.OPENCC) | (1 << MT22Parser.OPENBR) | (1 << MT22Parser.ID) | (1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.STRINGLIT))) != 0):
                self.state = 345
                self.expr()


            self.state = 348
            self.match(MT22Parser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def OPENCC(self):
            return self.getToken(MT22Parser.OPENCC, 0)

        def CLOSECC(self):
            return self.getToken(MT22Parser.CLOSECC, 0)

        def SEMICO(self):
            return self.getToken(MT22Parser.SEMICO, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MT22Parser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(MT22Parser.ID)
            self.state = 351
            self.match(MT22Parser.OPENCC)
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.TRUE) | (1 << MT22Parser.FALSE) | (1 << MT22Parser.NOT) | (1 << MT22Parser.MINUS) | (1 << MT22Parser.OPENCC) | (1 << MT22Parser.OPENBR) | (1 << MT22Parser.ID) | (1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.STRINGLIT))) != 0):
                self.state = 352
                self.expr_list()


            self.state = 355
            self.match(MT22Parser.CLOSECC)
            self.state = 356
            self.match(MT22Parser.SEMICO)
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
            return self.getToken(MT22Parser.OPENBR, 0)

        def CLOSEBR(self):
            return self.getToken(MT22Parser.CLOSEBR, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def vardec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.VardecContext)
            else:
                return self.getTypedRuleContext(MT22Parser.VardecContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = MT22Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(MT22Parser.OPENBR)
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BREAK) | (1 << MT22Parser.DO) | (1 << MT22Parser.CONTINUE) | (1 << MT22Parser.FOR) | (1 << MT22Parser.RETURN) | (1 << MT22Parser.IF) | (1 << MT22Parser.WHILE) | (1 << MT22Parser.OPENBR) | (1 << MT22Parser.ID))) != 0):
                self.state = 361
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 359
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 360
                    self.vardec()
                    pass


                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 366
            self.match(MT22Parser.CLOSEBR)
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = MT22Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.expr()
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 369
                self.match(MT22Parser.COMMA)
                self.state = 370
                self.expr()
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self._predicates[21] = self.expr2_sempred
        self._predicates[22] = self.expr3_sempred
        self._predicates[23] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




