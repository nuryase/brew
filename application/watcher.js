let fileWatcher = require("chokidar");

function StartWatcher(path){
    var chokidar = require("chokidar");

    var watcher = chokidar.watch(path, {
        ignored: /[\/\\]\./,
        persistent: true
    });

    function onWatcherReady(){
    }
    watcher.on('change', function(path) {
        console.log('File', path, 'has been changed');
        const data = fs.readFileSync('./application/eparser/parsed_data.json');
        const jsonData = JSON.parse(data);
        let count = 0
        console.log(jsonData[count]["contents"]["1"])
        count += 1
   })
};

StartWatcher('./application/eparser/parsed_data.json')