# GameWindow.Close icinde ara:
			advanced_options_runtime.SetGame(None)
		self.Hide()

# Altina ekle:
		if app.ENABLE_MOKOKO_SYSTEM:
			import uiMokokoRewards
			uiMokokoRewards.Destroy()


# GameWindow icinde ara:
		def __DamageTraceEnd(self, request, displayed, hpLoss):
			self.targetBoard.OnDamageTraceEnd(int(request), int(displayed), int(hpLoss))

# Altina ekle:
	if app.ENABLE_MOKOKO_SYSTEM:
		def __EnergyCrystalMsg(self, key):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GetText(key, key))
			self.__EnergyCrystalRefresh()

		def __EnergyCrystalRate(self, rate):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.ENERGY_CRYSTAL_RATE_RESULT.format(int(rate) / 10.0))
			self.__EnergyCrystalRefresh()

		def __EnergyCrystalRefine(self, success, grade):
			text = localeInfo.ENERGY_CRYSTAL_REFINE_SUCCESS if int(success) else localeInfo.ENERGY_CRYSTAL_REFINE_FAIL
			chat.AppendChat(chat.CHAT_TYPE_INFO, text.format(int(grade)))
			self.__EnergyCrystalRefresh()

		def __EnergyCrystalBonus(self, data):
			bonus = []
			for part in data.split("|"):
				fields = part.split(",")
				if len(fields) == 3:
					bonus.append((int(fields[0]), int(fields[1]), int(fields[2])))
			constInfo.ENERGY_CRYSTAL_BONUS = bonus
			constInfo.ENERGY_CRYSTAL_GAINS = [(a, g) for (a, g, u) in bonus if u]
			self.__EnergyCrystalRefresh()

		def __EnergyCrystalRefresh(self):
			wnd = self.interface and self.interface.wndEnergyCrystal
			if wnd and wnd.IsShow():
				wnd.Refresh()

		def __MokokoData(self, found, total, pending, regions = ""):
			import uiMokokoRewards
			uiMokokoRewards.OnData(found, total, pending, regions)

		def __MokokoFound(self, found, total, region, regionFound, regionTotal, pending = "0"):
			import uiMokokoRewards
			uiMokokoRewards.OnFound(found, total, region, regionFound, regionTotal, pending)
			if self.interface and self.interface.wndShopSoldNotice:
				self.interface.wndShopSoldNotice.ShowMessage("icon/emoji/mokoko.png", localeInfo.MOKOKO_FOUND_NOTIFICATION)

		def __MokokoRewardsBegin(self, found, total):
			import uiMokokoRewards
			uiMokokoRewards.OnRewardsBegin(found, total)

		def __MokokoRewardEntry(self, rewardID, rewardType, required, claimed, items = ""):
			import uiMokokoRewards
			uiMokokoRewards.OnRewardEntry(rewardID, rewardType, required, claimed, items)

		def __MokokoRewardsEnd(self, pending):
			import uiMokokoRewards
			uiMokokoRewards.OnRewardsEnd(pending)

		def __MokokoRewardResult(self, result, rewardID):
			import uiMokokoRewards
			uiMokokoRewards.OnRewardResult(result, rewardID)


# GameWindow.__ServerCommand_Build icinde ara:
			serverCommandList["DamageTraceRow"] = self.__DamageTraceRow
			serverCommandList["DamageTraceEnd"] = self.__DamageTraceEnd

# Altina ekle:
		if app.ENABLE_MOKOKO_SYSTEM:
			serverCommandList["MokokoData"] = self.__MokokoData
			serverCommandList["MokokoFound"] = self.__MokokoFound
			if app.ENABLE_ENERGY_CRYSTAL:
				serverCommandList["EnergyCrystalMsg"] = self.__EnergyCrystalMsg
				serverCommandList["EnergyCrystalRate"] = self.__EnergyCrystalRate
				serverCommandList["EnergyCrystalRefine"] = self.__EnergyCrystalRefine
				serverCommandList["EnergyCrystalBonus"] = self.__EnergyCrystalBonus
			serverCommandList["MokokoRewardsBegin"] = self.__MokokoRewardsBegin
			serverCommandList["MokokoRewardEntry"] = self.__MokokoRewardEntry
			serverCommandList["MokokoRewardsEnd"] = self.__MokokoRewardsEnd
			serverCommandList["MokokoRewardResult"] = self.__MokokoRewardResult

