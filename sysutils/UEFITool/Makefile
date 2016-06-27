# $OpenBSD$

COMMENT =		UEFI firmware image viewer and editor

V =			0.12.0
PKGNAME =		UEFITool-${V}
DISTNAME =		UE.$V
CATEGORIES =		sysutils

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/LongSoft/UEFITool

GH_ACCOUNT =		LongSoft
GH_PROJECT =		UEFITool

WRKDIST =		${WRKDIR}/${GH_PROJECT}-${DISTNAME}

WANTLIB +=		c m pthread stdc++ freetype
WANTLIB +=		ICE QtGui SM X11 Xext Xi Xinerama Xrender fontconfig

MODULES =		x11/qt4 devel/qmake

CONFIGURE_STYLE =       qmake
MODQMAKE_PROJECTS =     UEFITool/uefitool.pro

NO_TEST =		Yes

do-install:
		${INSTALL_PROGRAM} ${WRKBUILD}/UEFITool/UEFITool ${PREFIX}/bin

.include <bsd.port.mk>
