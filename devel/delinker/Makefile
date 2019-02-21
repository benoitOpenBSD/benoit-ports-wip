# $OpenBSD$

COMMENT =		Unlinks a binary executable to get back a set of .o files

DISTNAME =		delinker-20181216
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# ???
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/jnider/delinker

GH_ACCOUNT =		jnider
GH_PROJECT =		delinker
GH_COMMIT =		0cbb0336d52ab7f9fa4687a08d15bd05a2233f46

WANTLIB +=		c udis86

BUILD_DEPENDS =		devel/udis86
RUN_DEPENDS =		devel/udis86

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/delinker ${PREFIX}/bin/


.include <bsd.port.mk>
