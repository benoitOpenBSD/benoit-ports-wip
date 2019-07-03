# $OpenBSD: Makefile,v 1.5 2017/06/02 23:17:08 schwarze Exp $

COMMENT=	newlib for arm-none-eabi cross-development

DISTNAME=	newlib-2.4.0
VERSION=	2.4.0
PKGNAME=	${CONFIG}-newlib-nano-${VERSION}

MAKE_ENV+=	${CONFIGURE_ENV}

HOMEPAGE=	http://sourceware.org/newlib/

MASTER_SITES=	ftp://sourceware.org/pub/newlib/
#MASTER_SITES=	ftp://sources.redhat.com/pub/newlib/

EXTRACT_SUFX=	.tar.gz

BUILD_DEPENDS=	devel/arm-none-eabi/binutils \
		${RUN_DEPENDS}
RUN_DEPENDS=	devel/arm-none-eabi/gcc-linaro

# cope with user settings in /etc/mk.conf
MAKE_FLAGS=	CFLAGS="-I${LOCALBASE}/include"
USE_GMAKE=	Yes
CONFIGURE_ARGS+=--enable-interwork \
		--enable-multilib \
		--enable-newlib-reent-small \
		--disable-newlib-fvwrite-in-streamio \
		--disable-newlib-fseek-optimization \
		--disable-newlib-wide-orient \
		--enable-newlib-nano-malloc \
		--disable-newlib-unbuf-stream-opt \
		--enable-lite-exit \
		--enable-newlib-global-atexit \
		--enable-newlib-nano-formatted-io \
		--disable-newlib-supplied-syscalls \
		--enable-newlib-global-stdio-streams \
		--enable-newlib-retargetable-locking

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/arm-none-eabi/newlib-nano
	${INSTALL_DATA} ${WRKDIST}/COPYING.NEWLIB \
		${PREFIX}/share/doc/arm-none-eabi/newlib-nano

.include <bsd.port.mk>
