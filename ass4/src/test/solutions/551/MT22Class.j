.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public <init>()V
.var 0 is this LMT22Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static foo(III)V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
Label0:
	iload_1
	bipush 10
	iadd
	istore_1
	iload_0
	iload_2
	iadd
	bipush 20
	iadd
	istore_0
	iload_0
	invokestatic io/printInteger(I)V
	iload_1
	invokestatic io/printInteger(I)V
	iload_2
	invokestatic io/printInteger(I)V
	iload_0
	putstatic foo.a I
	iload_1
	putstatic foo.b I
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is j I from Label0 to Label1
	bipush 10
	istore_1
.var 2 is k I from Label0 to Label1
	bipush 15
	istore_2
	iload_1
	iload_1
	iload_2
	invokestatic MT22Class/foo(III)V
	getstatic foo.a I
	istore_1
	getstatic foo.b I
	istore_1
	iload_1
	invokestatic io/printInteger(I)V
	iload_2
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 3
.limit locals 3
.end method
