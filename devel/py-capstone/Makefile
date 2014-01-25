# $OpenBSD$

COMMENT =		Python API for dealing capstone disassembly engine

MODPY_EGG_VERSION =	2.0
DISTNAME =		capstone-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}
DIST_SUBDIR =		py-capstone
CATEGORIES =		devel

HOMEPAGE =		http://www.capstone-engine.org/
MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=c/capstone/}

MODULES =		lang/python

NO_TEST =		Yes

BUILD_DEPENDS =		devel/capstone

.include <bsd.port.mk>
