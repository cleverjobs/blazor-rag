# Cascading parameter on a razor component inside a Telerik window control - not getting a value set

## Question

**Mar** asked on 28 Nov 2019

Here is my situation -- I have a number of nested controls and I have a cascading value that encompasses all the controls. When I put one of my nested components inside a Telerik window then the cascading parameter on said component does not work (it gets value of null). If I move my component just outside the Telerik window and nothing else -- then the parameter gets the correct value. Is this a bug? Does the parameter not get a value in the control because the window's "visible property" is false initially which maybe prevents the property from being set properly?

## Answer

**Marin Bratanov** answered on 28 Nov 2019

Hello Mark, Could you take a look at the following KB articles and see whether they help: [https://docs.telerik.com/blazor-ui/knowledge-base/window-does-not-update-parent](https://docs.telerik.com/blazor-ui/knowledge-base/window-does-not-update-parent) [https://docs.telerik.com/blazor-ui/knowledge-base/window-in-form-edit-context](https://docs.telerik.com/blazor-ui/knowledge-base/window-in-form-edit-context) If not, could you post a simple example of the problem you are facing so I can investigate and avoid guessing? You could base it on the snippets from the KB if it will be easier for you. Regards, Marin Bratanov

### Response

**Mark** answered on 28 Nov 2019

I don't think either of the above is relevant to the situation. I created a sample project based on the Telerik templates and recreated the issue. Is there somewhere I can upload a .zip file? It looks like I can only attach an image here.

### Response

**Marin Bratanov** answered on 29 Nov 2019

Hello Mark, A snippet similar to the KB should be 50ish lines and you can paste it here. To attach entire projects, you can open a private support ticket. Regards, Marin Bratanov

### Response

**Mark** answered on 29 Nov 2019

I submitted a ticket.

### Response

**Marin Bratanov** answered on 02 Dec 2019

Thank you for the sample, Mark. It helped a lot. Here's the KB with the pertinent information for anyone else having a similar problem: [https://docs.telerik.com/blazor-ui/knowledge-base/window-cascading-parameter-null.](https://docs.telerik.com/blazor-ui/knowledge-base/window-cascading-parameter-null.) Regards, Marin Bratanov

### Response

**Mark** answered on 02 Dec 2019

Thanks Marin. That totally makes sense now. Cheers Mark
