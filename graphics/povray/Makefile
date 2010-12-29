# $OpenBSD: Makefile,v 1.12 2007/09/15 20:09:42 simon Exp $

COMMENT =			3D image rendering package

DISTNAME =			povray-3.6.1
CATEGORIES =			graphics

HOMEPAGE =			http://www.povray.org

MAINTAINER =			James Lecocq <james@heroine.cz>

PERMIT_PACKAGE_CDROM =		Perhaps we qualify for commercial distribution
PERMIT_PACKAGE_FTP =		Yes
PERMIT_DISTFILES_CDROM =	Our CDs are not too expensive, see povlegal.doc but I think we should ask them anyway
PERMIT_DISTFILES_FTP =		Yes

WANTLIB =			c m z stdc++

MASTER_SITES =			http://www.povray.org/ftp/pub/povray/Official/Unix/

LIB_DEPENDS =			graphics/png \
				graphics/jpeg \
				graphics/tiff

CONFIGURE_STYLE =       gnu
CONFIGURE_ARGS +=       --disable-optimiz
CONFIGURE_ENV +=	CPPFLAGS="-I${LOCALBASE}/include -I${LOCALBASE}/include/libpng" \
                        CFLAGS="${CFLAGS}" \
                        LDFLAGS="-L${LOCALBASE}/lib" \
                        COMPILED_BY="OpenBSD ports"

FLAVORS =			no_x11
FLAVOR ?=

.if !${FLAVOR:L:Mno_x11}
WANTLIB +=			X11 ICE SM Xpm
.else
CONFIGURE_ARGS +=		--without-x
.endif

NO_REGRESS =			Yes

do-install:
	${INSTALL_PROGRAM} ${WRKDIST}/unix/povray ${PREFIX}/bin
	${INSTALL_MAN} ${WRKDIST}/povray.1 ${PREFIX}/man/man1
	${INSTALL_DATA_DIR} ${PREFIX}/share/povray-3.6
	cp -R ${WRKDIST}/icons ${WRKDIST}/include \
	${WRKDIST}/scenes ${WRKDIST}/ini \
	${WRKDIST}/scripts ${PREFIX}/share/povray-3.6 
	chown -R ${SHAREOWN}:${SHAREGRP} ${PREFIX}/share/povray-3.6
	find ${PREFIX}/share/povray-3.6 -type d | xargs chmod ${DIRMODE}
	find ${PREFIX}/share/povray-3.6 -type f | xargs chmod ${SHAREMODE}  
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/povray-3.6
	cp -R ${WRKDIST}/doc/* ${PREFIX}/share/doc/povray-3.6

.include <bsd.port.mk>
