# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01cb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&")
        buf.write("\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/")
        buf.write("\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\7\64\u0146\n\64\f\64\16\64\u0149\13\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\7\65\u0151\n\65\f\65\16\65\u0154")
        buf.write("\13\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\6\66\u015d\n")
        buf.write("\66\r\66\16\66\u015e\3\67\3\67\7\67\u0163\n\67\f\67\16")
        buf.write("\67\u0166\13\67\38\68\u0169\n8\r8\168\u016a\39\39\79\u016f")
        buf.write("\n9\f9\169\u0172\139\3:\3:\5:\u0176\n:\3:\6:\u0179\n:")
        buf.write("\r:\16:\u017a\3;\6;\u017e\n;\r;\16;\u017f\3;\5;\u0183")
        buf.write("\n;\3;\3;\3;\6;\u0188\n;\r;\16;\u0189\3;\3;\5;\u018e\n")
        buf.write(";\5;\u0190\n;\3<\3<\3<\3<\3<\5<\u0197\n<\3=\3=\3=\3>\3")
        buf.write(">\7>\u019e\n>\f>\16>\u01a1\13>\3>\3>\3>\3?\3?\3@\6@\u01a9")
        buf.write("\n@\r@\16@\u01aa\3@\3@\3A\3A\3A\5A\u01b2\nA\3B\3B\3C\3")
        buf.write("C\7C\u01b8\nC\fC\16C\u01bb\13C\3C\5C\u01be\nC\3C\3C\3")
        buf.write("D\3D\7D\u01c4\nD\fD\16D\u01c7\13D\3D\3D\3D\3\u0152\2E")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q\2s")
        buf.write("\2u:w\2y\2{;}\2\177<\u0081\2\u0083=\u0085>\u0087?\3\2")
        buf.write("\r\4\2\f\f\17\17\6\2\62;C\\aac|\5\2C\\aac|\4\2GGgg\4\2")
        buf.write("--//\7\2\f\f\17\17$$))^^\t\2))^^ddhhppttvv\3\2\62;\5\2")
        buf.write("\13\f\17\17\"\"\3\2^^\7\3\n\f\16\17$$))^^\2\u01d8\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2u")
        buf.write("\3\2\2\2\2{\3\2\2\2\2\177\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\3\u0089\3\2\2\2\5\u008f\3\2\2")
        buf.write("\2\7\u0098\3\2\2\2\t\u009b\3\2\2\2\13\u00a0\3\2\2\2\r")
        buf.write("\u00a4\3\2\2\2\17\u00a9\3\2\2\2\21\u00af\3\2\2\2\23\u00b3")
        buf.write("\3\2\2\2\25\u00b9\3\2\2\2\27\u00be\3\2\2\2\31\u00c5\3")
        buf.write("\2\2\2\33\u00cc\3\2\2\2\35\u00d1\3\2\2\2\37\u00d7\3\2")
        buf.write("\2\2!\u00e3\3\2\2\2#\u00e7\3\2\2\2%\u00ec\3\2\2\2\'\u00f0")
        buf.write("\3\2\2\2)\u00f5\3\2\2\2+\u00fb\3\2\2\2-\u0100\3\2\2\2")
        buf.write("/\u0102\3\2\2\2\61\u0104\3\2\2\2\63\u0106\3\2\2\2\65\u0108")
        buf.write("\3\2\2\2\67\u010a\3\2\2\29\u010c\3\2\2\2;\u010f\3\2\2")
        buf.write("\2=\u0112\3\2\2\2?\u0115\3\2\2\2A\u0117\3\2\2\2C\u011a")
        buf.write("\3\2\2\2E\u011c\3\2\2\2G\u011f\3\2\2\2I\u0121\3\2\2\2")
        buf.write("K\u0124\3\2\2\2M\u0127\3\2\2\2O\u0129\3\2\2\2Q\u012b\3")
        buf.write("\2\2\2S\u012d\3\2\2\2U\u012f\3\2\2\2W\u0131\3\2\2\2Y\u0133")
        buf.write("\3\2\2\2[\u0135\3\2\2\2]\u0137\3\2\2\2_\u0139\3\2\2\2")
        buf.write("a\u013b\3\2\2\2c\u013d\3\2\2\2e\u013f\3\2\2\2g\u0141\3")
        buf.write("\2\2\2i\u014c\3\2\2\2k\u015a\3\2\2\2m\u0160\3\2\2\2o\u0168")
        buf.write("\3\2\2\2q\u016c\3\2\2\2s\u0173\3\2\2\2u\u018f\3\2\2\2")
        buf.write("w\u0196\3\2\2\2y\u0198\3\2\2\2{\u019b\3\2\2\2}\u01a5\3")
        buf.write("\2\2\2\177\u01a8\3\2\2\2\u0081\u01b1\3\2\2\2\u0083\u01b3")
        buf.write("\3\2\2\2\u0085\u01b5\3\2\2\2\u0087\u01c1\3\2\2\2\u0089")
        buf.write("\u008a\7d\2\2\u008a\u008b\7t\2\2\u008b\u008c\7g\2\2\u008c")
        buf.write("\u008d\7c\2\2\u008d\u008e\7m\2\2\u008e\4\3\2\2\2\u008f")
        buf.write("\u0090\7e\2\2\u0090\u0091\7q\2\2\u0091\u0092\7p\2\2\u0092")
        buf.write("\u0093\7v\2\2\u0093\u0094\7k\2\2\u0094\u0095\7p\2\2\u0095")
        buf.write("\u0096\7w\2\2\u0096\u0097\7g\2\2\u0097\6\3\2\2\2\u0098")
        buf.write("\u0099\7k\2\2\u0099\u009a\7h\2\2\u009a\b\3\2\2\2\u009b")
        buf.write("\u009c\7g\2\2\u009c\u009d\7n\2\2\u009d\u009e\7u\2\2\u009e")
        buf.write("\u009f\7g\2\2\u009f\n\3\2\2\2\u00a0\u00a1\7h\2\2\u00a1")
        buf.write("\u00a2\7q\2\2\u00a2\u00a3\7t\2\2\u00a3\f\3\2\2\2\u00a4")
        buf.write("\u00a5\7v\2\2\u00a5\u00a6\7t\2\2\u00a6\u00a7\7w\2\2\u00a7")
        buf.write("\u00a8\7g\2\2\u00a8\16\3\2\2\2\u00a9\u00aa\7h\2\2\u00aa")
        buf.write("\u00ab\7c\2\2\u00ab\u00ac\7n\2\2\u00ac\u00ad\7u\2\2\u00ad")
        buf.write("\u00ae\7g\2\2\u00ae\20\3\2\2\2\u00af\u00b0\7k\2\2\u00b0")
        buf.write("\u00b1\7p\2\2\u00b1\u00b2\7v\2\2\u00b2\22\3\2\2\2\u00b3")
        buf.write("\u00b4\7h\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6\7q\2\2\u00b6")
        buf.write("\u00b7\7c\2\2\u00b7\u00b8\7v\2\2\u00b8\24\3\2\2\2\u00b9")
        buf.write("\u00ba\7d\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc\7q\2\2\u00bc")
        buf.write("\u00bd\7n\2\2\u00bd\26\3\2\2\2\u00be\u00bf\7u\2\2\u00bf")
        buf.write("\u00c0\7v\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2\7k\2\2\u00c2")
        buf.write("\u00c3\7p\2\2\u00c3\u00c4\7i\2\2\u00c4\30\3\2\2\2\u00c5")
        buf.write("\u00c6\7t\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7v\2\2\u00c8")
        buf.write("\u00c9\7w\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7p\2\2\u00cb")
        buf.write("\32\3\2\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7w\2\2\u00ce")
        buf.write("\u00cf\7n\2\2\u00cf\u00d0\7n\2\2\u00d0\34\3\2\2\2\u00d1")
        buf.write("\u00d2\7e\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4\7c\2\2\u00d4")
        buf.write("\u00d5\7u\2\2\u00d5\u00d6\7u\2\2\u00d6\36\3\2\2\2\u00d7")
        buf.write("\u00d8\7e\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7p\2\2\u00da")
        buf.write("\u00db\7u\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7t\2\2\u00dd")
        buf.write("\u00de\7w\2\2\u00de\u00df\7e\2\2\u00df\u00e0\7v\2\2\u00e0")
        buf.write("\u00e1\7q\2\2\u00e1\u00e2\7t\2\2\u00e2 \3\2\2\2\u00e3")
        buf.write("\u00e4\7x\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7t\2\2\u00e6")
        buf.write("\"\3\2\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9\7g\2\2\u00e9")
        buf.write("\u00ea\7n\2\2\u00ea\u00eb\7h\2\2\u00eb$\3\2\2\2\u00ec")
        buf.write("\u00ed\7p\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7y\2\2\u00ef")
        buf.write("&\3\2\2\2\u00f0\u00f1\7x\2\2\u00f1\u00f2\7q\2\2\u00f2")
        buf.write("\u00f3\7k\2\2\u00f3\u00f4\7f\2\2\u00f4(\3\2\2\2\u00f5")
        buf.write("\u00f6\7e\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7p\2\2\u00f8")
        buf.write("\u00f9\7u\2\2\u00f9\u00fa\7v\2\2\u00fa*\3\2\2\2\u00fb")
        buf.write("\u00fc\7h\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe\7p\2\2\u00fe")
        buf.write("\u00ff\7e\2\2\u00ff,\3\2\2\2\u0100\u0101\7-\2\2\u0101")
        buf.write(".\3\2\2\2\u0102\u0103\7/\2\2\u0103\60\3\2\2\2\u0104\u0105")
        buf.write("\7,\2\2\u0105\62\3\2\2\2\u0106\u0107\7\61\2\2\u0107\64")
        buf.write("\3\2\2\2\u0108\u0109\7^\2\2\u0109\66\3\2\2\2\u010a\u010b")
        buf.write("\7#\2\2\u010b8\3\2\2\2\u010c\u010d\7(\2\2\u010d\u010e")
        buf.write("\7(\2\2\u010e:\3\2\2\2\u010f\u0110\7~\2\2\u0110\u0111")
        buf.write("\7~\2\2\u0111<\3\2\2\2\u0112\u0113\7?\2\2\u0113\u0114")
        buf.write("\7?\2\2\u0114>\3\2\2\2\u0115\u0116\7?\2\2\u0116@\3\2\2")
        buf.write("\2\u0117\u0118\7#\2\2\u0118\u0119\7?\2\2\u0119B\3\2\2")
        buf.write("\2\u011a\u011b\7>\2\2\u011bD\3\2\2\2\u011c\u011d\7>\2")
        buf.write("\2\u011d\u011e\7?\2\2\u011eF\3\2\2\2\u011f\u0120\7@\2")
        buf.write("\2\u0120H\3\2\2\2\u0121\u0122\7@\2\2\u0122\u0123\7?\2")
        buf.write("\2\u0123J\3\2\2\2\u0124\u0125\7<\2\2\u0125\u0126\7?\2")
        buf.write("\2\u0126L\3\2\2\2\u0127\u0128\7`\2\2\u0128N\3\2\2\2\u0129")
        buf.write("\u012a\5%\23\2\u012aP\3\2\2\2\u012b\u012c\7\'\2\2\u012c")
        buf.write("R\3\2\2\2\u012d\u012e\7\60\2\2\u012eT\3\2\2\2\u012f\u0130")
        buf.write("\7.\2\2\u0130V\3\2\2\2\u0131\u0132\7=\2\2\u0132X\3\2\2")
        buf.write("\2\u0133\u0134\7<\2\2\u0134Z\3\2\2\2\u0135\u0136\7*\2")
        buf.write("\2\u0136\\\3\2\2\2\u0137\u0138\7+\2\2\u0138^\3\2\2\2\u0139")
        buf.write("\u013a\7]\2\2\u013a`\3\2\2\2\u013b\u013c\7_\2\2\u013c")
        buf.write("b\3\2\2\2\u013d\u013e\7}\2\2\u013ed\3\2\2\2\u013f\u0140")
        buf.write("\7\177\2\2\u0140f\3\2\2\2\u0141\u0142\7\61\2\2\u0142\u0143")
        buf.write("\7\61\2\2\u0143\u0147\3\2\2\2\u0144\u0146\n\2\2\2\u0145")
        buf.write("\u0144\3\2\2\2\u0146\u0149\3\2\2\2\u0147\u0145\3\2\2\2")
        buf.write("\u0147\u0148\3\2\2\2\u0148\u014a\3\2\2\2\u0149\u0147\3")
        buf.write("\2\2\2\u014a\u014b\b\64\2\2\u014bh\3\2\2\2\u014c\u014d")
        buf.write("\7\61\2\2\u014d\u014e\7,\2\2\u014e\u0152\3\2\2\2\u014f")
        buf.write("\u0151\13\2\2\2\u0150\u014f\3\2\2\2\u0151\u0154\3\2\2")
        buf.write("\2\u0152\u0153\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0155")
        buf.write("\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u0156\7,\2\2\u0156")
        buf.write("\u0157\7\61\2\2\u0157\u0158\3\2\2\2\u0158\u0159\b\65\2")
        buf.write("\2\u0159j\3\2\2\2\u015a\u015c\7B\2\2\u015b\u015d\t\3\2")
        buf.write("\2\u015c\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015c")
        buf.write("\3\2\2\2\u015e\u015f\3\2\2\2\u015fl\3\2\2\2\u0160\u0164")
        buf.write("\t\4\2\2\u0161\u0163\t\3\2\2\u0162\u0161\3\2\2\2\u0163")
        buf.write("\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2")
        buf.write("\u0165n\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0169\5}?\2")
        buf.write("\u0168\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0168\3")
        buf.write("\2\2\2\u016a\u016b\3\2\2\2\u016bp\3\2\2\2\u016c\u0170")
        buf.write("\5S*\2\u016d\u016f\5}?\2\u016e\u016d\3\2\2\2\u016f\u0172")
        buf.write("\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171")
        buf.write("r\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0175\t\5\2\2\u0174")
        buf.write("\u0176\t\6\2\2\u0175\u0174\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0178\3\2\2\2\u0177\u0179\5}?\2\u0178\u0177\3\2")
        buf.write("\2\2\u0179\u017a\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b")
        buf.write("\3\2\2\2\u017bt\3\2\2\2\u017c\u017e\5}?\2\u017d\u017c")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u017d\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u0183\5q9\2\u0182")
        buf.write("\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\u0185\5s:\2\u0185\u0190\3\2\2\2\u0186\u0188\5}")
        buf.write("?\2\u0187\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u0187")
        buf.write("\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\u018d\5q9\2\u018c\u018e\5s:\2\u018d\u018c\3\2\2\2\u018d")
        buf.write("\u018e\3\2\2\2\u018e\u0190\3\2\2\2\u018f\u017d\3\2\2\2")
        buf.write("\u018f\u0187\3\2\2\2\u0190v\3\2\2\2\u0191\u0197\n\7\2")
        buf.write("\2\u0192\u0197\5y=\2\u0193\u0194\7)\2\2\u0194\u0195\7")
        buf.write("$\2\2\u0195\u0197\7$\2\2\u0196\u0191\3\2\2\2\u0196\u0192")
        buf.write("\3\2\2\2\u0196\u0193\3\2\2\2\u0197x\3\2\2\2\u0198\u0199")
        buf.write("\7^\2\2\u0199\u019a\t\b\2\2\u019az\3\2\2\2\u019b\u019f")
        buf.write("\7$\2\2\u019c\u019e\5w<\2\u019d\u019c\3\2\2\2\u019e\u01a1")
        buf.write("\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write("\u01a2\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a3\7$\2\2")
        buf.write("\u01a3\u01a4\b>\3\2\u01a4|\3\2\2\2\u01a5\u01a6\t\t\2\2")
        buf.write("\u01a6~\3\2\2\2\u01a7\u01a9\t\n\2\2\u01a8\u01a7\3\2\2")
        buf.write("\2\u01a9\u01aa\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad\b@\2\2\u01ad")
        buf.write("\u0080\3\2\2\2\u01ae\u01af\7^\2\2\u01af\u01b2\n\b\2\2")
        buf.write("\u01b0\u01b2\n\13\2\2\u01b1\u01ae\3\2\2\2\u01b1\u01b0")
        buf.write("\3\2\2\2\u01b2\u0082\3\2\2\2\u01b3\u01b4\13\2\2\2\u01b4")
        buf.write("\u0084\3\2\2\2\u01b5\u01b9\7$\2\2\u01b6\u01b8\5w<\2\u01b7")
        buf.write("\u01b6\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2")
        buf.write("\u01b9\u01ba\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3")
        buf.write("\2\2\2\u01bc\u01be\t\f\2\2\u01bd\u01bc\3\2\2\2\u01be\u01bf")
        buf.write("\3\2\2\2\u01bf\u01c0\bC\4\2\u01c0\u0086\3\2\2\2\u01c1")
        buf.write("\u01c5\7$\2\2\u01c2\u01c4\5w<\2\u01c3\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c8\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01c9\5")
        buf.write("\u0081A\2\u01c9\u01ca\bD\5\2\u01ca\u0088\3\2\2\2\27\2")
        buf.write("\u0147\u0152\u015e\u0164\u016a\u0170\u0175\u017a\u017f")
        buf.write("\u0182\u0189\u018d\u018f\u0196\u019f\u01aa\u01b1\u01b9")
        buf.write("\u01bd\u01c5\6\b\2\2\3>\2\3C\3\3D\4")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    IF = 3
    ELSE = 4
    FOR = 5
    TRUE = 6
    FALSE = 7
    INT = 8
    FLOAT = 9
    BOOL = 10
    STRING = 11
    RETURN = 12
    NULL = 13
    CLASS = 14
    CONSTRUCTOR = 15
    VAR = 16
    SELF = 17
    NEW = 18
    VOID = 19
    CONST = 20
    FUNC = 21
    PLUS = 22
    MINUS = 23
    MUL = 24
    DIV = 25
    BSLASH = 26
    NOT = 27
    AND = 28
    OR = 29
    EQUAL = 30
    EQ = 31
    DIF = 32
    LESS = 33
    LESS_EQUAL = 34
    GREATER = 35
    GREATER_EQUAL = 36
    ASSIGN = 37
    CONCAT = 38
    NEWOP = 39
    MOD = 40
    DOT = 41
    COMMA = 42
    SEMICO = 43
    COLON = 44
    OPENCC = 45
    CLOSECC = 46
    OPENSQ = 47
    CLOSESQ = 48
    OPENBR = 49
    CLOSEBR = 50
    LINE_CMT = 51
    BLOCK_CMT = 52
    At = 53
    ID = 54
    INTLIT = 55
    FLOATLIT = 56
    STRINGLIT = 57
    WS = 58
    ERROR_CHAR = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'break'", "'continue'", "'if'", "'else'", "'for'", "'true'", 
            "'false'", "'int'", "'float'", "'bool'", "'string'", "'return'", 
            "'null'", "'class'", "'constructor'", "'var'", "'self'", "'new'", 
            "'void'", "'const'", "'func'", "'+'", "'-'", "'*'", "'/'", "'\\'", 
            "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "':='", "'^'", "'%'", "'.'", "','", "';'", "':'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", 
            "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
            "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "PLUS", "MINUS", 
            "MUL", "DIV", "BSLASH", "NOT", "AND", "OR", "EQUAL", "EQ", "DIF", 
            "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", "ASSIGN", 
            "CONCAT", "NEWOP", "MOD", "DOT", "COMMA", "SEMICO", "COLON", 
            "OPENCC", "CLOSECC", "OPENSQ", "CLOSESQ", "OPENBR", "CLOSEBR", 
            "LINE_CMT", "BLOCK_CMT", "At", "ID", "INTLIT", "FLOATLIT", "STRINGLIT", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
                  "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
                  "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", 
                  "FUNC", "PLUS", "MINUS", "MUL", "DIV", "BSLASH", "NOT", 
                  "AND", "OR", "EQUAL", "EQ", "DIF", "LESS", "LESS_EQUAL", 
                  "GREATER", "GREATER_EQUAL", "ASSIGN", "CONCAT", "NEWOP", 
                  "MOD", "DOT", "COMMA", "SEMICO", "COLON", "OPENCC", "CLOSECC", 
                  "OPENSQ", "CLOSESQ", "OPENBR", "CLOSEBR", "LINE_CMT", 
                  "BLOCK_CMT", "At", "ID", "INTLIT", "DOTPART", "EXPPART", 
                  "FLOATLIT", "StringCharacter", "EscapeSequence", "STRINGLIT", 
                  "DIGIT", "WS", "ESC_ILLEGAL", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "CSlang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[60] = self.STRINGLIT_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    self.text = (self.text)[1:-1]
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    self.text = (self.text)[1:]
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    self.text = (self.text)[1:]
                
     


