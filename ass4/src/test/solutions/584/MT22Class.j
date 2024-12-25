.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static isAmstrong(I)Z
Label0:
.var 1 is sum I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is temp I from Label0 to Label1
	iload_0
	istore_2
Label2:
	iload_2
	iconst_0
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
.var 3 is digit I from Label6 to Label7
	iload_2
	bipush 10
	irem
	istore_3
	iload_1
	iload_3
	iload_3
	imul
	iload_3
	imul
	iadd
	istore_1
	iload_2
	i2f
	bipush 10
	i2f
	fdiv
	istore_2
	goto Label2
Label3:
	iload_1
	iload_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ireturn
Label1:
	return
.limit stack 11
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	sipush 153
	istore_1
	iload_1
	invokestatic MT22Class/isAmstrong(I)Z
	invokestatic io/printBoolean(Z)V
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
