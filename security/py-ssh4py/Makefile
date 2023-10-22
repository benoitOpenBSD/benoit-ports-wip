
COMMENT =		ssh4Py is a LibSSH2 Wrapper (SSH, SCP, SFTP).

MODPY_EGG_VERSION =	0.6.9
DISTNAME =		ssh4py-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}

CATEGORIES =		security

HOMEPAGE =		http://www.keyphrene.com/products/4py/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# LGPL
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		crypto ssl z

SITES =			http://www.keyphrene.com/download/

EXTRACT_SUFX =		.zip

MODULES =		lang/python

LIB_DEPENDS +=		security/libssh2
LIB_DEPENDS +=		textproc/hunspell

pre-build:
			@perl -pi -e 's|%%LOCALBASE%%|${LOCALBASE}|g' ${WRKSRC}/setup_ssh4.py
			
do-build:
			@cd ${WRKSRC} && ${MAKE_ENV} \
			PYTHONPATH=${WRKINST}${MODPY_SITEPKG} ${MODPY_BIN} ./setup_ssh4.py build
#do-test: fake
#			@cd ${WRKSRC} && ${MAKE_ENV} \
#			PYTHONPATH=${WRKINST}${MODPY_SITEPKG} ${MODPY_BIN} ./test_pydes.py

.include <bsd.port.mk>
