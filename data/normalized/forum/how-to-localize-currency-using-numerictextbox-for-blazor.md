# How to localize currency using numerictextbox for blazor

## Question

**EdEd** asked on 29 Jun 2022

I need to be able to display currency formatted to the users locale. My app is hosted on a machine in the U.S. but the users are in the UK. I need to have £ for the UK and $ for the U.S. A point in the right directly would be great! Thanks ... Ed

## Answer

**Svetoslav Dimitrov** answered on 04 Jul 2022

Hello Ed, There are two different approaches you can take to achieve the desired behavior: You can implement a Globalization dropdown in your application like in our Globalization demos. If you change the language from the DropDown you will see that the currency denominator will change accordingly. Use a WASM application. The server-side Blazor application takes the current culture of the server that hosts the application. So if you host the application in the US, the currency sign will be USD ($). If you are using a WASM application, it will automatically take the culture from the client's machine and apply the correct currency sign. Let me know if this helps you move forward. Regards, Svetoslav Dimitrov Progress Telerik
