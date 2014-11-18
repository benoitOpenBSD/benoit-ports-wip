# $OpenBSD: Makefile,v 1.22 2010/12/03 11:45:43 ajacoutot Exp $

COMMENT=	extension for unparsed raw whois information

DISTNAME=	Net-Whois-Raw-2.31
CATEGORIES=	net

# perl
PERMIT_PACKAGE_CDROM=   Yes

MODULES=		cpan

CONFIGURE_STYLE=	modbuild

BUILD_DEPENDS=		${RUN_DEPENDS}
RUN_DEPENDS=		www/p5-URI \
			www/p5-libwww \
			converters/p5-Net-IDN-Encode

TEST_IS_INTERACTIVE	= Yes

.include <bsd.port.mk>
