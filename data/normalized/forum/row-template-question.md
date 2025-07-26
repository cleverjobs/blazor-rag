# row template question

## Question

**Ran** asked on 30 Nov 2019

Hi, How can I translate the following markup into a row template? Thanks ... Ed <GridCommandColumn Width="300px"> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true">Update</GridCommandButton> <GridCommandButton OnClick="@((args)=> SelectDashboardModel(args.Item as DashboardModel))" Icon="edit">Edit</GridCommandButton> <GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true">Cancel</GridCommandButton> </GridCommandColumn>

## Answer

**Marin Bratanov** answered on 02 Dec 2019

Hello Ed, This needs to be implemented in order for something like this to become possible: [https://feedback.telerik.com/blazor/1422740-conditional-command-buttons-shown-on-condition-based-on-model-values-and-or-invoking-cud-operations-programmatically.](https://feedback.telerik.com/blazor/1422740-conditional-command-buttons-shown-on-condition-based-on-model-values-and-or-invoking-cud-operations-programmatically.) I must also note that at this point I can't say whether it will suffice, though. There is a general problem with the InCell and InLine edit modes - we don't have the cells to put our editors in, so we could not possibly do that. Perhaps the PopUp mode would work, though, it's early to say. Generally, when using a row template, one needs to implement all features the grid offers there. For example, use a generic button that toggles a flag in the model and shows a second set of markup instead - that allows editing. Regards, Marin Bratanov

### Response

**Randy Hompesch** answered on 02 Dec 2019

Ahh, the joys of being at the leading... ahem ... bleeding edge! Thanks, I'll dig in. Ed
