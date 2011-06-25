$OpenBSD$
--- setup.c.orig	Sun Jun 19 00:06:08 2011
+++ setup.c	Sat Jun 25 16:04:40 2011
@@ -237,7 +237,7 @@ char	drawPath[MAXPATHLENGTH]; /* last char is NOT '/' 
 char	bootDir[MAXPATHLENGTH+2];
 char	homeDir[MAXPATHLENGTH];
 char	tgifDir[MAXPATHLENGTH];
-char	tmpDir[MAXPATHLENGTH];
+char	tmpDir[MAXPATHLENGTH] = "/tmp";
 
 int	symPathNumEntries = INVALID;
 char	* * symPath=NULL;
