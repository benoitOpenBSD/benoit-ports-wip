
COMMENT =			display dhcp lease information

DISTNAME =			dhcpstatus_0.60
PKGNAME =			${DISTNAME:S/_/-/}

CATEGORIES =			net

HOMEPAGE =			http://dhcpstatus.sourceforge.net/

# GPLv2+
PERMIT_PACKAGE_CDROM =		Yes

SITES =				${SITE_SOURCEFORGE:=dhcpstatus/}

MODULES =			perl

NO_BUILD =			Yes
NO_TEST =			Yes

PKG_ARCH =			*

post-extract:
	cd ${WRKSRC}; tar xf libraries.tar

do-install:
	cd ${WRKSRC}; \
	${INSTALL_SCRIPT_DIR} ${PREFIX}/${P5SITE}/dhcpstatus; \
	${INSTALL_DATA_DIR} ${PREFIX}/share/examples/dhcpstatus/; \
	${INSTALL_SCRIPT} dhcpstatus/*pm ${PREFIX}/${P5SITE}/dhcpstatus/; \
	${SUBST_CMD} scripts/dhcpstatus scripts/dhcpstatus.cgi; \
	${INSTALL_SCRIPT} scripts/dhcpstatus scripts/dhcpstatus.cgi \
	    ${PREFIX}/bin/; \
	${INSTALL_DATA} dhcpstatus.ini ${PREFIX}/share/examples/dhcpstatus/

.include <bsd.port.mk>
