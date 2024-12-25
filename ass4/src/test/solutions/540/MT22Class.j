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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	ldc 1.0
	fstore_1
.var 2 is b F from Label0 to Label1
	ldc 2.0
	fstore_2
	fload_1
	fload_2
	invokestatic MT22Class/foo(FF)V
	getstatic foo.x F
	fstore_1
	getstatic foo.y F
	fstore_2
	fload_1
	invokestatic io/printFloat(F)V
	fload_2
	invokestatic io/printFloat(F)V
Label1:
	return
.limit stack 5
.limit locals 3
.end method

.method public static foo(FF)V
.var 0 is x F from Label0 to Label1
.var 1 is y F from Label0 to Label1
Label0:
	fload_0
	iconst_1
	i2f
	fadd
	fstore_0
	fload_1
	iconst_1
	i2f
	fadd
	fstore_1
	fload_0
	fload_1
	fadd
	invokestatic io/printFloat(F)V
	fload_0
	putstatic foo.x F
	fload_1
	putstatic foo.y F
Label1:
	return
.limit stack 4
.limit locals 2
.end method
