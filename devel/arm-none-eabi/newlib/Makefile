# $OpenBSD: Makefile,v 1.7 2011/11/01 19:22:24 naddy Exp $

COMMENT=	newlib for arm-none-eabi cross-development

VERSION=	2.1.0
DISTNAME=	newlib-${VERSION}
# BROKEN-amd64 =	as: unrecognized option -mfpu=softfpa

HOMEPAGE=	https://sourceware.org/newlib/

MASTER_SITES=	ftp://sources.redhat.com/pub/newlib/

EXTRACT_SUFX=	.tar.gz

BUILD_DEPENDS=	devel/arm-none-eabi/binutils \
		${RUN_DEPENDS}
RUN_DEPENDS=	devel/arm-none-eabi/gcc

# cope with user settings in /etc/mk.conf
MAKE_FLAGS=	CFLAGS="-I${LOCALBASE}/include"
USE_GMAKE=	Yes
USE_GROFF=	No
CONFIGURE_ARGS+=--enable-interwork \
		--enable-multilib

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/newlib
	${INSTALL_DATA} ${WRKDIST}/COPYING.NEWLIB \
		${PREFIX}/share/doc/newlib

.include <bsd.port.mk>
