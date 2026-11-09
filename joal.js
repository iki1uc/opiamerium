if(/^(javascript|vbscript):/i.test(url.protocol))add('bad','Gefährliches Schema: '+url.protocol,50);
else if(url.protocol==='data:'){
  const mime=url.pathname.split(';')[0].split(',')[0];
  if(/^(text\/html|application\/javascript|text\/javascript)/i.test(mime))add('bad','data:-URI mit HTML/JS – führt Code aus',50);
  else if(mime.startsWith('image/')||mime.startsWith('audio/')||mime.startsWith('video/'))add('warn','data:-URI mit Medien – meist harmlos, aber inline',5);
  else add('warn','data:-URI ungeklärter Art',15);
}
