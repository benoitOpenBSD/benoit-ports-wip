COMMENT =		research tool for SSH implementations

MODGO_MODNAME =		github.com/runZeroInc/sshamble
MODGO_VERSION =		v0.0.0-20240808164406-5ae73e8775fc

#MODGO_VERSION =	v20240808
#V =			v20240808
#GH_ACCOUNT =		runZeroInc
#GH_PROJECT =		sshamble
#GH_COMMIT =		5ae73e8775fc94a739a020060d057d76a345af18

DISTNAME =		sshamble-${MODGO_VERSION}
PKGNAME =		sshamble-0.0.0pl20240808

CATEGORIES =		security

HOMEPAGE =		https://SSHamble.com/

# BSD
PERMIT_PACKAGE =	Yes

WANTLIB += c pthread

MODULES =		lang/go
MODGO_TYPE =		bin

NO_TEST =		Yes

.include "modules.inc"

.include <bsd.port.mk>
