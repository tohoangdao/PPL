# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01db\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\6\2\u0085")
        buf.write("\n\2\r\2\16\2\u0086\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u008f")
        buf.write("\n\3\f\3\16\3\u0092\13\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u009a")
        buf.write("\n\4\f\4\16\4\u009d\13\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\7\64\u015c\n\64\f")
        buf.write("\64\16\64\u015f\13\64\3\65\3\65\3\65\5\65\u0164\n\65\3")
        buf.write("\65\7\65\u0167\n\65\f\65\16\65\u016a\13\65\3\65\5\65\u016d")
        buf.write("\n\65\3\66\6\66\u0170\n\66\r\66\16\66\u0171\3\66\5\66")
        buf.write("\u0175\n\66\3\66\3\66\3\66\6\66\u017a\n\66\r\66\16\66")
        buf.write("\u017b\3\66\3\66\3\66\3\66\3\66\5\66\u0183\n\66\3\66\3")
        buf.write("\66\3\67\3\67\7\67\u0189\n\67\f\67\16\67\u018c\13\67\3")
        buf.write("8\38\58\u0190\n8\38\68\u0193\n8\r8\168\u0194\39\39\69")
        buf.write("\u0199\n9\r9\169\u019a\39\79\u019e\n9\f9\169\u01a1\13")
        buf.write("9\59\u01a3\n9\3:\3:\3;\3;\3;\3;\5;\u01ab\n;\3<\3<\3<\3")
        buf.write("=\3=\7=\u01b2\n=\f=\16=\u01b5\13=\3=\3=\3=\3>\3>\3>\5")
        buf.write(">\u01bd\n>\3?\3?\3?\7?\u01c2\n?\f?\16?\u01c5\13?\3?\5")
        buf.write("?\u01c8\n?\3?\3?\3@\3@\3@\7@\u01cf\n@\f@\16@\u01d2\13")
        buf.write("@\3@\3@\3@\3@\3@\3A\3A\3A\3\u009b\2B\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\64g\65i\66k\67m\2o\2q\2s\2u\2w\2y8{\2}9\177")
        buf.write(":\u0081;\3\2\23\5\2\n\f\16\17\"\"\4\2\f\f\17\17\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\3\2\62\62\3\2\63;\3\2aa\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\4\2\62;aa\7\2\f\f\17\17$$))^^\t\2))^^d")
        buf.write("dhhppttvv\3\2^^\3\2$$\7\2\n\f\16\17$$))^^\n\2$$))^^dd")
        buf.write("hhppttvv\2\u01ee\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2y\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0084\3")
        buf.write("\2\2\2\5\u008a\3\2\2\2\7\u0095\3\2\2\2\t\u00a3\3\2\2\2")
        buf.write("\13\u00a8\3\2\2\2\r\u00ae\3\2\2\2\17\u00b1\3\2\2\2\21")
        buf.write("\u00ba\3\2\2\2\23\u00be\3\2\2\2\25\u00c3\3\2\2\2\27\u00c9")
        buf.write("\3\2\2\2\31\u00d1\3\2\2\2\33\u00d7\3\2\2\2\35\u00df\3")
        buf.write("\2\2\2\37\u00e6\3\2\2\2!\u00ed\3\2\2\2#\u00f2\3\2\2\2")
        buf.write("%\u00f6\3\2\2\2\'\u00ff\3\2\2\2)\u0102\3\2\2\2+\u0108")
        buf.write("\3\2\2\2-\u010b\3\2\2\2/\u0110\3\2\2\2\61\u0116\3\2\2")
        buf.write("\2\63\u011e\3\2\2\2\65\u0120\3\2\2\2\67\u0122\3\2\2\2")
        buf.write("9\u0125\3\2\2\2;\u0127\3\2\2\2=\u0129\3\2\2\2?\u012c\3")
        buf.write("\2\2\2A\u012e\3\2\2\2C\u0131\3\2\2\2E\u0134\3\2\2\2G\u0136")
        buf.write("\3\2\2\2I\u0139\3\2\2\2K\u013b\3\2\2\2M\u013d\3\2\2\2")
        buf.write("O\u0140\3\2\2\2Q\u0143\3\2\2\2S\u0145\3\2\2\2U\u0147\3")
        buf.write("\2\2\2W\u0149\3\2\2\2Y\u014b\3\2\2\2[\u014d\3\2\2\2]\u014f")
        buf.write("\3\2\2\2_\u0151\3\2\2\2a\u0153\3\2\2\2c\u0155\3\2\2\2")
        buf.write("e\u0157\3\2\2\2g\u0159\3\2\2\2i\u016c\3\2\2\2k\u0182\3")
        buf.write("\2\2\2m\u0186\3\2\2\2o\u018d\3\2\2\2q\u01a2\3\2\2\2s\u01a4")
        buf.write("\3\2\2\2u\u01aa\3\2\2\2w\u01ac\3\2\2\2y\u01af\3\2\2\2")
        buf.write("{\u01bc\3\2\2\2}\u01be\3\2\2\2\177\u01cb\3\2\2\2\u0081")
        buf.write("\u01d8\3\2\2\2\u0083\u0085\t\2\2\2\u0084\u0083\3\2\2\2")
        buf.write("\u0085\u0086\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3")
        buf.write("\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\b\2\2\2\u0089\4")
        buf.write("\3\2\2\2\u008a\u008b\7\61\2\2\u008b\u008c\7\61\2\2\u008c")
        buf.write("\u0090\3\2\2\2\u008d\u008f\n\3\2\2\u008e\u008d\3\2\2\2")
        buf.write("\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3")
        buf.write("\2\2\2\u0091\u0093\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094")
        buf.write("\b\3\2\2\u0094\6\3\2\2\2\u0095\u0096\7\61\2\2\u0096\u0097")
        buf.write("\7,\2\2\u0097\u009b\3\2\2\2\u0098\u009a\13\2\2\2\u0099")
        buf.write("\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u009c\3\2\2\2")
        buf.write("\u009b\u0099\3\2\2\2\u009c\u009e\3\2\2\2\u009d\u009b\3")
        buf.write("\2\2\2\u009e\u009f\7,\2\2\u009f\u00a0\7\61\2\2\u00a0\u00a1")
        buf.write("\3\2\2\2\u00a1\u00a2\b\4\2\2\u00a2\b\3\2\2\2\u00a3\u00a4")
        buf.write("\7c\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7")
        buf.write("\7q\2\2\u00a7\n\3\2\2\2\u00a8\u00a9\7d\2\2\u00a9\u00aa")
        buf.write("\7t\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad")
        buf.write("\7m\2\2\u00ad\f\3\2\2\2\u00ae\u00af\7f\2\2\u00af\u00b0")
        buf.write("\7q\2\2\u00b0\16\3\2\2\2\u00b1\u00b2\7e\2\2\u00b2\u00b3")
        buf.write("\7q\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6")
        buf.write("\7k\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7w\2\2\u00b8\u00b9")
        buf.write("\7g\2\2\u00b9\20\3\2\2\2\u00ba\u00bb\7h\2\2\u00bb\u00bc")
        buf.write("\7q\2\2\u00bc\u00bd\7t\2\2\u00bd\22\3\2\2\2\u00be\u00bf")
        buf.write("\7v\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7w\2\2\u00c1\u00c2")
        buf.write("\7g\2\2\u00c2\24\3\2\2\2\u00c3\u00c4\7h\2\2\u00c4\u00c5")
        buf.write("\7c\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8\26\3\2\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb")
        buf.write("\7p\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce")
        buf.write("\7i\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7t\2\2\u00d0\30")
        buf.write("\3\2\2\2\u00d1\u00d2\7h\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4")
        buf.write("\7q\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6\7v\2\2\u00d6\32")
        buf.write("\3\2\2\2\u00d7\u00d8\7d\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da")
        buf.write("\7q\2\2\u00da\u00db\7n\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd")
        buf.write("\7c\2\2\u00dd\u00de\7p\2\2\u00de\34\3\2\2\2\u00df\u00e0")
        buf.write("\7u\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3")
        buf.write("\7k\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7i\2\2\u00e5\36")
        buf.write("\3\2\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9")
        buf.write("\7v\2\2\u00e9\u00ea\7w\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec \3\2\2\2\u00ed\u00ee\7x\2\2\u00ee\u00ef")
        buf.write("\7q\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7f\2\2\u00f1\"")
        buf.write("\3\2\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5")
        buf.write("\7v\2\2\u00f5$\3\2\2\2\u00f6\u00f7\7h\2\2\u00f7\u00f8")
        buf.write("\7w\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7e\2\2\u00fa\u00fb")
        buf.write("\7v\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe")
        buf.write("\7p\2\2\u00fe&\3\2\2\2\u00ff\u0100\7q\2\2\u0100\u0101")
        buf.write("\7h\2\2\u0101(\3\2\2\2\u0102\u0103\7c\2\2\u0103\u0104")
        buf.write("\7t\2\2\u0104\u0105\7t\2\2\u0105\u0106\7c\2\2\u0106\u0107")
        buf.write("\7{\2\2\u0107*\3\2\2\2\u0108\u0109\7k\2\2\u0109\u010a")
        buf.write("\7h\2\2\u010a,\3\2\2\2\u010b\u010c\7g\2\2\u010c\u010d")
        buf.write("\7n\2\2\u010d\u010e\7u\2\2\u010e\u010f\7g\2\2\u010f.\3")
        buf.write("\2\2\2\u0110\u0111\7y\2\2\u0111\u0112\7j\2\2\u0112\u0113")
        buf.write("\7k\2\2\u0113\u0114\7n\2\2\u0114\u0115\7g\2\2\u0115\60")
        buf.write("\3\2\2\2\u0116\u0117\7k\2\2\u0117\u0118\7p\2\2\u0118\u0119")
        buf.write("\7j\2\2\u0119\u011a\7g\2\2\u011a\u011b\7t\2\2\u011b\u011c")
        buf.write("\7k\2\2\u011c\u011d\7v\2\2\u011d\62\3\2\2\2\u011e\u011f")
        buf.write("\7-\2\2\u011f\64\3\2\2\2\u0120\u0121\7#\2\2\u0121\66\3")
        buf.write("\2\2\2\u0122\u0123\7#\2\2\u0123\u0124\7?\2\2\u01248\3")
        buf.write("\2\2\2\u0125\u0126\7/\2\2\u0126:\3\2\2\2\u0127\u0128\7")
        buf.write(",\2\2\u0128<\3\2\2\2\u0129\u012a\7(\2\2\u012a\u012b\7")
        buf.write("(\2\2\u012b>\3\2\2\2\u012c\u012d\7>\2\2\u012d@\3\2\2\2")
        buf.write("\u012e\u012f\7~\2\2\u012f\u0130\7~\2\2\u0130B\3\2\2\2")
        buf.write("\u0131\u0132\7>\2\2\u0132\u0133\7?\2\2\u0133D\3\2\2\2")
        buf.write("\u0134\u0135\7\61\2\2\u0135F\3\2\2\2\u0136\u0137\7?\2")
        buf.write("\2\u0137\u0138\7?\2\2\u0138H\3\2\2\2\u0139\u013a\7@\2")
        buf.write("\2\u013aJ\3\2\2\2\u013b\u013c\7\'\2\2\u013cL\3\2\2\2\u013d")
        buf.write("\u013e\7@\2\2\u013e\u013f\7?\2\2\u013fN\3\2\2\2\u0140")
        buf.write("\u0141\7<\2\2\u0141\u0142\7<\2\2\u0142P\3\2\2\2\u0143")
        buf.write("\u0144\7\60\2\2\u0144R\3\2\2\2\u0145\u0146\7<\2\2\u0146")
        buf.write("T\3\2\2\2\u0147\u0148\7.\2\2\u0148V\3\2\2\2\u0149\u014a")
        buf.write("\7=\2\2\u014aX\3\2\2\2\u014b\u014c\7*\2\2\u014cZ\3\2\2")
        buf.write("\2\u014d\u014e\7+\2\2\u014e\\\3\2\2\2\u014f\u0150\7]\2")
        buf.write("\2\u0150^\3\2\2\2\u0151\u0152\7_\2\2\u0152`\3\2\2\2\u0153")
        buf.write("\u0154\7}\2\2\u0154b\3\2\2\2\u0155\u0156\7\177\2\2\u0156")
        buf.write("d\3\2\2\2\u0157\u0158\7?\2\2\u0158f\3\2\2\2\u0159\u015d")
        buf.write("\t\4\2\2\u015a\u015c\t\5\2\2\u015b\u015a\3\2\2\2\u015c")
        buf.write("\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2")
        buf.write("\u015eh\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u016d\t\6\2")
        buf.write("\2\u0161\u0168\t\7\2\2\u0162\u0164\t\b\2\2\u0163\u0162")
        buf.write("\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\3\2\2\2\u0165")
        buf.write("\u0167\t\t\2\2\u0166\u0163\3\2\2\2\u0167\u016a\3\2\2\2")
        buf.write("\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016b\3")
        buf.write("\2\2\2\u016a\u0168\3\2\2\2\u016b\u016d\b\65\3\2\u016c")
        buf.write("\u0160\3\2\2\2\u016c\u0161\3\2\2\2\u016dj\3\2\2\2\u016e")
        buf.write("\u0170\5q9\2\u016f\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0174\3\2\2\2")
        buf.write("\u0173\u0175\5m\67\2\u0174\u0173\3\2\2\2\u0174\u0175\3")
        buf.write("\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\5o8\2\u0177\u0183")
        buf.write("\3\2\2\2\u0178\u017a\5q9\2\u0179\u0178\3\2\2\2\u017a\u017b")
        buf.write("\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\u017d\3\2\2\2\u017d\u017e\5m\67\2\u017e\u0183\3\2\2\2")
        buf.write("\u017f\u0180\5m\67\2\u0180\u0181\5o8\2\u0181\u0183\3\2")
        buf.write("\2\2\u0182\u016f\3\2\2\2\u0182\u0179\3\2\2\2\u0182\u017f")
        buf.write("\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185\b\66\4\2\u0185")
        buf.write("l\3\2\2\2\u0186\u018a\5Q)\2\u0187\u0189\5s:\2\u0188\u0187")
        buf.write("\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018bn\3\2\2\2\u018c\u018a\3\2\2\2\u018d")
        buf.write("\u018f\t\n\2\2\u018e\u0190\t\13\2\2\u018f\u018e\3\2\2")
        buf.write("\2\u018f\u0190\3\2\2\2\u0190\u0192\3\2\2\2\u0191\u0193")
        buf.write("\5s:\2\u0192\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0194\u0195\3\2\2\2\u0195p\3\2\2\2\u0196\u01a3")
        buf.write("\t\6\2\2\u0197\u0199\t\7\2\2\u0198\u0197\3\2\2\2\u0199")
        buf.write("\u019a\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2")
        buf.write("\u019b\u019f\3\2\2\2\u019c\u019e\t\f\2\2\u019d\u019c\3")
        buf.write("\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0")
        buf.write("\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2")
        buf.write("\u0196\3\2\2\2\u01a2\u0198\3\2\2\2\u01a3r\3\2\2\2\u01a4")
        buf.write("\u01a5\t\t\2\2\u01a5t\3\2\2\2\u01a6\u01ab\n\r\2\2\u01a7")
        buf.write("\u01ab\5w<\2\u01a8\u01a9\7^\2\2\u01a9\u01ab\7$\2\2\u01aa")
        buf.write("\u01a6\3\2\2\2\u01aa\u01a7\3\2\2\2\u01aa\u01a8\3\2\2\2")
        buf.write("\u01abv\3\2\2\2\u01ac\u01ad\7^\2\2\u01ad\u01ae\t\16\2")
        buf.write("\2\u01aex\3\2\2\2\u01af\u01b3\7$\2\2\u01b0\u01b2\5u;\2")
        buf.write("\u01b1\u01b0\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1\3")
        buf.write("\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01b3")
        buf.write("\3\2\2\2\u01b6\u01b7\7$\2\2\u01b7\u01b8\b=\5\2\u01b8z")
        buf.write("\3\2\2\2\u01b9\u01ba\7^\2\2\u01ba\u01bd\n\16\2\2\u01bb")
        buf.write("\u01bd\n\17\2\2\u01bc\u01b9\3\2\2\2\u01bc\u01bb\3\2\2")
        buf.write("\2\u01bd|\3\2\2\2\u01be\u01c3\t\20\2\2\u01bf\u01c2\n\21")
        buf.write("\2\2\u01c0\u01c2\5w<\2\u01c1\u01bf\3\2\2\2\u01c1\u01c0")
        buf.write("\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3")
        buf.write("\u01c4\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2")
        buf.write("\u01c6\u01c8\7\2\2\3\u01c7\u01c6\3\2\2\2\u01c7\u01c8\3")
        buf.write("\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\b?\6\2\u01ca~\3")
        buf.write("\2\2\2\u01cb\u01d0\t\20\2\2\u01cc\u01cf\n\21\2\2\u01cd")
        buf.write("\u01cf\5w<\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cf")
        buf.write("\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2")
        buf.write("\u01d1\u01d3\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d4\7")
        buf.write("^\2\2\u01d4\u01d5\n\22\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7")
        buf.write("\b@\7\2\u01d7\u0080\3\2\2\2\u01d8\u01d9\13\2\2\2\u01d9")
        buf.write("\u01da\bA\b\2\u01da\u0082\3\2\2\2\34\2\u0086\u0090\u009b")
        buf.write("\u015d\u0163\u0168\u016c\u0171\u0174\u017b\u0182\u018a")
        buf.write("\u018f\u0194\u019a\u019f\u01a2\u01aa\u01b3\u01bc\u01c1")
        buf.write("\u01c3\u01c7\u01ce\u01d0\t\b\2\2\3\65\2\3\66\3\3=\4\3")
        buf.write("?\5\3@\6\3A\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    LINE_CMT = 2
    BLOCK_CMT = 3
    AUTO = 4
    BREAK = 5
    DO = 6
    CONTINUE = 7
    FOR = 8
    TRUE = 9
    FALSE = 10
    INTEGER = 11
    FLOAT = 12
    BOOLEAN = 13
    STRING = 14
    RETURN = 15
    VOID = 16
    OUT = 17
    FUNCTION = 18
    OF = 19
    ARRAY = 20
    IF = 21
    ELSE = 22
    WHILE = 23
    INHERIT = 24
    PLUS = 25
    NOT = 26
    DIF = 27
    MINUS = 28
    MUL = 29
    AND = 30
    SMALLER = 31
    OR = 32
    SMALLER_EQAL = 33
    DIV = 34
    EQ = 35
    GREATER = 36
    MOD = 37
    GREATER_EQAL = 38
    STRCONCAT = 39
    DOT = 40
    COLON = 41
    COMMA = 42
    SEMICO = 43
    OPENCC = 44
    CLOSECC = 45
    OPENSQ = 46
    CLOSESQ = 47
    OPENBR = 48
    CLOSEBR = 49
    ASSIGN = 50
    ID = 51
    INTLIT = 52
    FLOATLIT = 53
    STRINGLIT = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'do'", "'continue'", "'for'", "'true'", 
            "'false'", "'integer'", "'float'", "'boolean'", "'string'", 
            "'return'", "'void'", "'out'", "'function'", "'of'", "'array'", 
            "'if'", "'else'", "'while'", "'inherit'", "'+'", "'!'", "'!='", 
            "'-'", "'*'", "'&&'", "'<'", "'||'", "'<='", "'/'", "'=='", 
            "'>'", "'%'", "'>='", "'::'", "'.'", "':'", "','", "';'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "WS", "LINE_CMT", "BLOCK_CMT", "AUTO", "BREAK", "DO", "CONTINUE", 
            "FOR", "TRUE", "FALSE", "INTEGER", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "VOID", "OUT", "FUNCTION", "OF", "ARRAY", "IF", "ELSE", 
            "WHILE", "INHERIT", "PLUS", "NOT", "DIF", "MINUS", "MUL", "AND", 
            "SMALLER", "OR", "SMALLER_EQAL", "DIV", "EQ", "GREATER", "MOD", 
            "GREATER_EQAL", "STRCONCAT", "DOT", "COLON", "COMMA", "SEMICO", 
            "OPENCC", "CLOSECC", "OPENSQ", "CLOSESQ", "OPENBR", "CLOSEBR", 
            "ASSIGN", "ID", "INTLIT", "FLOATLIT", "STRINGLIT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "WS", "LINE_CMT", "BLOCK_CMT", "AUTO", "BREAK", "DO", 
                  "CONTINUE", "FOR", "TRUE", "FALSE", "INTEGER", "FLOAT", 
                  "BOOLEAN", "STRING", "RETURN", "VOID", "OUT", "FUNCTION", 
                  "OF", "ARRAY", "IF", "ELSE", "WHILE", "INHERIT", "PLUS", 
                  "NOT", "DIF", "MINUS", "MUL", "AND", "SMALLER", "OR", 
                  "SMALLER_EQAL", "DIV", "EQ", "GREATER", "MOD", "GREATER_EQAL", 
                  "STRCONCAT", "DOT", "COLON", "COMMA", "SEMICO", "OPENCC", 
                  "CLOSECC", "OPENSQ", "CLOSESQ", "OPENBR", "CLOSEBR", "ASSIGN", 
                  "ID", "INTLIT", "FLOATLIT", "DOTPART", "EXPPART", "INTPART", 
                  "DIGIT", "StringCharacter", "EscapeSequence", "STRINGLIT", 
                  "ESC_ILLEGAL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[51] = self.INTLIT_action 
            actions[52] = self.FLOATLIT_action 
            actions[59] = self.STRINGLIT_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_', '')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    self.text = (self.text)[1:-1]
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                y = str(self.text)
                raise UncloseString(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                y = str(self.text)
                raise IllegalEscape(y[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                raise ErrorToken(self.text)

     


