# DropdownList popup behind top-layer

## Question

**Fab** asked on 07 Dec 2022

We have a custom control where we host a Google Map. We created custom google map controls and placed it like google maps api requires. Everything works fine when the control is normally displayed as shown here: but when the user put the map in fullscreen mode, our dropdownlist can't be opened because the animation-container isn't placed within the hierarchy of the element hosting the map, causing the dropdownlist popup to be behind the "top-layer" element of the page. Technically the problem is that when an element is set in fullscreen mode (but this happens even for HTML dialog elements and popup), the browser create a special layer where it places these elements (and their childrens). In the case of dropdownlist, you create k-animation-container telerik-blazor elements straight under the app div, this mean that any dropdownlist (and i suppose combobox items and every component that has a "popup") can't be shown into fullscreen elements or HTML dialogs. Is it possible to explicitly set the dropdownlist animation container where I want? How can I fix this problem without recreate a dropdownlist component? Thanks

## Answer

**Dimo** answered on 09 Dec 2022

Hello Fabio, Our popups and dropdowns render as direct children of the <TelerikRootComponent>, i.e. in the <body>. As a result, they cannot show over a fullscreen element. There were some tricks in the past to achieve this, but they no longer work. The only exception with regard to rendering location is our AnimationContainer, which renders where you define it, so it can be inside the fullscreen element. So you have two options: Implement some sort of a custom dropdown with the AnimationContainer or any a similar custom popup. Use a fullscreen Window component instead of the system fullscreen feature. Regards, Dimo Progress Telerik
