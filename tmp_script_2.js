

const ctx=
document
.getElementById(
'deliveryChart'
);


new Chart(

ctx,

{

type:'line',

data:{

labels:
0,

datasets:[{

label:
'Deliveries',

data:
0,

borderColor:
'#00ff90',

backgroundColor:
'rgba(0,255,140,.2)',

fill:true,

tension:.4

}]

},

options:{

plugins:{

legend:{

labels:{

color:'white'

}

}

},

scales:{

x:{

ticks:{

color:'white'

}

},

y:{

ticks:{

color:'white'

}

}

}

}

}

);

