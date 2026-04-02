const fs = require('fs');
const path = require('path');

const FRONTEND_DIR = path.join(__dirname, 'src');

const COLOR_MAP = {
    "#6B2D3E": "#50768C",
    "#522231": "#3B596A",
    "#8B4A5C": "#E09F7D",
    "#B8907A": "#8D7A6A",
    "#F2E0E5": "#FAEBE3",
    "#E0C5CE": "#F0CDBA",
    "#EBD3DA": "#F2D8C9",
    "#E8D9CB": "#DBCBB4",
    "#D9C4B1": "#CBB69C",
    "#3A3530": "#423838",
    "#4A3040": "#423838",
    "#FAF5EF": "#F5EBE1",
    "#F0E6D8": "#EBDCCA"
};

function replaceInFile(filepath) {
    let content = fs.readFileSync(filepath, 'utf8');

    for (const [oldVal, newVal] of Object.entries(COLOR_MAP)) {
        content = content.replace(new RegExp(oldVal, 'gi'), newVal);
    }
    content = content.replace(/Murta Menu/gi, "Coffee Beans");
    content = content.replace(/Murta/gi, "Coffee Beans");

    fs.writeFileSync(filepath, content, 'utf8');
}

function processDirectory(directory) {
    const files = fs.readdirSync(directory);
    for (const file of files) {
        const fullPath = path.join(directory, file);
        if (fs.statSync(fullPath).isDirectory()) {
            processDirectory(fullPath);
        } else if (fullPath.endsWith('.jsx') || fullPath.endsWith('.js') || fullPath.endsWith('.css')) {
            console.log("Modifying", fullPath);
            replaceInFile(fullPath);
        }
    }
}

processDirectory(FRONTEND_DIR);
console.log("Done");
