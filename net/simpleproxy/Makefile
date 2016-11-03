# $OpenBSD$

COMMENT =		simple tcp proxy

V =			3.5
GH_ACCOUNT =		vzaliva
GH_PROJECT =		simpleproxy
GH_TAGNAME =		$V
DISTNAME =		${GH_PROJECT}-v.${V}
PKGNAME =		${GH_PROJECT}-${V}

CATEGORIES =		net

HOMEPAGE =		https://github.com/vzaliva/simpleproxy

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		c

CONFIGURE_STYLE =	gnu
WRKDIST =               ${WRKDIR}/${DISTNAME}

NO_TEST =		Yes

.include <bsd.port.mk>
