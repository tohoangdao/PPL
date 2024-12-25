.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static foo(IIF)V
Label0:
.var 3 is a I from Label0 to Label1
	iload_0
	iload_1
	irem
	istore_3
	iload_3
	i2f
	fload_2
	fadd
	invokestatic io/printFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 20
	iconst_5
	ldc 0.99
	invokestatic MT22Class/foo(IIF)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method

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

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
