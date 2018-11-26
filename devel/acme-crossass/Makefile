# $OpenBSD$

COMMENT =		cross assembler for 6502/6510/65816 CPU

DISTNAME =		acme-crossass-20170329
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/meonwax/acme

GH_ACCOUNT =		meonwax
GH_PROJECT =		acme
GH_COMMIT =		6f42edb13c4040707590ead8ed3927b361391f77

WANTLIB +=		c m

MAKE_FLAGS =		CC="${CC}" CFLAGS="${CFLAGS}"

WRKSRC =		${WRKDIST}/src

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/acme ${PREFIX}/bin/
	${INSTALL_DATA_DIR} ${PREFIX}/share/acme/examples
	cp -R ${WRKDIST}/examples/* ${PREFIX}/share/acme/examples
	${INSTALL_DATA_DIR} ${PREFIX}/share/acme/ACME_Lib
	cp -R ${WRKDIST}/ACME_Lib/* ${PREFIX}/share/acme/ACME_Lib
	${INSTALL_DATA_DIR} ${PREFIX}/share/acme/contrib
	cp -R ${WRKDIST}/contrib/* ${PREFIX}/share/acme/contrib
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/acme
	cp -R ${WRKDIST}/docs/* ${PREFIX}/share/doc/acme

.include <bsd.port.mk>
