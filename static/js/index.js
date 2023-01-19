const desktopTrigger = document.getElementById('desktop-mode-trigger')
const mobileTrigger = document.getElementById('mobile-mode-trigger')
const layout = document.getElementById('content-table')

let currentMode = "desktop"

desktopTrigger.onclick = () => toggleMode("desktop")
mobileTrigger.onclick = () => toggleMode("mobile")

function toggleMode(mode) {
  if(currentMode == mode) return;
  
  layout.style.width = mode == "desktop" ? "600px" : "360px"
  currentMode = mode
  toggleMediaQuery(mode)
}

function toggleMediaQuery(mode) {
  const mobileStyles = document.getElementById('mobile-css')

  mobileStyles.setAttribute('media', mode == "desktop" ? "(max-width: 360px)" : "all")
}