// Dosyanin uygun bir yerine ekle:
#ifdef ENABLE_MOKOKO_SYSTEM
#include "mokoko.h"
#ifdef ENABLE_ENERGY_CRYSTAL
#include "energy_crystal.h"
#endif
#endif


// void CInputLogin::Entergame(LPDESC d, const char * data) icinde:
// Ara:
	Wardrobe_OnLogin(ch);

// Altina ekle:
#ifdef ENABLE_MOKOKO_SYSTEM
	Mokoko_OnLogin(ch);
#endif

