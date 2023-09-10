// Handles the file input (Library [+] button) and obtains the filename and path.
//let file;
//let filename;
//let filepath;
const fs = require('fs');

document.getElementById('file-upload').addEventListener('change', function(e) {
    if (e.target.files[0]) {

      file = e.target.files[0].name;
      //console.log(file)
      fname = file.substring(0, file.lastIndexOf('.'))
      //console.log(filename)
      path = e.target.files[0].path;
      console.log(fname, path)
      //console.log(filepath)
      //bookJsonData = JSON.stringify(bookData);
      const data = fs.readFileSync('./application/eparser/data.json');
      const jsonData = JSON.parse(data);
      //console.log(jsonData)
      if (jsonData.length === 0) {
        jsonData.push({
          filename: fname,
          filepath: path,
          contents: "replace"
        });
        fs.writeFileSync('./application/eparser/data.json', JSON.stringify(jsonData, null, 2));
        //document.body.append('You selected ' + e.target.files[0].name);
        document.getElementById('selected-file').innerHTML = 'You selected ' + e.target.files[0].name
      }
      else {
        let exists = false;
        for (let i = 0; i < jsonData.length; i++) {
          let obj = jsonData[i];
          if (Object.values(obj).includes(fname)) {
            //document.body.append(e.target.files[0].name + ' already exists in library.');
            document.getElementById('selected-file').innerHTML = e.target.files[0].name + ' already exists in library.'
            exists = true
            break
          }      

      }
      if (exists === false) {
      jsonData.push({
        filename: fname,
        filepath: path,
        contents: "replace"
      });

      fs.writeFileSync('./application/eparser/data.json', JSON.stringify(jsonData, null, 2));
      //document.body.append('You selected ' + e.target.files[0].name);
      document.getElementById('selected-file').innerHTML = 'You selected ' + e.target.files[0].name
    }
      }
    }
    
  });
            





