// Dosyanin uygun bir yerine ekle:
#ifdef ENABLE_MOKOKO_SYSTEM
#include "mokoko.h"
#endif


// int SECTREE_MANAGER::Build(const char * c_pszListFileName, const char* c_pszMapBasePath) icinde:
// Ara:
			regen_load(szFilename, setting.iIndex, setting.iBaseX, setting.iBaseY);
			snprintf(szFilename, sizeof(szFilename), "%s/%s/stone.txt", c_pszMapBasePath, szMapName);
			regen_load(szFilename, setting.iIndex, setting.iBaseX, setting.iBaseY);

// Altina ekle:
#ifdef ENABLE_MOKOKO_SYSTEM
			Mokoko_SpawnMap(setting.iIndex, setting.iBaseX, setting.iBaseY);
#endif

