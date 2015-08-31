# $OpenBSD: Makefile,v 1.43 2015/07/16 23:22:20 ajacoutot Exp $

SHARED_ONLY =	Yes

COMMENT =	module to interface with the GD graphics library

DISTNAME =	GD-2.56
CATEGORIES =	graphics

# perl
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =	c fontconfig freetype gd jpeg m png tiff vpx z

CONFIGURE_STYLE =	modbuild

LIB_DEPENDS =	graphics/gd

MODULES =	converters/libiconv \
		cpan

MODCPAN_EXAMPLES =	Yes
MODCPAN_EXAMPLES_DIST =	demos

post-install:
	cd ${PREFIX}/bin && mv bdftogd bdftogd.pl && rm -f README

.include <bsd.port.mk>
