.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_5
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
.var 2 is temp I from Label7 to Label8
	getstatic MT22Class/a [I
	iload_1
	iaload
	istore_2
	getstatic MT22Class/a [I
	iload_1
	getstatic MT22Class/a [I
	bipush 9
	iload_1
	isub
	iaload
	iastore
	getstatic MT22Class/a [I
	bipush 9
	iload_1
	isub
	iload_2
	iastore
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	iconst_0
	istore_1
Label11:
	iload_1
	bipush 10
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
	getstatic MT22Class/a [I
	iload_1
	iaload
	invokestatic io/printInteger(I)V
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label11
Label10:
Label1:
	return
.limit stack 13
.limit locals 3
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
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	bipush 9
	iastore
	dup
	iconst_2
	iconst_1
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	dup
	iconst_4
	bipush 6
	iastore
	dup
	iconst_5
	iconst_4
	iastore
	dup
	bipush 6
	iconst_5
	iastore
	dup
	bipush 7
	bipush 8
	iastore
	dup
	bipush 8
	bipush 7
	iastore
	dup
	bipush 9
	iconst_2
	iastore
	putstatic MT22Class/a [I
Label1:
	return
.limit stack 12
.limit locals 0
.end method
