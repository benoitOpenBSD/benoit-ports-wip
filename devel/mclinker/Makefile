# $OpenBSD$

COMMENT =	full-fledged system linker for mobile devices

V =		2.1.0
DISTNAME =	mclinker-NanHu
PKGNAME =	mclinker-${V}
CATEGORIES = 	devel

HOMEPAGE =	http://code.google.com/p/mclinker/
 
MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =	http://mclinker.googlecode.com/files/

WANTLIB +=	c m pthread stdc++

MODULES +=              lang/clang

MODCLANG_ARCHS =        i386 amd64
MODCLANG_LANGS =        c c++

CONFIGURE_STYLE =	gnu

WRKDIST =	${WRKDIR}/mclinker-NanHu

.include <bsd.port.mk>
