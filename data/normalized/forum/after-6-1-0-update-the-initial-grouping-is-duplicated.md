# After 6.1.0 update the initial grouping is duplicated

## Question

**Mar** asked on 08 Aug 2024

Hy, I have a grid with aggregates and I set an initial grouping on the OnStateInit method: Everything is working fine but after the last update the initial grid view is as follows: As you can see the grouping is duplicated. Can anyone help me? The grid is attached Thanks

## Answer

**Dimo** answered on 09 Aug 2024

Hi Marco, Indeed, I reproduced the described behavior and I confirm this change occurs with the latest version 6.1.0. The easiest thing to do is reset the GroupDescriptors collection in OnStateInit before adding new descriptors. In the meantime, I am waiting for input from the developers if the change was intended or I should log a bug on your behalf. private void OnGridStateInit ( GridStateEventArgs<GridModel> args ) { args.GridState.GroupDescriptors=new List<GroupDescriptor>(); args.GridState.GroupDescriptors.Add( ... );
} Regards, Dimo

### Response

**Dimo** commented on 12 Aug 2024

P.S. We confirm this to be a regression. Here is the public bug report for tracking. @Marco, I also updated your Telerik points.
