# $OpenBSD$

COMMENT =	network time synchronization software

DISTNAME=	ntimed-0.0.2015.01.12
CATEGORIES=	net
HOMEPAGE=	https://github.com/bsdphk/Ntimed

MAINTAINER=	Christian Weisgerber <naddy@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM=	Yes

GH_ACCOUNT=	bsdphk
GH_PROJECT=	Ntimed
GH_COMMIT=	3da3e4bde33cf3eafe2158f358a47cbdd69e2c98

WANTLIB =	c m

CONFIGURE_STYLE=simple

MAKE_ENV=	NOMAN=noman \
		BINDIR=${PREFIX}/sbin

pre-configure:
	@chmod +x ${WRKSRC}/${CONFIGURE_SCRIPT}

NO_TEST=	Yes

.include <bsd.port.mk>
