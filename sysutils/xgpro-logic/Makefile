# $OpenBSD$

COMMENT =	commandline utility xgpro-logic

MODGO_MODNAME =	github.com/evolutional/xgpro-logic
MODGO_VERSION = v0.0.0-20210323030233-868ac3e5d6d2
GH_ACCOUNT =	evolutional
GH_PROJECT =	xgpro-logic
GH_COMMIT =	868ac3e5d6d2856713c08d1ffc5c29df5c82c2d9
DISTNAME =	xgpro-logic-${MODGO_VERSION}

CATEGORIES =	sysutils

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE= Yes

WANTLIB +=	c pthread

MODULES =	lang/go
MODGO_TYPE =	bin
	
do-build:
	cd ${WRKSRC} && ${MODGO_CMD} build ${MODGO_FLAGS} -o xgpro-logic cmd/xgpro-logic.app/main.go

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/xgpro-logic ${PREFIX}/bin
	${INSTALL_DATA_DIR} ${PREFIX}/share/examples/xgpro-logic
	${INSTALL_DATA} ${WRKSRC}/examples/* ${PREFIX}/share/examples/xgpro-logic
        
NO_TEST =	Yes

.include "modules.inc"

.include <bsd.port.mk>
