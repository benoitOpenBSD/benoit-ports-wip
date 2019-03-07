# $OpenBSD$

COMMENT =		C64 music debug output utility

DISTNAME =		siddump-20181216
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/cadaver/siddump

GH_ACCOUNT =		cadaver
GH_PROJECT =		siddump
GH_COMMIT =		f698a0698ca26b93643260eb4dbfdf74b19f6c49

WANTLIB +=		c m

# XXX Makefile to re-create
USE_GMAKE =		Yes
MAKE_FILE =		makefile
ALL_TARGET =		siddump

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/siddump ${PREFIX}/bin/

.include <bsd.port.mk>
