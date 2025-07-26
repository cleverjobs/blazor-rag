# When Modal Window is Shown background scrolling can still happen

## Question

**Mr** asked on 10 Aug 2020

When a modal window is shown the browser can still scroll in the background. See [https://www.telerik.com/forums/how-to-globally-disabled-scrolling-when-a-modal-is-open](https://www.telerik.com/forums/how-to-globally-disabled-scrolling-when-a-modal-is-open) for something similar that was happening in the kendo components. Any guidance on a fix for the blazor component?

## Answer

**Marin Bratanov** answered on 10 Aug 2020

Hello, The <body> is not available to Blazor to modify, the entire blazor app is in the <app> element inside it. So, such disabling of the scrollbar would have to happen with JS, like in the Stocks sample app we have (click the profile at the top right). Also, to modify the <body> in a Blazor way, it would have to be fully within our components, which it cannot be. Another thing to consider is that the element that actually scrolls can vary greatly with different layouts - it could be the <body>, it could be <app>, or it could be some element specific to the particular application layout and structure (which can even change from one page to the next). Thus, the Window cannot know which element to touch in order to disable its scrollbar. This is the major reason why our oldest modal popup, the RadWindow for ASP.NET WebForms does not disable scrollbars automatically either. So, the solution is to remove the scrollbar with your own code when and as desired, here's an example of that app: when the window is shown, remove the scrollbar by setting the DOM element overflow property ( line link and js function ) when it is closed, restore the scrollbar in the same fashion ( line link ) Regards, Marin Bratanov

### Response

**Mr Chas** answered on 10 Aug 2020

Thank you!
