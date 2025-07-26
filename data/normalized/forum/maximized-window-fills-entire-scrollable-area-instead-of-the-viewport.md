# Maximized window fills entire scrollable area instead of the viewport

## Question

**Gre** asked on 09 Apr 2021

I have a scrollable page that includes logic to show a Telerik window control. I have the window height set by default to 600px and I have included the default maximize action. The content of the Window may or may not be scrollable as well. When I maximize the window control it fills the entire scrollable area rather than just the current visible area. Any thoughts on what I might be doing wrong or if this is how the control is supposed to work? Thanks, Greg

## Answer

**Nadezhda Tacheva** answered on 14 Apr 2021

Hi Greg, In order to be able to provide a solution that will best match you case, I just want to double check if I correctly understand the behavior you are trying to achieve. As per your current setup, when you maximize the Window, it expands and fills up the whole scroll area. The desired scenario is when the Window is maximized it should fill just the visible part of the view port. If the above described is correct, could you please test the attached sample project and let me know if it matches your expectation? Thank you in advance! I'll be looking forward to receiving your response. Regards, Nadezhda Tacheva

### Response

**Greg** answered on 21 Apr 2021

Hi Nadezhda, Sorry it has taken me so long to get back to you. I have tested the attached project and it is working the way I would expect. Please let me know the next steps so that I can get my code working like yours. Thanks, Greg

### Response

**Nadezhda Tacheva** answered on 26 Apr 2021

Hi Greg, I'm glad to find out the project I sent matched your expectations. As a next step I would recommend to compare it against your application to see if any differences might be causing the behavior you are getting. If this does not help, you can send us a runnable reproduction, so we can investigate further and provide a solution. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Greg** answered on 26 Apr 2021

Hi Nadezhda, I'm having some issues creating a reproduction. I can't find anything in my CSS that would cause the problem. One thing that I have noticed is that in the example you send the Window HTML is being "injected" into the page outside of the "page" div and mine is inside the "page" and "content" divs. I've attached screenshots of both. I believe this is what is causing the different behaviours that we are seeing, but I am at a loss to explain why. In my application the Window is in a component that is inside several other components (I am dynamically building a form for the user to enter) so that is one explanation, but I have created a new page in your sample that has the Window embedded in a component that is inside 3 other components and it works fine. Can you explain how the Window component is detecting where it should inject the HTML code? That may help shed some light on what is going on here. Thanks, Greg

### Response

**Svetoslav Dimitrov** answered on 29 Apr 2021

Hello Greg, I would like to suggest some solutions that might hopefully help you move forward and solve the issue you are facing. The Telerik popup and modal components are rendered in the HTML with the help of the TelerikRootComponent. It allows those components, one of which is the Telerik Window, to detect the correct rendering place. In this regard, the TelerikRootComponent should wrap the Body. You should inspect the following: Under the Shared folder, there should be a TelerikLayout.razor file which contains: @inherits LayoutComponentBase <TelerikRootComponent> @Body </TelerikRootComponent> In the MainLayout.razor file the TelerikLayout should be included like so: @layout TelerikLayout @inherits LayoutComponentBase <div class="page"> <div class="sidebar"> <NavMenu /> </div> <div class="main"> <div class="top-row px-4"> <a href="[https://docs.microsoft.com/en-us/aspnet/"](https://docs.microsoft.com/en-us/aspnet/") target="_blank"> About </a> </div> <div class="content px-4" style="margin:auto;"> @Body </div> </div> </div> Another solution might be to set the width and height for the high-level HTML elements such as html, body, .page, and .main to fit the viewport height. In our public GitHub repository, we have a project that showcases the concept, you can extend it and modify it to match the needs of your application. Can you get back to me if either of those solutions solved the issue? Regards, Svetoslav Dimitrov

### Response

**Greg** answered on 29 Apr 2021

Hi Svetoslav, The first solution that you gave does help indeed. I had the TelerikRootComponent wrapping the body in my main layout rather than having it in a separate component. What I am finding now however is that if I am scrolled down in a page and I open a Window it displays properly, but when I maximize the window it shows it at the top of the page and I have to scroll up to see it. I have attached images that hopefully show it more clearly. Any thoughts on what might be causing that? Thanks, Greg

### Response

**Greg** answered on 29 Apr 2021

Hi again Svetoslav, I did some testing with the WindowTest sample that Nadezhda sent me previously and I was able to recreate the issue. I've attached the updated solution. It seems to be related to the Modal parameter. When Modal is off and you open the Window the page automatically scrolls to the top so when you maximize the Window it is positioned so that you can see it (In my case I would rather it keep the current scroll position so the user does lose their place). When Modal is on and you open the Window the page keeps its current scroll position and shows the Window centered on the page, but when you maximize the Window it displays at the top and you have to scroll up to see it instead of just filling the current viewport. In the attached solution, I've added a second button after the 2000 pixel tall div that opens the Window with the Modal parameter set to true so if you click the second "Toggle Window" button you should see the behaviour that I'm talking about. Hope this helps, Greg

### Response

**Marin Bratanov** answered on 30 Apr 2021

Hi Greg, Have you had a chance to try the CSS from t he sample my colleague Svetoslav linked? <style> /* set all top-level elements in the layout to height 100% so they match the viewport */ html, body,.page,.main { height: 100%; min-height: 100%; max-height: 100%; overflow: hidden;
} /* define where scrollbars can appear in the layout -
in a child element whose actual height
still matches the viewport*/.main { overflow: auto;
}
</style> What this does for the layout both projects use is that it stops the html from getting a scrollbar, the .main element will have that now. So, the parent element of the window will no longer be scrolled and it can match the viewport. The difference you observe stems from the different focused elements the browser has - the browser scrolls the focused element into view and whether the window is modal or not makes a difference which element that is. I have also extracted this into a new similar example project that you can find here: [https://github.com/telerik/blazor-ui/tree/master/window/block-all-content.](https://github.com/telerik/blazor-ui/tree/master/window/block-all-content.) Regards, Marin Bratanov

### Response

**Greg** commented on 30 Apr 2021

Thanks Martin, that works perfectly. One last question, is it on the roadmap to have a Maximize parameter on the Window so that the Window can open already maximized?

### Response

**Marin Bratanov** commented on 30 Apr 2021

Glad to see you moving forward, Greg. On opening maximized - this is possible from day 1 by using the State parameter of the component and setting it to Maximized: [https://docs.telerik.com/blazor-ui/components/window/size#maximize-and-minimize](https://docs.telerik.com/blazor-ui/components/window/size#maximize-and-minimize)

### Response

**Greg** commented on 30 Apr 2021

Great news, thanks again Marin!
