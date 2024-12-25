.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [I from Label0 to Label1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_3
	ineg
	iastore
	dup
	iconst_1
	bipush 9
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_1
	iastore
	dup
	iconst_4
	bipush 8
	iastore
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_2
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
.var 3 is temp I from Label7 to Label8
	aload_1
	iload_2
	iaload
	istore_3
	aload_1
	iload_2
	aload_1
	iconst_4
	iload_2
	isub
	iaload
	iastore
	aload_1
	iconst_4
	iload_2
	isub
	iload_3
	iastore
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
	iconst_0
	istore_2
Label11:
	iload_2
	iconst_5
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
	aload_1
	iload_2
	iaload
	invokestatic io/printInteger(I)V
Label9:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label11
Label10:
Label1:
	return
.limit stack 17
.limit locals 4
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
