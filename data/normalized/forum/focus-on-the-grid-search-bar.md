# focus on the grid search bar

## Question

**Kla** asked on 08 Apr 2021

Hi,
Is it possible to set the keyboard input focus on the grid search bar as soon as I load the entire page? Thanks.

## Answer

**Marin Bratanov** answered on 08 Apr 2021

Hi Klayton, You can focus it with plain JS, if you add a function similar to this one, you can call it in OnAfterRenderAsync by passing a correct selector: function focusElement ( selector ) { var elem=document.querySelector(selector); if (elem && elem.focus) { setTimeout ( function ( ) {
elem.focus();
}, 30 );
}
} Regards, Marin Bratanov Progress Telerik

### Response

**Klayton** answered on 08 Apr 2021

Sorry for my ignorance. But if I have three grids on a page, how do I reference which grid search bar I want to focus on? Thanks

### Response

**Marin Bratanov** answered on 09 Apr 2021

Hello Klayton, You can use any approach you like - n-th of type selectors, a Class on the individual grid to cascade through, or other identifiers in your structure that you can cascade selectors through. It is entirely up to your project logic to decide how to get the reference to the thing you want to alter. Regards, Marin Bratanov
