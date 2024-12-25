.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static removeMin([II)V
Label0:
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is min I from Label0 to Label1
	getstatic MT22Class/arr [I
	iconst_0
	iaload
	istore_3
	iconst_1
	istore_2
Label4:
	iload_2
	iload_1
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	iload_3
	getstatic MT22Class/arr [I
	iload_2
	iaload
	if_icmple Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
	istore_3
	getstatic MT22Class/arr [I
	iload_2
	iaload
Label11:
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
	iconst_0
	istore_2
Label16:
	iload_2
	iload_1
	if_icmpge Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label15
	getstatic MT22Class/arr [I
	iload_2
	iaload
	iload_3
	if_icmpne Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifle Label23
	iload_1
	iconst_1
	isub
	istore_1
.var 4 is j I from Label24 to Label25
	iconst_0
	istore 4
	iload_2
	istore 4
Label28:
	iload 4
	iload_1
	if_icmpge Label29
	iconst_1
	goto Label30
Label29:
	iconst_0
Label30:
	ifle Label27
	getstatic MT22Class/arr [I
	iload 4
	getstatic MT22Class/arr [I
	iload 4
	iconst_1
	iadd
	iaload
	iastore
Label26:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label28
Label27:
	iload_2
	iconst_1
	isub
	istore_2
Label23:
Label14:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label16
Label15:
Label1:
	return
.limit stack 30
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [I from Label0 to Label1
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	dup
	iconst_5
	bipush 6
	iastore
	dup
	bipush 6
	bipush 7
	iastore
	dup
	bipush 7
	bipush 8
	iastore
	dup
	bipush 8
	bipush 9
	iastore
	dup
	bipush 9
	iconst_1
	iastore
	astore_1
.var 2 is n I from Label0 to Label1
	bipush 10
	istore_2
	aload_1
	iload_2
	invokestatic MT22Class/removeMin([II)V
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
	iconst_0
	istore_3
Label4:
	iload_3
	iload_2
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	getstatic MT22Class/arr [I
	iload_3
	iaload
	invokestatic io/printInteger(I)V
Label2:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label3:
Label1:
	return
.limit stack 22
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
	bipush 10
	newarray int
	putstatic MT22Class/arr [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
