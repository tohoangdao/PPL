.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [[[[[I from Label0 to Label1
	iconst_1
	iconst_1
	iconst_1
	iconst_1
	iconst_2
	multianewarray [[[[[I 5
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	bipush 40
	iastore
	aload_1
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_1
	bipush 50
	iastore
	aload_1
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 9
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
