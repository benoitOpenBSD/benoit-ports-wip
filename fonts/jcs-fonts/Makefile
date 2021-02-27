# $OpenBSD$

COMMENT=		proper web fonts

DISTNAME=		jcs-webfonts-1.0
CATEGORIES=		fonts

MAINTAINER=		jcs@jcs.org

PERMIT_PACKAGE =	nope

MASTER_SITES=		http://jcs.org/tmp/

NO_BUILD=		Yes
NO_TEST=		Yes
PKG_ARCH=		*

INST_DIR=		${PREFIX}/lib/X11/fonts/jcs-webfonts

do-install:
	${INSTALL_DATA_DIR} ${INST_DIR}
	cp -r ${WRKSRC}/* ${INST_DIR}/

.include <bsd.port.mk>
