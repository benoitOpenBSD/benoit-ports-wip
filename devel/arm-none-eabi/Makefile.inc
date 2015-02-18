# $OpenBSD: Makefile.inc,v 1.5 2011/11/08 12:43:25 jasper Exp $

CONFIG=		arm-none-eabi
PKGNAME?=	${CONFIG}-${DISTNAME}
CATEGORIES+=	devel

# GPLv3
# For newlib: multiple copyrights, but basically BSD.
#   See: ${PREFIX}/share/doc/newlib
PERMIT_PACKAGE_CDROM=	Yes

CONFIGURE_STYLE=gnu
CONFIGURE_ARGS+=--target=arm-none-eabi	\
		--disable-shared	\
		--disable-nls		\
		--disable-werror

EXTRACT_SUFX?=	.tar.bz2
