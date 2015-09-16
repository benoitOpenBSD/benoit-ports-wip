# $RuOBSD: Makefile,v 1.3 2002/04/10 05:14:52 form Exp $
# $OpenBSD: Makefile,v 1.44 2015/08/25 13:18:25 sthen Exp $

COMMENT=		Joe's Own Editor

DISTNAME =		joe-4.1
CATEGORIES=		editors
MASTER_SITES=		${MASTER_SITE_SOURCEFORGE:=joe-editor/}

HOMEPAGE=		http://joe-editor.sourceforge.net/

# GPLv2 only
PERMIT_PACKAGE_CDROM=	Yes

WANTLIB=		c ncurses m util

CONFIGURE_STYLE=	gnu

FAKE_FLAGS=	sysconf_joedir=${PREFIX}/share/examples/joe \
		sysconf_docdir=${PREFIX}/share/doc/joe

post-install:
		${INSTALL_PROGRAM} ${WRKSRC}/joe/util/stringify ${PREFIX}/bin/
		${INSTALL_PROGRAM} ${WRKSRC}/joe/util/termidx ${PREFIX}/bin/
		${INSTALL_PROGRAM} ${WRKSRC}/joe/util/uniproc ${PREFIX}/bin/

.include <bsd.port.mk>
