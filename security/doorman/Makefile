
VERSION=	0.81
COMMENT=	open ports when requested by a *secret knock*
DISTNAME=	doorman-${VERSION}
CATEGORIES=	security net

HOMEPAGE=	http://doorman.sourceforge.net/

MAINTAINER=	Vlad Glagolev <stealth@sourcemage.org>

SITES=		${SITE_SOURCEFORGE:=doorman/}
EXTRACT_SUFX=	.tgz

# GPL
PERMIT_PACKAGE_CDROM=	Yes

CONFIGURE_STYLE=gnu

WANTLIB=	c pcap

BUILD_DEPENDS=	sysutils/lsof

FAKE_FLAGS=	sysconfdir=${PREFIX}/share/examples

.include <bsd.port.mk>
