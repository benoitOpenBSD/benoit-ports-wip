# $OpenBSD$

COMMENT =	Simple library to encode/decode DNS wire-format packets

MODPY_EGG_VERSION =	0.9.3
DISTNAME =		dnslib-${MODPY_EGG_VERSION}
PKGNAME =		py-dnslib-${MODPY_EGG_VERSION}
CATEGORIES =   		net

HOMEPAGE =		https://bitbucket.org/paulc/dnslib

# BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=d/dnslib/}

MODULES =		lang/python

pre-configure:
	@perl -pi -e 's,python,${MODPY_BIN},g' ${WRKDIST}/run_tests.sh

do-test:
	cd ${WRKSRC} && ./run_tests.sh

.include <bsd.port.mk>
