.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static reverse(I)I
Label0:
.var 1 is result I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is temp I from Label0 to Label1
	iload_0
	istore_2
	iload_2
	iconst_0
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_0
	ineg
	istore_0
Label4:
Label7:
	iload_0
	iconst_0
	if_icmple Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
	bipush 10
	iload_1
	imul
	iload_0
	bipush 10
	irem
	iadd
	istore_1
	iload_0
	i2f
	bipush 10
	i2f
	fdiv
	istore_0
	goto Label7
Label8:
	iload_2
	iconst_0
	if_icmpge Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label15
	iload_1
	ineg
	ireturn
Label15:
	iload_1
	ireturn
Label1:
	return
.limit stack 16
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
	invokestatic io/readInteger()I
	istore_1
	iload_1
	invokestatic MT22Class/reverse(I)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 1
.limit locals 2
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
