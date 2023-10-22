
COMMENT=	UCB/LBNL Network Simulator Version 2

DISTNAME=	ns-2.34-RC1
CATEGORIES=	net

HOMEPAGE=	http://nsnam.isi.edu/nsnam/index.php/Main_Page

# BSD
PERMIT_PACKAGE_CDROM=	Yes

WANTLIB=	X11 c m pcap stdc++ tcl84 tk84

SITES =		${SITE_SOURCEFORGE:=nsnam/}

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

do-test:
	cd ${WRKSRC} && ./validate

.include <bsd.port.mk>
