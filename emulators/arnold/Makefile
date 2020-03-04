# $OpenBSD$

COMMENT =		amstrad CPC, amstrad CPC+ and KC Compact emulator

DISTNAME =		arnsrc27012002
PKGNAME =		arnold-20020127
CATEGORIES =		emulators

HOMEPAGE =		http://arnold.emuunlim.com/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		c X11 Xext Xi m pthread

MASTER_SITES =		http://arnold.emuunlim.com/download/ \
			https://www.arcane-labs.net/download/OpenBSD/
			
EXTRACT_SUFX =		.zip

SHAREDIR =		${PREFIX}/share/arnold
MAKE_ENV +=		SHAREDIR=${SHAREDIR}

USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	${CONFIGURE_SHARED} \
			--with-x11
CONFIGURE_ENV =		CPPFLAGS="${CPPFLAGS} -I${LOCALBASE}/include -I${X11BASE}/include" \
			LDFLAGS="${LDFLAGS} -L${LOCALBASE}/libs -L${X11BASE}/lib"

NO_TEST =		Yes

WRKDIST =		${WRKDIR}/arnold
WRKSRC =		${WRKDIR}/arnold/src

ALL_TARGET =		arnold

pre-configure:
		chmod +x ${WRKDIR}/arnold/src/configure

do-install:
		${INSTALL_PROGRAM} ${WRKDIST}/arnold ${PREFIX}/bin
		${INSTALL_DATA_DIR} ${PREFIX}/share/arnold/roms
.for r in amsdose cpc464e cpc6128e cpc664e cpcplus kcc
	${INSTALL_DATA_DIR} ${PREFIX}/share/arnold/roms/${r}
	${INSTALL_DATA} ${WRKDIST}/roms/${r}/* ${PREFIX}/share/arnold/roms/${r}
.endfor
		${INSTALL_DATA_DIR} ${PREFIX}/share/doc/arnold
		${INSTALL_DATA} ${WRKSRC}/readme.* ${PREFIX}/share/doc/arnold
		${INSTALL_DATA} ${WRKDIST}/docs/*.txt ${PREFIX}/share/doc/arnold
                                          		
.include <bsd.port.mk>
