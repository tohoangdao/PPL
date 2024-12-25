from typing import List
from StaticError import *
from Visitor import Visitor
from AST import *
from abc import ABC


class StmtType: pass
class DeclType: pass

class VarDeclType(DeclType): pass
class FuncDeclType(DeclType): pass
class InvalidType(Type): pass

class LoopStmtType(StmtType): pass
class MustInLoopStmtType(StmtType): pass
class AssignStmtType(StmtType): pass
class IfStmtType(StmtType): pass
class ReturnStmtType(StmtType): pass
class BlockStmtType(StmtType): pass
class CallStmtType(StmtType): pass

class Symbol:
    def __init__(self, name, typ: Type):
        self.name = name
        self.typ = typ

class VarSym(Symbol):
    def __init__(self, name : str, typ : Type):
        super().__init__(name, typ)

class ParaSym(Symbol):
    def __init__(self, name : str, typ : Type, out: bool = False, inherit: bool = False):
        super().__init__(name, typ)
        self.out = out
        self.inherit = inherit

class FuncSym(Symbol):
    def __init__(self, name : str, typ : Type, params: List[Symbol] = [],
                 inherit: str or None = None, parentparams: List[ParaSym] = [],):
        super().__init__(name, typ)
        self.params = params
        self.inherit = inherit
        self.parentparams = parentparams

class Properties:
    def __init__(self, inFunc = None, inLoop = 0, isSuper = False):
        self.inFunc = inFunc
        self.inLoop = inLoop
        self.isSuper = isSuper

class SymbolTable:
    def __init__(self, envs = [[]],
                 funcprototype : List[FuncSym] = [],
                 properties : Properties = Properties()):

        self.envs = [[]] if envs == [[]] else envs
        self.funcprototype = [] if funcprototype == [] else funcprototype
        self.systemFunc = [FuncSym("readInteger", IntegerType()),
                        FuncSym("printInteger", VoidType(), [ParaSym("System", IntegerType())]),
                        FuncSym("readFloat", FloatType()),
                        FuncSym("writeFloat", VoidType(), [ParaSym("System", FloatType())]),
                        FuncSym("readBoolean", BooleanType()),
                        FuncSym("printBoolean", VoidType(), [ParaSym("System", BooleanType())]),
                        FuncSym("readString", StringType()),
                        FuncSym("printString", VoidType(), [ParaSym("System", StringType())])]

        self.properties = properties

class Utility:
    def combineSym(sym : Symbol, st : SymbolTable):
        st.envs[0] = [sym] + st.envs[0]
        return SymbolTable(st.envs, st.funcprototype, st.properties)

    def findVar(name : str, st : SymbolTable):
        for scope in st.envs:
            for sym in scope:
                if sym.name == name: 
                    return sym
    
    def findFunc(name : str, st : SymbolTable):
        for sym in st.systemFunc + st.funcprototype:
            if sym.name == name: 
                return sym
    
    def find(name : str, st : SymbolTable):
        sym = None
        sym = Utility.findVar(name, st)
        if not sym:
            sym = Utility.findFunc(name, st)
        return sym

    def forceType(typ1 : Type, typ2 : Type):
        if type(typ1) is not type(typ2):
            if isinstance(typ1, FloatType) and isinstance(typ2, IntegerType):
                return True
            return False
        else:
            if isinstance(typ1, ArrayType) and isinstance(typ2, ArrayType): 
                if typ1.dimensions != typ2.dimensions: 
                    return False
                if not Utility.forceType(typ1.typ, typ2.typ):
                    return False
            return True
    def goInFunc(st : SymbolTable, info : FuncSym):
        return SymbolTable([[]]+st.envs, st.funcprototype, 
                           Properties(info, st.properties.inLoop, st.properties.isSuper))

    def goInLoop(st : SymbolTable):
        return SymbolTable([[]]+st.envs, st.funcprototype, 
                           Properties(st.properties.inFunc, st.properties.inLoop + 1, st.properties.isSuper))
    
    def goInBlock(st : SymbolTable):
        return SymbolTable([[]]+st.envs, st.funcprototype, st.properties)
    
    def goOutLoop(st : SymbolTable):
        return SymbolTable([[]]+st.envs, st.funcprototype, 
                           Properties(st.properties.inFunc, st.properties.inLoop - 1, st.properties.isSuper))

    def changeDecl(decl : Decl):
        if isinstance(decl, VarDecl): 
            return VarSym(decl.name, decl.typ)
        if isinstance(decl, ParamDecl): 
            return ParaSym(decl.name, decl.typ, decl.out, decl.inherit)
        if isinstance(decl, FuncDecl): 
            return FuncSym(decl.name, decl.return_type, list(map(lambda x: Utility.changeDecl(x), decl.params)), decl.inherit, [])
    
    def local(name : str, st : SymbolTable):
        results = filter(lambda sym: sym.name == name, st.envs[0])
        return next(results, None)
    
    def inference(name : str, typ : Type, st : SymbolTable):
        Utility.find(name, st).typ = typ
        return typ
     
class PreCheck(Visitor):
    def __init__(self, ast):
        self.ast = ast

    def visitProgram(self, ast: Program, st: SymbolTable):
        for decl in ast.decls:
            if isinstance(decl, FuncDecl): 
                st = self.visit(decl, st)
        return st

    def visitFuncDecl(self, ast : FuncDecl, st : SymbolTable):
        return SymbolTable(st.envs, st.funcprototype + [Utility.changeDecl(ast)], st.properties)

class StaticChecker(Visitor):

    def __init__(self, ast):
        self.ast = ast
 
    def check(self):
        return self.visit(self.ast, [])

    def visitIntegerLit(self, ast : IntegerLit, st): 
        return st, IntegerType()

    def visitFloatLit(self, ast : FloatLit, st): 
        return st, FloatType()

    def visitStringLit(self, ast : StringLit, st): 
        return st, StringType()

    def visitBooleanLit(self, ast : BooleanLit, st): 
        return st, BooleanType()

    def visitArrayLit(self, ast : ArrayLit, st : SymbolTable):
        typ = AutoType()
        for exp in ast.explist:
            st, exptyp = self.visit(exp, st)

            if isinstance(exptyp, InvalidType):
                return st, InvalidType()
            elif isinstance(typ, AutoType): 
                typ = exptyp
            elif isinstance(exptyp,  AutoType):
                exptyp = Utility.inference(exp.name, typ, st)
            elif type(exp) is not type(exptyp): 
                return st, InvalidType()

        if isinstance(typ, AutoType): 
            return st, InvalidType()

        for exp in ast.explist:
            st, exptype = self.visit(exp, st)
            if isinstance(exptype, AutoType):
                exptype.typ = typ

        if isinstance(typ, ArrayType):
            return st, ArrayType([len(ast.explist)] + typ.dimensions, typ.typ)
        return st, ArrayType([len(ast.explist)], typ)

    def visitId(self, ast : Id, st: SymbolTable):
        symbol = Utility.findVar(ast.name, st)
        if not symbol:
            raise Undeclared(Identifier(), ast.name)
        if not isinstance(symbol, (VarSym, ParaSym)): 
            raise TypeMismatchInExpression(ast) 
        return st, symbol.typ

    def visitArrayCell(self, ast : ArrayCell, st : SymbolTable):
        symbol = Utility.findVar(ast.name, st)
        if not symbol:
            raise Undeclared(Identifier(), ast.name)
        if not isinstance(symbol, (VarSym, ParaSym)) or not isinstance(symbol.typ, ArrayType): 
            raise TypeMismatchInExpression(ast)

        if len(ast.cell) > len(symbol.typ.dimensions):
            raise TypeMismatchInExpression(ast)

        for idx in ast.cell:
            st, idxtype = self.visit(idx, st)
            if isinstance(idxtype, AutoType):
                if isinstance(idx, FuncCall): 
                    Utility.findFunc(idx.name, st).typ = IntegerType()
                else:
                    Utility.findVar(idx.name, st).typ = IntegerType()
            elif not isinstance(idxtype, IntegerType):
                raise TypeMismatchInExpression(ast)

        nextdim = symbol.typ.dimensions[len(ast.cell):]
        if len(nextdim) == 0: 
            return st, symbol.typ.typ
        return st, ArrayType(nextdim, symbol.typ.typ)

    def visitBinExpr(self, ast : BinExpr, st : SymbolTable):
        st, rtype = self.visit(ast.right, st)
        st, ltype = self.visit(ast.left, st)

        if isinstance(rtype, AutoType) and isinstance(ltype, AutoType):
            Utility.inference(ast.right.name, IntegerType, st)
            Utility.inference(ast.left.name, IntegerType, st)
            ltype = IntegerType()
            rtype = IntegerType()

        if isinstance(rtype, AutoType):
            Utility.inference(ast.right.name, ltype, st)
            rtype = ltype

        if isinstance(ltype, AutoType):
            Utility.inference(ast.left.name, rtype, st)
            ltype = rtype

        if ast.op in ["+", "-", "*"]:
            if not isinstance(ltype, (IntegerType, FloatType)) or not isinstance(rtype, (IntegerType, FloatType)):
                raise TypeMismatchInExpression(ast)
            if FloatType in [type(ltype), type(rtype)]:
                return st, FloatType()
            return st, IntegerType()

        elif ast.op == "/":
            if not isinstance(ltype, (IntegerType, FloatType)) or not isinstance(rtype, (IntegerType, FloatType)):
                raise TypeMismatchInExpression(ast)
            return st, FloatType()

        elif ast.op == "%":
            if not isinstance(ltype, IntegerType) or not isinstance(rtype, IntegerType):
                raise TypeMismatchInExpression(ast)
            return st, IntegerType()

        elif ast.op in ["&&", "||"]:
            if not isinstance(ltype, BooleanType) or not isinstance(rtype, BooleanType):
                raise TypeMismatchInExpression(ast)
            return st, BooleanType()

        elif ast.op == "::":
            if not isinstance(ltype, StringType) or not isinstance(rtype, StringType):
                raise TypeMismatchInExpression(ast)
            return st, StringType()

        elif ast.op in ["==", "!="]:
            if type(rtype) is not type(ltype): 
                raise TypeMismatchInExpression(ast)
            if not isinstance(ltype, (IntegerType, BooleanType)):
                raise TypeMismatchInExpression(ast)
            return st, BooleanType()

        elif ast.op in ["<", ">", "<=", ">="]:
            if not isinstance(ltype, (IntegerType, FloatType)) or not isinstance(rtype, (IntegerType, FloatType)):
                raise TypeMismatchInExpression(ast)
            return st, BooleanType()

    def visitUnExpr(self, ast, st):
        st, type = self.visit(ast.val, st)
        if ast.op == "-":
            if isinstance(type, AutoType): 
                type = Utility.inference(ast.val.name, IntegerType(), st)
            elif not isinstance(type, (IntegerType, FloatType)):
                raise TypeMismatchInExpression(ast)
            return st, type

        elif ast.op == "!":
            if isinstance(type, AutoType): 
                type = Utility.inference(ast.val.name, BooleanType(), st)
            elif not isinstance(type, BooleanType):
                raise TypeMismatchInExpression(ast)
            return st, BooleanType()

    def visitFuncCall(self, ast: FuncCall, st: SymbolTable):
        symbol = Utility.findFunc(ast.name, st)
        if not symbol:
            raise Undeclared(Function(), ast.name)
        if isinstance(symbol.typ, VoidType):
            raise TypeMismatchInExpression(ast)

        if len(symbol.params) < len(ast.args): 
            raise TypeMismatchInExpression(ast)
        if len(symbol.params) > len(ast.args): 
            raise TypeMismatchInExpression(ast)

        for i in range(len(symbol.params)):
            if symbol.params[i].out and not isinstance(ast.args[i], (Id, ArrayCell)):
                raise TypeMismatchInExpression(ast)

        for i in range(len(symbol.params)):
            st, paramType = self.visit(ast.args[i], st)
            if isinstance(symbol.params[i].typ, AutoType): 
                symbol.params[i].typ = paramType

            elif isinstance(paramType, AutoType):
                Utility.inference(ast.args[i].name, symbol.params[i].typ, st)

            elif not Utility.forceType(symbol.params[i].typ, paramType): 
                raise TypeMismatchInExpression(ast)
        return st, symbol.typ

    def visitAssignStmt(self, ast : AssignStmt, st : SymbolTable):
        st, rtype = self.visit(ast.rhs, st)
        st, ltype = self.visit(ast.lhs, st)

        if isinstance(ltype, (VoidType, ArrayType)):
            raise TypeMismatchInStatement(ast)

        elif isinstance(ltype, AutoType):
            Utility.inference(ast.lhs.name, rtype, st)

        elif isinstance(rtype, AutoType):
            Utility.inference(ast.rhs.name, ltype, st)

        elif not Utility.forceType(ltype, rtype):
            raise TypeMismatchInStatement(ast)
        return st, AssignStmtType()

    def visitIfStmt(self, ast : IfStmt, st : SymbolTable):
        st, condType = self.visit(ast.cond, st)
        if isinstance(condType, AutoType):
            Utility.inference(ast.cond.name, BooleanType, st)
        if not isinstance(condType, BooleanType): 
            raise TypeMismatchInStatement(ast)

        newst = Utility.goInBlock(st)

        newst, _ = self.visit(ast.tstmt, newst)

        if ast.fstmt: newst, _ = self.visit(ast.fstmt, newst)

        return st, IfStmtType()

    def visitForStmt(self, ast : ForStmt, st : SymbolTable):
        st, _ = self.visit(ast.init, st)
        st, lhs = self.visit(ast.init.lhs, st)
        st, rhs = self.visit(ast.init.rhs, st)

        if not isinstance(rhs, IntegerType) or not isinstance(lhs, IntegerType):
            raise TypeMismatchInStatement(ast)

        st, condType = self.visit(ast.cond, st)
        if isinstance(condType, AutoType):
            Utility.inference(ast.cond.name, BooleanType, st)
        if not isinstance(condType, BooleanType): 
            raise TypeMismatchInStatement(ast)

        st, updType = self.visit(ast.upd, st)
        if not isinstance(updType, IntegerType):
            raise TypeMismatchInStatement(ast)

        st, _ = self.visit(ast.stmt, Utility.goInLoop(st))
        return Utility.goOutLoop(st), LoopStmtType()

    def visitWhileStmt(self, ast : WhileStmt, st : SymbolTable):
        st, condType = self.visit(ast.cond, st)
        if isinstance(condType, AutoType): 
            Utility.inference(ast.cond.name, BooleanType, st)

        if not isinstance(condType, BooleanType): 
            raise TypeMismatchInStatement(ast)
        
        st, _ = self.visit(ast.stmt, Utility.goInLoop(st))
        return Utility.goOutLoop(st), LoopStmtType()

    def visitDoWhileStmt(self, ast, st):
        st, condType = self.visit(ast.cond, st)
        if isinstance(condType, AutoType): 
            Utility.inference(ast.cond.name, BooleanType, st)

        if not isinstance(condType, BooleanType): 
            raise TypeMismatchInStatement(ast)
        
        st, _ = self.visit(ast.stmt, Utility.goInLoop(st))
        return Utility.goOutLoop(st), LoopStmtType()

    def visitBreakStmt(self, ast : BreakStmt, st : SymbolTable):
        if st.properties.inLoop == 0 or st.properties is None:
            raise MustInLoop(ast)
        return st, MustInLoopStmtType()

    def visitContinueStmt(self, ast : ContinueStmt, st : SymbolTable):
        if st.properties.inLoop == 0 or st.properties is None:
            raise MustInLoop(ast)
        return st, MustInLoopStmtType()

    def visitReturnStmt(self, ast : ReturnStmt, st : SymbolTable):
        if not st.properties.inFunc:
            InvalidStatementInFunction(ast)

        if ast.expr is not None:
            st, exprtyp =  self.visit(ast.expr, st)

            if isinstance(st.properties.inFunc.typ, AutoType): 
                st.properties.inFunc.typ = exprtyp
            elif not Utility.forceType(st.properties.inFunc.typ, exprtyp):
                raise TypeMismatchInStatement(ast) 
        else: 
            if isinstance(st.properties.inFunc.typ, AutoType): 
                st.properties.inFunc.typ = VoidType()
            elif not isinstance( st.properties.inFunc.typ,VoidType): 
                raise TypeMismatchInStatement(ast)

        return st, ReturnStmt()

    def visitCallStmt(self, ast : CallStmt, st : SymbolTable):

        symbol = Utility.findFunc(ast.name, st)
        if not symbol: 
            raise Undeclared(Function(), ast.name)
        if not isinstance(symbol, FuncSym):
            raise TypeMismatchInStatement(ast)
        if st.properties.isSuper: 
            ast.name = 'super'

        if ast.name != "super" and len(symbol.params) != len(ast.args):
            raise TypeMismatchInStatement(ast)

        if len(symbol.params) < len(ast.args):
            raise TypeMismatchInExpression(ast.args[len(symbol.params)])
        if len(symbol.params) > len(ast.args):
            raise TypeMismatchInExpression(None)

        for i in range(len(symbol.params)):
            if symbol.params[i].out and not isinstance(ast.args[i], (Id, ArrayCell)):
                if ast.name != "super":
                    raise TypeMismatchInStatement(ast)
                raise TypeMismatchInExpression(ast.args[i])

        for i in range(len(symbol.params)):
            _, paramType = self.visit(ast.args[i], st)

            if isinstance(symbol.params[i].typ, AutoType): 
                symbol.params[i].typ = paramType

            elif isinstance(paramType, AutoType):
                Utility.inference(ast.args[i].name, symbol.params[i].typ, st)

            elif not Utility.forceType(symbol.params[i].typ, paramType): 
                if ast.name != "super": 
                    raise TypeMismatchInStatement(ast)
                raise TypeMismatchInExpression(ast.args[i])

        return st, CallStmtType()
    
    def visitBlockStmt(self, ast : BlockStmt, st : SymbolTable):
        for element in ast.body:
            if isinstance(element, CallStmt) and element.name in ['super', 'preventDefault']: 
                continue
            st, _ = self.visit(element, st)
            if isinstance(element, ReturnStmt): 
                break
        return st, BlockStmtType()

    def visitVarDecl(self, ast: VarDecl, st: SymbolTable):
        if len(list(filter(lambda sym: sym.name == ast.name, st.envs[0]))) > 0: 
            raise Redeclared(Variable(), ast.name)

        if not ast.init:
            if isinstance(ast.typ, AutoType): 
                raise Invalid(Variable(), ast.name)
        else:
            st, initTyp = self.visit(ast.init, st)
            st = Utility.combineSym(VarSym(ast.name, ast.typ), st)

            if type(initTyp) is InvalidType: 
                raise IllegalArrayLiteral(ast.init)
            if isinstance(ast.typ, AutoType) and isinstance(initTyp, AutoType):
                raise TypeMismatchInVarDecl(ast) 

            if isinstance(ast.typ, AutoType):
                ast.typ = Utility.inference(ast.name, initTyp, st)

            elif isinstance(initTyp, AutoType):
                Utility.inference(ast.init.name, ast.typ, st)

            elif not Utility.forceType(ast.typ, initTyp): 
                raise TypeMismatchInVarDecl(ast)

        return Utility.combineSym(VarSym(ast.name, ast.typ), st), DeclType()

    def visitParamDecl(self, ast: ParamDecl, st: SymbolTable): pass

    def visitFuncDecl(self, ast: FuncDecl, st: SymbolTable):
        for sym in st.envs[0]:
            if sym.name == ast.name:
                raise Redeclared(Function(), ast.name)

        for symbol in st.funcprototype:
            if symbol.name == ast.name:
                st = Utility.combineSym(symbol, st)
                break

        symbol = st.envs[0][0]
        newst = Utility.goInFunc(st, symbol)

        if ast.inherit:
            parentsym = Utility.findFunc(ast.inherit, st)
            if not parentsym: 
                raise Undeclared(Function(), ast.inherit)

            for parentparam in parentsym.params:
                if parentparam.inherit:
                    newst = Utility.combineSym(parentparam, newst)

            for param in symbol.params:
                if Utility.local(param.name, newst): 
                    raise Invalid(Parameter(), param.name)

            for param in symbol.params:
                if Utility.findVar(param.name, newst): 
                    raise Redeclared(Parameter(), param.name)
                newst = Utility.combineSym(param, newst)

            if len(ast.body.body) == 0 or not hasattr(ast.body.body[0], 'name') or ast.body.body[0].name not in ['preventDefault', 'super']: 
                if len(parentsym.params) != 0: 
                    raise InvalidStatementInFunction(ast.name)

            elif ast.body.body[0].name == 'super':
                newst.properties.isSuper = True
                newst, _ = self.visit(CallStmt(parentsym.name, ast.body.body[0].args), newst)
        else:
            for param in symbol.params:
                if Utility.local(param.name, newst): 
                    raise Redeclared(Parameter(), param.name)
                newst = Utility.combineSym(param, newst)

            if len(ast.body.body) > 0 and isinstance(ast.body.body[0], CallStmt) and ast.body.body[0].name in ['preventDefault', 'super']:
                raise InvalidStatementInFunction(ast.name)

        newst, _ = self.visit(ast.body, newst)
        return st, DeclType()

    def visitProgram(self, ast : Program, st : SymbolTable):
        st = SymbolTable()
        st = PreCheck(ast).visit(ast, st)

        for decl in ast.decls:
            st, _ = self.visit(decl, st)
        mainFunc = False
        for symbol in st.funcprototype:
            if symbol.name == 'main' and symbol.params == [] and isinstance(symbol.typ, VoidType):
                mainFunc = True
        if not mainFunc: 
            raise NoEntryPoint()

