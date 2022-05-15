import { ipcRenderer } from 'electron'

// background 中把环境隔离设置为false eg: contextIsolation： false
window.isClient = true
window.ipcRenderer = ipcRenderer
