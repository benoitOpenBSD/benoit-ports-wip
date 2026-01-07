
COMMENT =		small processor disassembler suite

DISTNAME =		dasmxx-20250619
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/nejohnson/dasmxx

GH_ACCOUNT =		nejohnson
GH_PROJECT =		dasmxx
GH_COMMIT =		d5d8bce99670c4aaea9bcabb0e700f3a7b9ad140

WANTLIB +=		c

USE_GMAKE =		Yes

MAKE_FLAGS =		CC="${CC}" CFLAGS="${CFLAGS}"

WRKSRC =		${WRKDIST}/src

NO_TEST =		Yes

# More to add : dasm02, dasm09, ...
do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/txt2bin ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/dasm1802 ${PREFIX}/bin/
	${INSTALL_DATA_DIR} ${PREFIX}/share/dasmxx/test
	cp -R ${WRKDIST}/test/* ${PREFIX}/share/dasmxx/test

.include <bsd.port.mk>
