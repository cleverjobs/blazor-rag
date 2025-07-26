# UI for Blazor and .Net Core Preview8

## Question

**Mar** asked on 14 Aug 2019

Has anyone else encountered issue using version 1.4.1 with preview8? Trying to show a grid that worked correctly in 1.4.0 and preview7.

## Answer

**Bozhidar** answered on 14 Aug 2019

Hi, You can expect the 1.5.0 version, which will be compatible with Preview 8, tomorrow. Regards, Bozhidar

### Response

**Mark** answered on 15 Aug 2019

Preview 1.5.0 works with .Net Core preview8 with one exception. I previous releases of Telerik UI for Blazor we used the following script tag in _Host.cshtml: <script src="[https://kendo.cdn.telerik.com/blazor/1.4.1/telerik-blazor.min.js"](https://kendo.cdn.telerik.com/blazor/1.4.1/telerik-blazor.min.js") defer></script> Referencing the 1.5.0 version of the js file from the cdn fails. Its it missing? The current documentation says to use the following: <script src="_content/telerik.ui.for.blazor/js/telerik-blazor.js" defer></script> Where is the referenced js file? What is the correct way to reverence the telerik-balzor.js file? Thanks for any clarification on this issue.

### Response

**Tom** answered on 15 Aug 2019

We're seeing the same issues as Mark, there doesn't appear to be a 1.5.0 JS file on the CDN, and there's no JS file in the 1.5.0 zip file?

### Response

**Marin Bratanov** answered on 16 Aug 2019

Hello Mark, Tom, Thanks for reaching out. It seems there had been some hiccup with the CDN file upload and it...well, didn't upload. We fixed it now, so you should be able to use the 1.5.0 CDN. As for the local reference - this is the approach we'd recommend to use instead of a CDN, because it relies on the static assets feature from the framework, and takes the correct file from our package, so you don't have to remember to update the CDN path. You can read more about it here: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#static-assets.](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#static-assets.) Regards, Marin Bratanov

### Response

**Tom** answered on 16 Aug 2019

Hi Marin Thanks for the reply. I'd got so used to static assets not working in Blazor that I'd completely forgotten the feature existed! To anyone who hasn't encountered the static assets, it means the Nuget package will sort out getting the JS file and you just need to reference it. I've stuck in a PR to make that slightly clearer in the Telerik docs and also to highlight that this is now the preferred approach (rather than using the CDN)

### Response

**Marin Bratanov** answered on 16 Aug 2019

Hello Tom, They started working in Preview 6, and Preview 7 fixed deployment issues with them. Of course, a purely client-side app (that is, not hosted on ASP.NET Core) still can't use them, hopefully it will be able to come the winter and the official versions of the wasm-based blazor. Thank you for the pull request, it's live now (I took the liberty of amending it a little to make the suggestions more visible). You will find your Telerik points updated as a small "thank you". If you do see other things we've missed or don't look right, don't hesitate to open an issue or a pull request in the docs repo, they are more than welcome :) Regards, Marin Bratanov

### Response

**Tom** answered on 16 Aug 2019

Hi Marin, that's great and thanks for the points. That's a good point re client-side, I've been working exclusively in server-side Blazor so I keep forgetting to think about the client-side differences.

### Response

**Marin Bratanov** answered on 16 Aug 2019

Hi Tom, I imagine most people are focused on the server-side flavor at the moment, as it is more mature and stable, even though the real innovation is the client-side model (or, at least, it is going to be once it is mature enough). Regards, Marin Bratanov

### Response

**Mark** answered on 16 Aug 2019

Not sure if this is the best place for this, but it applies to 1.5.0 in preview8. When you add the Filterable option to a grid that displays a column with type long? and there is a record with a null value, then the following error is raised: [2019-08-16T12:49:33.513Z] Error: System.InvalidCastException: Unable to cast object of type 'System.String' to type 'System.Nullable`1[System.Int64]'. at Telerik.Blazor.Components.Common.Editors.TelerikLongEditor.get_LongValue() at Telerik.Blazor.Components.Common.Editors.TelerikLongEditor.BuildRenderTree(RenderTreeBuilder builder) at Microsoft.AspNetCore.Components.ComponentBase.<.ctor>b__5_0(RenderTreeBuilder builder) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment) at Microsoft.AspNetCore.Components.Rendering.Renderer.RenderInExistingBatch(RenderQueueEntry renderQueueEntry) at Microsoft.AspNetCore.Components.Rendering.Renderer.ProcessRenderQueue() <TelerikGrid TItem="SavMorModel.Entities.Pharmacy" Data="ViewModel.Pharmacies.ToList()" FilterMode="Telerik.Blazor.FilterMode.FilterRow" Pageable="true" PageSize="10" Sortable="true"> <TelerikGridEvents> <EventsManager OnEdit="((args)=> DisplayDetail(args))" /> </TelerikGridEvents> <TelerikGridColumns> <TelerikGridCommandColumn Title="Select" Width="75"> <TelerikGridCommandButton Command="Edit" Icon="edit"> </TelerikGridCommandButton> </TelerikGridCommandColumn> <TelerikGridColumn Field=@nameof(SavMorModel.Entities.Pharmacy.CustomerID) Title="NCPDP#" /> <TelerikGridColumn Field=@nameof(SavMorModel.Entities.Pharmacy.StoreNumber) Title="Store#" /> <TelerikGridColumn Field=@nameof(SavMorModel.Entities.Pharmacy.NPINumber) Title="NPI#" /> (This is of type long?) <TelerikGridColumn Field=@nameof(SavMorModel.Entities.Pharmacy.DBAName) Title="Pharmacy" /> <TelerikGridColumn Field=@nameof(SavMorModel.Entities.Pharmacy.City) Title="City" /> <TelerikGridColumn Field=@nameof(SavMorModel.Entities.Pharmacy.State) Title="State" /> </TelerikGridColumns> </TelerikGrid>

### Response

**Marin Bratanov** answered on 16 Aug 2019

Hello Mark, Generally, I'd suggest we keep each thread more concise, so such a question would, ideally, have its own thread. I went a little astray in this one myself, though :) I am logging this bug for research and fixing, and you can Follow it in this page (your vote is already in): [https://feedback.telerik.com/blazor/1425703-fields-of-type-long-cause-errors-in-the-grid-editing-or-when-filtering-is-enabled.](https://feedback.telerik.com/blazor/1425703-fields-of-type-long-cause-errors-in-the-grid-editing-or-when-filtering-is-enabled.) Regards, Marin Bratanov
