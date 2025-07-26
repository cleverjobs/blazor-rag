# MDI layout with Telerik UI for Blazor

## Question

**Zwa** asked on 05 May 2022

Hi, About to start modernizing an old desktop application and moving it to web. Due to change management with operators we are not allowed to make significant changes to UI layout etc. Therefore we must keep the MDI layout of the pages. What components and layout would you suggest for this task? A Menu in the top and TelerikWindow's? It should be possible to open many windows BR Ulrik

## Answer

**Marin Bratanov** answered on 07 May 2022

Hi Ulrik, The Window component is like any other component - you can declare as many as you want on the page. If needed, you can generate them with a @foreach loop (e.g., have a descriptor model to iterate over). Probably the same model can be used for a collection of toggle button components to indicate which windows one can open and which are open (hence, the toggle button over a regular button). You could use other components for this, or even relatively plain HTML, whatever matches your design. Of course, you could also build a menu whose clicks you can handle to open the windows. If you do implement such an interface, I'd encourage you to share your sample in this repo (fork it, then do a pull request, or simply send the sample to us with a note to put it in the repo, and with appropriate attribution text). We award such contributions to the community with Telerik points that you can use towards a renewal discount, for example. Regards, Marin Bratanov Progress Telerik

### Response

**ZwapSharp** commented on 10 May 2022

Great thanks. Have done that and polishing it of to an initial user presentation. But! How to avoid the windows overlapping the TelerikMenu (see screen shot)? (Probably simple answer) ...and how to avoid a maximized TelerikWindow to cover the menu in the top part? BR Ulrik

### Response

**ZwapSharp** commented on 10 May 2022

PS: MainLayout looks like this: (using DynamicComponent inside my Window component to fill contents) Havent changed Teleriklayout

### Response

**Marin Bratanov** commented on 11 May 2022

The best idea I can offer is to wrap the menu in a div with sufficiently high z-index (I think a maximized window had a very high one, inspect its rendered markup to make sure, and add at least 1000 as focusing one increases the z-index).

### Response

**ZwapSharp** commented on 12 May 2022

Hi Marin, Thanks for the tip. The menu drop downs now shows over windows, but the menu itself is still behind windows. I made a <div> around the <TelerikMenu> and set the z-index to a huge number.

### Response

**Marin Bratanov** commented on 12 May 2022

The Window renders very high in the DOM - where the TelerikRootComponent is, and it is likely that some other nodes between there and where the main element of the menu renders have some other z-index order. You may need to inspect the rendering to see what renders where and where the z-index needs to be set. Note that you need to be careful not to put everything above the window.

### Response

**ZwapSharp** commented on 18 May 2022

Hi again, The optimal solution for us would be if the TelerikWindow could stay inside the green box and never overlap or move over the blue and orange boxes. I have tried but without success to accomplish this. If I maximize the TelerikWindow, it maximixes under the menu and the action buttons are inaccessible. The Menu, MenuItems and Footer has very high z-indexes. Best regards Ulrik

### Response

**Tsvetomir** commented on 23 May 2022

Hi, Ulrik, we do have a Feature Request on our

### Response

**ZwapSharp** commented on 23 May 2022

Thanks. I have upvoted and implemented the left/top check and it works!

### Response

**Tsvetomir** commented on 26 May 2022

I am happy to hear that the workaround has been helpful to your case. Indeed, I have updated the feedback item so that it targets the implementation of a restriction zone for the window instead of only restricting it within the viewport. This way, users will be able to supply any HTML element within which the window should be locked.
