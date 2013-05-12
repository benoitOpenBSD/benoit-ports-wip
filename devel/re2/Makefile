# $OpenBSD$

COMMENT =	alternative to pcre, perl and python

DISTNAME =	re2-20130115
SHARED_LIBS +=	re2	0.0
CATEGORIES = 	devel

HOMEPAGE =	http://code.google.com/p/re2/
 
MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB += 	pthread m stdc++

MASTER_SITES =	https://re2.googlecode.com/files/

EXTRACT_SUFX =	.tgz

WRKDIST =	${WRKDIR}/re2

USE_GMAKE =	Yes

MAKE_FLAGS =	LIBre2_VERSION=${LIBre2_VERSION}

TEST_TARGET =test

.include <bsd.port.mk>
