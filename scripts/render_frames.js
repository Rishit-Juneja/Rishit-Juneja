const fs = require('fs');
const els = {};
function mkEl(id){ const el = { id, textContent:"", value:"", style:{}, classList:{add(){},remove(){},toggle(){},contains:()=>false}, appendChild(){}, onclick:null, oninput:null, onchange:null, dataset:{}, addEventListener(){} }; if(id==="selMode") el.value="auto"; return el; }
const document = { createElement:t=>mkEl(t), createTextNode:t=>({textContent:t}), createDocumentFragment:()=>({appendChild(){}}), addEventListener(){}, body:{classList:{add(){},remove(){},toggle(){}},appendChild(){},removeChild(){}}, getElementById:id=>els[id]||(els[id]=mkEl(id)), fullscreenElement:null, execCommand:()=>true };
const window = { addEventListener(){}, innerWidth: 1000 };
const navigator = { clipboard: { writeText: () => Promise.resolve() } };
global.document=document; global.window=window; global.navigator=navigator;
global.requestAnimationFrame=()=>0; global.URL={createObjectURL:()=>"x",revokeObjectURL(){}}; global.Blob=class{}; global.setInterval=()=>0;
const SRC = fs.readFileSync('/home/dangerking8x/ascii-generator/index.html','utf8');
const boot = SRC.match(/<script>([\s\S]*?)<\/script>/)[1];
const test = `
size = 60; cur.seed = 1337; for (const k in ctxCache) delete ctxCache[k];
const frames = [];
function snap(ms) {
  const grid = g.map(r => r.join(""));
  frames.push({ mode: cur.mode, grid });
}
cur.charset = "classic"; cur.mode = "plasma";
for (let f = 0; f < 14; f++) { t = 0.5 + f * 0.35; draw(); snap(); }
cur.mode = "vortex";
for (let f = 0; f < 14; f++) { t = 0.5 + f * 0.3; draw(); snap(); }
cur.mode = "fire";
for (let f = 0; f < 14; f++) { t = 0.5 + f * 0.4; draw(); snap(); }
fs.writeFileSync("/tmp/ghprofile/frames.json", JSON.stringify(frames));
console.log("frames:", frames.length, "grid:", frames[0].grid.length + "x" + frames[0].grid[0].length, "size=" + size, "h=" + Math.max(12, Math.round(size * 0.42)));
`;
global.fs = fs;
eval(boot + "\n" + test);
