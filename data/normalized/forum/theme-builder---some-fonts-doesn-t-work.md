# Theme Builder - some fonts doesn't work

## Question

**Dan** asked on 01 Feb 2023

Hi, I have some concerns with default font changing in the ThemeBuilder. Problem 1 : when i select Avenir-next, he display a yellow question mark ( missing?) and renders in Times New Roman Problem 2 : i upload the Gilroy-Medium font and i have the same result (renders in Times New Roman) . Both with Woff2 and Tiff. Can you give me some advices to overcom these problems or : as Workaround, instruct me how i ca change te default font in my Blazor Serv App Thanks

## Answer

**Yanislav** answered on 06 Feb 2023

Hello Daniel, Based on the description I understand that you want to change the font family for the whole application not only for the Telerik components. Am I correct? You have to import the font. To do this you can use CDN or save the font file locally. Then you can apply it for the <body> element to make sure the whole page will use the font: @font-face { font-family: myFirstFont; src: url ( "AvenirNextLTPro-It.otf" );
} body { font-family: myFirstFont, sans-serif;
} I hope this helps. Regards, Yanislav
