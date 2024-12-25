from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *
from Utils import *
from CodeGenError import *

class ClassType(Type):
    def __init__(self, classname):
        self.classname = classname

class ArrayPointerType(Type):
    def __init__(self, eleType):
        self.eleType = eleType

class SubBody():
    def __init__(self, frame, sym, isGlobal=False):
        self.frame = frame
        self.sym = sym
        self.isGlobal = isGlobal

class Access():
    def __init__(self, frame, sym, isLeft=False, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        self.value = value

class CName(Val):
    def __init__(self, value):
        self.value = value

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self, name, mtype, value=None, init=None, isGlobal=True):
        self.name = name
        self.isGlobal = isGlobal
        self.value = value
        self.init = init
        self.mtype = mtype

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInteger", MType([], IntegerType()), CName(self.libName)),
                Symbol("readFloat", MType([], FloatType()), CName(self.libName)),
                Symbol("readBoolean", MType([], BooleanType()), CName(self.libName)),
                Symbol("readString", MType([], StringType()), CName(self.libName)),
                Symbol("printInteger", MType([IntegerType()], VoidType()), CName(self.libName)),
                Symbol("printFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("printBoolean", MType([BooleanType()], VoidType()), CName(self.libName)),
                Symbol("printString", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("super", MType(list(), VoidType()), CName(self.libName)),
                Symbol("preventDefault", MType([], VoidType()), CName(self.libName)),]

    def gen(self, ast, path):
        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)

class CodeGenVisitor(Visitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.className = "MT22Class"
        self.emit = Emitter(self.path + '/' + self.className + '.j')

    def visitProgram(self, ctx: Program, o):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        declaration = self.env
        for decl in ctx.decls:
            if isinstance(decl, FuncDecl):
                partype = [i.typ for i in decl.params]
                declaration = [Symbol(decl.name, MType(partype, decl.return_type), CName(self.className))] + declaration
            else:
                newSym = self.visit(decl, SubBody(None, None, True))
                declaration = [newSym] + declaration

        [self.visit(decl, SubBody(None, declaration)) for decl in ctx.decls if isinstance(decl, FuncDecl)]

        self.genMETHOD(FuncDecl("<init>", VoidType(), list(), None, BlockStmt([])), declaration, Frame("<init>", VoidType()))

        self.genMETHOD(FuncDecl("<clinit>", VoidType(), list(), None, BlockStmt([])), declaration, Frame("<clinit>", VoidType()))

        self.emit.emitEPILOG()
        return

    def visitFuncDecl(self, ctx: FuncDecl, o):
        frame = Frame(ctx.name, ctx.return_type)
        o.sym += [Symbol(paramdecl.name, paramdecl.typ, Index(frame.getNewIndex())) for paramdecl in ctx.params]
        self.genMETHOD(ctx, o.sym, frame)
        return Symbol(ctx.name, MType([x.typ for x in ctx.params], ctx.return_type), CName(self.className))

    def genMETHOD(self, Funcdecl: FuncDecl, o, frame):
        isInit = Funcdecl.name == "<init>"

        isMain = Funcdecl.name == "main" and len(Funcdecl.params) == 0 and isinstance(Funcdecl.return_type, VoidType)

        if isInit:
            returnType = VoidType()
        else:
            returnType = Funcdecl.return_type

        if isInit: 
            methodName = "<init>" 
        else: 
            methodName = Funcdecl.name
        intype = [ArrayPointerType(StringType())] if isMain else list(
            map(lambda x: x.typ, Funcdecl.params))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(False)
        glenv = o

        if isInit:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(), "this",
                    ClassType(Id(self.className)),
                    frame.getStartLabel(), frame.getEndLabel(), frame)
            )
        elif isMain:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(), "args",
                    ArrayPointerType(StringType()),
                    frame.getStartLabel(), frame.getEndLabel(), frame)
            )

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        if Funcdecl.name == "<clinit>":
            for vardecl in glenv:
                if type(vardecl.mtype) is not MType and vardecl.isGlobal:
                    if isinstance(vardecl.mtype, ArrayType):
                        pass
                    else:
                        if vardecl.init is not None:
                            initCode = self.visit(
                                vardecl.init, Access(frame, glenv, False, True))
                            self.emit.printout(initCode)
                            self.emit.printout(self.emit.emitPUTSTATIC(
                                self.className + "/" + vardecl.name, vardecl.mtype, frame)
                            )

        for decl in Funcdecl.body.body:
            self.visit(decl, SubBody(frame, glenv, False))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitAssignStmt(self, ctx: AssignStmt, o):
        rhs, rtype = self.visit(ctx.rhs, Access(o.frame, o.sym, False))
        lhs, ltype = self.visit(ctx.lhs, Access(o.frame, o.sym, True))

        if isinstance(ctx.lhs, (Id, FuncCall)):
            lSym = list(filter(lambda x: x.name == ctx.lhs.name, o.sym))[-1]
            if isinstance(ltype, AutoType):
                lSym.mtype = rtype
            else:
                lSym.mtype = ltype
        if isinstance(ctx.rhs, (Id, FuncCall)):
            rSym = list(filter(lambda x: x.name == ctx.rhs.name, o.sym))[-1]
            if isinstance(rtype, AutoType):
                rSym.mtype = ltype
            else:
                rSym.mtype = rtype

        if isinstance(ctx.lhs, ArrayCell) or isinstance(ctx.rhs, ArrayCell):
            pass
        else:
            self.emit.printout(rhs)
            self.emit.printout(lhs)

    def visitBlockStmt(self, ctx: BlockStmt, o):
        o.frame.enterScope(False)
        for decl in ctx.body:
            self.visit(decl, o)
        o.frame.exitScope()

    def visitForStmt(self, ctx: ForStmt, o):
        o.frame.enterLoop()
        CONTINUELABEL = o.frame.getContinueLabel()
        BREAKLABEL = o.frame.getBreakLabel()
        STARTLABEL = o.frame.getNewLabel()
        
        self.visit(ctx.init, o)
        self.emit.printout(self.emit.emitLABEL(STARTLABEL, o.frame))
        self.emit.printout(self.visit(ctx.cond, Access(o.frame, o.sym))[0])
        self.emit.printout(self.emit.emitIFFALSE(BREAKLABEL, o.frame))
        self.visit(ctx.stmt, o)
        self.emit.printout(self.emit.emitLABEL(CONTINUELABEL, o.frame))
        
        updateExpr = AssignStmt(
            ctx.init.lhs, BinExpr("+", ctx.init.lhs, ctx.upd))
        self.visit(updateExpr, o)
        self.emit.printout(self.emit.emitGOTO(STARTLABEL, o.frame))
        self.emit.printout(self.emit.emitLABEL(BREAKLABEL, o.frame))

        o.frame.exitLoop()

    def visitIfStmt(self, ctx: IfStmt, o):
        if ctx.fstmt is None:
            cond = self.visit(ctx.cond, Access(o.frame, o.sym, False))
            self.emit.printout(cond)
            FLABEL = o.frame.getNewLabel()

            fStmt = self.emit.emitIFFALSE(FLABEL, o.frame)
            self.emit.printout(fStmt)
            self.visit(ctx.tstmt, o)

            self.emit.printout(self.emit.emitLABEL(FLABEL, o.frame))
        else:
            cond = self.visit(ctx.cond, Access(o.frame, o.sym, False))
            self.emit.printout(cond)
            FLABEL = o.frame.getNewLabel()
            EXITLABEL = o.frame.getNewLabel()
            
            fStmt = self.emit.emitIFFALSE(FLABEL, o.frame)
            self.emit.printout(fStmt)
            self.visit(ctx.tstmt, o)
            
            goTo = self.emit.emitGOTO(EXITLABEL, o.frame)
            self.emit.printout(goTo)
            
            tStmt = self.emit.emitLABEL(FLABEL, o.frame)
            self.emit.printout(tStmt)
            self.visit(ctx.fstmt, o)
            
            exitL = self.emit.emitLABEL(EXITLABEL, o.frame)
            self.emit.printout(exitL)

    def visitWhileStmt(self, ctx: WhileStmt, o):
        o.frame.enterLoop()
        CONTINUELABEL = o.frame.getContinueLabel()
        BREAKLABEL = o.frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(CONTINUELABEL, o.frame))
        
        cond = self.visit(ctx.cond, Access(o.frame, o.sym, False))[0]
        self.emit.printout(cond)
        self.emit.printout(self.emit.emitIFFALSE(BREAKLABEL, o.frame))
        self.visit(ctx.stmt, o)
        self.emit.printout(self.emit.emitGOTO(CONTINUELABEL, o.frame))
        self.emit.printout(self.emit.emitLABEL(BREAKLABEL, o.frame))

        o.frame.exitLoop()

    def visitDoWhileStmt(self, ctx: DoWhileStmt, o):
        o.frame.enterLoop()
        CONTINUELABEL = o.frame.getContinueLabel()
        BREAKLABEL = o.frame.getBreakLabel()
        self.visit(ctx.stmt, Access(o.frame, o.sym, False))
        self.emit.printout(self.emit.emitLABEL(CONTINUELABEL, o.frame))
        
        cond = self.visit(ctx.cond, Access(o.frame, o.sym, False))[0]
        self.emit.printout(cond)
        self.emit.printout(self.emit.emitIFFALSE(BREAKLABEL, o.frame))
        self.visit(ctx.stmt, Access(o.frame, o.sym, False))
        self.emit.printout(self.emit.emitGOTO(CONTINUELABEL, o.frame))
        self.emit.printout(self.emit.emitLABEL(BREAKLABEL, o.frame))
        o.frame.exitLoop()

    def visitBreakStmt(self, ctx: BreakStmt, o):
        frame = o.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinueStmt(self, ctx: ContinueStmt, o):
        frame = o.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

    def visitReturnStmt(self, ctx: ReturnStmt, o):
        if not isinstance(o.frame.returnType, VoidType):
            ret, retType = self.visit(ctx.expr, Access(o.frame, o.sym, False, False))
            if isinstance(o.frame.returnType, FloatType) and isinstance(retType, IntegerType):
                ret = ret + self.emit.emitI2F(o.frame)
            self.emit.printout(ret)
        
        self.emit.printout(self.emit.emitRETURN(o.frame.returnType, o.frame))

    def visitCallStmt(self, ctx: CallStmt, o):
        if ctx.name in ['super', 'preventDefault']:
            return
        sym = next(filter(lambda x: ctx.name == x.name, o.sym), None)
        cname = sym.value.value
        func = sym.mtype
        if isinstance(func.rettype, AutoType):
            func.rettype = VoidType()
        code = ""
        i = 0
        for x in ctx.args:
            arg, atype = self.visit(x, Access(o.frame, o.sym, False, False))
            code += arg
            if isinstance(func.partype[i], FloatType) and isinstance(atype, IntegerType):
                code += self.emit.emitI2F(o.frame)
            i += 1
        self.emit.printout(code)

        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ctx.name, func, o.frame))
    def visitFuncCall(self, ctx: FuncCall, o):
        for defaultFunction in self.env:
            if ctx.name == defaultFunction.name:
                code = self.emit.emitINVOKESTATIC(
                    defaultFunction.value.value + "/" + defaultFunction.name,
                    defaultFunction.mtype, o.frame
                )
                return code, defaultFunction.mtype.rettype
        sym = next(filter(lambda x: ctx.name == x.name, o.sym), None)
        cname = sym.value.value
        func = sym.mtype
        pair = ["", list()]
        for arg in ctx.args:
            str1, typ1 = self.visit(arg, Access(o.frame, o.sym, False, True))
            pair = [pair[0] + str1, pair[1].append(typ1)]
            if isinstance(func.rettype, FloatType) and isinstance(typ1, IntegerType):
                pair[0] += self.emit.emitI2F(o.frame)

        pair[0] = pair[0] + \
            self.emit.emitINVOKESTATIC(cname + "/" + ctx.name, func, o.frame)
        return pair[0], func.rettype

    def visitBinExpr(self, ctx: BinExpr, o):
        exp1, type1 = self.visit(ctx.left, o)
        exp2, type2 = self.visit(ctx.right, o)

        if isinstance(type1, AutoType):
            leftSym = list(filter(lambda x: x.name == ctx.left.name, o.sym))[-1]
            if isinstance(ctx.left, Id):
                leftSym.mtype = type2
            else:
                leftSym.mtype.rettype = type2

        if isinstance(type2, AutoType):
            rightSym = list(filter(lambda x: x.name == ctx.right.name, o.sym))[-1]
            if isinstance(ctx.right, Id):
                rightSym.mtype = type1
            else:
                rightSym.mtype.rettype = type1

        if type(type1) == type(type2):
            reType = type1
        elif isinstance(type1, IntegerType) and isinstance(type2, FloatType):
            exp1 = exp1 + self.emit.emitI2F(o.frame)
            reType = FloatType()
        else:
            exp2 = exp2 + self.emit.emitI2F(o.frame)
            reType = FloatType()

        if ctx.op == '*':
            op = self.emit.emitMULOP(ctx.op, reType, o.frame)
        elif ctx.op in ['+', '-']:
            op = self.emit.emitADDOP(ctx.op, reType, o.frame)
        elif ctx.op == '/':
            if isinstance(type1, IntegerType) and isinstance(type2, IntegerType):
                exp1 = exp1 + self.emit.emitI2F(o.frame)
                exp2 = exp2 + self.emit.emitI2F(o.frame)
                reType = FloatType()
            op = self.emit.emitMULOP(ctx.op, reType, o.frame)
        elif ctx.op == '%':
            reType = IntegerType()
            op = self.emit.emitMOD(o.frame)
        elif ctx.op == '::':
            reType = StringType()
            op = self.emit.emitINVOKEVIRTUAL(
                'java/lang/String/concat', MType([StringType()], StringType()), o.frame)
        elif ctx.op == '&&':
            reType = BooleanType()
            op = self.emit.emitANDOP(o.frame)
        elif ctx.op == '||':
            reType = BooleanType()
            op = self.emit.emitOROP(o.frame)
        else:
            op = self.emit.emitREOP(ctx.op, reType, o.frame)
            reType = BooleanType()

        return exp1 + exp2 + op, reType

    def visitUnExpr(self, ctx: UnExpr, o):
        exp, eType = self.visit(ctx.val, o)

        if isinstance(eType, AutoType):
            sym = list(filter(lambda x: x.name == ctx.val.name, o.sym))[-1]
            if isinstance(ctx.val, Id): 
                if ctx.op == '-':
                    sym.mtype = IntegerType()  
                else: 
                    sym.mtype = BooleanType()
            else:
                if ctx.op == '-':
                    sym.mtype.rettype = IntegerType()  
                else:
                    sym.mtype.rettype = BooleanType()

        if ctx.op == '-':
            reType = eType
            op = self.emit.emitNEGOP(eType, o.frame)
        elif ctx.op == '!':
            reType = BooleanType()
            op = self.emit.emitNOT(0, o.frame)

        return exp + op, reType

    def visitId(self, ctx: Id, o):
        sym = list(filter(lambda x: x.name == ctx.name, o.sym))[-1]
        if o.isLeft == False:
            if isinstance(sym.value, Index):
                code = self.emit.emitREADVAR(
                    sym.name, sym.mtype, sym.value.value, o.frame)
            else:
                code = self.emit.emitGETSTATIC(
                    sym.value.value + "." + sym.name, sym.mtype, o.frame)
        else:
            if isinstance(sym.value, Index):
                o.frame.push()
                code = self.emit.emitWRITEVAR(
                    sym.name, sym.mtype, sym.value.value, o.frame)
            else:
                code = self.emit.emitPUTSTATIC(
                    sym.value.value + "." + sym.name, sym.mtype, o.frame)
        return code, sym.mtype

    def visitArrayCell(self, ctx: ArrayCell, o):pass

    def visitIntegerLit(self, ctx: IntegerLit, o):
        return self.emit.emitPUSHICONST(ctx.val, o.frame), IntegerType()

    def visitFloatLit(self, ctx: FloatLit, o):
        return self.emit.emitPUSHFCONST(str(ctx.val), o.frame), FloatType()

    def visitStringLit(self, ctx: StringLit, o):
        return self.emit.emitPUSHCONST("\"" + ctx.val + "\"", StringType(), o.frame), StringType()

    def visitBooleanLit(self, ctx: BooleanLit, o):
        return self.emit.emitPUSHICONST(str(ctx.val).lower(), o.frame), BooleanType()

    def visitArrayLit(self, ctx: ArrayLit, o): pass