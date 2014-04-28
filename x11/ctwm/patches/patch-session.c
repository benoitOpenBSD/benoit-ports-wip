$OpenBSD$
--- session.c.orig	Fri Feb  2 09:56:54 2007
+++ session.c	Mon Apr 28 14:06:51 2014
@@ -838,6 +838,7 @@
     return found;
 }
 
+#ifndef __OpenBSD__
 /*===[ Unique Filename Generator ]===========================================*/
 
 static char *unique_filename (char *path, char *prefix)
@@ -865,6 +866,7 @@
 #endif
 }
 
+#endif /* ! __OpenBSD__ */
 /*===[ SAVE WINDOW INFORMATION ]=============================================*/
 
 #ifndef PATH_MAX
@@ -891,6 +893,10 @@
     char discardCommand[PATH_MAX + 4];
     int numVals, i;
     static int first_time = 1;
+#ifdef __OpenBSD__
+    int tmphandle;
+    char tmpprefix[256];
+#endif
 
     if (first_time)
     {
@@ -942,12 +948,20 @@
      *        no longer the same since the new format supports
      *        virtaul workspaces.
      *========================================================*/
+#ifdef __OpenBSD__
+    strncpy(tmpprefix, path, 256);
+    strncat(tmpprefix, "/.ctwmXXXXXX", (sizeof(path) - 12));
+    if ((tmphandle = mkstemp(tmpprefix)) == -1)
+      goto bad;
+    if ((configFile = fdopen(tmphandle, "wb")) == NULL)
+      goto bad;
+#else
     if ((filename = unique_filename (path, ".ctwm")) == NULL)
 	goto bad;
 
     if (!(configFile = fopen (filename, "wb"))) /* wb = write bytes ? */
 	goto bad;
-
+#endif /* __OpenBSD__ */
     if (!write_ushort (configFile, SAVEFILE_VERSION))
 	goto bad;
 
