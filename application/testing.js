
function getContents(filename, filepath) {
    const spawn = require("child_process").spawn;

    let contents = spawn('python',["./application/eparser/app.py", filename, filepath]);
    contents.stdout.on('data', data => console.log('data: ', data.toString()))
    contents.on('close', () => {
        console.log('test')
    })
    return data
}