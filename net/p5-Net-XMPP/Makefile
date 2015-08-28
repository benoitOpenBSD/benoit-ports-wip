# $OpenBSD: Makefile,v 1.8 2015/01/21 14:40:10 sthen Exp $

COMMENT=		XMPP perl library

DISTNAME =		Net-XMPP-1.05
CATEGORIES=		net

MODULES=		cpan

# LGPL v2.1
PERMIT_PACKAGE_CDROM=	Yes

CONFIGURE_STYLE=	perl modbuild

RUN_DEPENDS=		security/p5-Digest-SHA1 \
			textproc/p5-XML-Stream
TEST_DEPENDS =		devel/p5-YAML-Tiny \
			www/p5-LWP-Online

MODCPAN_EXAMPLES=	Yes

.include <bsd.port.mk>
