# Showing a dynamic dialog

## Question

**Ger** asked on 11 Apr 2023

Dear Team, I am looking into the possibility to show a dialog via a capsulated service (DialogService.Show<DialogType>(...) ) but because the dialogs are only made visible they have to be in place. I managed to do this via a DynamicComponent, but I would like to inject the dialog dynamically into the dom. I have no idea how to do that though. In WPF f.e. I can add a new object into the tree at any given place. Is this not possible in Blazor? Would love to get some support on putting such a service for showing a dialog just by a given type from an injected "Service". Thanks for your help and best regards Gerrit Puddig

### Response

**Gerrit** commented on 11 Apr 2023

Just found the WindowAsAService Sample which may do what I am looking for (GitHub). Will check...

## Answer

**Svetoslav Dimitrov** answered on 14 Apr 2023

Hello Gerrit, Indeed, I believe that the Window As a Service demo application is what you are looking for. Can you confirm if it helped you move forward and if you have any further questions? Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Gerrit** commented on 14 Apr 2023

Yes, thank you Svetoslav, I was able to use this sample and edit it to my needs. The only thing I still do not get is why I cannot render a DynamicComponent inside the WindowContent. It only works when using the BuildRenderTree Method. But using a DynamicCompent and setting its "Type" Property always brings up an Error about using SetParameters or so and that the Type-Property could not be found. Strange...

### Response

**Svetoslav Dimitrov** commented on 18 Apr 2023

Hello Gerrit, Can you send me a runnable code snippet where I can see the configuration of the project and the error so that we can investigate if it is a bug?
