
COMMENT =		parse and dump UEFI firmware image

V =			0.11.0
PKGNAME =		UEFIFind-${V}
DISTNAME =		UE.$V
CATEGORIES =		sysutils

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/LongSoft/UEFITool

GH_ACCOUNT =		LongSoft
GH_PROJECT =		UEFITool

WRKDIST =		${WRKDIR}/${GH_PROJECT}-${DISTNAME}

WANTLIB +=		c m pthread stdc++

MODULES =		x11/qt4 devel/qmake

CONFIGURE_STYLE =       qmake
MODQMAKE_PROJECTS =     UEFIFind/uefifind.pro

NO_TEST =		Yes

do-install:
		${INSTALL_PROGRAM} ${WRKBUILD}/UEFIFind/UEFIFind ${PREFIX}/bin

.include <bsd.port.mk>
