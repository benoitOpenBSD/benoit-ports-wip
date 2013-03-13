# $OpenBSD$

COMMENT =	full-fledged system linker for mobile devices

V =		2.0.2
DISTNAME =	mclinker-RockBull-${V}-1
PKGNAME =	mclinker-${V}
CATEGORIES = 	devel

HOMEPAGE =	http://code.google.com/p/mclinker/
 
MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_DISTFILES_FTP =		Yes

MASTER_SITES =	http://mclinker.googlecode.com/files/

WANTLIB +=	c m pthread stdc++

MODULES +=              lang/clang

MODCLANG_ARCHS =        i386 amd64
MODCLANG_LANGS =        c c++

CONFIGURE_STYLE =	gnu

WRKDIST =	${WRKDIR}/mclinker-RockBull

.include <bsd.port.mk>
