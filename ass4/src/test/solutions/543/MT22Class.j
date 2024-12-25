.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a I

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
.var 1 is b I from Label0 to Label1
	getstatic MT22Class.a I
	getstatic MT22Class.a I
	iconst_1
	iadd
	invokestatic MT22Class/foo(II)I
	istore_1
	getstatic MT22Class.a I
	invokestatic io/printInteger(I)V
	iload_1
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public static foo(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static <clinit>()V
Label0:
	iconst_1
	iconst_2
	invokestatic MT22Class/foo(II)I
	iconst_1
	iadd
	putstatic MT22Class.a I
Label1:
	return
.limit stack 5
.limit locals 0
.end method
