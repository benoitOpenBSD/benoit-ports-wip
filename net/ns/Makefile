# $OpenBSD: Makefile,v 1.31 2007/11/17 20:39:03 steven Exp $
# $FreeBSD: ports/net/ns/Makefile,v 1.3 1999/11/28 18:31:26 steve Exp $

COMMENT=	UCB/LBNL Network Simulator Version 2

DISTNAME=	ns-2.34-RC1
CATEGORIES=	net

HOMEPAGE=	http://nsnam.isi.edu/nsnam/index.php/Main_Page

# BSD
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes

WANTLIB=	X11 c m pcap stdc++ tcl84 tk84

MASTER_SITES=	${MASTER_SITE_SOURCEFORGE:=nsnam/}

BUILD_DEPENDS=	devel/tclcl>=1.0b13p0
LIB_DEPENDS=	lang/otcl

USE_GROFF =	Yes
CONFIGURE_STYLE=gnu
CONFIGURE_ARGS=	--with-tcl-ver=8.4 --with-tk-ver=8.4 \
		--x-includes=${X11BASE}/include \
		--x-libraries=${X11BASE}/lib \
		--with-tcl=${LOCALBASE}

pre-configure:
	@perl -pi -e 's,!!X11BASE!!,${X11BASE},' ${WRKSRC}/Makefile.in

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/ns ${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/ns.1 ${PREFIX}/man/man1
	${INSTALL_DATA_DIR} ${PREFIX}/share/examples/ns2
	${INSTALL_DATA} ${WRKSRC}/tcl/ex/*.tcl ${PREFIX}/share/examples/ns2

do-regress:
	cd ${WRKSRC} && ./validate

.include <bsd.port.mk>
