# $OpenBSD$

COMMENT =		small processor disassembler suite

DISTNAME =		dasmxx-20220907
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/nejohnson/dasmxx

GH_ACCOUNT =		nejohnson
GH_PROJECT =		dasmxx
GH_COMMIT =		95ad19458233adee72166cdd72dfa24e32f5992b

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
