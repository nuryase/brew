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
        //icon: nativeImage.createFromDataURL(icon.default),
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
        }
        //icon: __dirname + '/assets/macos/icon.icns',
    });
    // Open devtools if in developer env
    if (devenv) {
        mainWindow.webContents.openDevTools();
    }
    // Fullscreen button with mainWindow.maximize();

    // Run watcher when application starts
    var python = require('child_process').spawn('python', ['./application/eparser/main.py']);
    
    mainWindow.loadFile('./application/index.html')

    // File Dialog --> Create Library window then setup this on a button
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

