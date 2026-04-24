// Navigation Logic
document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        // Remove active class from all buttons and sections
        document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.cipher-section').forEach(s => s.classList.remove('active'));
        
        // Add active class to clicked button and target section
        btn.classList.add('active');
        document.getElementById(btn.dataset.target).classList.add('active');
    });
});

// Caesar Cipher Logic
function processCaesar(decrypt) {
    const text = document.getElementById('caesar-text').value;
    let shift = parseInt(document.getElementById('caesar-shift').value);
    
    if (isNaN(shift)) {
        alert('Please enter a valid shift number.');
        return;
    }

    if (decrypt) {
        shift = -shift;
    }

    let result = '';
    for (let i = 0; i < text.length; i++) {
        let char = text[i];
        if (char.match(/[a-z]/i)) {
            let code = text.charCodeAt(i);
            // Uppercase letters
            if (code >= 65 && code <= 90) {
                char = String.fromCharCode(((code - 65 + shift) % 26 + 26) % 26 + 65);
            }
            // Lowercase letters
            else if (code >= 97 && code <= 122) {
                char = String.fromCharCode(((code - 97 + shift) % 26 + 26) % 26 + 97);
            }
        }
        result += char;
    }
    
    document.getElementById('caesar-output').innerText = result || '...';
}

// Vigenère Cipher Logic
function processVigenere(decrypt) {
    const text = document.getElementById('vigenere-text').value.toUpperCase();
    let keyword = document.getElementById('vigenere-key').value.toUpperCase().replace(/[^A-Z]/g, '');
    
    if (!text || !keyword) {
        alert('Please enter both text and a keyword.');
        return;
    }

    let result = '';
    let j = 0;
    
    for (let i = 0; i < text.length; i++) {
        let char = text[i];
        if (char.match(/[A-Z]/)) {
            let shift = keyword[j % keyword.length].charCodeAt(0) - 65;
            if (decrypt) shift = -shift;
            
            let code = text.charCodeAt(i);
            result += String.fromCharCode(((code - 65 + shift) % 26 + 26) % 26 + 65);
            j++;
        } else {
            result += char;
        }
    }

    document.getElementById('vigenere-output').innerText = result || '...';
}

// Playfair Cipher Logic
function createPlayfairMatrix(keyword) {
    keyword = keyword.toLowerCase().replace(/j/g, 'i').replace(/[^a-z]/g, '');
    const alphabet = 'abcdefghiklmnopqrstuvwxyz'; // 'j' is omitted
    const matrix = [];
    const used = new Set();
    
    for (let char of keyword) {
        if (!used.has(char)) {
            used.add(char);
            matrix.push(char);
        }
    }
    for (let char of alphabet) {
        if (!used.has(char)) {
            used.add(char);
            matrix.push(char);
        }
    }
    
    const grid = [];
    for(let i=0; i<5; i++){
        grid.push(matrix.slice(i*5, i*5+5));
    }
    return grid;
}

function findPositionPlayfair(char, grid) {
    for (let r = 0; r < 5; r++) {
        for (let c = 0; c < 5; c++) {
            if (grid[r][c] === char) return [r, c];
        }
    }
    return [-1, -1];
}

function processPlayfair(decrypt) {
    let text = document.getElementById('playfair-text').value.toLowerCase().replace(/j/g, 'i').replace(/[^a-z]/g, '');
    const keyword = document.getElementById('playfair-key').value;
    
    if (!text || !keyword) {
        alert('Please enter both text and a keyword.');
        return;
    }

    const grid = createPlayfairMatrix(keyword);
    
    let pairs = [];
    let i = 0;
    while (i < text.length) {
        if (i === text.length - 1 || text[i] === text[i+1]) {
            pairs.push(text[i] + 'x');
            i++;
        } else {
            pairs.push(text[i] + text[i+1]);
            i += 2;
        }
    }

    let result = '';
    const shift = decrypt ? -1 : 1;

    for (let pair of pairs) {
        const [r1, c1] = findPositionPlayfair(pair[0], grid);
        const [r2, c2] = findPositionPlayfair(pair[1], grid);
        
        if (r1 === r2) {
            result += grid[r1][(c1 + shift + 5) % 5];
            result += grid[r2][(c2 + shift + 5) % 5];
        } else if (c1 === c2) {
            result += grid[(r1 + shift + 5) % 5][c1];
            result += grid[(r2 + shift + 5) % 5][c2];
        } else {
            result += grid[r1][c2];
            result += grid[r2][c1];
        }
    }

    if (decrypt) result = result.replace(/x/g, ''); // Crude way, but matches typical simple implementation
    
    document.getElementById('playfair-output').innerText = result.toUpperCase() || '...';
}

// Rail Fence Cipher Logic
function processRailFence(decrypt) {
    const text = document.getElementById('railfence-text').value;
    const rails = parseInt(document.getElementById('railfence-rails').value);
    
    if (!text || isNaN(rails) || rails < 2) {
        alert('Please enter text and a valid number of rails (>= 2).');
        return;
    }

    if (rails >= text.length) {
        document.getElementById('railfence-output').innerText = text;
        return;
    }

    let result = '';
    
    if (!decrypt) {
        const fence = Array.from({ length: rails }, () => []);
        let dirDown = false;
        let row = 0;
        
        for (let i = 0; i < text.length; i++) {
            if (row === 0 || row === rails - 1) dirDown = !dirDown;
            fence[row].push(text[i]);
            row += dirDown ? 1 : -1;
        }
        
        result = fence.flat().join('');
    } else {
        const fence = Array.from({ length: rails }, () => Array(text.length).fill(null));
        let dirDown = false;
        let row = 0;
        
        for (let i = 0; i < text.length; i++) {
            if (row === 0) dirDown = true;
            if (row === rails - 1) dirDown = false;
            fence[row][i] = '*';
            row += dirDown ? 1 : -1;
        }
        
        let index = 0;
        for (let i = 0; i < rails; i++) {
            for (let j = 0; j < text.length; j++) {
                if (fence[i][j] === '*' && index < text.length) {
                    fence[i][j] = text[index++];
                }
            }
        }
        
        row = 0;
        dirDown = false;
        for (let i = 0; i < text.length; i++) {
            if (row === 0) dirDown = true;
            if (row === rails - 1) dirDown = false;
            if (fence[row][i] !== null) result += fence[row][i];
            row += dirDown ? 1 : -1;
        }
    }

    document.getElementById('railfence-output').innerText = result || '...';
}
