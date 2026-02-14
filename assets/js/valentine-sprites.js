(function(global) {
  function buildValentineSprites(makeSprite) {
    var CHAR_SCALE = 1;

    var PP = {
      'F':'#c8956a','f':'#b07848',
      'D':'#1a1a22','d':'#2a2a33',
      'W':'#ffffff','E':'#1a1a22',
      'C':'#ff5577','h':'#ff4477',
      'R':'#7744bb','r':'#553399','S':'#9966dd',
      'K':'#e8a020',
      'A':'#6633aa','a':'#4a2288',
      'B':'#7744bb','b':'#e8a020',
      'T':'#ffcc44'
    };

    var pf1 = makeSprite([
      '.............a..............',
      '............aAa.............',
      '...........aAAAa............',
      '..........aAAAABa...........',
      '.........aAAAAABa...........',
      '........aAAAAAABBa..........',
      '.......aAAAAAAAABBa.........',
      '......bbbbbbbbbbbbbbb.......',
      '.....bbTbbbbbbbbbbTbbb......',
      '.....DDDDDDDDDDDDDDDDd......',
      '....DdDDfffffffDDDDDdDd.....',
      '....DdDfFFFFFFFFFfDDdDd.....',
      '....DdDfFEEFFFEEFFfDdDd.....',
      '....DdDfFEEFFFEEFFfDdDd.....',
      '....DdDfFEWFFFEWFFfDdDd.....',
      '....DdDfFFFFFFFFFfDDdDd.....',
      '....DdDfFFCFFFFCFfDDdDd.....',
      '....DdDDfFFFFFFFfDDDdDd.....',
      '....DdDDDfffffffDDDDdDd.....',
      '.....DdDDDDDDDDDDDDdDd......',
      '.....DdDDDDKDDDDDDDdDd......',
      '.....DdrRRRRRRRRRRrdDd......',
      '....DdrRRSRRRRRRSRRrdDd.....',
      '....DdrRRRRRRRRRRRRrdDd.....',
      '......rRRR.hh.hh.RRRr.......',
      '.....rRRRRhhhhhhhRRRRr......',
      '....rRRRRRhhhhhhhRRRRRr.....',
      '....rRRSRR.hhhhh.RRSRRr.....',
      '...rRRRRRR.hhh.RRRRRRRr.....',
      '...rRRRRRRRR.h.RRRRRRRRr....',
      '..rRRSRRRRRRRRRRRRRSRRRr....',
      '..rRRRRRRRRRRRRRRRRRRRRRr...',
      '..rRSRRRRRSRRRRSRRRRRSRRr...',
      '...rrRRRRRrrrrrrRRRRRrr.....',
      '.....rrrrr....rrrrr.........'
    ], PP);

    var pf2 = makeSprite([
      '.............a..............',
      '............aAa.............',
      '...........aAAAa............',
      '..........aAAAABa...........',
      '.........aAAAAABa...........',
      '........aAAAAAABBa..........',
      '.......aAAAAAAAABBa.........',
      '......bbbbbbbbbbbbbbb.......',
      '.....bbTbbbbbbbbbbTbbb......',
      '.....DDDDDDDDDDDDDDDDd......',
      '....DdDDfffffffDDDDDdDd.....',
      '....DdDfFFFFFFFFFfDDdDd.....',
      '....DdDfFEEFFFEEFFfDdDd.....',
      '....DdDfFEEFFFEEFFfDdDd.....',
      '....DdDfFEWFFFEWFFfDdDd.....',
      '....DdDfFFFFFFFFFfDDdDd.....',
      '....DdDfFFCFFFFCFfDDdDd.....',
      '....DdDDfFFFFFFFfDDDdDd.....',
      '....DdDDDfffffffDDDDdDd.....',
      '.....DdDDDDDDDDDDDDdDd......',
      '.....DdDDDDKDDDDDDDdDd......',
      '.....DdrRRRRRRRRRRrdDd......',
      '....DdrRRSRRRRRRSRRrdDd.....',
      '....DdrRRRRRRRRRRRRrdDd.....',
      '......rRRR.hh.hh.RRRr.......',
      '.....rRRRRhhhhhhhRRRRr......',
      '....rRRRRRhhhhhhhRRRRRr.....',
      '....rRRSRR.hhhhh.RRSRRr.....',
      '...rRRRRRR.hhh.RRRRRRRr.....',
      '...rRRRRRRRR.h.RRRRRRRRr....',
      '..rRRSRRRRRRRRRRRRRSRRRr....',
      '..rRRRRRRRRRRRRRRRRRRRRRr...',
      '..rRSRRRRRSRRRRSRRRRRSRRr...',
      '...rrRRRRrrrrrrrrRRRRrr.....',
      '......rrrr..rrrr..rr........'
    ], PP);

    var pClimb1 = makeSprite([
      '.............a..............',
      '............aAa.............',
      '...........aAAAa............',
      '..........aAAAABa...........',
      '.........aAAAAABa...........',
      '........aAAAAAABBa..........',
      '.......aAAAAAAAABBa.........',
      '......bbbbbbbbbbbbbbb.......',
      '.....bbTbbbbbbbbbbTbbb......',
      '.....DDDDDDDDDDDDDDDDd......',
      '....DdDDfffffffDDDDDdDd.....',
      '....DdDfFFFFFFFFFfDDdDd.....',
      '....DdDfFEEFFFEEFFfDdDd.....',
      '....DdDfFEEFFFEEFFfDdDd.....',
      '....DdDfFEWFFFEWFFfDdDd.....',
      '....DdDfFFFFFFFFFfDDdDd.....',
      '....DdDfFFCFFFFCFfDDdDd.....',
      '....DdDDfFFFFFFFfDDDdDd.....',
      '....DdDDDDDKDDDDDDDdDd......',
      'FF..DdrRRRRRRRRRRrdDd..FF...',
      'FFf.DdrRRSRRRRSRRrdDd.fFF...',
      'FFf...rRR.hh.hh.Rr....fFF...',
      'FF....rRRhhhhhhhRRr.....FF...',
      '.....rRRRhhhhhhhRRRr........',
      '....rRRSR.hhhhh.RRSRr.......',
      '....rRRRRR.hhh.RRRRRr.......',
      '...rRRRRRRR.h.RRRRRRRr......',
      '...rRRSRRRRRRRRRRRSRRr......',
      '..rRRRRRRRRRRRRRRRRRRRRr....',
      '..rRSRRRRRSRRRRSRRRRRSRr....',
      '...rrRRRRRrrrrrrRRRRRrr.....',
      '.....rrrrr....rrrrr.........'
    ], PP);

    var pClimb2 = makeSprite([
      '.............a..............',
      '............aAa.............',
      '...........aAAAa............',
      '..........aAAAABa...........',
      '.........aAAAAABa...........',
      '........aAAAAAABBa..........',
      '.......aAAAAAAAABBa.........',
      '......bbbbbbbbbbbbbbb.......',
      '.....bbTbbbbbbbbbbTbbb......',
      '.....DDDDDDDDDDDDDDDDd......',
      '....DdDDfffffffDDDDDdDd.....',
      '....DdDfFFFFFFFFFfDDdDd.....',
      '....DdDfFEEFFFEEFFfDdDd.....',
      '....DdDfFEEFFFEEFFfDdDd.....',
      '....DdDfFEWFFFEWFFfDdDd.....',
      '....DdDfFFFFFFFFFfDDdDd.....',
      '....DdDfFFCFFFFCFfDDdDd.....',
      '....DdDDfFFFFFFFfDDDdDd.....',
      '....DdDDDDDKDDDDDDDdDd......',
      'FF..DdrRRRRRRRRRRrdDd..FF...',
      'fFF.DdrRRSRRRRSRRrdDd.FFf...',
      'fFF...rRR.hh.hh.Rr....FFf...',
      '.FF...rRRhhhhhhhRRr.....FF...',
      '.....rRRRhhhhhhhRRRr........',
      '....rRRSR.hhhhh.RRSRr.......',
      '....rRRRRR.hhh.RRRRRr.......',
      '...rRRRRRRR.h.RRRRRRRr......',
      '...rRRSRRRRRRRRRRRSRRr......',
      '..rRRRRRRRRRRRRRRRRRRRRr....',
      '..rRSRRRRRSRRRRSRRRRRSRr....',
      '...rrRRRRRrrrrrrRRRRRrr.....',
      '.....rrrrr....rrrrr.........'
    ], PP);

    var climbFrames = [pClimb1, pClimb2];
    var playerFrames = [pf1, pf2];

    var EP = {
      'K':'#2e1518','S':'#541d22','s':'#7a2d3d',
      'G':'#a83848','g':'#cc5868',
      'P':'#ddb844','p':'#aa8833',
      'H':'#6a2828','h':'#8a4444',
      'E':'#ffffff','e':'#ffaa88',
      'L':'#4a1a1a','l':'#6a3a3a',
      'W':'#ff8866','w':'#ffbb99',
      'T':'#5a4a2a','t':'#7a6a4a',
      'M':'#1a0a0a'
    };
    var elaraSp = makeSprite([
      '..wW.Ww..............................',
      '.wWWwWWw.............................',
      '..wW.Ww..............................',
      '.KKKKKKKKKKK.........................',
      'KKSSSsssssSSSKK......................',
      'KSSssGGGGGGGssSSK....................',
      'KSSsGGGgPPPgGGGsSSK.................',
      'KSSsGGPPPgPgPPPGGsSSK...............',
      'KSSsGGPPgPPPPPgPPGGsSSK.............',
      'KSSsGgPgPgPgPgPgPgGGsSSK.hhHHh.....',
      'KSSsGGGPPPPgPPPPGGGGsSSKHhEeHh.....',
      'KSSssGGGggPPPggGGGssSSK.HhEeHh.....',
      '.KSSSsssGGGGGGsssSSSKK..HhHhHh.....',
      '..KKSSSSsssssssSSSSKKK...hHMHH.....',
      '...KTTTTTTTTTTTTTTTTK.....hHH.......',
      '...KTtTTTTTTTTTtTTTK......H.........',
      '...KTTTTTTTTTTTTTTTTK..................',
      '..KLlLLLK.......KLLLlLK...............',
      '...KLlK...........KLlK................',
      '....KK.............KK.................',
    ], EP);

    var lilacSp = makeSprite([
      '..PP.PP.',
      '.PPPLPP.',
      'PPPPPPPP',
      'PPPLPLPP',
      '.PPPPPP.',
      '..PPPP..',
      '...gG...',
      '...GG...'
    ], { 'P':'#9944cc', 'L':'#bb66ee', 'g':'#228822', 'G':'#33aa33' });

    var gooseSp = makeSprite([
      '.gGGg.',
      'gGLLGg',
      'GLLLLg',
      'GLLLGg',
      'gGLLGg',
      '.gGGg.',
      '..ss..'
    ], { 'G':'#44aa33', 'g':'#338822', 'L':'#66cc44', 's':'#225511' });

    var heartSp = makeSprite([
      '.HH..HH.',
      'HLLHHLLH',
      'HLLLLLLH',
      'HLLLLLLH',
      '.HLLLLH.',
      '..HLLH..',
      '...HH...'
    ], { 'H':'#cc2266', 'L':'#ff6699' });

    var itemSprites = [lilacSp, gooseSp, heartSp];
    var itemColors = ['#9944cc', '#44aa33', '#ff6699'];
    var itemNames = ['Anodium Petalus', 'Cathodis Essentia', 'Electrolytum Cordis'];
    var itemPickMsgs = [
      'Anodium Petalus... it crackles with positive energy.',
      'Cathodis Essentia... a catalyst that draws the truth forth.',
      'Electrolytum Cordis... the conductor of all hidden bonds.'
    ];

    var torchPal = { 'Y':'#FFD700', 'O':'#ff8800', 'R':'#ff4400', 'B':'#5a3a1a' };
    var torchF1 = makeSprite([
      '..YO',
      '.YYO',
      '.OYY',
      '..OY',
      '..BB',
      '..BB',
      '..BB',
      '..BB'
    ], torchPal);
    var torchF2 = makeSprite([
      '.OY.',
      '.OYY',
      '..YO',
      '..YO',
      '..BB',
      '..BB',
      '..BB',
      '..BB'
    ], torchPal);
    var torchFrames = [torchF1, torchF2];

    var chestPal = { 'W':'#8B6342', 'B':'#6B4522', 'G':'#FFD700', 'L':'#C9A84C' };
    var chestClosedSp = makeSprite([
      '.WWWWWWWW.',
      'WBBBBBBBBW',
      'WBBBBBBBBW',
      'WBBBGGBBBW',
      'WWWWGGWWWW',
      'WBBBBBBBBW',
      'WBBBBBBBBW',
      'WWWWWWWWWW'
    ], chestPal);

    var chestOpenSp = makeSprite([
      '.WWWWWWWW.',
      'WLLLLLLLLW',
      'WLLLLLLLLW',
      '.WWWWWWWW.',
      '.WWWWWWWW.',
      'WBBBBBBBBW',
      'WBBBBBBBBW',
      'WBBBGGBBBW',
      'WWWWGGWWWW',
      'WBBBBBBBBW',
      'WBBBBBBBBW',
      'WWWWWWWWWW'
    ], chestPal);

    var keySp = makeSprite([
      '.GGG.GGG',
      'GG...GGG',
      '.GGG....'
    ], { 'G':'#FFD700' });

    var catPal = { 'O':'#dd8833','o':'#cc7722','D':'#aa5500','W':'#ffffff','E':'#228844','N':'#ff9999','T':'#bb6611' };
    var catSp1 = makeSprite([
      '..D....D..',
      '.DOOOOOOD.',
      '.OOEWWEOO.',
      '.OOONNOOO.',
      '..OOOOOO..',
      '.OOOOOOOO.',
      '.OO.OO.OOT',
      '.DD....DD.'
    ], catPal);
    var catSp2 = makeSprite([
      '..D....D..',
      '.DOOOOOOD.',
      '.OOEWWEOO.',
      '.OOONNOOO.',
      '..OOOOOO..',
      '.OOOOOOOO.',
      '.OO.OO.OO.',
      '.D..OO..DT'
    ], catPal);

    var dogPal = { 'B':'#8a6a3a','D':'#aa8844','L':'#ccaa66','W':'#ffffff','E':'#221100','N':'#222222','T':'#cc7777','G':'#bb9955' };
    var dogSp1 = makeSprite([
      '..BB....BB..',
      '.BDDDDDDDDB.',
      '.BDDEWWEDDB.',
      '.BDDDNNDDDB.',
      '..BDDTTDDB..',
      '..BDDBBDDB..',
      '..BD.BB.DBL.',
      '..BB....BB..'
    ], dogPal);
    var dogSp2 = makeSprite([
      '..BB....BB..',
      '.BDDDDDDDDB.',
      '.BDDEWWEDDB.',
      '.BDDDNNDDDB.',
      '..BDDTTDDB..',
      '..BDDBBDDB..',
      '.BD..BB..BDL',
      '..BB....BB..'
    ], dogPal);

    var sqPal = { 'B':'#5a3218','F':'#8a5a2a','L':'#aa7a4a','W':'#ffffff','E':'#111111','T':'#7a4a1a','N':'#332211' };
    var sqSp1 = makeSprite([
      '....TT...',
      '...TLT...',
      '..BBBB...',
      '.BFELB...',
      '.BFFNB...',
      '..BFFB...',
      '..FF.FF..',
      '.FF...FF.'
    ], sqPal);
    var sqSp2 = makeSprite([
      '...TT....',
      '..TLT....',
      '..BBBB...',
      '.BFELB...',
      '.BFFNB...',
      '..BFFB...',
      '.FF...FF.',
      '..FF.FF..'
    ], sqPal);

    var turtPal = { 'S':'#336633','G':'#55aa55','L':'#77cc77','H':'#88bb44','E':'#111','B':'#664422','D':'#445533','W':'#aaddaa' };
    var turtSp1 = makeSprite([
      '..SSSSS...',
      '.SGLGGLS..',
      '.SGLGLGS..',
      'HHSSSSSHH.',
      'HHE.HH.EHH',
      '.HH....HH.'
    ], turtPal);
    var turtSp2 = makeSprite([
      '..SSSSS...',
      '.SGLGGLS..',
      '.SGLGLGS..',
      '.HHSSSSSHH',
      'HHE.HH.EHH',
      '..HH..HH..'
    ], turtPal);

    var animalTypes = [
      { sp1: catSp1, sp2: catSp2 },
      { sp1: dogSp1, sp2: dogSp2 },
      { sp1: sqSp1, sp2: sqSp2 },
      { sp1: turtSp1, sp2: turtSp2 }
    ];

    return {
      CHAR_SCALE: CHAR_SCALE,
      pf1: pf1,
      pf2: pf2,
      pClimb1: pClimb1,
      pClimb2: pClimb2,
      climbFrames: climbFrames,
      playerFrames: playerFrames,
      elaraSp: elaraSp,
      lilacSp: lilacSp,
      gooseSp: gooseSp,
      heartSp: heartSp,
      itemSprites: itemSprites,
      itemColors: itemColors,
      itemNames: itemNames,
      itemPickMsgs: itemPickMsgs,
      torchFrames: torchFrames,
      chestClosedSp: chestClosedSp,
      chestOpenSp: chestOpenSp,
      keySp: keySp,
      animalTypes: animalTypes
    };
  }

  global.buildValentineSprites = buildValentineSprites;
})(window);
