const { app, BrowserWindow, dialog, nativeImage} = require('electron')
const path = require('path')
const macOS = process.platform === 'darwin';
// Set to production when deployed

const devenv = process.env.NODE_ENV !== 'production';

const createMainWindow = () => {
    const mainWindow = new BrowserWindow(
        {
        width: devenv ? 1600 : 800,
        height: 800,
        center: true,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
        }
    });
    // Open devtools if in developer env
    if (devenv) {
        mainWindow.webContents.openDevTools();
    }

    // Run watcher when application starts
    var python = require('child_process').spawn('python', ['./application/eparser/main.py']);
    
    mainWindow.loadFile('./application/index.html')
}


app.whenReady().then(() => {
    createMainWindow()

    app.on('activate', () => {
        // If no windows are open, create a new window.
        if (BrowserWindow.getAllWindows().length === 0) {
            createMainWindow()
        }
    })
})

// Closes the app when all windows are closed (if user is NOT on macOS -- darwin)
app.on('window-all-closed', () => {
    if (!macOS) {
        app.quit()
    }
})

