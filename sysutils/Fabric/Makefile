# $OpenBSD$

COMMENT =		Pythonic tool for remote execution and deployment.

MODPY_EGG_VERSION =	1.8.1
DISTNAME =		Fabric-${MODPY_EGG_VERSION}
CATEGORIES =		sysutils

HOMEPAGE =		http://www.fabfile.org/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=F/Fabric/}

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes

BUILD_DEPENDS =		${RUN_DEPENDS}
RUN_DEPENDS =		security/py-paramiko

TEST_DEPENDS =		devel/py-nose \
			devel/py-fudge

#NO_TEST =		Yes

do-test:
			@cd ${WRKSRC}/tests && PYTHONPATH=${WRKINST}${MODPY_SITEPKG} \
			${MODPY_BIN} ./test_main.py

.include <bsd.port.mk>
