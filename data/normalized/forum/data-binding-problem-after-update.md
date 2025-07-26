# Data Binding Problem After Update

## Question

**Den** asked on 04 Feb 2020

Hi Guys, im developing a server-side-blazor app on .NetCore 3.1 and up to now i was really happy with your components. But after update from version 2.5.1 to 2.6.1/ 2.7.0 i had a binding problem without any change. (Following Example i created for testing) <TelerikGrid Data="@LagerOrte"> <GridColumns> <GridColumn Field="@(nameof(LagerOrt.Nummer))" Title="Nr" Width="75px" /> <GridColumn Field="@(nameof(LagerOrt.Zeichen))" Title="Barcode" Width="150px" /> </GridColumns> </TelerikGrid> LagerOrte=new ObservableCollection<LagerOrt>(Enumerable.Range(1, 30).Select(x=> new LagerOrt { Id=Guid.NewGuid(), Nummer=x, Zeichen="zeichen " + x })); In Version 2.5.1 i had no problem but since Version 2.6.1 i get following ErrorMessage: [2020-02-04T15:30:32.500Z] Error: System.Collections.Generic.KeyNotFoundException: The given key 'HWE.DAL.DOMAIN.Models.LagerOrt' was not present in the dictionary. at System.Collections.Generic.Dictionary`2.get_Item(TKey key) at Microsoft.AspNetCore.Components.RenderTree.RenderTreeDiffBuilder.AppendDiffEntriesForRange(DiffContext& diffContext, Int32 oldStartIndex, Int32 oldEndIndexExcl, Int32 newStartIndex, Int32 newEndIndexExcl) at Microsoft.AspNetCore.Components.RenderTree.RenderTreeDiffBuilder.ComputeDiff(Renderer renderer, RenderBatchBuilder batchBuilder, Int32 componentId, ArrayRange`1 oldTree, ArrayRange`1 newTree) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment) at Microsoft.AspNetCore.Components.RenderTree.Renderer.RenderInExistingBatch(RenderQueueEntry renderQueueEntry) at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue() i would be very grateful for a solution regards Dennis

## Answer

**Marin Bratanov** answered on 04 Feb 2020

Hello Dennis, I am attaching a sample project I built with 2.7.0 that seems to work fine for me with this code. Could you compare against it to see what is the difference causing the problem? Since the stack trace contains only framework methods and the class name, it seems like something was wrongly built/cached, so I can also suggest you try the steps for cleaning the nuget cache and bin/obj folders here: [https://docs.telerik.com/blazor-ui/upgrade/overview#troubleshooting.](https://docs.telerik.com/blazor-ui/upgrade/overview#troubleshooting.) If neither helps, could you modify my sample to showcase the problem so I can investigate? Regards, Marin Bratanov

### Response

**Dennis** answered on 04 Feb 2020

Hi Marin, thanks for the fast response.i will check and test it tomorrow and give you then (hopefully) a last replie. regards Dennis

### Response

**Dennis** answered on 05 Feb 2020

Hi Marin, ich checked the project again, and have applied all your tips (clear cache etc.). Problem is the same. I was able to narrow down the problem further and integrated it into your project accordingly. When exchange the local object "LagerOrt" for my domain object from Domain.dll, the error occurs. But only in Telerik Blazor Version greater than 2.5.1. Perhaps problems in grid with interfaces or derivations of classes (models) ? domain.ddl is added to the project. I hope it brings us closer to the solution. How can i send you the project back? can't attache it to this post ? regards Dennis

### Response

**Marin Bratanov** answered on 05 Feb 2020

Hello Dennis, Forums allow images as attachments, but you can open a private support ticket where you can attach a .zip of the sample project. Regards, Marin Bratanov

### Response

**Dennis** answered on 05 Feb 2020

Hi Marin, I send the Project via SupportTicket (1452350). Hope we can find a solution now. regards Dennis

### Response

**Marin Bratanov** answered on 05 Feb 2020

To post publicly as well, we are looking into the situation and at this point it is likely to be the same as this: [https://feedback.telerik.com/blazor/1452386-add-support-for-lazyloadingproxies-in-ef](https://feedback.telerik.com/blazor/1452386-add-support-for-lazyloadingproxies-in-ef) We will post updates when we know more. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 06 Feb 2020

To post here as well, We think the issue is caused by the fact that the custom model class has an override of the Equals method that contains an implementation that is not sufficient to perform an actual equals check and it confuses the framework. The ways to fix that would be to: implement a view model that has all the fields you need, but without those overrides Or, remove the override for Equals and let the framework do this Or, implement the Equals override fully Regards, Marin Bratanov

### Response

**Dennis** answered on 06 Feb 2020

Hi Marin, i implemented the Equals Override in my BaseEntity fully, ther was missing a part...:-) that fixed my Problem. Great. Thank you for Support. Thumbs up and best wishes regards Dennis
