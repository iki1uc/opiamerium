if(/^(javascript|vbscript):/i.test(url.protocol)) add('bad','Gefährliches Schema: '+url.protocol,50);
else if(url.protocol==='data:'){
  const mime=(url.pathname.split(';')[0]||'').toLowerCase();
  if(/^(text\/html|application\/javascript|text\/javascript)/.test(mime))
    add('bad','data:-URI führt Code aus: '+mime,50);
  else if(/^(image|audio|video)\//.test(mime))
    add('warn','data:-URI (Medium, inline)',5);
  else add('warn','data:-URI ungeklärter Art',15);
}
