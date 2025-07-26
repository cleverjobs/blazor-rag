# Issue with Telerik Notification Component in Blazor Server: Notifications Not Rendering Across Threads

## Question

I'm encountering an issue with the Telerik Notification component in my Blazor Server. The problem arises when I attempt to display a notification from a function that is not on the same thread as the component. In such cases, the notification item doesn't render in the UI. To address this, I've made a modification to my component by replacing StateHasChanged with InvokeAsync(StateHasChanged) to ensure thread safety during invocation. I'd like to seek input to determine whether this is a bug in the Telerik component or if there's a better approach to solving this issue. Any advice or suggestions would be greatly appreciated. Thank you! USE::: BEFORE::: AFTER FIX::::

## Answer

**Nadezhda Tacheva** answered on 18 Sep 2023

Hi Víctor, I am not able to confirm the root cause based on just the screenshots and without the ability to test the scenario. As a first step, I suggest revising this sample application: One Notification Instance for All Components. It demonstrates how you can declare a single Notification component and then show it across various pages. You may use this sample as a base to set up your application. If you are still experiencing issues showing the Notification, please send us an isolated runnable sample that reproduces the use case. This will allow us to debug it and try to find what causes the problem. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Víctor** commented on 26 Sep 2023

Thanks for the answer, I have created a project to ilustrate the issue.

### Response

**Nadezhda Tacheva** commented on 29 Sep 2023

Hi Victor, Thank you for sharing the sample! I see the issue you are referring to. It looks to me that the problem is not associated with the Notification as the instance is correctly created. The problem, based on my research, stems from the fact that the UI is not updated. This is why, clicking on the other button shows both Notifications, as this forces the UI refresh. While researching, I found this thread on the matter [https://stackoverflow.com/questions/10285863/update-ui-label-from-task-continuewith.](https://stackoverflow.com/questions/10285863/update-ui-label-from-task-continuewith.) The first answer in it suggests that you have to set TaskScheduler.FromCurrentSynchronizationContext. Otherwise, ContinueWith will not be run in the UI context. I hope this will help you move forward with the configuration on your end.

### Response

**Víctor** commented on 29 Sep 2023

Hy there, I tested your solution and it works: Nevertheless, this is not how Blazor wants you to do things and it's not a good developer experience. For starters, I don't want to use ContinueWith. Second, Blazor ofers InvokeAsync method so you don't have to worry about SynchronizationContext. And also, StateHasChanged is avaliable. I strongly think Telerik should handle de SynchronizationContext (as it's a fairly advanced concet) by using the provided tools by the framework: InvokeAsync=> StateHasChanged. This would make Telerik Blazor a more robust library and it would take 1 minute to fix. Don't you agree?

### Response

**Nadezhda Tacheva** commented on 04 Oct 2023

Hi Victor, Thank you for getting back to me! I am happy to find out that the solution I suggested helped you to achieve the desired result. As for whether Telerik UI for Blazor should handle such a scenario out of the box, the short answer is no. Please see the details below. The Notification is a relatively simple component whose purpose is to show a message to the user in a nice-looking UI. The methods that the Notification exposes are synchronous. If the component has to be shown asynchronously, this should be handled by the developer as per the specific application requirements. I am not completely aware of the exact use case and why it is needed to show the Notification from a function that is not in the same thread but in this case you may also consider using the InvokeAsync method. It dispatches code execution to Blazor's synchronization context. For example: await InvokeAsync(()=>
{ // show notification here StateHasChanged(); }); Here is one more article on the matter that you may find useful: Thread safety using InvokeAsync.
