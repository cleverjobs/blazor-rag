# Any way to set height and width of signature to be relative to screen size?

## Question

**Dou** asked on 17 Nov 2022

If I use anything other than pixels (or if I don't set it at all) I get an error. My app will be running on a cell phone or tablet which could be in portrait or landscape orientation so setting the size in pixels doesn't work very well.

## Answer

**Dimo** answered on 21 Nov 2022

Hi Doug, The Signature component uses a drawing <canvas>. Alas, relative sizes with automatic HTML element resizing are not supported (we tried to handle them initially, but hit unwanted side effects). As a possible workaround, you can use our MediaQuery component to handle device orientation and screen changes. Regards, Dimo

### Response

**Doug** commented on 24 Nov 2022

Dimo, Thanks for the response. This works to some extent, at least in the sense that I can get the signature to resize even if I would have to create lots of media query components to cover lots of different screen widths, but more importantly, as soon as you change the size of the signature, the line (signature) you draw with the cursor doesn't follow where the cursor is. It will be ahead or behind where you're attempting to draw. I recreated this in your signature demo page. Change the width of the signature component in dev tools and then draw a line and you'll see what I mean. Is this a bug or is there a way to get around this?

### Response

**Dimo** commented on 25 Nov 2022

You are right, Doug, thanks for reporting this! It's a bug and I logged it on your behalf in our public portal, together with the workaround.
