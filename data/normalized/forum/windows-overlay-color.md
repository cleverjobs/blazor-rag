# Windows overlay color

## Question

**Nik** asked on 10 Jan 2022

Hello, Is there a way to change the color or opacity of the k-overlay class, without overwriting the class? I have a scenario where I would like the color to be transparent, but keep it black in other scenarios. Regards, Nikolas

## Answer

**Marin Bratanov** answered on 10 Jan 2022

Hello Nikolas, CSS is the only way. You can consider adding a class to the <body> element (or similar very high-level element) to cascade your styles through only when needed. Perhaps using JS Interop for that is going to perform better as you won't have to re-render a lot, and you have easier access to high-level elements that way. Just make sure to remove it once the window closes in the VisibleChanged event. Regards, Marin Bratanov
