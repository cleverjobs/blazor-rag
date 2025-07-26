# Individual independent Appointment colors

## Question

**Rol** asked on 30 Jul 2020

How do I influence the styling of appointments, and in particular the background color, without using a resource/groupby view or css? I want to be able to decide runtime what the color should be.

## Answer

**Marin Bratanov** answered on 30 Jul 2020

Hi Roland, When Templates get implemented you will be able to add your own rendering at runtime: [https://feedback.telerik.com/blazor/1457901-templates-for-appointments.](https://feedback.telerik.com/blazor/1457901-templates-for-appointments.) Regards, Marin Bratanov

### Response

**Roland** answered on 31 Jul 2020

My current workaround is introducing a <SchedulerResource> for the types of Appointments I want to have a distinct color. This works because <SchedulerResource> changes nothing about the presentation other than the Appointment color. It will backfire when proper Resource Views are implemented, but it'll do for now.

### Response

**Roland** answered on 31 Aug 2020

No idea what changed, but I now always get an error when using: <TelerikScheduler...> <SchedulerViews> ... </SchedulerViews> <SchedulerResources> <SchedulerResource... Data="@myList"... ColorField="@nameof(SomeEntity.Color)" /> </SchedulerResources> </TelerikScheduler> myList is populated in OnInitializedAsync(). The error is: System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.Scheduler.ViewModels.SchedulerViewModelBase.GetResourceColors(). Any ideas?

### Response

**Marin Bratanov** answered on 31 Aug 2020

Hi Roland, Since this worked recently, I'd suggest reviewing the source control history of the scheduler settings, the data service and the resource model for changes that can cause issues. My best guess is that something in the names of the fields does not match between the resource tag settings and the actual model data - for example, missing values in the resource collection or them being in another field, or missing public getters. If this does not help you move forward, please modify the sample from the docs to showcase the issues so I can have a look. Regards, Marin Bratanov

### Response

**Roland** answered on 31 Aug 2020

In fact this has bothered me from the start, but at first only incidentally. I assumed it was some sort of race condition, or I had picked the wrong Blazor event to populate my lists. But I'll have a look at your demo and report back :).

### Response

**Roland** answered on 01 Sep 2020

I looked at the online demo, and it has the exact same problem. As soon as the data is retrieved in OnInitializedAsync() and you have to await the data loading you get the beforementioned exception. The demo only works because all data is loaded (synchronously, hardcoded) in the constructor.

### Response

**Roland** answered on 01 Sep 2020

And as soon as I retrieve the appointments synchronously, the error goes away... Also the demo documentation says that SchedulerResource.Field and .ValueField must be strings, but using Guid IDs works as well.

### Response

**Marin Bratanov** answered on 01 Sep 2020

Hi Roland, Does initializing the collection help, like in the sample I am attaching below? It should, and I've added that to the docs ( commit and changed article ). On another note, you may want to use the standard loading sign pattern from the default FetchData.razor page to only show the scheduler after all relevant data has arrived. Regards, Marin Bratanov

### Response

**Roland** answered on 01 Sep 2020

Yes, your solution works as well. You don't need to retrieve the resource data synchronously. As long as the resource list ("Managers" in the demo) is initialised with an empty list, you can than retrieve the resource asynchronously. Leaving the resource list null while awaiting the data causes the exception.
