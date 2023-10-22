
COMMENT =		multi-pass Cross Assembler 6502 and 65c816 processors

PKGNAME =		merlin32-1.0
DISTNAME =		Merlin32_v1.0
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

SITES =			${HOMEPAGE}

HOMEPAGE =		https://www.brutaldeluxe.fr/products/crossdevtools/merlin/

EXTRACT_SUFX=		.zip

WANTLIB +=		c

USE_GMAKE =		Yes

do-build:
	cd ${WRKBUILD}/Source && ${GMAKE} -f linux_makefile

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/Source/Merlin32 ${PREFIX}/bin/

.include <bsd.port.mk>
