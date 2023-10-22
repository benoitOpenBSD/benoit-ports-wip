
COMMENT =		a subdomain enumeration tool
DISTNAME =		dnssearch-1.0.1-20170704
CATEGORIES =		net
HOMEPAGE =		https://github.com/evilsocket/dnssearch

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE_CDROM =	Yes

GH_ACCOUNT =		evilsocket
GH_PROJECT =		dnssearch
GH_COMMIT =		54cd420b446359a29a6319fba4e6ded787514acc

WANTLIB +=		c pthread

MODULES =		lang/go
MODGO_ENV =		PATH="${PORTPATH}"

do-build:
	${MODGO_BUILD_TARGET}
	${MODGO_CMD} build ${MODGO_FLAGS} -o ${MODGO_WORKSPACE}/bin/dnssearch main.go

NO_TEST =		Yes

.include <bsd.port.mk>
