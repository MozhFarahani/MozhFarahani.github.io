(function(){
  // project filters
  var btns=document.querySelectorAll('.filters button'),items=document.querySelectorAll('#projlist .proj');
  btns.forEach(function(b){b.addEventListener('click',function(){
    btns.forEach(function(o){o.setAttribute('aria-pressed',o===b?'true':'false')});
    var f=b.dataset.f;items.forEach(function(it){it.hidden=!(f==='all'||it.dataset.tags.split(' ').indexOf(f)>-1)});
  })});

  // copy email
  var c=document.getElementById('copy'),m=document.getElementById('mail');
  if(c&&m)c.addEventListener('click',function(){
    function sel(){var r=document.createRange();r.selectNodeContents(m);var s=getSelection();s.removeAllRanges();s.addRange(r);c.textContent='Selected, press Ctrl+C';}
    try{navigator.clipboard.writeText(m.textContent).then(function(){c.textContent='Copied';setTimeout(function(){c.textContent='Copy email'},1600)},sel);}catch(e){sel();}
  });

  // active section in index
  var links=document.querySelectorAll('.index nav a');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){
      links.forEach(function(a){a.classList.toggle('on',a.getAttribute('href')==='#'+e.target.id)});}})},{rootMargin:'-30% 0px -60% 0px'});
    document.querySelectorAll('main section').forEach(function(s){io.observe(s)});
  }
})();
