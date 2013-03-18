# $OpenBSD: Makefile,v 1.5 2013/03/11 10:50:06 espie Exp $

COMMENT =	C++ unit test framework

DISTNAME =	gtest-1.6.0

SHARED_LIBS +=	gtest		0.0   # .0.0
SHARED_LIBS +=	gtest_main	0.0   # .0.0

CATEGORIES =	devel

HOMEPAGE =	http://code.google.com/p/googletest/

MAINTAINER =	Vincent Auclair <auclair.vincent@gmail.com>

# New BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =	http://googletest.googlecode.com/files/
EXTRACT_SUFX =		.zip

MODULES =		lang/python devel/cmake

SEPARATE_BUILD =	Yes

WANTLIB =		m stdc++

USE_LIBTOOL =		Yes
CONFIGURE_STYLE =	cmake
CONFIGURE_ARGS +=	${CONFIGURE_SHARED}
CFLAGS +=		-DGTEST_CREATE_SHARED_LIBRARY=1

NO_TEST =	Yes

.include <bsd.port.mk>
