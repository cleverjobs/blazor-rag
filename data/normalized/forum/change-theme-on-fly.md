# Change theme on fly

## Question

**And** asked on 05 Sep 2019

Hello Marin I learn article about themes support and I use it [https://docs.telerik.com/blazor-ui/themes](https://docs.telerik.com/blazor-ui/themes) Also I was create own theme by your theme builder. It's work fine. But i want to change themes as in your blazor demo site by select from dropdown list and change theme immediatelly. Can you explain me short and right way how to do this. Thank you.

## Answer

**Marin Bratanov** answered on 05 Sep 2019

Hi Andriy, You can inspect the theme manager code from our demos to see how we did this in the demos (you have the demos project in the zip or msi packages). Basically, JS code is called to change the <link> element with a new one, and it gets recognized by an id attribute from its markup. The old element must, of course, be removed. Here's the abridged version of the code changeCss: function ( cssFileUrl ) { var oldLink=document.getElementById( "kendoCss" ); if (cssFileUrl===oldLink.getAttribute( "href" )) { return;
} var newLink=document.createElement( "link" );
newLink.setAttribute( "id", "kendoCss" );
newLink.setAttribute( "rel", "stylesheet" );
newLink.setAttribute( "type", "text/css" );
newLink.setAttribute( "href", cssFileUrl);
newLink.onload=()=> {
oldLink.parentElement.removeChild(oldLink);
}; document.getElementsByTagName( "head" )[ 0 ].appendChild(newLink);
} Regards, Marin Bratanov

### Response

**Andriy** answered on 05 Sep 2019

Thank you, very much! All works fine.
