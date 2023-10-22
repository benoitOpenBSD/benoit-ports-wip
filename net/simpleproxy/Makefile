
COMMENT =		simple tcp proxy

V =			v.3.5
GH_ACCOUNT =		vzaliva
GH_PROJECT =		simpleproxy
GH_TAGNAME =		$V
DISTNAME =		${GH_PROJECT}-${V}
PKGNAME =		${GH_PROJECT}-${V:S/v.//}

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
