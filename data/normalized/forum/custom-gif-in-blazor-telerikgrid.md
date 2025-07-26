# Custom GIF in Blazor TelerikGrid

## Question

**Joe** asked on 15 Nov 2023

Can you point me at example code on how to set the busy indicator in the TelerikGrid to my GIF?

## Answer

**Dimo** answered on 20 Nov 2023

Hi Joel, There are two ways to customize the Grid loading indicator: Override the Telerik theme CSS and apply your loading GIF as a background image to the Grid's internal LoaderContainer. Use a separate LoaderContainer component for the Grid. This is the recommended option and it requires: Bind the Grid with its OnRead event. This will allow you to know when each data request starts and ends. Wrap the Grid with a <div> with position:relative style. In this way, the LoaderContainer will cover only the Grid. Place a LoaderContainer with a <Template> inside the <div>. Show and hide the LoaderContainer inside the Grid OnRead handler. Be aware of possible UI thread blockage (see the note below the "Basic LoaderContainer" example). Here is an REPL example for both options. I recommend using a separate LoaderContainer, because it doesn't require knowledge of our internal HTML rendering. For the same reason, this approach is also more future-proof. Regards, Dimo Progress Telerik

### Response

**Joel** answered on 28 Nov 2023

Thanks for the REPL examples. It seems your "Built-in Grid LoaderContainer" example doesn't show the loading gif. I followed that approach on my MVC application so I need to have that approach working. I'll see if I can get it running on my app but because this is a widely available solution you may want to update it.

### Response

**Dimo** commented on 28 Nov 2023

Perhaps your comment is related to this paragraph just above the example? The Grid will not display a loading animation during its initial rendering. The component cannot know when or even if data will be provided to it. Initial automatic loading sign can either show indefinitely, or it could prevent the user from altering any saved Grid state (such as changing filters). If you want a loading animation on the initial load, you can use a LoaderContainer component. See the Grid Loading Animation Live Demo.
