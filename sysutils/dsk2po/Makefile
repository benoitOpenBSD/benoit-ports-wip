
COMMENT =	convert Apple II/III DSK images to ProDOS orderer images

DISTNAME =	dsk2po-20210503
CATEGORIES =	sysutils

HOMEPAGE =	https://github.com/paulhagstrom/dsk2po

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Public
PERMIT_PACKAGE =	Yes

MODULES =		lang/python

GH_ACCOUNT =		paulhagstrom
GH_PROJECT =		dsk2po
GH_COMMIT =		2f199f601c0764a5eb9f646d325b88ff2d64fb5e

FLAVORS =		python3
FLAVOR =		python3

NO_BUILD =		Yes
NO_TEST =		Yes

do-install:
		${INSTALL_PROGRAM} ${WRKBUILD}/dsk2po.py ${PREFIX}/bin
		${INSTALL_PROGRAM} ${WRKBUILD}/po2dsk.py ${PREFIX}/bin
		
.include <bsd.port.mk>
