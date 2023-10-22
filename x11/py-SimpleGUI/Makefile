
COMMENT =		python GUIs for humans

DISTNAME =		PySimpleGUI-4.33.0
CATEGORIES =		x11
PKGNAME =		py-SimpleGUI-4.33.0

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# LGPLv3+
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/PySimpleGUI/PySimpleGUI

SITES =			${SITE_PYPI:=P/PySimpleGUI/}

WANTLIB +=		${MODPY_WANTLIB}

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes

FLAVORS =		python3
FLAVOR  =		python3

RUN_DEPENDS =		${MODPY_TKINTER_DEPENDS}

DEBUG_PACKAGES =	${BUILD_PACKAGES}

NO_TEST =		Yes
	

.include <bsd.port.mk>
