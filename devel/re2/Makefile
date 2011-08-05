# $OpenBSD$

COMMENT =	alternative to pcre, perl and python

DISTNAME =	re2-0.7007b2180a42
SHARED_LIBS +=	re2	0.0
CATEGORIES = 	devel

HOMEPAGE =	http://code.google.com/p/re2/
 
MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_DISTFILES_FTP =		Yes
PERMIT_DISTFILES_CDROM =	Yes
PERMIT_PACKAGE_FTP =		Yes
PERMIT_PACKAGE_CDROM =		Yes

WANTLIB += 	c m stdc++

MASTER_SITES =	http://code.google.com/p/re2/

USE_GMAKE =	Yes

MAKE_FLAGS =	LIBre2_VERSION=${LIBre2_VERSION}

REGRESS_TARGET =test

.include <bsd.port.mk>
