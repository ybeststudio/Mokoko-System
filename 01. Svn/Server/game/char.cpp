// Ara:
	using namespace std;

// Altina ekle:
#ifdef ENABLE_MOKOKO_SYSTEM
#include "mokoko.h"
#endif


// void CHARACTER::Destroy() icinde:
// Ara:
	if (IsPC())
		Wardrobe_OnDestroy(this);

// Altina ekle:
#ifdef ENABLE_MOKOKO_SYSTEM
	if (IsPC())
		Mokoko_OnDestroy(this);
#endif


// void CHARACTER::EncodeInsertPacket(LPENTITY entity) icinde:
// Ara:
	if (!(d = entity->GetDesc()))
		return;
	LPCHARACTER ch = (LPCHARACTER) entity;

// Altina ekle:
#ifdef ENABLE_MOKOKO_SYSTEM
	if (Mokoko_IsHiddenFor(this, ch))
		return;
#endif


// void CHARACTER::OnClick(LPCHARACTER pkChrCauser) icinde:
// Ara:
	}
	DWORD vid = GetVID();
	sys_log(0, "OnClick %s[vnum %d ServerUniqueID %d, pid %d] by %s", GetName(), GetRaceNum(), vid, GetPlayerID(), pkChrCauser->GetName());

// Altina ekle:
#ifdef ENABLE_MOKOKO_SYSTEM
	if (Mokoko_OnClick(pkChrCauser, this))
		return;
#endif

