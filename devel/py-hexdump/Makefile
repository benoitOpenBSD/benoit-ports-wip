
COMMENT =		dump binary data to hex format and restore from there

MODPY_EGG_VERSION = 	3.3
DISTNAME =		hexdump-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}
CATEGORIES =		devel

HOMEPAGE =		https://bitbucket.org/techtonik/hexdump/src/default/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE =	Yes

EXTRACT_SUFX =		.zip

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes
MODPY_PI =		Yes

FLAVORS =		python3
FLAVOR =		python3

WRKDIST =		${WRKDIR}

do-install:
			cd ${WRKSRC} && ${MODPY_BIN} ${WRKSRC}/setup.py \
				install --prefix=$(PREFIX)

NO_TEST =		Yes

.include <bsd.port.mk>
