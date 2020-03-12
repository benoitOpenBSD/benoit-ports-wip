# $OpenBSD$

COMMENT =	tools for encoding and decoding dumps of NAND memory chips

MODPY_EGG_VERSION =	200312
DISTNAME =	nand-dump-tools-${MODPY_EGG_VERSION}
PKGNAME =	py-${DISTNAME}

CATEGORIES =	sysutils

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

HOMEPAGE =	https://github.com/SySS-Research/nand-dump-tools

# MIT
PERMIT_PACKAGE =	Yes

GH_ACCOUNT =    SySS-Research
GH_PROJECT =    nand-dump-tools
GH_COMMIT =	b1238f645b4e529510d7e4d141a5e34b68ff4736

MODULES =	lang/python

FLAVORS =	python3
FLAVOR ?=	python3

NO_BUILD =	Yes

RUN_DEPENDS =	math/py-bchlib

do-install:
		${INSTALL_SCRIPT} ${WRKBUILD}/nand_dump_decoder.py ${PREFIX}/bin
		${INSTALL_SCRIPT} ${WRKBUILD}/nand_dump_encoder.py ${PREFIX}/bin
		${INSTALL_DATA_DIR} ${PREFIX}/share/doc/nand-dump-tools/conf
		${INSTALL_DATA} ${WRKSRC}/*.sh ${PREFIX}/share/doc/nand-dump-tools
		${INSTALL_DATA} ${WRKSRC}/images/* ${PREFIX}/share/doc/nand-dump-tools
		${INSTALL_DATA} ${WRKSRC}/conf/* ${PREFIX}/share/doc/nand-dump-tools/conf

NO_TEST =	Yes

.include <bsd.port.mk>
