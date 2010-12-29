# $OpenBSD$

COMMENT =		client for Cisco's AnyConnect SSL VPN

DISTNAME =		openconnect-2.26

CATEGORIES =		net

HOMEPAGE =		http://www.infradead.org/openconnect.html

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB +=		c crypto m ssl z iconv xml2

VPNCSCRIPT =		vpnc-script:0

MASTER_SITES =		ftp://ftp.infradead.org/pub/openconnect/
MASTER_SITES0 =		http://git.infradead.org/users/dwmw2/vpnc-scripts.git/blob_plain/HEAD:/

DISTFILES =		${DISTNAME}${EXTRACT_SUFX} ${VPNCSCRIPT}
EXTRACT_ONLY =		${DISTNAME}${EXTRACT_SUFX}
EXTRACT_SUFX =		.tar.gz

LIB_DEPENDS =		converters/libiconv \
			textproc/libxml
USE_GMAKE =		Yes

NO_REGRESS =		Yes

ALL_TARGET =		openconnect

post-extract:
	cp ${FULLDISTDIR}/vpnc-script ${WRKSRC}/

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/openconnect ${PREFIX}/bin
	${INSTALL_DATA_DIR} ${PREFIX}/share/examples/openconnect
	${INSTALL_DATA} ${WRKSRC}/vpnc-script ${PREFIX}/share/examples/openconnect/

.include <bsd.port.mk>
