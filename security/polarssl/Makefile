# $OpenBSD$

COMMENT =		library implementing the SSH2 protocol

V =			1.3.1
DISTNAME =		polarssl-${V}-gpl
PKGNAME =		${DISTNAME:S/-gpl//}
CATEGORIES =		security
SHARED_LIBS +=		polarssl	0.0	# .1.1

HOMEPAGE =              https://polarssl.org/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		z

MASTER_SITES =		https://polarssl.org/download/
EXTRACT_SUFX =		.tgz

MODULES =		devel/cmake

WRKDIST =		${WRKDIR}/polarssl-${V}

.include <bsd.port.mk>
