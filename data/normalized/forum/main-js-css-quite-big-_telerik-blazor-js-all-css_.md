# main js & css quite big (telerik-blazor.js & all.css)

## Question

**Ale** asked on 23 Nov 2020

can the lazy loading be implementing to load just components with are on the page?

## Answer

**Lachezar Georgiev** answered on 24 Nov 2020

Hi Aleksandr, Telerik UI for Blazor Lazy Loading As of version 2.19.0, we support lazy loading. Our documentation includes a great sample project that you can clone and experiment with. If you follow that approach in your project, the components which are on the page will be loaded lazily. CSS As for the slow CSS load, are you loading the CSS file statically or via a CDN? When using the CDN approach, sometimes if the internet connection is slow, the download form the CDN could potentially be slowed down as well. Further steps If the issue persists, could you send me a sample project that I can inspect and debug? Regards, Lachezar Georgiev

### Response

**Aleksandr** answered on 24 Nov 2020

i mean css loads normally, but the size of file can be smaller if we will have ability to load styles just for the components which are in use (on the page) currently, are you going to switch to isolated css in future?

### Response

**Lachezar Georgiev** answered on 25 Nov 2020

Hi Aleksandr, CSS isolation To make sure we are on the same page, In the context of Blazor, CSS isolation refers to preventing dependencies on global styles and avoiding styling conflicts among components and libraries, as documented in the official Blazor docs. If you are experiencing an issue with this feature of Blazor, check out this article in our documentation - CSS Isolation does not work for Telerik components. CSS Bundling If I am understanding correctly, what you are referring to, is called CSS bundling as described in the official Blazor docs. Our built-in themes is bundled in a single .css file which is well below 1 megabyte. Is that the size of the file you are referring to? In order for our components to work, the whole theme file must be downloaded by the browser (if you are using Client side - WebAssembly blazor project). There is no way to load just parts of it. If you use very few components, you could build a custom theme that contains the bare minimum for them. Regards, Lachezar Georgiev
