# $OpenBSD$

COMMENT =	ESP32 Firmware Image to ELF

MODPY_EGG_VERSION =	20200301
DISTNAME =	esp32_image_parser-${MODPY_EGG_VERSION}
PKGNAME =	py-${DISTNAME}

CATEGORIES =	sysutils

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE =	Yes

GH_ACCOUNT =    tenable
GH_PROJECT =    esp32_image_parser
GH_COMMIT =	0c9ff48d56c8e1e65ba93213400b4d469b84c8ce

MODULES =	lang/python

FLAVORS =	python3
FLAVOR =	python3

RUN_DEPENDS =	devel/py-esptool${MODPY_FLAVOR} \
		devel/py-hexdump${MODPY_FLAVOR} \
		devel/py-makeelf${MODPY_FLAVOR}

NO_BUILD =	Yes

NO_TEST =	Yes

do-install:
		${INSTALL_SCRIPT} ${WRKBUILD}/esp32_image_parser.py ${PREFIX}/bin
                
.include <bsd.port.mk>
