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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("%\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\2\3\2\3\3\3\3\3\3\3\3\7\3\26\n\3\f\3\16\3\31\13")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\2\2\6\2")
        buf.write("\4\6\b\2\3\3\2\t\n\2\"\2\13\3\2\2\2\4\21\3\2\2\2\6\34")
        buf.write("\3\2\2\2\b\"\3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2")
        buf.write("\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\17\3\2\2\2\17\20\7\2")
        buf.write("\2\3\20\3\3\2\2\2\21\22\7\3\2\2\22\23\7\13\2\2\23\27\7")
        buf.write("\4\2\2\24\26\5\6\4\2\25\24\3\2\2\2\26\31\3\2\2\2\27\25")
        buf.write("\3\2\2\2\27\30\3\2\2\2\30\32\3\2\2\2\31\27\3\2\2\2\32")
        buf.write("\33\7\5\2\2\33\5\3\2\2\2\34\35\7\6\2\2\35\36\7\13\2\2")
        buf.write("\36\37\7\7\2\2\37 \5\b\5\2 !\7\b\2\2!\7\3\2\2\2\"#\t\2")
        buf.write("\2\2#\t\3\2\2\2\4\r\27")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'{'", "'}'", "'var'", "':'", 
                     "';'", "'int'", "'void'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INTTYPE", 
                      "VOIDTYPE", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_memdecl = 2
    RULE_cslangtype = 3

    ruleNames =  [ "program", "classdecl", "memdecl", "cslangtype" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    INTTYPE=7
    VOIDTYPE=8
    ID=9
    WS=10
    ERROR_CHAR=11
    UNCLOSE_STRING=12
    ILLEGAL_ESCAPE=13

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

        def classdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ClassdeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ClassdeclContext,i)


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
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.classdecl()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSlangParser.T__0):
                    break

            self.state = 13
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def memdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.MemdeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.MemdeclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_classdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = CSlangParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(CSlangParser.T__0)
            self.state = 16
            self.match(CSlangParser.ID)
            self.state = 17
            self.match(CSlangParser.T__1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.T__3:
                self.state = 18
                self.memdecl()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(CSlangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def cslangtype(self):
            return self.getTypedRuleContext(CSlangParser.CslangtypeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_memdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemdecl" ):
                return visitor.visitMemdecl(self)
            else:
                return visitor.visitChildren(self)




    def memdecl(self):

        localctx = CSlangParser.MemdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(CSlangParser.T__3)
            self.state = 27
            self.match(CSlangParser.ID)
            self.state = 28
            self.match(CSlangParser.T__4)
            self.state = 29
            self.cslangtype()
            self.state = 30
            self.match(CSlangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CslangtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(CSlangParser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(CSlangParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_cslangtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCslangtype" ):
                return visitor.visitCslangtype(self)
            else:
                return visitor.visitChildren(self)




    def cslangtype(self):

        localctx = CSlangParser.CslangtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cslangtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not(_la==CSlangParser.INTTYPE or _la==CSlangParser.VOIDTYPE):
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





