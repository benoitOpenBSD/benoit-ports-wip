# $OpenBSD$

COMMENT =		an SSL library with an intuitive API

V =			1.3.1
DISTNAME =		polarssl-${V}-gpl
PKGNAME =		${DISTNAME:S/-gpl//}
CATEGORIES =		security
SHARED_LIBS +=		polarssl	0.0	# .1.1

HOMEPAGE =              https://polarssl.org/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		 c crypto ssl

MASTER_SITES =		https://polarssl.org/download/
EXTRACT_SUFX =		.tgz

USE_GMAKE =		Yes

WRKDIST =		${WRKDIR}/polarssl-${V}

do-install:

.include <bsd.port.mk>
