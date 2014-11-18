# $OpenBSD: Makefile.template,v 1.55 2008/08/23 15:28:00 ajacoutot Exp $
# $FreeBSD/NetBSD: credit FreeBSD/NetBSD if thats where the port came from $
# Original from: credit the original author here
#
# Replace ??? with appropriate values
# Remove extraneous comments before commit.

# Reasons why the port/package shouldn't be built
#
#ONLY_FOR_ARCHS =	???
#NOT_FOR_ARCHS =	???
#SHARED_ONLY =		???
#COMES_WITH =		???
#BROKEN =		reason

#
# Very short description of the package, 60 chars max
#
COMMENT =		API/framework for generating random, malformed data
# COMMENT-foo =		???	for multi packages

#
# What port/package will be created
#
DISTNAME =		antiparser-2.0
#PKGNAME =		???
#PKGNAME-foo =		???	for multi packages

# for any port that create shared libraries.
# both libtool and cmake handle this automatically.
# for libtool-based ports, have a look at WRKBUILD/shared_libs.log
#SHARED_LIBS =		???

CATEGORIES =		security

HOMEPAGE =		http://www.antiparser.org/

# where to send bitches about this port
# Put a complete email address with a real name, e.g.,
# MAINTAINER=	John Doe <doe57@machine.somewhere.org>
# if you maintain several ports, try to use the same line each time.
# MAINTAINER implies some amount of responsibility.
# If you no longer use the port, or are unwilling/unable to handle issues
# in a timely manner, *leave the field blank*.
# Default value is ports@openbsd.org, no need to fill in
MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

#WANTLIB =		???

# where the source files and patches can be fetched
#
MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=antiparser/}

MODULES =		lang/python

.include <bsd.port.mk>
