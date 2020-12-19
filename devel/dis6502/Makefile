# $OpenBSD$

COMMENT =		disassembler for 6502 processors 

DISTNAME =		dis6502-0.13
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/SteveFosdick/dis6502

GH_ACCOUNT =		SteveFosdick
GH_PROJECT =		dis6502
GH_COMMIT =		a9bb52e3e5f1eec56c361ca23a008e32f8cb869d

WANTLIB +=		c

USE_GMAKE =		Yes

BUILD_DEPENDS =		textproc/py-docutils

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/dis6502 ${PREFIX}/bin/
	${INSTALL_MAN} ${WRKSRC}/dis6502.1 ${PREFIX}/man/man1

.include <bsd.port.mk>
