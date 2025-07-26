# Do we need to manually Dispose Telerik components we create a hard reference to in the code section?

## Question

**Pin** asked on 30 Dec 2021

Hi, As the question states, do we need to do this? A very brief example in REPL: [https://blazorrepl.telerik.com/cPlQROaw54hvorQ145](https://blazorrepl.telerik.com/cPlQROaw54hvorQ145) Say I wanted that reference to the button (or any other Telerik Component), to do other things with elsewhere, is the dispose call necessary, or is that totally unnecessary? Thanks.

## Answer

**Marin Bratanov** answered on 30 Dec 2021

Hi, Our components handle their own disposing to free resources and if you have a reference to such a disposed component somewhere it will likely become null (which should be done by the framework) so you may want to consider checking for that. That said, I would caution against using references in the first place, the better approach in Blazor is to use the view-model fields, and fields in the component reference are not to be used to make modifications or to obtain information. Thus, I would strongly advise you reconsider the need for that reference - very few components expose methods that you'd need to call and most are typically short lived - such as setting or getting state or focusing. Regards, Marin Bratanov

### Response

**Pingu** commented on 31 Dec 2021

Hi Marin, Thanks for the response. The example I gave wasn't the best, I am not referencing a button anywhere and don't have loads of these, but there are places where in the Telerik docs it shows using these references, and that is where I am also. For example with TelerikGrids to persist state, I am calling Grid.SetState(...), the same thing with TelerikTileLayout (SetState), on TelerikDrawer calling ToggleAsync(), etc. (These are all shown with examples creating references in the docs) So when I have these references due to me needing to call SetState, ToggleAsync etc, there is no need for me to dispose these references then? Thanks.

### Response

**Marin Bratanov** commented on 01 Jan 2022

The framework should do that for you - when a component disposes its reference in memory should be null, and you should just have some null reference checks when using it.
