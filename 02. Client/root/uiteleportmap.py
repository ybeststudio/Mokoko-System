# Ara:
import teleportData
import uiDungeonTrack

# Altina ekle:
if app.ENABLE_MOKOKO_SYSTEM:
	import uiMokokoRewards


# Ara:
PREVIEW_MARKER = "d:/ymir work/ui/minimap/mini_waypoint%02d.sub"
PREVIEW_MARKER_SIZE = 30

# Altina ekle:
MOKOKO_TOTAL = 530
MOKOKO_COUNTER_BG = "ikashop/lite/business/counter.png"


# TeleportMapPage.Destroy icinde ara:
	def Destroy(self):

# Altina ekle:
		if app.ENABLE_MOKOKO_SYSTEM:
			uiMokokoRewards.RemoveListener(self.RefreshMokoko)


# TeleportMapPage.__Build icinde ara:
			self.prevButton.Hide()
			self.nextButton.Hide()

# Altina ekle:
		self.mokokoButton = self.__Button(556, 5, "btn_mokako")
		self.mokokoText = ui.TextLine()
		self.mokokoText.SetParent(self)
		self.mokokoText.SetPosition(630, 15)
		self.mokokoText.SetHorizontalAlignCenter()
		self.mokokoText.SetText(localeInfo.MOKOKO_TOTAL_PROGRESS.format(0, MOKOKO_TOTAL))
		self.mokokoText.Show()
		self.keep.append(self.mokokoText)
		if app.ENABLE_MOKOKO_SYSTEM:
			self.mokokoButton.SetEvent(ui.__mem_func__(self.__OpenMokokoRewards))
			self.mokokoCounterBg = self.__Image(self.mokokoButton, MOKOKO_COUNTER_BG, 26, -3)
			self.mokokoCounterText = ui.TextLine()
			self.mokokoCounterText.SetParent(self.mokokoCounterBg)
			self.mokokoCounterText.SetPosition(10, 3)
			self.mokokoCounterText.SetHorizontalAlignCenter()
			self.mokokoCounterText.Show()
			self.keep.append(self.mokokoCounterText)
			self.mokokoCounterBg.Hide()
			uiMokokoRewards.AddListener(self.RefreshMokoko)
			self.RefreshMokoko()


# TeleportMapPage icine ekle:
	if app.ENABLE_MOKOKO_SYSTEM:
		def __OpenMokokoRewards(self):
			uiMokokoRewards.Open()

		def RefreshMokoko(self):
			state = uiMokokoRewards.STATE
			if state.pending > 0:
				self.mokokoText.SetText(localeInfo.MOKOKO_TOTAL_PROGRESS_AVAILABLE.format(state.found, state.total, state.pending))
				self.mokokoCounterText.SetText(str(state.pending) if state.pending < 100 else "99+")
				self.mokokoCounterBg.Show()
			else:
				self.mokokoText.SetText(localeInfo.MOKOKO_TOTAL_PROGRESS.format(state.found, state.total))
				self.mokokoCounterBg.Hide()
			if self.hoverRegion and self.hoverRegion in self.regions:
				self.__ShowToolTip(self.regions[self.hoverRegion][1])


# TeleportMapPage.__ShowToolTip icinde ara:
		self.toolTip.AutoAppendTextLine(MapName(region["id"]), TOOLTIP_TITLE_COLOR)
		color = TOOLTIP_TEXT_COLOR if player.GetStatus(player.LEVEL) >= region["level"] else TOOLTIP_LOCKED_COLOR

# Altina ekle:
		self.toolTip.AutoAppendTextLine(localeInfo.MOKOKO_MAP_REQUIRED_LEVEL.format(region["level"]), color)
		if app.ENABLE_MOKOKO_SYSTEM and region["id"] in uiMokokoRewards.STATE.regions:
			(found, total) = uiMokokoRewards.STATE.regions[region["id"]]
			self.toolTip.AutoAppendTextLine(localeInfo.MOKOKO_MAP_PROGRESS.format(found, total), TOOLTIP_TEXT_COLOR)


# TeleportMapPage.Show icinde ara:
	def Show(self):
		ui.Window.Show(self)

# Altina ekle:
		if app.ENABLE_MOKOKO_SYSTEM:
			uiMokokoRewards.RequestInfo()

