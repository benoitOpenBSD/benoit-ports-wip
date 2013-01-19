# $OpenBSD$

COMMENT =		module for using fake objects (mocks and stubs) to test real ones

MODPY_EGG_VERSION =	1.0.3
DISTNAME =		fudge-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}

CATEGORIES =		devel

HOMEPAGE =		http://farmdev.com/projects/fudge/

# MIT
PERMIT_PACKAGE_CDROM =		Yes
PERMIT_PACKAGE_FTP =		Yes
PERMIT_DISTFILES_CDROM =	Yes
PERMIT_DISTFILES_FTP =		Yes

MASTER_SITES=		${MASTER_SITE_PYPI:=f/fudge/}

MODULES =		lang/python

MODPY_SETUPTOOLS =	Yes
NO_REGRESS =		Yes

# XXX: need tox http://pypi.python.org/pypi/tox/
#do-regress: fake
#			@cd ${WRKSRC} && PYTHONPATH=${WRKINST}${MODPY_SITEPKG} \
#			./run_tests.sh

.include <bsd.port.mk>
