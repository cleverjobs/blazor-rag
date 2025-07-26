# Hyperlinkbutton in blazor

## Question

**Anj** asked on 02 Dec 2020

Do we have a replacement for Hyperlinkbutton in Blazor?

## Answer

**Svetoslav Dimitrov** answered on 03 Dec 2020

Hello Anju, If you are referring to the <a> tag with the href attribute you could use the NavLink from Microsoft. Alternatively, you could use our TelerikButton together with the NavigationManager to navigate to a page. The difference between the two is that the NavLink renders as <a href="google.com"></a>, whereas our renders as a <button>. This means that when you click Control + Click on the NavLink it would open the page in a new tab, whereas if you click on our button it would open the page in the same tab. Below, I have prepared a short example of both so you could compare their behavior and decide which one is more appropriate for your application. @inject NavigationManager Navigation <NavLink href="[https://www.google.bg/">](https://www.google.bg/">) Google link </NavLink> <br /> <TelerikButton OnClick="@( _=> Navigation.NavigateTo(" https: // www.google.bg /"))"> Navigation to Google </TelerikButton> Regards, Svetoslav Dimitrov
